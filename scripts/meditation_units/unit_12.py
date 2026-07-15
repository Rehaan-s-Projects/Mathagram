#!/usr/bin/env python3
"""Meditation Unit 12 — Concentration & Jhana (lessons 166-180)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Samatha — Calm Abiding",
     "body_html": r"""<p><em>Samatha</em> is the cultivation of calm and one-pointed attention. While Vipassana investigates, Samatha gathers the mind. Both are needed; neither alone is enough.</p><ul><li>Pali: <em>samatha</em> (calm).</li><li>Object: a single chosen anchor — usually breath.</li><li>Result: stable, pliable, peaceful mind.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Samatha means ___.", "answer": "calm"},
         {"type": "multiple-choice", "question": "Samatha gathers the mind via: ", "options": ["multiple anchors", "one anchor", "no anchor", "music"], "correctIndex": 1},
         {"type": "true-false", "question": "Vipassana and samatha both matter.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Common anchor: ___.", "answer": "breath"},
         {"type": "true-false", "question": "Samatha is the same as Vipassana.", "correctAnswer": False}]},
    {"title": "The Five Factors of Absorption",
     "body_html": r"""<p>Classical texts list five factors that mark deepening concentration:</p><ul><li>Vitakka — applied thought (placing attention).</li><li>Vicara — sustained thought (holding attention).</li><li>Piti — rapture, joy, energy.</li><li>Sukha — happiness, ease.</li><li>Ekaggata — one-pointedness.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Applied thought: ___.", "answer": "vitakka"},
         {"type": "multiple-choice", "question": "One-pointedness: ", "options": ["piti", "sukha", "ekaggata", "vicara"], "correctIndex": 2},
         {"type": "true-false", "question": "Piti means rapture.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sustained thought: ___.", "answer": "vicara"},
         {"type": "true-false", "question": "Sukha is sadness.", "correctAnswer": False}]},
    {"title": "Access Concentration",
     "body_html": r"""<p>Before jhana proper, attention reaches a stable threshold called <em>upacara samadhi</em> — access concentration. The mind no longer wanders for minutes at a time and a "counterpart sign" or steady warm presence may appear.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Pali for access: ___ samadhi.", "answer": "upacara"},
         {"type": "multiple-choice", "question": "Counterpart sign is: ", "options": ["a name", "a steady mental image", "a smell only", "a partner"], "correctIndex": 1},
         {"type": "true-false", "question": "Access is the same as full jhana.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Mind is stable for ___ at a time.", "answer": "minutes"},
         {"type": "true-false", "question": "Access concentration precedes jhana.", "correctAnswer": True}]},
    {"title": "First Jhana",
     "body_html": r"""<p>The first jhana has all five factors: vitakka, vicara, piti, sukha, ekaggata. The mind is delighted, energetic, and absorbed. Hindrances are temporarily suppressed.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "First jhana has ___ factors.", "answer": "5"},
         {"type": "multiple-choice", "question": "First jhana is marked by: ", "options": ["dullness", "absorption with rapture", "sleep", "frustration"], "correctIndex": 1},
         {"type": "true-false", "question": "Hindrances are suppressed in jhana.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Vitakka and ___ are present.", "answer": "vicara"},
         {"type": "true-false", "question": "First jhana is dull.", "correctAnswer": False}]},
    {"title": "Second Jhana",
     "body_html": r"""<p>Vitakka and vicara fall away. Piti, sukha, and ekaggata remain. Confidence rises. Mental verbalizing has stopped.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Drops out: vitakka and ___.", "answer": "vicara"},
         {"type": "multiple-choice", "question": "Remaining factor list: ", "options": ["piti, sukha, ekaggata", "vitakka only", "anger only", "doubt only"], "correctIndex": 0},
         {"type": "true-false", "question": "Mental verbalizing stops.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Mind grows in ___.", "answer": "confidence"},
         {"type": "true-false", "question": "Vicara remains.", "correctAnswer": False}]},
    {"title": "Third Jhana",
     "body_html": r"""<p>Rapture (piti) fades. Only sukha (a calmer happiness) and ekaggata remain. Equanimity grows. The body feels suffused with deep ease.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Rapture (___) fades.", "answer": "piti"},
         {"type": "multiple-choice", "question": "Body feels: ", "options": ["agitated", "suffused with ease", "numb", "cold"], "correctIndex": 1},
         {"type": "true-false", "question": "Equanimity grows in third jhana.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Calmer happiness: ___.", "answer": "sukha"},
         {"type": "true-false", "question": "Piti remains in third jhana.", "correctAnswer": False}]},
    {"title": "Fourth Jhana",
     "body_html": r"""<p>Even sukha is replaced by deep equanimity. Breath becomes nearly imperceptible. Ekaggata and equanimity remain. This is the platform many traditions use as the launchpad for insight or for the formless realms.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sukha is replaced by ___.", "answer": "equanimity"},
         {"type": "multiple-choice", "question": "Breath becomes: ", "options": ["loud", "imperceptible", "ragged", "rapid"], "correctIndex": 1},
         {"type": "true-false", "question": "Fourth jhana is a launchpad for insight.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Remaining factor: ___ + equanimity.", "answer": "ekaggata"},
         {"type": "true-false", "question": "Fourth jhana keeps rapture.", "correctAnswer": False}]},
    {"title": "Formless Jhanas — Overview",
     "body_html": r"""<p>Beyond the four material jhanas lie four formless states:</p><ul><li>Boundless space</li><li>Boundless consciousness</li><li>Nothingness</li><li>Neither perception nor non-perception</li></ul><p>Each transcends the previous object. They are extremely subtle.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "There are ___ formless states.", "answer": "4"},
         {"type": "multiple-choice", "question": "First formless state: ", "options": ["nothingness", "boundless space", "rapture", "fire"], "correctIndex": 1},
         {"type": "true-false", "question": "Formless jhanas are crude.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Final formless: neither perception nor ___.", "answer": "non-perception"},
         {"type": "true-false", "question": "Formless states transcend their objects.", "correctAnswer": True}]},
    {"title": "Ajahn Brahm's Approach",
     "body_html": r"""<p>Ajahn Brahm (Australian Theravadan teacher) emphasizes letting go: do nothing more than what is necessary to remain aware. He calls this <em>kindfulness</em> — kindness plus mindfulness.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Term Ajahn Brahm coined: ___.", "answer": "kindfulness"},
         {"type": "multiple-choice", "question": "Style: ", "options": ["force concentration", "let go", "scold the mind", "argue"], "correctIndex": 1},
         {"type": "true-false", "question": "Ajahn Brahm is Theravadan.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Kindfulness = ___ + mindfulness.", "answer": "kindness"},
         {"type": "true-false", "question": "Ajahn Brahm scolds the mind.", "correctAnswer": False}]},
    {"title": "Leigh Brasington's Light Jhanas",
     "body_html": r"""<p>Leigh Brasington (American teacher) describes "lighter" jhanas accessible in months, not years. Used widely in modern lay practice.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Brasington describes ___ jhanas.", "answer": "light"},
         {"type": "multiple-choice", "question": "Time scale: ", "options": ["minutes", "months", "decades", "centuries"], "correctIndex": 1},
         {"type": "true-false", "question": "Light jhanas suit lay practitioners.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Brasington is ___ (American/Burmese).", "answer": "American"},
         {"type": "true-false", "question": "Light jhanas take decades.", "correctAnswer": False}]},
    {"title": "Setting Up for Jhana",
     "body_html": r"""<p>Practical conditions:</p><ul><li>Quiet space, undisturbed for at least an hour.</li><li>Body relaxed, alertness up.</li><li>Brief metta or gratitude warm-up.</li><li>Anchor: long, soft breaths at the nose.</li><li>No clock-watching.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Aim for at least ___ hour undisturbed.", "answer": "1"},
         {"type": "multiple-choice", "question": "Anchor location: ", "options": ["the nose", "the foot", "the elbow", "outside"], "correctIndex": 0},
         {"type": "true-false", "question": "Metta warm-up helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "No ___-watching.", "answer": "clock"},
         {"type": "true-false", "question": "Stress speeds entry to jhana.", "correctAnswer": False}]},
    {"title": "Common Obstacles",
     "body_html": r"""<ul><li>Pushing too hard creates tension.</li><li>Drowsiness — open eyes briefly, sit upright.</li><li>Excitement at piti — relax into it.</li><li>Doubt — return to the breath.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Pushing too hard creates ___.", "answer": "tension"},
         {"type": "multiple-choice", "question": "Drowsy? ", "options": ["close eyes harder", "lie down", "open eyes briefly", "leave"], "correctIndex": 2},
         {"type": "true-false", "question": "Doubt: return to the breath.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Excitement at piti: ___ into it.", "answer": "relax"},
         {"type": "true-false", "question": "Force is the path to jhana.", "correctAnswer": False}]},
    {"title": "Concentration Cycles",
     "body_html": r"""<p>Concentration ebbs and flows across days, weeks, months. A great sit doesn't guarantee the next; a poor sit doesn't predict the next. Patience is the lineage.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Concentration ___ and flows.", "answer": "ebbs"},
         {"type": "multiple-choice", "question": "A great sit guarantees: ", "options": ["nothing about next", "the next", "all future sits", "awakening"], "correctIndex": 0},
         {"type": "true-false", "question": "Patience is the lineage.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Patience is ___.", "answer": "the lineage"},
         {"type": "true-false", "question": "Concentration is always linear.", "correctAnswer": False}]},
    {"title": "Concentration Plus Insight",
     "body_html": r"""<p>The classical pairing: enter jhana, then on emerging, observe the residual factors (sukha, equanimity, etc.) as impermanent. Calm becomes the platform; insight does the carving.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Calm is the ___.", "answer": "platform"},
         {"type": "multiple-choice", "question": "After jhana, observe: ", "options": ["residual factors as impermanent", "the cushion only", "social media", "nothing"], "correctIndex": 0},
         {"type": "true-false", "question": "Insight does the carving.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pair: concentration + ___.", "answer": "insight"},
         {"type": "true-false", "question": "Calm without insight is enough.", "correctAnswer": False}]},
    {"title": "Concentration Checkpoint",
     "body_html": r"""<ul><li>Samatha = calm; Vipassana = insight; you need both.</li><li>Five factors: vitakka, vicara, piti, sukha, ekaggata.</li><li>Four material jhanas + four formless states.</li><li>Modern lay paths (Ajahn Brahm, Leigh Brasington) make jhana accessible.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Both samatha and vipassana matter.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Total jhana states (incl. formless): ", "options": ["3", "4", "8", "16"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Calm is ___.", "answer": "samatha"},
         {"type": "true-false", "question": "Brasington and Ajahn Brahm teach jhana.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Insight is ___.", "answer": "vipassana"}]},
]

if __name__ == "__main__":
    render_unit(12, "Concentration & Jhana", 166, LESSONS)
