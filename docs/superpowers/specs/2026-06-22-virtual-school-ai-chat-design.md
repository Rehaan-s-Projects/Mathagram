# Virtual School — AI "Live Chat" with Ms. Gosia (Duolingo-Lily style)

**Date:** 2026-06-22
**Status:** Awaiting user review

## Problem

The Virtual School "Online Classroom — Live Chat" in `school.html` is not real AI. `getGosiaReply()`
regex-matches keywords (`math`, `science`, …) and returns a random canned string from the
`gosiaResponses` map. It cannot answer a student's actual question. The goal is to make Gosia a
genuine LLM conversation, like Duolingo's Lily Chat — multi-turn, responsive, with streaming "typing"
and her existing spoken voice.

## Decisions (locked)

- **Provider/model:** Claude (Anthropic), model `claude-haiku-4-5` — fast and low-cost for a
  high-volume kids' tutor. Wired as a single constant; trivially swappable.
- **Scope:** Full rebuild of the Online Classroom chat. Replace canned replies AND retire the
  scripted `chatLessons`/`askChatQuiz` flow; Gosia handles "teach me"/"quiz me" conversationally.
- **Access:** Signed-in Firebase users only; rate-limited.
- **Streaming:** Yes — token-by-token, for the Lily-like typing feel.

## Architecture

Static site → new **Netlify Edge Function** (Deno) `/api/gosia-chat` → Anthropic Messages API.
This mirrors the existing `netlify/edge-functions/mga-token.ts` pattern (Deno handler +
`export const config = { path: ... }`, secrets in Netlify env vars, CORS helper).

```
school.html (browser)
  └─ POST /api/gosia-chat  { idToken, messages:[{role,content}...] }   (SSE response)
       └─ gosia-chat.ts (edge)
            • verify Firebase ID token (JWKS — reuse mga-token.ts logic)
            • rate-limit per uid (Netlify Blobs)
            • POST api.anthropic.com/v1/messages  (stream:true, system=GOSIA_PROMPT)
            • pipe SSE text deltas back to the browser
```

### Component 1 — `netlify/edge-functions/gosia-chat.ts` (new)

- **Method/CORS:** POST only; `OPTIONS` preflight; CORS headers like `mga-token.ts`.
- **Auth:** Read `idToken` from the JSON body. Verify with the same JWKS/issuer/audience/expiry
  checks already implemented in `mga-token.ts` (`FIREBASE_PROJECT_ID`). Reject with 401 if missing/invalid.
  The verified `sub` (uid) keys the rate limiter.
- **Rate limit (Netlify Blobs):** per-uid sliding window — **20 messages / 60s**. Also reject input
  whose latest user message exceeds **1500 chars**. Over limit → 429 with a short JSON error.
  If Blobs is unavailable, fail open (allow) rather than block learning — logged, not fatal.
- **Anthropic call:** `POST https://api.anthropic.com/v1/messages`, headers
  `x-api-key: ANTHROPIC_API_KEY`, `anthropic-version: 2023-06-01`. Body:
  - `model: "claude-haiku-4-5"` (constant `MODEL`)
  - `max_tokens: 600`
  - `stream: true`
  - `system: GOSIA_SYSTEM_PROMPT`
  - `messages`: the client-supplied history (already trimmed/validated; roles `user`/`assistant` only,
    must start with `user`, must alternate — the function sanitizes/clamps to the last 10 turns).
- **System prompt (`GOSIA_SYSTEM_PROMPT`):** Ms. Gosia, a warm, encouraging elementary/middle-school
  teacher at Mathagram's Virtual School. Teaches across subjects (math, science, English, history,
  study skills) in plain, age-appropriate language; explains step by step; asks guiding questions;
  never just gives homework answers outright. **Safety:** education-only; if a student raises anything
  unsafe, hateful, sexual, violent, or self-harm related, respond with a brief, kind redirection and
  do not engage with the content. Keep replies concise (a few short paragraphs max).
- **Streaming passthrough:** Stream the Anthropic SSE body to the client. The browser only needs the
  text deltas, so the function forwards the raw SSE (`content_block_delta` / `text_delta`) and the
  client extracts text. (Simplest: pipe the response body through unchanged with
  `content-type: text/event-stream`.)
- **Errors/refusal:** On non-2xx from Anthropic, `stop_reason: "refusal"`, or a thrown error, emit a
  single SSE event carrying a safe in-character fallback string and close. Never surface raw errors or
  keys to the client.

### Component 2 — `school.html` Online Classroom rebuild

- **Remove:** `gosiaResponses`, `getGosiaReply()`, `chatLessons`, `askChatQuiz`, `chatQuizStep`,
  `chatQuizScore`, and the canned-reply branch of `sendChat()`.
- **Add `chatHistory`** (module-scoped array of `{role, content}`), capped to the last ~10 turns.
- **`sendChat()` (rewritten):**
  1. Read + trim input; if empty, return. If `chatBanned`, keep current banned behavior.
  2. **Client moderation:** run existing `isInappropriate()` — on a hit, keep the current
     strike/warning/censor behavior and do **not** call the API.
  3. Render the student bubble (existing styling). Push `{role:'user', content:msg}` to `chatHistory`.
  4. Render an empty Gosia bubble + typing indicator. Call
     `streamGosiaReply(chatHistory)` → fetch `/api/gosia-chat` with `{ idToken, messages: chatHistory }`.
  5. As SSE text deltas arrive, append into the Gosia bubble (remove the typing indicator on first token).
  6. On completion: push `{role:'assistant', content:fullText}` to `chatHistory`; call `gosiaSpeak(fullText)`
     **once** (new utterance — never re-`speak()` an existing one, per the speech-synthesis rule).
  7. On error: show the in-character fallback line in the bubble; do not corrupt `chatHistory`.
- **idToken:** obtained via the page's existing Firebase auth (`auth.currentUser.getIdToken()`); if the
  user is not signed in, the classroom shows a short "sign in to chat with Ms. Gosia" prompt instead of sending.
- **Keep:** typing indicator, bubble/avatar markup, `gosiaSpeak()` voice, the 3-strike
  `vs_chat_warnings`/`vs_chat_banned` moderation, and the welcome message on entry.

## Data flow (one turn)

1. Student types → `sendChat()` → client moderation passes.
2. Browser POSTs `{idToken, messages}` to `/api/gosia-chat`.
3. Edge verifies token, checks rate limit, calls Anthropic with `stream:true`.
4. SSE deltas stream back; browser fills the Gosia bubble live.
5. On done, browser speaks the reply once and stores both turns in `chatHistory`.

## Error handling

| Condition | Behavior |
|---|---|
| Not signed in | Client shows sign-in prompt; no request sent |
| 401 from edge | In-character "please sign in again" line |
| 429 rate limit | "One question at a time, please! Try again in a moment." |
| Network / 5xx / refusal | "I can't reach the classroom right now — try again in a moment!" |
| Inappropriate input | Existing strike system; no API call |
| Localhost | Works only against deployed function; documented, not a code path |

## Out of scope / non-goals

- No persistence of chat history to Firestore (in-memory per session only).
- No change to other site chat (`rita-chat.js`) — this is the Virtual School classroom only.
- No streaming of thinking (Haiku has no extended thinking surface here).

## Operational prerequisite

- Set `ANTHROPIC_API_KEY` in Netlify environment variables (user action — cannot be committed).
- `FIREBASE_PROJECT_ID` is already required by `mga-token.ts`; reused here.

## Testing / verification

- `node --check`-equivalent: `deno check` is not in the toolchain; verify TS parses and the function
  shape matches `mga-token.ts`. Lint by structure.
- After deploy + env var: on `mathagram.org`, sign in, open Virtual School → Online Classroom, send a
  real question, confirm streamed reply + voice; send an inappropriate message, confirm strike still fires;
  hammer >20 msgs/min, confirm 429 fallback.
- Cannot verify the live AI from localhost (no key / public host); call this out, don't claim it works.
