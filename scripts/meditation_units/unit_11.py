#!/usr/bin/env python3
"""Meditation Unit 11 — Vipassana Deep Dive (lessons 151-165)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "What Is Vipassana?",
     "body_html": r"""<p>Vipassana means <em>insight</em> in Pali — the direct seeing of impermanence, unsatisfactoriness, and non-self. It is the central practice of early Buddhism.</p><ul><li>Pali word: <em>vipassanā</em>.</li><li>Aim: liberation through wisdom, not just calm.</li><li>Modern revival: Mahasi Sayadaw (Burma), S.N. Goenka (India).</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Vipassana means ___.", "answer": "insight"},
         {"type": "multiple-choice", "question": "Vipassana's aim is: ", "options": ["calm only", "liberation through wisdom", "physical fitness", "social bonding"], "correctIndex": 1},
         {"type": "true-false", "question": "Vipassana is from the Pali tradition.", "correctAnswer": True},
         {"type": "fill-blank", "question": "S.N. ___ revived Vipassana in India.", "answer": "Goenka"},
         {"type": "true-false", "question": "Vipassana ignores impermanence.", "correctAnswer": False}]},
    {"title": "The Three Marks of Existence",
     "body_html": r"""<p>Insight rests on three observations:</p><ul><li><strong>Anicca</strong> — impermanence; everything changes.</li><li><strong>Dukkha</strong> — unsatisfactoriness; clinging causes suffering.</li><li><strong>Anatta</strong> — non-self; no fixed unchanging self.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Impermanence: ___.", "answer": "anicca"},
         {"type": "multiple-choice", "question": "Anatta means: ", "options": ["non-self", "always", "perfect", "calm"], "correctIndex": 0},
         {"type": "true-false", "question": "Dukkha means unsatisfactoriness.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Three marks: anicca, dukkha, ___.", "answer": "anatta"},
         {"type": "true-false", "question": "Vipassana looks at these three marks.", "correctAnswer": True}]},
    {"title": "Mahasi Noting Technique",
     "body_html": r"""<p>The Mahasi method labels every experience as it arises — silently noting "rising," "falling," "thinking," "hearing." Labels are gentle, not judgmental.</p><ul><li>Anchor: rising/falling of the abdomen.</li><li>When attention wanders, note the wandering, then return.</li><li>Pace: every 1–2 seconds at first; faster as practice deepens.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mahasi anchors on ___ /falling.", "answer": "rising"},
         {"type": "multiple-choice", "question": "Note tone should be: ", "options": ["harsh", "judgmental", "gentle", "loud"], "correctIndex": 2},
         {"type": "true-false", "question": "Wandering thoughts are themselves noted.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Notes are made ___ (silent/aloud).", "answer": "silent"},
         {"type": "true-false", "question": "The Mahasi method labels experiences.", "correctAnswer": True}]},
    {"title": "Goenka Body-Sweeping",
     "body_html": r"""<p>S.N. Goenka taught a body-scan style of Vipassana. Move attention slowly from head to feet, observing sensations without reacting.</p><ul><li>Equanimity is the central skill.</li><li>Sensations arise and pass — anicca made tangible.</li><li>10-day silent retreats are the standard introduction.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Central skill: ___.", "answer": "equanimity"},
         {"type": "multiple-choice", "question": "Standard Goenka retreat length: ", "options": ["1 day", "3 days", "10 days", "1 year"], "correctIndex": 2},
         {"type": "true-false", "question": "Goenka teaches body-sweeping.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sensations arise and ___.", "answer": "pass"},
         {"type": "true-false", "question": "Goenka retreats are noisy.", "correctAnswer": False}]},
    {"title": "Choiceless Awareness",
     "body_html": r"""<p>Choiceless awareness simply receives whatever appears — sound, sensation, thought — without selecting or steering. The mind becomes a wide open space.</p><ul><li>No object is privileged.</li><li>Attention is panoramic, not narrow.</li><li>Best after some concentration is established.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Attention is ___ (narrow/panoramic).", "answer": "panoramic"},
         {"type": "multiple-choice", "question": "Best practiced after: ", "options": ["heavy meal", "concentration is established", "exercise only", "many hours of sleep"], "correctIndex": 1},
         {"type": "true-false", "question": "Choiceless awareness selects favorite objects.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Whatever appears is ___ (received/rejected).", "answer": "received"},
         {"type": "true-false", "question": "Choiceless awareness is panoramic.", "correctAnswer": True}]},
    {"title": "Working with Hindrances",
     "body_html": r"""<p>The Buddha named five hindrances:</p><ul><li>Sensual desire</li><li>Ill will</li><li>Sloth and torpor</li><li>Restlessness and worry</li><li>Doubt</li></ul><p>Each is met by recognition, not suppression. Naming the hindrance dissolves much of its grip.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "There are ___ hindrances.", "answer": "5"},
         {"type": "multiple-choice", "question": "Antidote to a hindrance: ", "options": ["suppression", "recognition", "denial", "panic"], "correctIndex": 1},
         {"type": "true-false", "question": "Doubt is one of the hindrances.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sloth and ___ pair together.", "answer": "torpor"},
         {"type": "true-false", "question": "Sensual desire is on the list.", "correctAnswer": True}]},
    {"title": "Insight Stages — Overview",
     "body_html": r"""<p>Classical texts map a sequence of insight stages (the <em>nanas</em>):</p><ul><li>Mind and body</li><li>Cause and effect</li><li>Three characteristics</li><li>Arising and passing</li><li>Dissolution</li><li>Equanimity</li><li>Path moments</li></ul><p>These describe shifts in perception, not goals to chase.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Insight stages are called ___.", "answer": "nanas"},
         {"type": "multiple-choice", "question": "An early stage: ", "options": ["dissolution", "mind and body", "path moment", "rebirth"], "correctIndex": 1},
         {"type": "true-false", "question": "Stages should be chased aggressively.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Stage of arising and ___.", "answer": "passing"},
         {"type": "true-false", "question": "Equanimity is one of the stages.", "correctAnswer": True}]},
    {"title": "Arising and Passing",
     "body_html": r"""<p>This stage is often vivid — bright lights, rapture, ease. Practitioners can mistake it for awakening. Stay with the practice; the experience also passes.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "This stage often feels ___.", "answer": "vivid"},
         {"type": "multiple-choice", "question": "Common error: ", "options": ["mistaking it for awakening", "ignoring the breath", "skipping retreats", "shouting"], "correctIndex": 0},
         {"type": "true-false", "question": "Arising and passing also passes.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Practitioners may experience ___ lights.", "answer": "bright"},
         {"type": "true-false", "question": "This stage is the final stage.", "correctAnswer": False}]},
    {"title": "The Dark Night",
     "body_html": r"""<p>After the ease of arising and passing comes a stretch of harder stages — fear, misery, disgust, desire for deliverance. Western teachers borrow the Christian phrase "Dark Night" for this period.</p><ul><li>Stay with a teacher if possible.</li><li>Continue daily practice — don't quit at the hardest part.</li><li>Sleep, food, and exercise help.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Christian phrase used: ___ Night.", "answer": "Dark"},
         {"type": "multiple-choice", "question": "Best advice: ", "options": ["quit", "stay with a teacher", "ignore food", "double caffeine"], "correctIndex": 1},
         {"type": "true-false", "question": "Dark Night follows arising and passing.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Dark Night includes fear, misery, ___, desire for deliverance.", "answer": "disgust"},
         {"type": "true-false", "question": "Sleep and food don't matter here.", "correctAnswer": False}]},
    {"title": "Equanimity Stage",
     "body_html": r"""<p>After the difficult stages, perception settles into a wide, even stillness. Sensations come and go without grip. This is sometimes called the <em>knowledge of equanimity about formations</em>.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Wide, even ___ describes this stage.", "answer": "stillness"},
         {"type": "multiple-choice", "question": "Sensations are met with: ", "options": ["grip", "rejection", "equanimity", "fear"], "correctIndex": 2},
         {"type": "true-false", "question": "Equanimity follows the Dark Night.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Equanimity about ___.", "answer": "formations"},
         {"type": "true-false", "question": "Equanimity is itself permanent.", "correctAnswer": False}]},
    {"title": "Path Moments",
     "body_html": r"""<p>Classical texts describe four "paths" or stages of awakening: stream-entry, once-returner, non-returner, arahant. Each is said to permanently uproot specific fetters.</p><ul><li>Stream-entry: doubt and identity-view fall away.</li><li>Arahant: full liberation; rare.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "First path is ___-entry.", "answer": "stream"},
         {"type": "multiple-choice", "question": "Final path: ", "options": ["arahant", "once-returner", "non-returner", "stream-entry"], "correctIndex": 0},
         {"type": "true-false", "question": "There are four paths.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Stream-entry uproots ___ and identity-view.", "answer": "doubt"},
         {"type": "true-false", "question": "Arahant is common.", "correctAnswer": False}]},
    {"title": "Daily Vipassana Routine",
     "body_html": r"""<p>A workable daily routine:</p><ul><li>20–60 minutes of formal sitting, ideally morning.</li><li>Brief noting practice during walks or commutes.</li><li>End-of-day review: where did mindfulness slip?</li><li>Read a sutta or modern teacher once a week.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Aim for at least ___ minutes daily.", "answer": "20"},
         {"type": "multiple-choice", "question": "Best time: ", "options": ["right after a fight", "morning", "during a meal", "during a movie"], "correctIndex": 1},
         {"type": "true-false", "question": "End-of-day review helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Read suttas roughly once per ___.", "answer": "week"},
         {"type": "true-false", "question": "Walking can also be Vipassana.", "correctAnswer": True}]},
    {"title": "Sitting Through Discomfort",
     "body_html": r"""<p>Pain in the knees or back will arise. The instruction: note <em>"pain, pain"</em> and observe its texture, location, and changes. If pain becomes harmful, adjust posture mindfully.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Note pain by saying ___, pain.", "answer": "pain"},
         {"type": "multiple-choice", "question": "If harmful: ", "options": ["force through", "adjust mindfully", "leave the cushion", "give up forever"], "correctIndex": 1},
         {"type": "true-false", "question": "Pain has changing texture.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Observe location and ___ of pain.", "answer": "texture"},
         {"type": "true-false", "question": "Always force through any pain.", "correctAnswer": False}]},
    {"title": "Vipassana Retreats",
     "body_html": r"""<p>Retreats accelerate practice. A typical 10-day Goenka retreat: silent, no reading or writing, 10+ hours of sitting daily, basic vegetarian food, dorm housing.</p><ul><li>Apply 1–3 months in advance.</li><li>Bring warm clothes and earplugs.</li><li>Plan re-entry: post-retreat days are tender.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Goenka retreat lasts ___ days.", "answer": "10"},
         {"type": "multiple-choice", "question": "Allowed during retreat: ", "options": ["talking", "phones", "silent sitting", "TV"], "correctIndex": 2},
         {"type": "true-false", "question": "Re-entry is tender.", "correctAnswer": True},
         {"type": "fill-blank", "question": "No reading or ___.", "answer": "writing"},
         {"type": "true-false", "question": "Most retreats serve meat.", "correctAnswer": False}]},
    {"title": "Vipassana Deep Dive Checkpoint",
     "body_html": r"""<ul><li>Vipassana = insight into anicca, dukkha, anatta.</li><li>Mahasi noting and Goenka body-sweeping are the two main modern lineages.</li><li>Insight stages move from joy through difficulty to equanimity.</li><li>Daily practice plus retreats deepens the work.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Anicca means impermanence.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Body-sweeping comes from: ", "options": ["Goenka", "Mahasi", "Zen", "Sufi"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Final classical stage: ___.", "answer": "arahant"},
         {"type": "true-false", "question": "Retreats often help.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Vipassana means ___.", "answer": "insight"}]},
]

if __name__ == "__main__":
    render_unit(11, "Vipassana Deep Dive", 151, LESSONS)
