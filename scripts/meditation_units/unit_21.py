#!/usr/bin/env python3
"""Meditation Unit 21 — Sleep & Insomnia (lessons 301-315)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Why Sleep Matters",
     "body_html": r"""<p>Sleep clears metabolic waste, consolidates memory, regulates hormones. Adults need 7–9 hours. Chronic sleep loss is linked to anxiety, depression, immune dysfunction.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Adults need ___-9 hours.", "answer": "7"},
         {"type": "multiple-choice", "question": "Sleep clears: ", "options": ["metabolic waste", "books", "muscle", "thoughts only"], "correctIndex": 0},
         {"type": "true-false", "question": "Chronic loss links to anxiety.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sleep consolidates ___.", "answer": "memory"},
         {"type": "true-false", "question": "5 hours is plenty for adults.", "correctAnswer": False}]},
    {"title": "Sleep Stages",
     "body_html": r"""<p>Four stages cycle through the night:</p><ul><li>N1 — light entry sleep.</li><li>N2 — body temperature drops.</li><li>N3 — deep slow-wave sleep; physical recovery.</li><li>REM — vivid dreams; memory and emotion processing.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Deep stage: ___.", "answer": "N3"},
         {"type": "multiple-choice", "question": "Vivid dreams: ", "options": ["REM", "N1", "N2", "N3"], "correctIndex": 0},
         {"type": "true-false", "question": "Stages cycle through the night.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Light entry: ___.", "answer": "N1"},
         {"type": "true-false", "question": "There are 7 sleep stages.", "correctAnswer": False}]},
    {"title": "Yoga Nidra",
     "body_html": r"""<p>Yoga Nidra (\"yogic sleep\") is a 20–45 minute guided practice. Lie still while a teacher's voice walks you through body parts, breath, and intention. Said to give the rest of several hours of sleep.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Length: 20–___ min.", "answer": "45"},
         {"type": "multiple-choice", "question": "Position: ", "options": ["lying", "standing", "running", "sitting straight"], "correctIndex": 0},
         {"type": "true-false", "question": "Yoga Nidra means yogic sleep.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Walks through body parts and ___.", "answer": "breath"},
         {"type": "true-false", "question": "Yoga Nidra requires hard movement.", "correctAnswer": False}]},
    {"title": "Body Scan in Bed",
     "body_html": r"""<p>Lying down, scan from feet to head — release each part. Slows the mind and signals safety to the nervous system. Most people don't make it past the knees before drifting off.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Direction: feet to ___.", "answer": "head"},
         {"type": "multiple-choice", "question": "Signals: ", "options": ["safety", "danger", "hunger", "thirst"], "correctIndex": 0},
         {"type": "true-false", "question": "Most drift off before the knees.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Done lying ___.", "answer": "down"},
         {"type": "true-false", "question": "Body scan should be done while exercising.", "correctAnswer": False}]},
    {"title": "Counting Breaths",
     "body_html": r"""<p>Count breath cycles backwards from 100. If you lose track, start at 100 again. The combination of slight challenge and rhythm settles a busy mind.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Start at ___.", "answer": "100"},
         {"type": "multiple-choice", "question": "Direction: ", "options": ["backwards", "forwards", "random", "skipping"], "correctIndex": 0},
         {"type": "true-false", "question": "Lose track? Start again.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Combines challenge and ___.", "answer": "rhythm"},
         {"type": "true-false", "question": "Counting must be perfect or it fails.", "correctAnswer": False}]},
    {"title": "Sleep Hygiene Basics",
     "body_html": r"""<ul><li>Same wake time daily.</li><li>Cool, dark, quiet room.</li><li>No screens 30 min pre-bed.</li><li>Bed is for sleep and intimacy only.</li><li>If awake 20 min, get up briefly.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Awake ___ min, get up.", "answer": "20"},
         {"type": "multiple-choice", "question": "Bed is for: ", "options": ["sleep and intimacy", "work", "TV", "phone"], "correctIndex": 0},
         {"type": "true-false", "question": "Same wake time daily.", "correctAnswer": True},
         {"type": "fill-blank", "question": "No screens for ___ min.", "answer": "30"},
         {"type": "true-false", "question": "A warm bright room helps sleep.", "correctAnswer": False}]},
    {"title": "Insomnia & Acceptance",
     "body_html": r"""<p>Fighting insomnia worsens it. The instruction: meet the awake state without judgment. "I am awake; that's okay." Often the body falls asleep when the mind stops resisting.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "I am ___.", "answer": "awake"},
         {"type": "multiple-choice", "question": "Effect of fighting: ", "options": ["worsens it", "fixes it", "no effect", "speeds sleep"], "correctIndex": 0},
         {"type": "true-false", "question": "Acceptance often invites sleep.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Meet the state without ___.", "answer": "judgment"},
         {"type": "true-false", "question": "Resistance is the path to sleep.", "correctAnswer": False}]},
    {"title": "Worry Window",
     "body_html": r"""<p>Schedule 15 min "worry time" earlier in the day. If worries pop up at 2am, tell them: "I have a meeting with you at 6pm tomorrow." Mind learns to defer.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Window length: ___ min.", "answer": "15"},
         {"type": "multiple-choice", "question": "Effect: ", "options": ["mind learns to defer", "mind worsens", "no effect", "shortens life"], "correctIndex": 0},
         {"type": "true-false", "question": "Schedule it earlier in the day.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tell worries: meeting at ___pm tomorrow.", "answer": "6"},
         {"type": "true-false", "question": "Worry window encourages 24/7 worry.", "correctAnswer": False}]},
    {"title": "Light Exposure",
     "body_html": r"""<p>Bright daylight in the morning anchors the circadian rhythm. Aim for 10+ minutes outdoors within an hour of waking. Dim lights at home after sunset.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Aim for ___+ min outdoor light.", "answer": "10"},
         {"type": "multiple-choice", "question": "Anchors: ", "options": ["circadian rhythm", "appetite", "metabolism only", "memory only"], "correctIndex": 0},
         {"type": "true-false", "question": "Dim home lights after sunset.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Within an hour of ___.", "answer": "waking"},
         {"type": "true-false", "question": "Bright lights at midnight help sleep.", "correctAnswer": False}]},
    {"title": "Naps",
     "body_html": r"""<p>Short naps (10–20 min) refresh; long ones (60+ min) interfere with night sleep. Best nap window: 1pm–3pm. NSDR (non-sleep deep rest) recordings are an alternative.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Short nap: 10–___ min.", "answer": "20"},
         {"type": "multiple-choice", "question": "Best window: ", "options": ["1pm–3pm", "8pm–10pm", "midnight", "5am"], "correctIndex": 0},
         {"type": "true-false", "question": "Long naps can interfere with night sleep.", "correctAnswer": True},
         {"type": "fill-blank", "question": "NSDR = non-sleep deep ___.", "answer": "rest"},
         {"type": "true-false", "question": "All naps must be 3 hours long.", "correctAnswer": False}]},
    {"title": "Pre-Sleep Routine",
     "body_html": r"""<ul><li>Dim lights 1 hour before bed.</li><li>Warm shower 90 min before bed (drops core temp).</li><li>Brief stretch or yoga.</li><li>Journal or brain dump.</li><li>5 min meditation.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Warm shower ___ min before bed.", "answer": "90"},
         {"type": "multiple-choice", "question": "Final step: ", "options": ["5 min meditation", "loud movie", "shopping online", "argument"], "correctIndex": 0},
         {"type": "true-false", "question": "Journaling before bed helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Dim lights ___ hour before bed.", "answer": "1"},
         {"type": "true-false", "question": "Loud action movies are pre-sleep ideal.", "correctAnswer": False}]},
    {"title": "Working with Nightmares",
     "body_html": r"""<p>Imagery rehearsal therapy: rewrite the nightmare's ending while awake. Practice the new version daily. Within weeks, nightmares often shift or fade.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Rewrite the ___.", "answer": "ending"},
         {"type": "multiple-choice", "question": "Therapy name: ", "options": ["imagery rehearsal", "EMDR", "CBT", "ACT"], "correctIndex": 0},
         {"type": "true-false", "question": "Practice daily while awake.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Nightmares often ___ or fade.", "answer": "shift"},
         {"type": "true-false", "question": "Nightmares cannot be changed.", "correctAnswer": False}]},
    {"title": "Falling Back Asleep at 3am",
     "body_html": r"""<p>Common waking. Don't check the clock. Slow exhale. Body scan. If still awake at 20 min, get up to a dim room and read non-stimulating material. Return when sleepy.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Don't check the ___.", "answer": "clock"},
         {"type": "multiple-choice", "question": "If still awake at 20 min: ", "options": ["get up to dim room", "scroll phone", "eat a meal", "exercise hard"], "correctIndex": 0},
         {"type": "true-false", "question": "Body scan can help.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Read ___-stimulating material.", "answer": "non"},
         {"type": "true-false", "question": "Stay forcing in bed all night.", "correctAnswer": False}]},
    {"title": "Sleep Apps & Tools",
     "body_html": r"""<ul><li>Yoga Nidra recordings (Liam Gillen, Tracee Stanley).</li><li>NSDR (Andrew Huberman or Madefor).</li><li>Calm and Headspace sleep stories.</li><li>White / pink / brown noise.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "NSDR teacher: Andrew ___.", "answer": "Huberman"},
         {"type": "multiple-choice", "question": "Useful color noise: ", "options": ["pink", "purple", "yellow", "neon"], "correctIndex": 0},
         {"type": "true-false", "question": "Sleep stories exist on apps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Yoga Nidra teacher: Tracee ___.", "answer": "Stanley"},
         {"type": "true-false", "question": "No tool can help with sleep.", "correctAnswer": False}]},
    {"title": "Sleep & Insomnia Checkpoint",
     "body_html": r"""<ul><li>Sleep stages: N1, N2, N3, REM.</li><li>Yoga Nidra and body scan support deep rest.</li><li>Hygiene: same wake time, cool dark room, no screens.</li><li>Insomnia responds to acceptance, light, worry-window, gentle routines.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Yoga Nidra is a guided practice.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "REM is when: ", "options": ["vivid dreams happen", "body is awake", "no brain activity", "metabolism stops"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Adults need ___ hours min.", "answer": "7"},
         {"type": "true-false", "question": "Bright bedroom helps sleep.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Andrew Huberman's NSDR = ___-Sleep Deep Rest.", "answer": "Non"}]},
]

if __name__ == "__main__":
    render_unit(21, "Sleep & Insomnia", 301, LESSONS)
