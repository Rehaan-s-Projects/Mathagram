# Python Translation Mode — Design

**Date:** 2026-05-03
**Status:** Approved (pending implementation)
**Revision:** 2 — pivoted from "add Python alongside Google Translate" to "replace Google Translate entirely with Python."

## Summary

Replace Mathagram's Google-Translate-driven translation system with a single client-side **Python translation mode**. The 130+ real-language entries, the Google Translate Element widget, the `.translate.goog` proxy fallback, the `googtrans` cookie handling, and the post-translation course-grid resort are all removed.

What remains is a "Translate" button that toggles between English (default) and Python — a deterministic text transform that rewrites visible English prose with Python keyword/idiom equivalents (`function`→`def`, `True/False/None`) and rewrites math notation as Python expressions (`f(x)=x²`→`def f(x): return x**2`).

## Goals

- Single Python translation mode reachable from the existing Translate button in the nav.
- Toggle on / off cleanly — original English is restored on deactivate.
- Persist the choice across pages via `localStorage['mathagram-mode']`.
- Remove all Google Translate code, language data, proxy logic, and translation-besties reveal logic.
- Keep the Lingo & Babel mascots in the dropdown header — they remain Mathagram's translation guides, just for a different translation now.

## Non-goals (YAGNI)

- Other fun modes (Pirate, Yoda) — punt until requested.
- Server-side rendering or pre-baked Python HTML files.
- Continuing to support real-language translation of any kind (this is the explicit user-approved regression — see "Acknowledged regression" below).
- Comprehensive English-to-Python translation of arbitrary prose — the dictionary is curated, not exhaustive.

## Acknowledged regression

This change removes real-language translation for non-English speakers. Recent work in commits `e9d7084` (Reveal Lingo & Babel translation besties on non-English pages) and `338cd15` (Fix translation-besties detection on the in-place translated homepage) is deliberately reverted. Users who relied on Spanish / French / etc. via the dropdown will lose that capability. This was confirmed explicitly during brainstorming.

## Architecture

A new ES module `js/python-translate.js` holds the transform engine. `js/nav.js` is rewritten to (a) delete the Google Translate code paths and (b) replace the language picker with a two-entry mode picker: **English** (off) and **🐍 Python** (on). Mode persists in `localStorage['mathagram-mode']` (`'py'` or unset). Original text is preserved in WeakMaps so deactivation cleanly restores English.

```
click 🐍 Python  → localStorage='py' → dynamic import python-translate.js → activate()
                 → walk DOM, transform text nodes, install MutationObserver
click English    → deactivate() restores from WeakMaps → clear localStorage
page load        → nav.js init → if localStorage='py', auto-activate
```

## Components

### `js/python-translate.js` (NEW)

Exports `{ activate, deactivate, isActive }`.

**Module-private state:**

- `_originalsText: WeakMap<Text, string>` — backup of pre-transform text-node content for clean restore.
- `_originalsAttr: WeakMap<Element, Map<string, string>>` — backup of pre-transform `placeholder/title/aria-label` values per element.
- `_observer: MutationObserver | null`
- `_active: boolean`
- `_applying: boolean` — flag to prevent feedback loops while we mutate text.

**`wordMap`** — ordered list of `[RegExp, string]` for prose. ~40 entries. Word-boundary anchored.

| English | Python |
|---|---|
| `function(s)` | `def` |
| `true` / `false` / `nothing` / `null` | `True` / `False` / `None` / `None` |
| `for each X in Y` | `for X in Y` |
| `if X then Y` | `if X: Y` |
| `equals` / `is equal to` | `==` |
| `not equal` | `!=` |
| `list(s)` | `list` |
| `dictionary` / `dictionaries` | `dict` |
| `set(s)` | `set` |
| `tuple(s)` | `tuple` |
| `print` (imperative) | `print` |
| `return` | `return` |
| `import` / `imports` | `import` |
| `length of` | `len()` of |
| `range from A to B` | `range(A, B)` |
| `lambda function` | `lambda` |
| `class(es)` | `class` |
| `inherit(s) from` | `(parent)` |
| `iterate over` | `for ... in` |

Illustrative; implementer iterates based on what reads well in real Mathagram copy.

**`mathMap`** — `[RegExp, string | (match) => string]` for math expressions. Fires only on text fragments matching a "looks like math" guard (contains `=`, `f(x)`, digit-letter juxtaposition, Unicode superscript, or LaTeX delimiters).

- `xⁿ` (Unicode superscripts ²³⁴⁵⁶⁷⁸⁹⁰¹) → `x**n`
- `(\d+)([a-zA-Z])` → `\1*\2` (implicit multiplication)
- `=` (single equals, not `==` or `!=`) inside math context → `==`
- `\\sqrt\{(.+?)\}` → `math.sqrt(\1)`
- `\\frac\{(.+?)\}\{(.+?)\}` → `(\1)/(\2)`
- `f\(x\)\s*=\s*(.+)` → `def f(x): return \1`
- `\\(\)` and `$$ $$` LaTeX delimiters: process the inside, drop the delimiters.

**DOM walker** — `walkAndTransform(root)`:

- `TreeWalker` over `NodeFilter.SHOW_TEXT` rooted at `root` (defaults to `document.body`).
- Skip if any ancestor matches: `SCRIPT, STYLE, CODE, PRE, TEXTAREA, INPUT, [contenteditable], [data-no-py]`.
- For each text node: store original in `_originalsText` if not already stored; apply `wordMap` then `mathMap`; assign back to `node.textContent`.
- Also processes `placeholder`, `title`, `aria-label` attributes on elements outside `[data-no-py]`, backing up to `_originalsAttr`.

**`MutationObserver`** — installed on `document.body` with `{ childList: true, subtree: true, characterData: true }`. Debounced ~50ms via `setTimeout`. On fire: collect newly-added nodes, run `walkAndTransform` on each. Guarded by `_applying` flag.

**`activate()`** — idempotent. Sets `_active = true`, walks `document.body`, installs observer.

**`deactivate()`** — disconnects observer, restores all entries in `_originalsText` to text nodes and `_originalsAttr` to elements, clears both maps, sets `_active = false`.

**`isActive()`** — returns `_active`.

### `js/nav.js` — major surgery

**Delete:**

- Lines ~38-43: `.translate.goog` proxy detection block (no longer reachable).
- Lines ~192-217: the `languages` array (130+ entries).
- Lines ~262-318: `loadGoogleTranslateElement()` and the goog-te suppress style block.
- Lines ~320-364: the `translatePage()` function — `.translate.goog` proxy navigation, `googtrans` cookie handling, widget driving, and proxy-fallback `window.open`.
- Lines ~366-end of resort logic: `scheduleResortAfterTranslation()` and its `_resortObserver` / `_resortTimer` state. (Course tiles ship in English-alphabetical order; with no real translation, no resort is needed.)

**Replace:**

- The dropdown's scrollable language list becomes a two-entry list: **English** (default) and **🐍 Python**. Both entries are buttons; clicking dispatches to `setMode('en')` or `setMode('py')`.
- The search input is removed (two entries don't need search).
- The "Search 130+ languages…" placeholder and `.search 130+` UI string are gone.
- Lingo & Babel mascot header **stays**, with copy adjusted: `"Your translation guides — English or Python!"`. The mascot wrapper element is marked `data-no-py` so its label doesn't get rewritten when Python mode is active.

**Add:**

- `setMode(mode)`:
  - `'en'`: dynamic-import `python-translate.js` (it's already loaded if Python was active), call `deactivate()`, `localStorage.removeItem('mathagram-mode')`.
  - `'py'`: `localStorage.setItem('mathagram-mode', 'py')`, dynamic-import `python-translate.js`, call `activate()`.
- In `initNav()` (top of file), after `DOMContentLoaded`: if `localStorage.getItem('mathagram-mode') === 'py'`, dynamic-import and call `activate()`.

### `index.html` — remove translation-besties reveal

**Delete (lines ~197 area and ~215-244):**

- The HTML comment block introducing the "Translation besties" decoration.
- The script that detects `.translate.goog` (or in-place translation) and reveals Lingo & Babel as "translation besties."
- The text update at line ~244 that mentions "translation besties." Replace with copy that no longer mentions translation besties — keep general mascot reference if appropriate.

The Lingo & Babel SVG assets in `assets/characters/` stay (still used by the dropdown header).

### `js/python-translate.test.html` (NEW)

Standalone manual-test page. Loads `python-translate.js` as a module, runs ~20 fixture pairs `[inputHTML, expectedText]`, renders pass/fail rows. Covers:

- Single-word substitutions (`function` → `def`).
- Multi-word patterns (`for each x in items` → `for x in items`).
- Math: `f(x) = x²`, `2x + 3 = 7`, `\(x^2 + 1\)`.
- Negatives: code in `<code>` blocks unchanged; text in `[data-no-py]` unchanged.
- Activation/deactivation round-trip restores original.

## Data flow

**On user clicking 🐍 Python:**

1. `nav.js` click handler runs `setMode('py')`.
2. `localStorage['mathagram-mode'] = 'py'`.
3. `await import('./python-translate.js')`.
4. `module.activate()`.
5. `activate()` walks `document.body`, transforms text nodes, installs `MutationObserver`.

**On user clicking English:**

1. `nav.js` click handler runs `setMode('en')`.
2. If module loaded, call `deactivate()`.
3. `localStorage.removeItem('mathagram-mode')`.

**On page load (any page):**

1. `initNav()` runs.
2. If `localStorage['mathagram-mode'] === 'py'`, after `DOMContentLoaded`, dynamic-import and `activate()`.

## Error handling

- Per-node transform wrapped in `try { ... } catch (e) { console.warn(...) }`. A regex failure on one node never stops the walk.
- `activate()` is idempotent.
- `deactivate()` is safe when not active.
- If `document.body` is missing, `activate()` defers via `requestAnimationFrame`.
- If the dynamic import fails (offline), the click handler logs a warning and leaves the page in English.

## Testing

No existing test framework. Verification is two parts:

1. **`js/python-translate.test.html`** — fixture-based test page.
2. **Manual smoke checklist:**
   - Homepage: activate → tile titles transform; courses-grid still renders; "translation besties" copy is gone.
   - Courses page: activate → course names transform; English toggle restores cleanly.
   - A calculus lesson with math: confirm math transforms; LaTeX-wrapped equations transform inside the delimiters.
   - Toggle on → off → on: original text restored each cycle.
   - Reload after activating: page comes up already in Python mode.
   - Lingo & Babel dropdown header text is NOT rewritten (under `[data-no-py]`).
   - Confirm the `.translate.goog` proxy URL no longer 200s — visiting `mathagram-org.translate.goog/...` should be effectively dead (we don't control Google's proxy, but our own code doesn't generate or follow those URLs anymore).
   - Network tab on page load: no requests to `translate.google.com`.
   - `document.cookie` contains no `googtrans` cookie after page load (even if a stale one exists from prior visits — though we don't actively clear stale cookies, which is fine; they're inert without the widget).

## Edge cases / risks

- **Mutation feedback loop**: `_applying` flag plus the "store original on first transform" check prevents re-transforming our own output.
- **Forms inside `[data-no-py]`**: the dropdown's mascot header text and any future search/filter inputs need `data-no-py` to avoid being rewritten.
- **Performance on large pages**: a course page with 800+ lesson titles is the worst case. Initial walk should complete under ~50ms; if not, batch via `requestIdleCallback`. Watch during smoke.
- **Stale `googtrans` cookies**: users who previously selected a language have a `googtrans` cookie in their browser. With the widget removed, the cookie is inert — no action needed. (Optional cleanup: `setMode('en')` on first load could opportunistically clear it. Cheap insurance; include in the implementation.)
- **External links into `.translate.goog`**: any inbound link from Google's translate proxy will land on Mathagram with no Python mode active and no real translation. That's the regression. Acceptable per user direction.

## Files

| File | Action | Approx LOC |
|---|---|---|
| `js/python-translate.js` | NEW | ~250 |
| `js/python-translate.test.html` | NEW | ~80 |
| `js/nav.js` | MODIFY (mostly deletion) | -200 / +60 |
| `index.html` | MODIFY (remove translation-besties block) | -30 |

## Open questions

None at design time. Implementer should confirm during smoke test that the curated `wordMap` reads naturally on real Mathagram content; iterate the dictionary if specific phrases sound off.
