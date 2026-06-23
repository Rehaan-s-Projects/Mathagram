// Netlify Edge Function — Ms. Gosia AI classroom chat for the Virtual School.
// Verifies the caller's Firebase ID token, rate-limits per user, then
// stream-proxies the Anthropic Messages API back to the browser as SSE.
//
// REQUIRED Netlify env vars:
//   ANTHROPIC_API_KEY   — Anthropic API key (server-only; never sent to client)
//   FIREBASE_PROJECT_ID — e.g. "mathagram-org" (same value mga-token.ts uses)

import type { Context } from "https://edge.netlify.com";

const MODEL = "claude-haiku-4-5";
const ANTHROPIC_VERSION = "2023-06-01";
const MAX_TOKENS = 600;
const RATE_MAX = 20;          // messages per window
const RATE_WINDOW_MS = 60_000;
const MAX_INPUT_CHARS = 1500;

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

Keep replies concise — a few short paragraphs at most.`;

const ISSUER_PREFIX = "https://securetoken.google.com/";

function b64urlDecodeText(s: string): string {
  const pad = "=".repeat((4 - (s.length % 4)) % 4);
  const b64 = (s + pad).replace(/-/g, "+").replace(/_/g, "/");
  const bin = atob(b64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}

// Validate issuer/audience/expiry of the Firebase ID token and return its uid (sub).
// Mirrors mga-token.ts: payload checks are sufficient here — the token was just
// minted by Firebase for this project, and a forgery would need Google's key.
function uidFromIdToken(idToken: string, projectId: string): string {
  const parts = idToken.split(".");
  if (parts.length !== 3) throw new Error("malformed token");
  const payload = JSON.parse(b64urlDecodeText(parts[1]));
  if (payload.aud !== projectId) throw new Error("audience mismatch");
  if (payload.iss !== ISSUER_PREFIX + projectId) throw new Error("issuer mismatch");
  if (payload.exp <= Math.floor(Date.now() / 1000)) throw new Error("token expired");
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
    headers: { "Content-Type": "text/event-stream", "Cache-Control": "no-cache" },
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
  const apiKey = Deno.env.get("ANTHROPIC_API_KEY");
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
  try { uid = uidFromIdToken(idToken, projectId); }
  catch (e) {
    return new Response(JSON.stringify({ error: "unauthorized", message: String(e) }), {
      status: 401, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  // Sanitize history: keep only user/assistant text turns, clamp to last 10,
  // and ensure it starts on a user turn (Anthropic requires messages[0].role==="user").
  let clean = messages
    .filter((m: any) => (m?.role === "user" || m?.role === "assistant") && typeof m?.content === "string")
    .map((m: any) => ({ role: m.role, content: String(m.content).slice(0, MAX_INPUT_CHARS) }))
    .slice(-10);
  while (clean.length && clean[0].role !== "user") clean = clean.slice(1);
  if (!clean.length) {
    return new Response(JSON.stringify({ error: "empty_history" }), {
      status: 400, headers: { ...cors, "Content-Type": "application/json" },
    });
  }
  const last = clean[clean.length - 1];
  if (last.role === "user" && last.content.length > MAX_INPUT_CHARS) {
    return sseFallback("That message is a bit long for me! Try asking it in fewer words. 💜");
  }

  if (!(await allowRequest(uid))) {
    return new Response(JSON.stringify({ error: "rate_limited" }), {
      status: 429, headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  let upstream: Response;
  try {
    upstream = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": apiKey,
        "anthropic-version": ANTHROPIC_VERSION,
      },
      body: JSON.stringify({
        model: MODEL,
        max_tokens: MAX_TOKENS,
        stream: true,
        system: GOSIA_SYSTEM_PROMPT,
        messages: clean,
      }),
    });
  } catch (_e) {
    return sseFallback("I can't reach the classroom right now — try again in a moment!");
  }

  if (!upstream.ok || !upstream.body) {
    return sseFallback("I can't reach the classroom right now — try again in a moment!");
  }

  // Pipe the Anthropic SSE straight through to the browser.
  return new Response(upstream.body, {
    status: 200,
    headers: {
      ...cors,
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
    },
  });
};

export const config = { path: "/api/gosia-chat" };
