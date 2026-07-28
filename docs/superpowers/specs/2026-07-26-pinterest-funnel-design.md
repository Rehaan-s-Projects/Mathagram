# Pinterest Growth Funnel — Design

**Date:** 2026-07-26
**Status:** Approved for planning
**Scope:** mathagram.org — Pinterest discoverability, YouTube embeds, email capture

## Goal

Build an organic acquisition funnel that does not depend on paid advertising:

```
Pinterest Pin  →  mathagram.org course page  →  embedded YouTube video (click-to-play)
                                             →  email capture (parents/teachers)
                                             →  email list  →  organic YouTube views on upload
```

Google Ads produced subscribers and views that YouTube excludes from the 4,000-hour
monetization threshold. Watch time from a video embedded on an external site is valid
public watch time, so routing discovery traffic through mathagram.org converts otherwise
unusable paid-style traffic into legitimate, countable watch time.

## Constraint: content length caps what this funnel can deliver

The channel (@Mathagram_Org, 3.07K subscribers) holds 10 videos totalling 10m45s, averaging
~65 seconds. Reaching 4,000 watch hours (240,000 minutes) at that average with 60% retention
requires roughly 370,000 complete views.

**This funnel will not by itself reach the watch-hour threshold.** It is still worth building:
it produces real traffic, a durable email list, and compliant watch time that compounds. But
monetization realistically requires either the Shorts path (10M Shorts views in 90 days, which
suits the existing format) or new 8–15 minute videos built from existing course material.

This spec builds the funnel. Content strategy is out of scope.

## Non-goals

- Paid Pinterest ad campaigns (run only after organic pins prove which creative converts)
- Per-course video production
- An email service provider integration (Firestore now; ESP is a later, separable step)
- Redesigning course pages beyond the additions described here

## Components

### 1. Pinterest domain claim

Add to `index.html` `<head>` only — Pinterest verifies the root domain:

```html
<meta name="p:domain_verify" content="PINTEREST_VERIFICATION_CODE_GOES_HERE">
```

The value comes from Pinterest → Settings → Claimed accounts → Claim website → meta tag.
It is committed as the literal placeholder string above and replaced by the user.

**Nothing else in this spec produces Pinterest analytics or Rich Pins until the domain is
claimed.** This ships first.

### 2. Rich Pin metadata across 341 course pages

Course pages currently have no `og:*`, no `canonical`, and no `meta description`. Only
`index.html` has them.

A Node script, `scripts/pinterest/add-course-meta.mjs`, walks `courses/*/index.html` and injects
into each `<head>`. Course title comes from `extractMeta(slug)` (see §3) so title handling stays
consistent with the quiz tooling; the description is read directly from the page.

| Tag | Source |
|---|---|
| `meta description` | existing `<p>` in `.course-header`, truncated to 160 chars |
| `link canonical` | `https://mathagram.org/courses/<slug>/` |
| `og:type` | `article` (Pinterest Article Rich Pin) |
| `og:site_name` | `Mathagram` |
| `og:title` | existing `<h1>` + ` — Mathagram` |
| `og:description` | same as meta description |
| `og:url` | canonical URL |
| `og:image` | `https://mathagram.org/assets/lighthouse/og-card.png` (landscape, shared) |
| `article:section` | category from `.course-badge` text |
| `twitter:card` | `summary_large_image` |
| `twitter:title` / `twitter:description` / `twitter:image` | mirror the OG values |

The script is **idempotent**: it delimits its output with `<!-- pin:meta:start -->` and
`<!-- pin:meta:end -->` and replaces any existing block rather than appending. Re-running after
a course description changes updates the tags in place.

Courses with 3 pin variants (see §3) additionally receive the hidden pin-media element from §3.

This is a significant SEO improvement independent of Pinterest.

### 3. Pin images — 3 variants × top 40 courses

Pinterest's ranking favours *fresh* pins (new images), so multiple distinct images per
destination URL is the growth lever, not one image per course.

**Template:** three SVG templates at 1000×1500 (2:3) in `scripts/pinterest/templates/`:

1. `v1-title.svg` — bold course title on the brand gradient
2. `v2-stat.svg` — "N lessons · 100% free · no signup" stat card
3. `v3-hook.svg` — question hook ("Still confused by integrals?") over the course title

**Rendering:** `scripts/pinterest/gen-pins.mjs` substitutes course data into each template and
rasterizes with **`rsvg-convert`** (v2.61.3, at `/opt/homebrew/bin/rsvg-convert`) — the same tool
that produced `assets/lighthouse/og-card.png` from `og-card.svg`. Output:
`assets/pins/<slug>-v1.png`, `-v2.png`, `-v3.png`.

Two consequences of rsvg-convert that the templates must respect:

- **No web fonts.** Templates declare explicit `font-family` values available locally; text is
  not styled via external CSS.
- **No `<foreignObject>` text wrapping.** SVG `<text>` does not wrap, so the generator computes
  line breaks itself and emits one `<tspan>` per line, with an approximate character-width
  budget per template and a font-size step-down for long course titles.

**Course selection:** the top 40 by total lesson count. Course data comes from the existing
`extractMeta(slug)` in `scripts/quiz-buildout/extract-units.mjs`, which already parses the inline
`const units = [...]` array out of a course page and returns `courseName`, `unitNames`, and
`lessonsPerUnit`. It handles both the tuple format and the `unitNames.map(...)` format, so no
second parser is written.

Rationale for capping at 40: long-tail courses have negligible Pinterest search volume, and
341×3 PNGs would add ~150 MB of binaries to a repo on a disk at 99% capacity.

Note: `extract-units.mjs` is currently untracked in git. It must be committed before the pin
scripts can depend on it.

Expected output: ~120 PNGs, ~20 MB.

**Wiring into pages:** `og:image` stays landscape for Twitter/Facebook. Pinterest's save button
is pointed at the vertical image with a hidden element:

```html
<img src="/assets/pins/<slug>-v1.png" alt="" data-pin-media="/assets/pins/<slug>-v1.png"
     data-pin-description="<course title> — free interactive lessons on Mathagram"
     style="display:none">
```

Variants v2 and v3 are pinned manually from the Pinterest UI; they exist as assets, not as page
elements.

### 4. Click-to-play YouTube embeds

**Component:** `js/video-embed.js` exports a function that renders a *facade* — the video
thumbnail from `https://i.ytimg.com/vi/<id>/maxresdefault.jpg` plus a play button — and swaps in
a `https://www.youtube-nocookie.com/embed/<id>` iframe only on click.

Rationale: no third-party JavaScript or cookies load until the user acts; the page stays fast;
and playback is unambiguously user-initiated, which is what makes the view valid. **Autoplay is
never used** — autoplayed or hidden embeds risk being filtered as invalid views.

**Video map:** `js/videos.js`, keyed by course slug:

| Key | Video ID | Title |
|---|---|---|
| `calculus` | `5NfBbViWmRQ` | What are Integrals for kids |
| `circuits` | `P3lDex2QSPI` | What are Circuits for kids |
| `clustering-and-classification` | `8buAOAnFU64` | Clustering & Classification for kids |
| `algebra` | `fymLtux-g3c` | Sigma Notation for kids |
| `social-media-rules` | `VRroVDswkE4` | Before You Post: Edam's 12 Must-Know Rules |
| `_home` | `E1jJj3Pklz4` | This Site Teaches EVERYTHING For Free |

Unmapped courses render no embed. Videos not in the map (`LW2a87Tj2iQ`, `KCFniwSsbpQ`,
`NyisUTZFZSE`, `eed7efthjho`) are retained in the file as a commented inventory so future
mappings do not require re-scraping the channel.

**CSP — required, or embeds fail silently in production.** `_headers` gains, in both the
`/*.html` and `/` blocks:

- `frame-src`: `https://www.youtube-nocookie.com`
- `img-src`: `https://i.ytimg.com`

CSP stays in `_headers` and never moves to `<meta>`, so translate.goog continues to work.

A channel link (`https://www.youtube.com/@Mathagram_Org`) is added to the site footer.

### 5. Email capture

**Storage:** new Firestore collection `subscribers`, documents shaped:

```
{ email: string (≤254 chars), source: string (course slug or 'footer'),
  role: 'parent' | 'teacher' | 'learner', createdAt: serverTimestamp }
```

**Rules** (`firestore.rules`) — create-only, never readable from the client:

```
match /subscribers/{id} {
  allow create: if request.resource.data.email is string
    && request.resource.data.email.size() <= 254
    && request.resource.data.email.matches('^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$')
    && request.resource.data.role in ['parent','teacher','learner']
    && request.resource.data.source is string
    && request.resource.data.source.size() <= 64;
  allow read, update, delete: if false;
}
```

**Component:** `js/subscribe.js` renders the form and writes via the existing Firebase SDK.

**Spam defense:** a honeypot input (hidden, must stay empty), plus a client-side throttle of one
submission per 60 seconds per browser via `localStorage`.

**COPPA:** the site serves children — `firestore.rules` already gates posts on an `under13`
flag. Collecting email addresses from under-13 users would require verifiable parental consent.
The form therefore:

- is addressed to parents and teachers in its copy, not to kids
- requires an explicit role selection (`parent` / `teacher` / `learner 13+`)
- requires a checked affirmation before the submit button enables
- is **not** rendered on any page behind the kid-facing lesson flow

**Placement:** bottom of course pages, and in the site footer.

**Privacy policy:** `privacy.html` gains a section covering what is collected (email, role,
source page), why (new-lesson notifications), that it is never sold or shared, and how to
request deletion. Drafted for user approval before commit.

### 6. Measurement

- GA4 (`G-1JKG4MN6XX`) events: `video_play` (params: `video_id`, `course`) and `subscribe`
  (params: `source`, `role`).
- UTM convention for Pinterest, documented in `docs/pinterest-playbook.md`:
  `?utm_source=pinterest&utm_medium=social&utm_campaign=<course-slug>&utm_content=v<1|2|3>`
  — `utm_content` identifies which pin variant converted, which is what tells you where to
  spend later.
- Verification that the funnel works end to end: YouTube Studio → Analytics → Traffic sources →
  External should show `mathagram.org` rising.

## File manifest

**New**
- `js/video-embed.js`, `js/videos.js`, `js/subscribe.js`
- `scripts/pinterest/add-course-meta.mjs`, `gen-pins.mjs`
- `scripts/pinterest/templates/v1-title.svg`, `v2-stat.svg`, `v3-hook.svg`
- `assets/pins/*.png` (~120)
- `docs/pinterest-playbook.md`

**Modified**
- `index.html` — domain-verify tag, homepage embed
- `courses/*/index.html` — meta block (341), embed + subscribe mounts (mapped courses only)
- `_headers` — CSP `frame-src` / `img-src`
- `firestore.rules` — `subscribers` collection
- `privacy.html` — email collection section

**Reused as-is**
- `scripts/quiz-buildout/extract-units.mjs` — `extractMeta(slug)`; currently untracked, must be
  committed first

## Verification

1. `scripts/serve_local.mjs` — load a course page, confirm meta tags present and correct.
2. Browser console clean of CSP violations with an embed on the page; clicking the facade loads
   the iframe and plays.
3. Meta block re-run: run `add-course-meta.mjs` twice, confirm `git diff` is empty on the second
   run (idempotency).
4. Subscribe: valid submission writes a document; honeypot-filled submission does not; reading
   the collection from the client is denied.
5. Pin images: spot-check three PNGs are exactly 1000×1500 and legible at Pinterest feed size.
6. Deploy with the full 5-path Netlify cleanup, then verify a live course page's headers carry
   the updated CSP.

## Manual steps required from the user

1. Provide the Pinterest verification code (blocks §1, and §1 blocks Pinterest analytics).
2. Create the Pinterest business account and boards.
3. Approve the privacy policy wording.
4. Deploy to Netlify (git push does not publish; direct upload with full clean is required).

## Risks

| Risk | Mitigation |
|---|---|
| Embeds silently blocked by CSP in prod | CSP change is part of the same change set; verified against the live site after deploy |
| Editing 341 files breaks pages | Idempotent, delimited injection; verify on a 3-course subset before the full run |
| Subscriber spam | Honeypot + throttle + create-only rules; revisit if abused |
| COPPA exposure | Role gate, affirmation, parent/teacher copy, no placement in kid-facing flows |
| Disk at 99% | Scope capped at ~20 MB of PNGs; `/free-space` available if needed |
| Pinterest results look flat early | Pinterest has a 45–90 day ramp; judge on outbound clicks, not impressions |
