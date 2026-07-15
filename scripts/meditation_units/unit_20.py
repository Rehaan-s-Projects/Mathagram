#!/usr/bin/env python3
"""Meditation Unit 20 — Stress, Anxiety & Panic (lessons 286-300)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "The Stress Response",
     "body_html": r"""<p>Stress activates the sympathetic nervous system: heart rate up, breath rapid, attention narrowed, digestion paused. Useful in emergencies, exhausting if chronic.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Stress activates the ___ nervous system.", "answer": "sympathetic"},
         {"type": "multiple-choice", "question": "Effect: ", "options": ["heart rate up", "heart rate down", "no change", "vision improves perfectly"], "correctIndex": 0},
         {"type": "true-false", "question": "Chronic stress is exhausting.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Digestion is ___.", "answer": "paused"},
         {"type": "true-false", "question": "Stress narrows attention.", "correctAnswer": True}]},
    {"title": "Box Breathing",
     "body_html": r"""<p>Used by Navy SEALs and clinicians:</p><ul><li>Inhale 4 seconds.</li><li>Hold 4.</li><li>Exhale 4.</li><li>Hold empty 4.</li></ul><p>Repeat 4–8 cycles. Activates the parasympathetic system.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Each phase: ___ seconds.", "answer": "4"},
         {"type": "multiple-choice", "question": "Activates: ", "options": ["parasympathetic", "sympathetic", "neither", "neutral"], "correctIndex": 0},
         {"type": "true-false", "question": "There are 4 phases.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Repeat 4–8 ___.", "answer": "cycles"},
         {"type": "true-false", "question": "Box breathing accelerates panic.", "correctAnswer": False}]},
    {"title": "4-7-8 Breathing",
     "body_html": r"""<p>Andrew Weil's calming pattern:</p><ul><li>Inhale 4 seconds.</li><li>Hold 7 seconds.</li><li>Exhale 8 seconds.</li></ul><p>Long exhale shifts toward parasympathetic.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hold ___ seconds.", "answer": "7"},
         {"type": "multiple-choice", "question": "Founder: ", "options": ["Andrew Weil", "Jon Kabat-Zinn", "Tara Brach", "Pema Chodron"], "correctIndex": 0},
         {"type": "true-false", "question": "Exhale is the longest phase.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Inhale ___ seconds.", "answer": "4"},
         {"type": "true-false", "question": "Holding breath is the longest phase.", "correctAnswer": False}]},
    {"title": "Physiological Sigh",
     "body_html": r"""<p>Two quick inhales through the nose, one long exhale through the mouth. Andrew Huberman's research shows this resets CO2 levels and lowers heart rate within seconds.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Researcher: Andrew ___.", "answer": "Huberman"},
         {"type": "multiple-choice", "question": "Pattern: ", "options": ["2 inhales, 1 exhale", "1 inhale, 2 exhales", "no exhale", "10 inhales"], "correctIndex": 0},
         {"type": "true-false", "question": "Resets CO2 levels quickly.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Inhales through the ___.", "answer": "nose"},
         {"type": "true-false", "question": "Sighing has no effect on heart rate.", "correctAnswer": False}]},
    {"title": "5-4-3-2-1 Grounding",
     "body_html": r"""<p>For acute anxiety:</p><ul><li>Name 5 things you see.</li><li>4 you hear.</li><li>3 you feel.</li><li>2 you smell.</li><li>1 you taste.</li></ul><p>Forces attention into present senses.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "5 things you ___.", "answer": "see"},
         {"type": "multiple-choice", "question": "Method: ", "options": ["sense grounding", "running", "shouting", "sleeping"], "correctIndex": 0},
         {"type": "true-false", "question": "Counts down from 5.", "correctAnswer": True},
         {"type": "fill-blank", "question": "1 you ___.", "answer": "taste"},
         {"type": "true-false", "question": "It pulls attention away from senses.", "correctAnswer": False}]},
    {"title": "Body Scan for Stress",
     "body_html": r"""<p>Lie or sit. Move attention slowly head to feet, simply noticing. Where there's tension, breathe into it; don't force release. 10–20 minutes is enough.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Direction: ___ to feet.", "answer": "head"},
         {"type": "multiple-choice", "question": "Length: ", "options": ["10–20 min", "30 sec", "2 hours", "8 hours"], "correctIndex": 0},
         {"type": "true-false", "question": "Don't force release.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Where tension, ___ into it.", "answer": "breathe"},
         {"type": "true-false", "question": "Body scan ignores tension.", "correctAnswer": False}]},
    {"title": "Walking Off Stress",
     "body_html": r"""<p>Walking, especially outdoors, drops cortisol. Bilateral movement (left-right-left-right) regulates the nervous system. Even 10 minutes shifts the day.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Drops the hormone ___.", "answer": "cortisol"},
         {"type": "multiple-choice", "question": "Movement style: ", "options": ["bilateral", "circular only", "vertical only", "none"], "correctIndex": 0},
         {"type": "true-false", "question": "Outdoors helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "10 minutes shifts the ___.", "answer": "day"},
         {"type": "true-false", "question": "Walking raises stress.", "correctAnswer": False}]},
    {"title": "Cold Exposure",
     "body_html": r"""<p>Cold showers, cold plunges, or even a cold splash on the face activate the diving reflex and stimulate the vagus nerve. Reduces sympathetic dominance for hours.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Reflex name: ___.", "answer": "diving"},
         {"type": "multiple-choice", "question": "Stimulates: ", "options": ["vagus nerve", "sciatic nerve", "median nerve", "ulnar nerve"], "correctIndex": 0},
         {"type": "true-false", "question": "Reduces sympathetic dominance.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Even a cold splash on the ___.", "answer": "face"},
         {"type": "true-false", "question": "Cold raises stress hormones forever.", "correctAnswer": False}]},
    {"title": "Panic Attacks",
     "body_html": r"""<p>A panic attack is a sudden surge of intense fear with physical symptoms (racing heart, dizziness, derealization). It peaks in 10 minutes; it does not harm you.</p><ul><li>Don't fight; let it pass.</li><li>Slow exhale.</li><li>Name what's happening: "this is a panic attack."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Peak in roughly ___ minutes.", "answer": "10"},
         {"type": "multiple-choice", "question": "What harms: ", "options": ["nothing physical", "the heart fails", "fainting forever", "irreversible damage"], "correctIndex": 0},
         {"type": "true-false", "question": "Naming reduces grip.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Don't fight; let it ___.", "answer": "pass"},
         {"type": "true-false", "question": "Panic attacks always last all day.", "correctAnswer": False}]},
    {"title": "Worry vs Problem-Solving",
     "body_html": r"""<p>Worry feels productive but isn't. Test:</p><ul><li>If there's a clear next action, take it.</li><li>If not, label "worry" and return to breath.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "If clear next action: ___ it.", "answer": "take"},
         {"type": "multiple-choice", "question": "Otherwise: ", "options": ["label worry", "panic", "shout", "ignore body"], "correctIndex": 0},
         {"type": "true-false", "question": "Worry is unproductive when looped.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Return to ___.", "answer": "breath"},
         {"type": "true-false", "question": "Worry always solves problems.", "correctAnswer": False}]},
    {"title": "Catastrophic Thinking",
     "body_html": r"""<p>Common cognitive distortion: assuming the worst-case outcome. Tools:</p><ul><li>Ask: "What's the actual evidence?"</li><li>"What's most likely?"</li><li>"What would I tell a friend?"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Ask: what's the actual ___?", "answer": "evidence"},
         {"type": "multiple-choice", "question": "Useful question: ", "options": ["what's most likely", "what's the worst", "what won't help", "what's the past"], "correctIndex": 0},
         {"type": "true-false", "question": "Catastrophizing is a distortion.", "correctAnswer": True},
         {"type": "fill-blank", "question": "What would I tell a ___?", "answer": "friend"},
         {"type": "true-false", "question": "Catastrophic thinking is always accurate.", "correctAnswer": False}]},
    {"title": "Sleep & Anxiety",
     "body_html": r"""<p>Anxiety often disrupts sleep. Practices that help:</p><ul><li>No screens 30 minutes pre-bed.</li><li>Body scan in bed.</li><li>Brain dump on paper before bed.</li><li>Wake at the same time daily.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "No screens for ___ minutes pre-bed.", "answer": "30"},
         {"type": "multiple-choice", "question": "Practice in bed: ", "options": ["body scan", "loud singing", "scrolling", "running"], "correctIndex": 0},
         {"type": "true-false", "question": "Brain dump before bed helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Wake at the same ___ daily.", "answer": "time"},
         {"type": "true-false", "question": "Late-night phone use aids sleep.", "correctAnswer": False}]},
    {"title": "Caffeine, Alcohol & Anxiety",
     "body_html": r"""<p>Caffeine after 2 pm and alcohol within 3 hours of bed both disrupt sleep architecture. Anxiety improves measurably after 2–4 weeks of cleaner consumption.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Cut caffeine after ___ pm.", "answer": "2"},
         {"type": "multiple-choice", "question": "Alcohol within ___ hours of bed: ", "options": ["3", "0", "12", "20"], "correctIndex": 0},
         {"type": "true-false", "question": "Anxiety improves with cleaner consumption.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sleep ___ is disrupted.", "answer": "architecture"},
         {"type": "true-false", "question": "Coffee at 11 pm is fine for anxiety.", "correctAnswer": False}]},
    {"title": "Building a Daily Anti-Stress Stack",
     "body_html": r"""<ul><li>Morning: 10 minutes meditation, walk outside.</li><li>Midday: 4-7-8 breath before lunch.</li><li>Evening: body scan or gentle yoga.</li><li>Weekly: nature time, no-phone block.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Midday: ___-7-8 breath.", "answer": "4"},
         {"type": "multiple-choice", "question": "Morning duration: ", "options": ["10 min", "0 min", "3 hours", "6 hours"], "correctIndex": 0},
         {"type": "true-false", "question": "Weekly nature time helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Evening: body ___ or yoga.", "answer": "scan"},
         {"type": "true-false", "question": "Doing nothing differently improves stress.", "correctAnswer": False}]},
    {"title": "Stress & Anxiety Checkpoint",
     "body_html": r"""<ul><li>Box breathing, 4-7-8, physiological sigh shift the nervous system.</li><li>Grounding (5-4-3-2-1) and body scan return to the present.</li><li>Walking, cold, sleep hygiene, less caffeine all support practice.</li><li>Panic attacks pass; naming and slow exhaling helps.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Long exhale calms.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Grounding numbers: ", "options": ["5-4-3-2-1", "1-2-3", "10-9-8", "100-99"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Hormone lowered by walking: ___.", "answer": "cortisol"},
         {"type": "true-false", "question": "Panic attacks last forever.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Two quick inhales, one long exhale: physiological ___.", "answer": "sigh"}]},
]

if __name__ == "__main__":
    render_unit(20, "Stress, Anxiety & Panic", 286, LESSONS)
