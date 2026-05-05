# Python Translation Mode — Design

**Date:** 2026-05-03
**Status:** Approved (pending implementation)

## Summary

Add "Python" as a selectable mode in Mathagram's existing translate dropdown. Unlike the 130+ real-language entries (which pipe through Google Translate), Python mode is a client-side text transform that rewrites visible English prose with Python keyword/idiom equivalents (e.g., `function`→`def`, `True/False/None`) and rewrites math notation as Python expressions (e.g., `f(x)=x²`→`def f(x): return x**2`).

The mode lives in a new "Fun modes" section at the bottom of the dropdown — visually distinct from real languages so users don't expect Google-quality output, and extensible for future modes (Pirate, Yoda, etc.).

## Goals

- Add a single "🐍 Python (programmer mode)" entry to the translate dropdown.
- When activated, transform visible page text using both a prose word-skin and a math-expression rewriter.
- Persist the choice across pages via `localStorage`.
- Cleanly toggle off (restore original English) when the user picks any other language or English.
- Coexist safely with Google Translate: clear `googtrans` cookie before activating; deactivate before letting Google Translate run.

## Non-goals (YAGNI)

- Other fun modes (Pirate, Yoda) — section is structured to extend, but only Python ships.
- Server-side rendering or pre-baked Python HTML files.
- Translating the Lingo & Babel mascot header copy (it's marketing copy, not lesson content).
- Comprehensive English-to-Python translation of arbitrary prose — the dictionary is curated, not exhaustive.

## Architecture

A new ES module `js/python-translate.js` holds the transform engine. `js/nav.js` adds a "Fun modes" section to the existing translate dropdown and lazy-imports the engine on first activation. Mode persists in `localStorage['mathagram-mode'] = 'py'`. Original text is preserved in a `WeakMap<TextNode, string>` so deactivation cleanly restores English.

```
click 🐍 → clear googtrans cookie → localStorage='py' → dynamic import python-translate.js
        → activate(): walk DOM, transform text nodes, install MutationObserver
page load → nav.js init → if localStorage='py', auto-activate
click any other lang or English → deactivate() restores from WeakMap → existing flow runs
```

## Components

### `js/python-translate.js`

Exports `{ activate, deactivate, isActive }`.

**Module-private state:**

- `_originalsText: WeakMap<Text, string>` — backup of pre-transform text-node content for clean restore.
- `_originalsAttr: WeakMap<Element, Map<string, string>>` — backup of pre-transform `placeholder/title/aria-label` values per element.
- `_observer: MutationObserver | null`
- `_active: boolean`
- `_applying: boolean` — flag to prevent feedback loops while we mutate text.

**`wordMap`** — ordered list of `[RegExp, string]` for prose. ~40 entries. Word-boundary anchored; preserves leading capitalization where it makes sense.

Curated entries (initial set):

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
| `print` (when imperative) | `print` |
| `return` | `return` |
| `import` / `imports` | `import` |
| `length of` | `len()` of |
| `range from A to B` | `range(A, B)` |
| `lambda function` | `lambda` |
| `class(es)` | `class` |
| `inherit(s) from` | `(parent)` |
| `iterate over` | `for ... in` |

These are illustrative — the implementer should iterate based on what reads well in actual Mathagram lesson copy.

**`mathMap`** — `[RegExp, string | (match) => string]` for math expressions. Fires only on text fragments matching a "looks like math" guard (contains `=`, `f(x)`, digit-letter juxtaposition, Unicode superscript, or LaTeX delimiters). Conservative — false positives in plain prose are worse than false negatives in math.

Initial rules:

- `xⁿ` (Unicode superscripts ²³⁴⁵⁶⁷⁸⁹⁰¹) → `x**n`
- `(\d+)([a-zA-Z])` → `\1*\2` (implicit multiplication: `2x` → `2*x`)
- `=` (single equals, not `==` or `!=`) inside math context → `==`
- `\\sqrt\{(.+?)\}` → `math.sqrt(\1)`
- `\\frac\{(.+?)\}\{(.+?)\}` → `(\1)/(\2)`
- `f\(x\)\s*=\s*(.+)` → `def f(x): return \1`
- `\\(\)` and `$$ $$` LaTeX delimiters: process the inside, drop the delimiters.

**DOM walker** — `walkAndTransform(root)`:

- `TreeWalker` over `NodeFilter.SHOW_TEXT` rooted at `root` (defaults to `document.body`).
- Skip if any ancestor matches: `SCRIPT, STYLE, CODE, PRE, TEXTAREA, INPUT, [contenteditable], [data-no-py]`.
- For each text node: store original in `_originals` if not already stored; apply `wordMap` then `mathMap`; assign back to `node.textContent`.
- Also processes `placeholder`, `title`, `aria-label` attributes on elements outside `[data-no-py]`.

**`MutationObserver`** — installed on `document.body` with `{ childList: true, subtree: true, characterData: true }`. Debounced ~50ms via `setTimeout`. On fire: collect newly-added nodes from records, run `walkAndTransform` on each. Guarded by `_applying` flag — set true before our mutations, false after a microtask.

**`activate()`** — idempotent. Sets `_active = true`, walks `document.body`, installs observer.

**`deactivate()`** — disconnects observer, restores all entries in `_originalsText` to their text nodes and `_originalsAttr` to their elements, clears both maps, sets `_active = false`.

**`isActive()`** — returns `_active`.

### `js/nav.js` changes

- After the existing `languages.forEach(...)` block (around line 233), append a divider element and a "Fun modes" subheader, then a single button entry: `🐍 Python (programmer mode)`. The container element is marked `data-no-py` so the engine doesn't rewrite "Python (programmer mode)" itself.
- The Python entry's click handler:
  1. Hide dropdown.
  2. Clear `googtrans` cookie (same logic as the English-reset branch in `translatePage`).
  3. Set `localStorage.setItem('mathagram-mode', 'py')`.
  4. Dynamic `import('./python-translate.js').then(m => m.activate())`.
- In `initNav()` (top of file), after `DOMContentLoaded`: if `localStorage.getItem('mathagram-mode') === 'py'`, dynamic-import and call `activate()`.
- In the existing per-language click handler, before calling `translatePage(code)`: if `isActive()` (lazy check), call `deactivate()` and clear `localStorage['mathagram-mode']`. This ensures Python and Google Translate never run simultaneously.
- Skip `scheduleResortAfterTranslation` for Python mode — alphabetical sort doesn't apply since text is still English-rooted.

### `js/python-translate.test.html`

Standalone manual-test page. Loads `python-translate.js` as a module, runs ~20 fixture pairs `[inputHTML, expectedText]`, renders pass/fail rows. Covers:

- Single-word substitutions (`function` → `def`).
- Multi-word patterns (`for each x in items` → `for x in items`).
- Math: `f(x) = x²`, `2x + 3 = 7`, `\(x^2 + 1\)`.
- Negatives: code in `<code>` blocks unchanged; text in `[data-no-py]` unchanged.
- Activation/deactivation round-trip restores original.

## Data flow (detail)

**On user clicking 🐍:**

1. `nav.js` click handler runs.
2. Clears `googtrans` cookie via `document.cookie = 'googtrans=; expires=...; path=/'` (and the domain variant).
3. Sets `localStorage['mathagram-mode'] = 'py'`.
4. `await import('./python-translate.js')`.
5. Calls `module.activate()`.
6. `activate()` walks `document.body`, transforms text nodes, installs `MutationObserver`.

**On page load (any page):**

1. `initNav()` runs (existing).
2. New code: if `localStorage['mathagram-mode'] === 'py'`, after DOM ready, dynamic-import and `activate()`.
3. `activate()` walks the page; observer catches anything rendered later (learning path, modals, lesson cards).

**On user clicking any real language (or English):**

1. Existing per-language handler runs.
2. New guard: if Python mode is active, call `deactivate()` and clear `localStorage['mathagram-mode']`.
3. Existing `translatePage(code)` runs as today.

## Error handling

- Per-node transform wrapped in `try { ... } catch (e) { console.warn(...) }`. A regex failure on one node never stops the walk.
- `activate()` is idempotent: calling it while already active is a no-op.
- `deactivate()` is safe to call when not active.
- If `document.body` is missing (script loaded before body), `activate()` defers via `requestAnimationFrame`.
- If the dynamic import fails (offline, network error), the click handler logs a warning and leaves the page unchanged — the user can simply pick a real language instead.
- If Google Translate is mid-render when the user clicks Python, we wait one animation frame after clearing the cookie before walking, so we don't fight `<font>` insertions.

## Testing

No existing test framework in the repo. Verification has two parts:

1. **`js/python-translate.test.html`** — manual fixture-based test page (described above). Opened in a browser; pass/fail visible inline.
2. **Manual smoke checklist** (run before merge):
   - Homepage: activate, confirm tile titles transform, courses-grid still renders.
   - Courses page: activate, confirm course names transform, search box still functional.
   - Calculus course page: activate, confirm unit/lesson titles transform, learning-path zigzag still draws.
   - A calculus lesson with math (e.g., lesson with `f(x) = x²`): confirm math transforms; LaTeX-wrapped equations transform inside the delimiters.
   - Toggle on → off → on: original text restored on each cycle.
   - Activate Python, then pick Spanish: Python deactivates cleanly, Google Translate takes over.
   - Reload after activating: page comes up already in Python mode (localStorage persistence).
   - Lingo & Babel dropdown header text is NOT rewritten (lives under `[data-no-py]`).

## Edge cases / risks

- **Mutation feedback loop**: `_applying` flag plus the "store original on first transform" check in `_originals` prevents re-transforming our own output.
- **Google Translate's `<font>` wrappers**: when a real language is active and the user clicks Python, our cookie-clear + frame-wait avoids walking partially-translated DOM. The observer will pick up Google's removal of its wrappers as `characterData` mutations, which we then re-walk cleanly.
- **Forms inside `[data-no-py]`**: the dropdown's "Search 130+ languages…" placeholder must NOT be rewritten. The dropdown wrapper gets `data-no-py`.
- **Performance on large pages**: a course page with 800+ lesson titles is the worst case. The initial walk should still complete under ~50ms; if it doesn't, batch via `requestIdleCallback`. Watch during smoke testing.
- **Course tiles' alphabetical re-sort**: existing `scheduleResortAfterTranslation` only fires on real-language paths. Python mode skips it, which is correct (titles are still English-rooted).

## Files

| File | Action | Approx LOC |
|---|---|---|
| `js/python-translate.js` | NEW | ~250 |
| `js/python-translate.test.html` | NEW | ~80 |
| `js/nav.js` | MODIFY | +30 |

## Open questions

None at design time. Implementer should confirm during smoke test that the curated `wordMap` reads naturally on real Mathagram content; iterate the dictionary if specific phrases sound off.
