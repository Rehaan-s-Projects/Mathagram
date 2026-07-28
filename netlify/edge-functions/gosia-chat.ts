// Netlify Edge Function — Ms. Gosia AI classroom chat for the Virtual School.
// Verifies the caller's Firebase ID token (full RS256 signature check),
// rate-limits per user, then stream-proxies an OpenAI-compatible LLM API
// (PPQ.AI) to the browser, normalizing its SSE into the simple event shape
// school.html parses.
//
// REQUIRED Netlify env vars:
//   PPQ_API_KEY         — PPQ.AI API key (OpenAI-compatible; server-only, never sent to client)
//   FIREBASE_PROJECT_ID — e.g. "mathagram-org" (same value mga-token.ts uses)

import type { Context } from "https://edge.netlify.com";
import { decodeProtectedHeader, importX509, jwtVerify } from "https://esm.sh/jose@5.9.6";

const PPQ_URL = "https://api.ppq.ai/chat/completions";
const MODEL = "claude-haiku-4.5";
const MAX_TOKENS = 600;
const RATE_MAX = 20;          // messages per window
const RATE_WINDOW_MS = 60_000;
const MAX_INPUT_CHARS = 1500;
const ISSUER_PREFIX = "https://securetoken.google.com/";
// Google's public X.509 certs for Firebase Secure Token Service.
const FIREBASE_CERTS_URL =
  "https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com";

const GOSIA_SYSTEM_PROMPT = `You are Ms. Gosia, a warm, patient, encouraging teacher at Mathagram's Virtual School for kids and teens. You teach across subjects — math, science, English, history, and study skills — in plain, age-appropriate language.

Teaching style:
- Explain step by step, in short paragraphs. Use simple words and concrete examples.
- Ask a guiding question when it helps the student think, rather than only handing over the answer.
- For homework, help the student understand and work through it — don't just give final answers to copy.
- Be upbeat and supportive. A little warmth and the occasional emoji is good; don't overdo it.

Safety (very important — this is a children's classroom):
- Stay strictly on education and school topics.
- If a student brings up anything unsafe, hateful, sexual, violent, or about self-harm, do not engage with the content. Respond briefly and kindly, steer back to learning, and if they seem to be in danger gently suggest talking to a trusted adult.
- Never produce profanity, slurs, or adult content.

Formatting:
- Write in plain, conversational text, like you're speaking to the student.
- Do NOT use Markdown or any special formatting — no #, *, **, backticks, headers, or bullet-point symbols. Just normal sentences.

Keep replies concise — a few short paragraphs at most.`;

// Cache Google's signing certs (~30 min) so we don't refetch per request.
let _certsCache: { keys: Record<string, string>; at: number } | null = null;
async function getFirebaseCerts(): Promise<Record<string, string>> {
  if (_certsCache && Date.now() - _certsCache.at < 30 * 60 * 1000) return _certsCache.keys;
  const res = await fetch(FIREBASE_CERTS_URL);
  if (!res.ok) throw new Error("certs fetch failed: " + res.status);
  const keys = await res.json();
  _certsCache = { keys, at: Date.now() };
  return keys;
}

// Fully verify a Firebase ID token (RS256 signature against Google's public
// certs, plus issuer/audience/expiry) and return its uid (sub). Throws on any
// failure — there is NO payload-only fallback, because this is the whole gate.
async function uidFromIdToken(idToken: string, projectId: string): Promise<string> {
  const header = decodeProtectedHeader(idToken);
  if (header.alg !== "RS256" || !header.kid) throw new Error("bad token header");
  const certs = await getFirebaseCerts();
  const pem = certs[header.kid];
  if (!pem) throw new Error("unknown signing key");
  const key = await importX509(pem, "RS256");
  const { payload } = await jwtVerify(idToken, key, {
    issuer: ISSUER_PREFIX + projectId,
    audience: projectId,
  });
  if (!payload.sub) throw new Error("no subject");
  return payload.sub as string;
}

// Best-effort per-uid sliding-window rate limit via Netlify Blobs.
// Fails OPEN: any store error returns true (allowed) so a flaky store never
// blocks a student from learning.
async function allowRequest(uid: string): Promise<boolean> {
  try {
    const { getStore } = await import("https://esm.sh/@netlify/blobs@8");
    const store = getStore("gosia-rate");
    const now = Date.now();
    const raw = await store.get(uid, { type: "json" }) as number[] | null;
    const hits = (raw || []).filter((t) => now - t < RATE_WINDOW_MS);
    if (hits.length >= RATE_MAX) return false;
    hits.push(now);
    await store.setJSON(uid, hits);
    return true;
  } catch (_e) {
    return true; // fail open
  }
}

function sseFallback(text: string): Response {
  const body = `data: ${JSON.stringify({ type: "fallback", text })}\n\n`;
  return new Response(body, {
    status: 200,
    headers: { "Content-Type": "text/event-stream", "Cache-Control": "no-cache, no-transform" },
  });
}

export default async (req: Request, _ctx: Context) => {
  const origin = req.headers.get("origin") || "*";
  const cors = {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "content-type",
    "Access-Control-Max-Age": "600",
  };
  if (req.method === "OPTIONS") return new Response(null, { headers: cors });
  if (req.method !== "POST") return new Response("POST only", { status: 405, headers: cors });

  const projectId = Deno.env.get("FIREBASE_PROJECT_ID");
  const apiKey = Deno.env.get("PPQ_API_KEY");
  if (!projectId || !apiKey) {
    return new Response(JSON.stringify({ error: "server_not_configured" }), {
      status: 503, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  let body: any;
  try { body = await req.json(); } catch { body = null; }
  const idToken = body?.idToken;
  const messages = Array.isArray(body?.messages) ? body.messages : null;
  if (!idToken || !messages) {
    return new Response(JSON.stringify({ error: "bad_request" }), {
      status: 400, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  let uid: string;
  try { uid = await uidFromIdToken(idToken, projectId); }
  catch (_e) {
    // Generic message to the client; details stay server-side (no forgery oracle).
    return new Response(JSON.stringify({ error: "unauthorized" }), {
      status: 401, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  // Reject (don't silently truncate) an over-long latest user message.
  const rawLast = messages[messages.length - 1];
  if (rawLast && rawLast.role === "user" && typeof rawLast.content === "string"
      && rawLast.content.length > MAX_INPUT_CHARS) {
    return sseFallback("That message is a bit long for me! Try asking it in fewer words. 💜");
  }

  // Sanitize history: keep only user/assistant text turns, clamp to last 10,
  // then trim non-user turns off BOTH ends so messages[0] and messages[-1] are
  // "user" (Anthropic requires first=user and a completion needs last=user).
  let clean = messages
    .filter((m: any) => (m?.role === "user" || m?.role === "assistant") && typeof m?.content === "string")
    .map((m: any) => ({ role: m.role, content: String(m.content).slice(0, MAX_INPUT_CHARS) }))
    .slice(-10);
  while (clean.length && clean[0].role !== "user") clean = clean.slice(1);
  while (clean.length && clean[clean.length - 1].role !== "user") clean = clean.slice(0, -1);
  if (!clean.length) {
    return new Response(JSON.stringify({ error: "empty_history" }), {
      status: 400, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  if (!(await allowRequest(uid))) {
    return new Response(JSON.stringify({ error: "rate_limited" }), {
      status: 429, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  let upstream: Response;
  try {
    upstream = await fetch(PPQ_URL, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "authorization": "Bearer " + apiKey,
      },
      body: JSON.stringify({
        model: MODEL,
        max_tokens: MAX_TOKENS,
        stream: true,
        // PPQ.AI is OpenAI-compatible: the system prompt is a message, not a top-level field.
        messages: [{ role: "system", content: GOSIA_SYSTEM_PROMPT }, ...clean],
      }),
    });
  } catch (_e) {
    return sseFallback("I can't reach the classroom right now — try again in a moment!");
  }

  if (!upstream.ok || !upstream.body) {
    return sseFallback("I can't reach the classroom right now — try again in a moment!");
  }

  // Normalize the upstream OpenAI-style SSE (choices[].delta.content, plus ":"
  // keepalive comments and a final [DONE]) into the simple text_delta events
  // that school.html's streamGosiaReply already understands. Keeps the browser
  // decoupled from the provider's wire format. An empty/refusal stream yields no
  // text events, which the client renders as a gentle fallback line.
  const decoder = new TextDecoder();
  const encoder = new TextEncoder();
  let buf = "";
  const normalize = new TransformStream<Uint8Array, Uint8Array>({
    transform(chunk, controller) {
      buf += decoder.decode(chunk, { stream: true });
      const parts = buf.split("\n");
      buf = parts.pop() as string;
      for (const line of parts) {
        const l = line.trim();
        if (!l || l.startsWith(":") || !l.startsWith("data:")) continue;
        const data = l.slice(5).trim();
        if (data === "[DONE]") continue;
        try {
          const obj = JSON.parse(data);
          const text = obj?.choices?.[0]?.delta?.content;
          if (text) {
            controller.enqueue(encoder.encode(
              `data: ${JSON.stringify({ type: "content_block_delta", delta: { type: "text_delta", text } })}\n\n`,
            ));
          }
        } catch (_e) { /* ignore keepalive / partial line */ }
      }
    },
  });

  return new Response(upstream.body.pipeThrough(normalize), {
    status: 200,
    headers: {
      ...cors,
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache, no-transform",
    },
  });
};

export const config = { path: "/api/gosia-chat" };
