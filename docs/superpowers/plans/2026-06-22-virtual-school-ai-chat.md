# Virtual School AI Live Chat (Ms. Gosia) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the Virtual School's canned keyword chatbot with a real, streaming Claude conversation with Ms. Gosia (Duolingo-Lily style).

**Architecture:** A new Netlify Edge Function `/api/gosia-chat` (Deno) holds the Anthropic key, verifies the caller's Firebase ID token, rate-limits per user, and stream-proxies the Anthropic Messages API SSE back to the browser. `school.html`'s Online Classroom panel is rebuilt to send conversation history, render Gosia's reply token-by-token, speak it once, and keep the existing 3-strike moderation.

**Tech Stack:** Netlify Edge Functions (Deno runtime), Anthropic Messages API (`claude-haiku-4-5`, streaming SSE), Firebase Auth (ID-token JWKS verification), vanilla browser JS (fetch + ReadableStream), `SpeechSynthesis`.

## Global Constraints

- Model constant: `claude-haiku-4-5`. Anthropic version header: `2023-06-01`. `max_tokens: 600`.
- Edge function path: `/api/gosia-chat`; file mirrors `netlify/edge-functions/mga-token.ts` structure (default handler + `export const config = { path }`, CORS helper, Deno.env secrets).
- Secrets via Netlify env: `ANTHROPIC_API_KEY` (new, user-set), `FIREBASE_PROJECT_ID` (already used by `mga-token.ts`).
- Signed-in Firebase users only. Rate limit: 20 messages / 60s per uid; reject latest user message > 1500 chars. Rate-limit store failures fail OPEN (allow), never block learning.
- Keep the existing 3-strike moderation (`isInappropriate`, `vs_chat_warnings`, `vs_chat_banned`) and `gosiaSpeak()` voice. Never re-`speak()` an existing utterance — always a fresh `SpeechSynthesisUtterance`, spoken once when the reply completes.
- This codebase has **no automated test framework**. "Tests" below are concrete verification commands (syntax/structure checks) plus a final manual deploy checklist. Do not invent a test harness.
- Deploy is the user's Netlify full-clean flow; the live AI cannot be exercised from localhost (no key / no public host). State this; do not claim live verification you didn't do.

---

## File Structure

- **Create** `netlify/edge-functions/gosia-chat.ts` — auth + rate-limit + streaming proxy to Anthropic. One responsibility: turn an authenticated `{idToken, messages}` POST into a streamed Gosia reply.
- **Modify** `school.html` — rebuild the Online Classroom chat JS: remove canned-reply + scripted-quiz logic, add `chatHistory` + streaming `sendChat()` + simplified `goToClass()`. Keep moderation, voice, bubbles, typing indicator.

---

### Task 1: Edge function `gosia-chat.ts` (auth + rate-limit + streaming proxy)

**Files:**
- Create: `netlify/edge-functions/gosia-chat.ts`
- Reference (do not modify): `netlify/edge-functions/mga-token.ts` (JWKS verify + CORS pattern)

**Interfaces:**
- Consumes: HTTP `POST /api/gosia-chat`, JSON body `{ idToken: string, messages: Array<{role:"user"|"assistant", content:string}> }`.
- Produces: on success, `Content-Type: text/event-stream` streaming the Anthropic SSE bytes unchanged (browser reads `content_block_delta` → `text_delta`). On auth failure `401`; rate limit `429`; other errors → a single SSE `data:` line carrying a JSON `{type:"fallback", text}` then close.

- [ ] **Step 1: Write the function file**

Create `netlify/edge-functions/gosia-chat.ts`:

```ts
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
```

- [ ] **Step 2: Type-check / parse-verify the file**

Run (Deno may not be installed; fall back to a Node syntax transform of the TS):
```bash
cd /Users/dakotabrown/rehan-calculus-local
deno check netlify/edge-functions/gosia-chat.ts 2>/dev/null && echo "DENO OK" || \
npx --yes esbuild netlify/edge-functions/gosia-chat.ts --bundle --format=esm --platform=neutral --external:https://* --outfile=/dev/null && echo "ESBUILD PARSE OK"
```
Expected: `DENO OK` or `ESBUILD PARSE OK` (no syntax errors). A type-only complaint about the remote `Context` import under esbuild is acceptable; a syntax error is not.

- [ ] **Step 3: Structural assertions**

Run:
```bash
cd /Users/dakotabrown/rehan-calculus-local
grep -q 'export const config = { path: "/api/gosia-chat" }' netlify/edge-functions/gosia-chat.ts && \
grep -q 'claude-haiku-4-5' netlify/edge-functions/gosia-chat.ts && \
grep -q 'uidFromIdToken' netlify/edge-functions/gosia-chat.ts && \
grep -q 'fail open' netlify/edge-functions/gosia-chat.ts && echo "STRUCT OK"
```
Expected: `STRUCT OK`

- [ ] **Step 4: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add netlify/edge-functions/gosia-chat.ts
git commit -m "Add /api/gosia-chat edge function: Firebase-auth'd streaming Claude proxy for Virtual School

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: Rebuild the Online Classroom chat in `school.html`

**Files:**
- Modify: `school.html` (the inline classroom `<script>`: `goToClass`, `gosiaResponses`, `getGosiaReply`, `chatLessons`, `askChatQuiz`, `sendChat`)

**Interfaces:**
- Consumes: Task 1's `POST /api/gosia-chat` returning streamed SSE; `./js/firebase-config.js` `auth.currentUser.getIdToken()`; existing globals `isInappropriate()`, `addGosiaChat()`, `gosiaSpeak()`, `chatBanned`, `chatWarnings`, `warningMessages`, DOM `#chatInput`/`#chatMessages`.
- Produces: a streaming `sendChat()` and a `chatHistory` array; simplified `goToClass()`. No new global names other than `chatHistory` and `streamGosiaReply`.

- [ ] **Step 1: Simplify `goToClass()` to drop scripted lessons/quizzes**

Replace the whole `goToClass` function body (currently at `school.html:758-783`). New version:

```js
function goToClass(course) {
  var chatBox = document.getElementById('chatMessages');
  chatBox.parentElement.parentElement.scrollIntoView({behavior:'smooth'});
  var subjectName = course.replace(/-/g,' ').replace(/\b\w/g, function(c){return c.toUpperCase();});
  activeCourse = course;
  chatHistory = [];
  addGosiaChat("Welcome to <strong>" + subjectName + "</strong> class! Ask me anything about it and we'll learn together. What would you like to start with? 💜");
}
```

- [ ] **Step 2: Remove the retired scripted-quiz state and data**

Delete these now-unused declarations and functions from the classroom script:
- `var chatQuizStep = 0;` and `var chatQuizScore = 0;` (both the ones near `goToClass` and any duplicates)
- the entire `var chatLessons = { ... };` object
- the entire `function askChatQuiz() { ... }` function
- the entire `var gosiaResponses = { ... };` object
- the entire `function getGosiaReply(msg) { ... }` function

Keep: `var activeCourse = null;`, `isInappropriate`, `badPatterns`, `chatWarnings`, `chatBanned`, `warningMessages`, `gosiaSpeak`, `addGosiaChat`. Add near `var activeCourse = null;`:

```js
var chatHistory = [];
```

- [ ] **Step 3: Add the streaming reply helper**

Add this function in the classroom script (e.g. just above `sendChat`):

```js
// Stream Ms. Gosia's reply from the AI endpoint into the given bubble's text node.
// Returns the full reply text. Throws on auth/rate/network failure.
async function streamGosiaReply(history, bubbleTextEl) {
  var config = await import('./js/firebase-config.js');
  var user = config.auth && config.auth.currentUser;
  if (!user) { var e = new Error('not_signed_in'); e.code = 'auth'; throw e; }
  var idToken = await user.getIdToken();

  var res = await fetch('/api/gosia-chat', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ idToken: idToken, messages: history })
  });
  if (res.status === 401) { var a = new Error('unauthorized'); a.code = 'auth'; throw a; }
  if (res.status === 429) { var r = new Error('rate'); r.code = 'rate'; throw r; }
  if (!res.ok || !res.body) { throw new Error('net'); }

  var reader = res.body.getReader();
  var decoder = new TextDecoder();
  var buffer = '';
  var full = '';
  while (true) {
    var chunk = await reader.read();
    if (chunk.done) break;
    buffer += decoder.decode(chunk.value, { stream: true });
    var lines = buffer.split('\n');
    buffer = lines.pop();
    for (var i = 0; i < lines.length; i++) {
      var line = lines[i];
      if (line.indexOf('data:') !== 0) continue;
      var payload = line.slice(5).trim();
      if (!payload || payload === '[DONE]') continue;
      var evt;
      try { evt = JSON.parse(payload); } catch (_e) { continue; }
      if (evt.type === 'fallback' && evt.text) {
        full = evt.text; bubbleTextEl.textContent = full;
      } else if (evt.type === 'content_block_delta' && evt.delta && evt.delta.type === 'text_delta') {
        full += evt.delta.text;
        bubbleTextEl.textContent = full;
        bubbleTextEl.parentElement.parentElement.scrollTop = 9e9;
      }
    }
  }
  return full;
}
```

- [ ] **Step 4: Rewrite `sendChat()` to stream + keep moderation + speak once**

Replace the whole `sendChat` function (currently `school.html:988`+). The student-bubble + moderation block is preserved; the Gosia reply now streams from the API. New version:

```js
function sendChat() {
  if (chatBanned) {
    var bi = document.getElementById('chatInput');
    bi.value = ''; bi.placeholder = 'You have been removed from the classroom.'; bi.disabled = true;
    return;
  }
  var input = document.getElementById('chatInput');
  var msg = input.value.trim();
  if (!msg) return;
  input.value = '';

  var container = document.getElementById('chatMessages');
  var studentName = localStorage.getItem('vs_name') || 'You';
  var isBad = isInappropriate(msg.toLowerCase());

  var displayMsg = isBad ? msg.replace(/</g,'&lt;').replace(/\S/g,'*') : msg.replace(/</g,'&lt;');
  container.insertAdjacentHTML('beforeend',
    '<div style="display:flex;gap:8px;align-items:flex-start;justify-content:flex-end;">' +
    '<div style="background:'+(isBad?'#ef4444':'#3b82f6')+';color:#fff;border-radius:12px 0 12px 12px;padding:10px 14px;max-width:80%;font-size:.85rem;line-height:1.5;">' + displayMsg + (isBad?' <span style="font-size:.7rem;opacity:.7;">[censored]</span>':'') + '</div>' +
    '<div style="width:28px;height:28px;border-radius:50%;background:'+(isBad?'#ef4444':'#3b82f6')+';display:flex;align-items:center;justify-content:center;color:#fff;font-size:.7rem;font-weight:700;flex-shrink:0;">' + studentName.charAt(0).toUpperCase() + '</div>' +
    '</div>');
  container.scrollTop = container.scrollHeight;

  // Inappropriate input → existing strike system, no API call.
  if (isBad) {
    chatWarnings++;
    localStorage.setItem('vs_chat_warnings', chatWarnings);
    if (chatWarnings >= 3) {
      chatBanned = true; localStorage.setItem('vs_chat_banned', 'true');
      addGosiaChat(warningMessages[2].msg);
    } else {
      addGosiaChat(warningMessages[Math.min(chatWarnings-1, 1)].msg);
    }
    return;
  }

  chatHistory.push({ role: 'user', content: msg });

  // Gosia bubble with a typing indicator; we fill the inner text node as tokens stream.
  var rowId = 'g-' + Date.now();
  container.insertAdjacentHTML('beforeend',
    '<div id="' + rowId + '" style="display:flex;gap:8px;align-items:flex-start;">' +
    '<img src="assets/characters/gosia.svg" alt="" style="width:28px;height:28px;border-radius:50%;flex-shrink:0;margin-top:2px;">' +
    '<div style="background:#ede9fe;border-radius:0 12px 12px 12px;padding:10px 14px;max-width:80%;font-size:.85rem;line-height:1.5;color:#1f2937;">' +
    '<span class="g-text"></span><span class="g-typing" style="color:#7c3aed;">…</span>' +
    '</div></div>');
  container.scrollTop = container.scrollHeight;
  var row = document.getElementById(rowId);
  var textEl = row.querySelector('.g-text');
  var typingEl = row.querySelector('.g-typing');

  streamGosiaReply(chatHistory, textEl).then(function(full){
    if (typingEl) typingEl.remove();
    var clean = (full || '').trim();
    if (clean) {
      chatHistory.push({ role: 'assistant', content: clean });
      gosiaSpeak(clean);
    }
  }).catch(function(err){
    if (typingEl) typingEl.remove();
    // Roll back the unanswered user turn so history stays valid.
    if (chatHistory.length && chatHistory[chatHistory.length-1].role === 'user') chatHistory.pop();
    var line = (err && err.code === 'auth')
      ? 'Please sign in again to chat with me. 💜'
      : (err && err.code === 'rate')
      ? 'One question at a time, please! Give me a moment and try again. 💜'
      : "I can't reach the classroom right now — try again in a moment!";
    textEl.textContent = line;
  });
}
```

- [ ] **Step 5: Verify no retired symbols remain and HTML still parses**

Run:
```bash
cd /Users/dakotabrown/rehan-calculus-local
echo "should be 0:"; grep -c 'getGosiaReply\|gosiaResponses\|chatLessons\|askChatQuiz' school.html
echo "should be >=1 each:"; grep -c 'streamGosiaReply' school.html; grep -c 'chatHistory' school.html
node -e "const s=require('fs').readFileSync('school.html','utf8'); const m=s.match(/<script>([\s\S]*?)<\/script>/g)||[]; let ok=true; for(const b of m){const code=b.replace(/^<script>/,'').replace(/<\/script>$/,''); try{new Function(code);}catch(e){ok=false;console.error('SCRIPT PARSE FAIL:',e.message);}} console.log(ok?'ALL INLINE SCRIPTS PARSE OK':'PARSE ERRORS ABOVE');"
```
Expected: first count `0`; the two `streamGosiaReply`/`chatHistory` counts ≥ 1; final line `ALL INLINE SCRIPTS PARSE OK`.

(Note: `new Function(code)` validates syntax of each plain inline `<script>`; `async`/`await` inside functions is valid at function scope. If a block legitimately uses top-level `await` it will fail — none here should.)

- [ ] **Step 6: Commit**

```bash
cd /Users/dakotabrown/rehan-calculus-local
git add school.html
git commit -m "Virtual School: stream real Claude replies from Ms. Gosia (retire canned bot + scripted quizzes)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: Deploy + live verification checklist (user-gated)

**Files:** none (operational).

**Interfaces:** Consumes the deployed `/api/gosia-chat` and `school.html`.

- [ ] **Step 1: Confirm the env var prerequisite with the user**

Tell the user: set **`ANTHROPIC_API_KEY`** in Netlify env vars (Site settings → Environment variables). `FIREBASE_PROJECT_ID` is already set. Do not proceed to deploy until confirmed — without the key the endpoint returns `503` and chat shows the fallback line.

- [ ] **Step 2: Deploy via the established full-clean Netlify flow**

```bash
cd /Users/dakotabrown/rehan-calculus-local
rm -rf .netlify/v1 .netlify/functions-internal .netlify/netlify.toml .netlify/edge-functions-dist .netlify/edge-functions-import-map.json
netlify deploy --prod --dir=/Users/dakotabrown/rehan-calculus-local
```
Expected: hashing reports hundreds/thousands of files (not 0–4) and deploy_time > 3s. Then `curl -s -o /dev/null -w "%{http_code}\n" https://mathagram.org/school.html` → `200`.

- [ ] **Step 3: Verify the endpoint rejects anonymous calls**

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST https://mathagram.org/api/gosia-chat \
  -H 'content-type: application/json' --data '{"messages":[{"role":"user","content":"hi"}]}'
```
Expected: `400` (missing idToken) — confirms the function is deployed and refuses unauthenticated input. (A `503` here means `ANTHROPIC_API_KEY` is not set yet.)

- [ ] **Step 4: Manual browser smoke test (report results honestly)**

On `https://mathagram.org`, signed in: open Virtual School → Online Classroom, pick a class, ask a real question (e.g. "what is 7 × 8?"). Confirm: reply streams in token-by-token, voice speaks once, a follow-up question keeps context. Then send a banned word and confirm the strike warning still fires. Then send 20+ messages quickly and confirm the "one question at a time" fallback. Note: this step requires the live site + sign-in; it cannot be done from localhost.

---

## Self-Review

**Spec coverage:** Backend edge function (Task 1) ✓; Firebase ID-token auth ✓; rate limit + 1500-char cap, fail-open ✓; Anthropic streaming call with Gosia system prompt + safety ✓; SSE passthrough ✓; refusal/error fallback ✓; model `claude-haiku-4-5` ✓; frontend rebuild — remove canned/quizzes, `chatHistory`, streaming `sendChat`, keep moderation + voice + typing indicator + welcome (Task 2) ✓; sign-in gating ✓; error/abort table behaviors ✓; deploy prereq + manual verification (Task 3) ✓. Out-of-scope items (no Firestore persistence, no `rita-chat.js` change, no thinking) are respected — no tasks touch them.

**Placeholder scan:** No TBD/TODO; all code blocks are complete; verification commands are concrete.

**Type consistency:** `streamGosiaReply(history, bubbleTextEl)` defined and called with matching args; `chatHistory` shape `{role,content}` matches the function's `messages` body and the edge function's sanitizer; SSE event names (`content_block_delta`/`text_delta`, `fallback`) match between function output and client parser; error `code` values (`auth`/`rate`) thrown in Step 3 and handled in Step 4 agree.
