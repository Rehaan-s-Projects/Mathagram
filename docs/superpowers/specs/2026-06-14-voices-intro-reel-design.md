# Mathagram "How Voices Work" — Pitch Ladder Intro Reel

**Date:** 2026-06-14
**Status:** Approved approach (A), pending script + spec sign-off

## Goal

A ~90-second kids' video that doubles as (1) a character intro reel and (2) a
mini-lesson about voices/sound. The 8 Mathagram characters appear ordered from
the deepest voice to the highest, each speaking in their **real macOS `say`
voice**, while an on-screen pitch meter climbs. The reel demonstrates what it
teaches: voices are vibrating air; slow vibration = low pitch, fast = high.

## The 8 characters (the non-bird cast — the 8 with existing intro audio)

Ordered low → high pitch:

| # | Character | Role | `say` voice | Web pitch | `say` rate (wpm) |
|---|-----------|------|-------------|-----------|------------------|
| 1 | William | old wise man | Rishi    | 0.5 | ~131 |
| 2 | James   | strongman    | Albert   | 0.6 | ~149 |
| 3 | Edam    | bear         | Daniel   | 0.8 | ~158 |
| 4 | Diego   | researcher   | Ralph    | 1.0 | ~175 |
| 5 | Steve   | fox          | Fred     | 1.2 | ~201 |
| 6 | Gosia   | girl         | Moira    | 1.4 | ~184 |
| 7 | Sam     | kid          | Samantha | 1.6 | ~228 |
| 8 | Rita    | cat          | Karen    | 1.8 | ~210 |

`say` rate ≈ 175 × (Web rate from `js/characters.js` VOICE_SETTINGS).
Pitch is applied with the embedded `[[pbas N]]` command so the heard pitch
matches the on-screen meter. pbas mapping (to test/tune): `pbas = round(30 + (pitch-0.5)*30)` → range ~30 (William) to ~69 (Rita).

## Script (8 lines + outro) — DRAFT FOR REVIEW

- **Title card (text, ~4s):** "How Voices Work — with the Mathagram Crew"
- **1. William:** "Listen closely, young ones. Every voice begins as a tiny shiver of air. We call that a vibration."
- **2. James:** "My voice is big and low! Low voices come from slow, heavy vibrations."
- **3. Edam:** "Hello there. The faster the air shakes, the higher the voice climbs. Watch us go up!"
- **4. Diego:** "I'm right in the middle — a calm, even pitch. Not too low, not too high."
- **5. Steve:** "Heh — my voice is quicker and a touch higher. Hear the difference?"
- **6. Gosia:** "Hi! My voice is brighter and higher still."
- **7. Sam:** "I'm a kid, so my voice is high and zippy and fast!"
- **8. Rita:** "Meow! I'm the highest of all — super fast, super tiny vibrations!"
- **Outro (Edam, ~5s):** "Now you know — your voice is made of vibrations, and it's one of a kind."
- **Outro card (text):** "Every voice is unique. Explore more at Mathagram!"

## Pipeline (all local — no external services, nothing deploys)

1. **Audio:** for each character, `say -v <Voice> -r <wpm> "[[pbas N]] <line>" -o seg.aiff`, then ffmpeg → normalized WAV. Outro line uses Edam's voice.
2. **Visuals:** render each character's existing `assets/characters/<id>.svg` to PNG (via headless Chrome — already used in this repo — or rsvg/ImageMagick if present). Compose a bright 1920×1080 slide: character art, the spoken caption (large, kid-friendly), and a low→high **pitch meter** filled to that character's level (1/8 … 8/8).
3. **Assemble:** each segment's duration = its audio length + ~0.4s pad; build per-segment MP4s (image + audio), then ffmpeg-concat with title and outro cards → final **MP4** (1080p, H.264, AAC).

## Output

- Working files: `assets/video/voices-reel/` (audio segments, PNG slides, segment MP4s).
- Final: `assets/video/voices-intro-reel.mp4`.
- Standalone artifact for review/publishing. **No Netlify deploy** as part of this task.

## Out of scope (YAGNI)

- Birds Babel/Lingo (no intro audio; keeps it to a clean 8).
- invideo / any external generation.
- Subtitles file, multiple aspect ratios, music bed (can add later if wanted).
- Publishing to the live site.

## Success criteria

- MP4 plays start-to-finish; all 8 characters audible in their distinct voices.
- Heard pitch visibly climbs William → Rita and matches the on-screen meter.
- Captions readable; total length 75–100s.
