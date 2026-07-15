#!/usr/bin/env python3
"""Build the Mathagram "How Voices Work" pitch-ladder intro reel.

Pipeline (all local):
  1. say -> per-character audio in their real voice (pitch via [[pbas]], rate via -r)
  2. HTML slide per segment -> Chrome headless screenshot -> PNG (1920x1080)
  3. ffmpeg: image + audio -> per-segment MP4, then concat -> final MP4

See docs/superpowers/specs/2026-06-14-voices-intro-reel-design.md
"""
import os
import subprocess
import json
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "video", "voices-reel")
CHARS_DIR = os.path.join(ROOT, "assets", "characters")
FINAL = os.path.join(ROOT, "assets", "video", "voices-intro-reel.mp4")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

os.makedirs(OUT, exist_ok=True)

# pitch (web speech 0.5-1.8) -> say [[pbas N]];  rate (web) -> say -r wpm
def pbas(pitch):
    return round(30 + (pitch - 0.5) * 30)

def wpm(rate):
    return round(175 * rate)

# order = low pitch -> high pitch
CHARACTERS = [
    {"id": "william", "name": "William", "role": "the wise one", "voice": "Rishi",
     "pitch": 0.5, "rate": 0.75, "color": "#6C5CE7",
     "line": "Listen closely, young ones. Every voice begins as a tiny shiver of air. We call that a vibration."},
    {"id": "james", "name": "James", "role": "the strong one", "voice": "Albert",
     "pitch": 0.6, "rate": 0.85, "color": "#E74C3C",
     "line": "My voice is big and low! Low voices come from slow, heavy vibrations."},
    {"id": "edam", "name": "Edam", "role": "the bear", "voice": "Daniel",
     "pitch": 0.8, "rate": 0.9, "color": "#B5651D",
     "line": "Hello there. The faster the air shakes, the higher the voice climbs. Watch us go up!"},
    {"id": "diego", "name": "Diego", "role": "the researcher", "voice": "Ralph",
     "pitch": 1.0, "rate": 1.0, "color": "#16A085",
     "line": "I'm right in the middle: a calm, even pitch. Not too low, not too high."},
    {"id": "steve", "name": "Steve", "role": "the fox", "voice": "Fred",
     "pitch": 1.2, "rate": 1.15, "color": "#E67E22",
     "line": "Heh, my voice is quicker and a touch higher. Hear the difference?"},
    {"id": "gosia", "name": "Gosia", "role": "the friend", "voice": "Moira",
     "pitch": 1.4, "rate": 1.05, "color": "#E84393",
     "line": "Hi! My voice is brighter and higher still."},
    {"id": "sam", "name": "Sam", "role": "the kid", "voice": "Samantha",
     "pitch": 1.6, "rate": 1.3, "color": "#0984E3",
     "line": "I'm a kid, so my voice is high and zippy and fast!"},
    {"id": "rita", "name": "Rita", "role": "the cat", "voice": "Karen",
     "pitch": 1.8, "rate": 1.2, "color": "#9B59B6",
     "line": "Meow! I'm the highest of all: super fast, super tiny vibrations!"},
]

OUTRO = {"id": "edam", "voice": "Daniel", "pitch": 0.8, "rate": 0.9, "color": "#2D3436",
         "line": "Now you know. Your voice is made of vibrations, and it's one of a kind."}

N = len(CHARACTERS)


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def gen_audio(voice, pitch, rate, line, out_wav):
    aiff = out_wav.replace(".wav", ".aiff")
    text = f"[[pbas {pbas(pitch)}]] {line}"
    run(["say", "-v", voice, "-r", str(wpm(rate)), text, "-o", aiff])
    run(["ffmpeg", "-y", "-i", aiff, "-ar", "44100", "-ac", "2", out_wav],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(aiff)
    dur = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", out_wav]).decode().strip()
    return float(dur)


def pitch_meter(active_index):
    """Vertical ladder, rung 0 = bottom (low), rung N-1 = top (high)."""
    rungs = []
    for i in range(N - 1, -1, -1):  # top to bottom in DOM
        on = "on" if i <= active_index else ""
        cur = "cur" if i == active_index else ""
        rungs.append(f'<div class="rung {on} {cur}"></div>')
    return "\n".join(rungs)


SLIDE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html,body { width:1920px; height:1080px; overflow:hidden;
  font-family:-apple-system,'Helvetica Neue',sans-serif; }
.stage { width:1920px; height:1080px; position:relative; display:flex;
  align-items:center; justify-content:flex-start; }
.title { position:absolute; top:54px; left:0; right:0; text-align:center;
  font-size:46px; font-weight:800; color:#fff; letter-spacing:1px;
  text-shadow:0 3px 10px rgba(0,0,0,.25); opacity:.95; }
.char { width:760px; display:flex; flex-direction:column; align-items:center;
  margin-left:120px; }
.char img { width:520px; height:520px;
  filter:drop-shadow(0 18px 30px rgba(0,0,0,.30)); }
.name { margin-top:18px; font-size:64px; font-weight:800; color:#fff;
  text-shadow:0 3px 8px rgba(0,0,0,.25); }
.role { font-size:30px; font-weight:600; color:rgba(255,255,255,.85);
  margin-top:2px; }
.caption { position:absolute; left:120px; right:380px; bottom:70px;
  background:rgba(255,255,255,.94); border-radius:28px; padding:34px 44px;
  font-size:46px; line-height:1.32; font-weight:700; color:#1d2330;
  box-shadow:0 14px 40px rgba(0,0,0,.22); }
.meter { position:absolute; right:120px; top:170px; bottom:170px; width:150px;
  display:flex; flex-direction:column; align-items:center; }
.meter .lbl { font-size:26px; font-weight:800; color:#fff; letter-spacing:2px;
  text-shadow:0 2px 6px rgba(0,0,0,.3); }
.meter .ladder { flex:1; display:flex; flex-direction:column;
  justify-content:space-between; padding:18px 0; width:96px; }
.rung { height:54px; border-radius:14px; background:rgba(255,255,255,.22);
  border:3px solid rgba(255,255,255,.35); }
.rung.on { background:rgba(255,255,255,.92);
  border-color:#fff; box-shadow:0 0 18px rgba(255,255,255,.5); }
.rung.cur { transform:scaleX(1.28); background:#FFE66D; border-color:#fff;
  box-shadow:0 0 26px rgba(255,230,109,.9); }
"""


def slide_html(c, idx):
    img = os.path.join(CHARS_DIR, c["id"] + ".svg")
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>{SLIDE_CSS}
.stage {{ background:radial-gradient(circle at 35% 35%, {c['color']}, {darken(c['color'])}); }}
</style></head><body>
<div class="stage">
  <div class="title">HOW VOICES WORK &middot; the Mathagram crew</div>
  <div class="char">
    <img src="file://{img}">
    <div class="name">{html.escape(c['name'])}</div>
    <div class="role">{html.escape(c['role'])}</div>
  </div>
  <div class="caption">{html.escape(c['line'])}</div>
  <div class="meter">
    <div class="lbl">HIGH</div>
    <div class="ladder">{pitch_meter(idx)}</div>
    <div class="lbl">LOW</div>
  </div>
</div></body></html>"""


def card_html(big, small, color):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{SLIDE_CSS}
.stage {{ background:radial-gradient(circle at 50% 40%, {color}, {darken(color)});
  flex-direction:column; align-items:center; justify-content:center; }}
.big {{ font-size:96px; font-weight:900; color:#fff; text-align:center;
  max-width:1500px; line-height:1.12; text-shadow:0 5px 16px rgba(0,0,0,.3); }}
.small {{ font-size:44px; font-weight:600; color:rgba(255,255,255,.9);
  margin-top:34px; }}
</style></head><body><div class="stage">
  <div class="big">{html.escape(big)}</div>
  <div class="small">{html.escape(small)}</div>
</div></body></html>"""


def darken(hexcol, f=0.55):
    h = hexcol.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return f"#{int(r*f):02x}{int(g*f):02x}{int(b*f):02x}"


def render_png(html_str, out_png):
    tmp = out_png.replace(".png", ".html")
    with open(tmp, "w") as f:
        f.write(html_str)
    run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
         "--force-device-scale-factor=1", "--window-size=1920,1080",
         f"--screenshot={out_png}", f"file://{tmp}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def seg_mp4(png, wav, dur, out_mp4):
    run(["ffmpeg", "-y", "-loop", "1", "-i", png, "-i", wav,
         "-t", f"{dur:.3f}", "-r", "30",
         "-vf", "scale=1920:1080,format=yuv420p",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-shortest", out_mp4],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def card_mp4(png, dur, out_mp4):
    """Silent card with a matching silent audio track for clean concat."""
    run(["ffmpeg", "-y", "-loop", "1", "-i", png,
         "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
         "-t", f"{dur:.3f}", "-r", "30",
         "-vf", "scale=1920:1080,format=yuv420p",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", out_mp4],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    segments = []

    # Title card
    print("title card...")
    p = os.path.join(OUT, "00_title.png")
    render_png(card_html("How Voices Work", "with the Mathagram crew", "#2D6CDF"), p)
    m = os.path.join(OUT, "00_title.mp4")
    card_mp4(p, 3.8, m)
    segments.append(m)

    # Character segments
    for i, c in enumerate(CHARACTERS):
        print(f"segment {i+1}/{N}: {c['name']} ({c['voice']})...")
        wav = os.path.join(OUT, f"{i+1:02d}_{c['id']}.wav")
        dur = gen_audio(c["voice"], c["pitch"], c["rate"], c["line"], wav)
        png = os.path.join(OUT, f"{i+1:02d}_{c['id']}.png")
        render_png(slide_html(c, i), png)
        m = os.path.join(OUT, f"{i+1:02d}_{c['id']}.mp4")
        seg_mp4(png, wav, dur + 0.45, m)
        segments.append(m)

    # Outro spoken line (Edam) over outro card
    print("outro...")
    owav = os.path.join(OUT, "98_outro.wav")
    odur = gen_audio(OUTRO["voice"], OUTRO["pitch"], OUTRO["rate"], OUTRO["line"], owav)
    opng = os.path.join(OUT, "98_outro.png")
    render_png(card_html("Every voice is unique.",
                         "And every voice is yours. — Mathagram", OUTRO["color"]), opng)
    om = os.path.join(OUT, "98_outro.mp4")
    seg_mp4(opng, owav, odur + 0.7, om)
    segments.append(om)

    # Concat
    print("concatenating...")
    listfile = os.path.join(OUT, "concat.txt")
    with open(listfile, "w") as f:
        for s in segments:
            f.write(f"file '{s}'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listfile,
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", FINAL],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    tot = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", FINAL]).decode().strip()
    print(f"\nDONE -> {FINAL}  ({float(tot):.1f}s)")


if __name__ == "__main__":
    main()
