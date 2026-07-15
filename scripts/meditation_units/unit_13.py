#!/usr/bin/env python3
"""Meditation Unit 13 — Zen Practice (lessons 181-195)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "What Is Zen?",
     "body_html": r"""<p>Zen is the Japanese name for a Buddhist tradition that came from Chinese Chan, which itself drew on Indian Dhyana. Its emphasis: direct experience over doctrine.</p><ul><li>Indian root: <em>dhyana</em> (meditative absorption).</li><li>Chinese: Chan.</li><li>Japanese: Zen.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Indian root word: ___.", "answer": "dhyana"},
         {"type": "multiple-choice", "question": "Chinese name: ", "options": ["Zen", "Chan", "Sufi", "Yoga"], "correctIndex": 1},
         {"type": "true-false", "question": "Zen emphasizes direct experience.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Japanese: ___.", "answer": "Zen"},
         {"type": "true-false", "question": "Zen rejects all meditation.", "correctAnswer": False}]},
    {"title": "Bodhidharma & Lineage",
     "body_html": r"""<p>Bodhidharma is the legendary Indian monk who brought Chan to China around the 5th–6th century. He sat facing a wall for nine years at Shaolin, the story goes.</p><ul><li>Bodhidharma → 6 patriarchs in China.</li><li>Wall-facing meditation: <em>biguan</em>.</li><li>Famously short, blunt teaching style.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Wall-facing: ___ (Chinese).", "answer": "biguan"},
         {"type": "multiple-choice", "question": "Bodhidharma sat facing wall for: ", "options": ["3 days", "9 years", "lifetime", "1 hour"], "correctIndex": 1},
         {"type": "true-false", "question": "Bodhidharma was Indian.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Lineage went through six ___.", "answer": "patriarchs"},
         {"type": "true-false", "question": "He had a long, ornate teaching style.", "correctAnswer": False}]},
    {"title": "Soto Zen — Just Sitting",
     "body_html": r"""<p>Soto Zen, founded by Dogen, centers on <em>shikantaza</em> — "just sitting." No object, no goal, no special technique; just the upright presence of sitting.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Soto practice: ___.", "answer": "shikantaza"},
         {"type": "multiple-choice", "question": "Founder: ", "options": ["Dogen", "Bodhidharma", "Hakuin", "Rinzai"], "correctIndex": 0},
         {"type": "true-false", "question": "Just sitting has no special technique.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Shikantaza means just ___.", "answer": "sitting"},
         {"type": "true-false", "question": "Shikantaza uses many techniques.", "correctAnswer": False}]},
    {"title": "Rinzai Zen — Koans",
     "body_html": r"""<p>Rinzai Zen, revived by Hakuin, uses <em>koans</em> — paradoxical phrases like "What is the sound of one hand clapping?" — to break the discursive mind.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Paradoxical phrase: ___.", "answer": "koan"},
         {"type": "multiple-choice", "question": "Revived by: ", "options": ["Dogen", "Hakuin", "Bodhidharma", "Suzuki"], "correctIndex": 1},
         {"type": "true-false", "question": "Koans break discursive mind.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sound of one ___ clapping.", "answer": "hand"},
         {"type": "true-false", "question": "Koans are easily solved logically.", "correctAnswer": False}]},
    {"title": "Famous Koans",
     "body_html": r"""<ul><li>Mu — "A monk asked Joshu, 'Does a dog have Buddha nature?' Joshu said, 'Mu.'"</li><li>"What was your original face before your parents were born?"</li><li>"What is the sound of one hand clapping?"</li><li>"If you meet the Buddha on the road, kill him."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Joshu's answer to dog/Buddha-nature: ___.", "answer": "Mu"},
         {"type": "multiple-choice", "question": "Before parents were born: ", "options": ["face", "hands", "voice", "name"], "correctIndex": 0},
         {"type": "true-false", "question": "Koans push past concepts.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Meet the Buddha on the road, ___ him.", "answer": "kill"},
         {"type": "true-false", "question": "Koans are casual riddles for fun.", "correctAnswer": False}]},
    {"title": "Zazen Posture",
     "body_html": r"""<p>Posture in zazen is precise:</p><ul><li>Half-lotus, full-lotus, Burmese, or seiza.</li><li>Spine erect; chin slightly tucked.</li><li>Hands in cosmic mudra: left over right, thumbs touching.</li><li>Eyes half-open, gaze about a meter ahead and down.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hand position: cosmic ___.", "answer": "mudra"},
         {"type": "multiple-choice", "question": "Eye state: ", "options": ["fully closed", "fully open", "half-open", "moving"], "correctIndex": 2},
         {"type": "true-false", "question": "Spine should be erect.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Chin slightly ___.", "answer": "tucked"},
         {"type": "true-false", "question": "Eyes should always be tightly closed.", "correctAnswer": False}]},
    {"title": "Sesshin — Intensive Retreat",
     "body_html": r"""<p>A sesshin is a multi-day intensive: typically 3 to 7 days, with 8–14 hours of zazen each day, formal meals (oryoki), silence, and dokusan (private interview with the teacher).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Formal meal practice: ___.", "answer": "oryoki"},
         {"type": "multiple-choice", "question": "Sesshin length range: ", "options": ["3-7 days", "1 hour", "1 month", "1 year"], "correctIndex": 0},
         {"type": "true-false", "question": "Dokusan is private interview.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sesshin emphasizes ___.", "answer": "silence"},
         {"type": "true-false", "question": "Sesshin has no schedule.", "correctAnswer": False}]},
    {"title": "Kinhin — Walking Zen",
     "body_html": r"""<p>Kinhin is slow walking meditation between zazen periods. One foot moves on each in-breath, often with hands held in shashu (left fist wrapped by right hand at the chest).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Walking Zen: ___.", "answer": "kinhin"},
         {"type": "multiple-choice", "question": "Pace: ", "options": ["very slow", "running", "skipping", "stopping"], "correctIndex": 0},
         {"type": "true-false", "question": "Kinhin breaks up sitting periods.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Hands held in ___.", "answer": "shashu"},
         {"type": "true-false", "question": "Kinhin involves running.", "correctAnswer": False}]},
    {"title": "Oryoki — Formal Eating",
     "body_html": r"""<p>Oryoki means "just enough." A nested set of bowls is unwrapped, used, washed, and rewrapped — every motion choreographed. Eating becomes practice.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Oryoki means just ___.", "answer": "enough"},
         {"type": "multiple-choice", "question": "Bowls are: ", "options": ["disposable", "nested", "made of paper", "plastic"], "correctIndex": 1},
         {"type": "true-false", "question": "Eating becomes practice.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Bowls are washed and ___.", "answer": "rewrapped"},
         {"type": "true-false", "question": "Oryoki is casual and fast.", "correctAnswer": False}]},
    {"title": "Dokusan — Teacher Interview",
     "body_html": r"""<p>In dokusan, a student bows, sits, and presents understanding of practice or a koan to the teacher. The teacher may probe, push, or simply ring the bell to dismiss.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Private teacher meeting: ___.", "answer": "dokusan"},
         {"type": "multiple-choice", "question": "May happen at end: ", "options": ["bell rings", "lunch served", "song sung", "movie shown"], "correctIndex": 0},
         {"type": "true-false", "question": "Students present understanding.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Student begins by ___.", "answer": "bowing"},
         {"type": "true-false", "question": "Dokusan is loud and casual.", "correctAnswer": False}]},
    {"title": "Zen Arts — Tea, Calligraphy, Archery",
     "body_html": r"""<p>Zen permeates traditional Japanese arts: tea (chado), calligraphy (shodo), archery (kyudo), flower arranging (ikebana), gardening, and noh theater.</p><ul><li>Each art is meditation in motion.</li><li>Form is liberation, not restriction.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tea ceremony: ___.", "answer": "chado"},
         {"type": "multiple-choice", "question": "Archery: ", "options": ["kyudo", "kendo", "judo", "sumo"], "correctIndex": 0},
         {"type": "true-false", "question": "Form is liberation.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Calligraphy: ___.", "answer": "shodo"},
         {"type": "true-false", "question": "Ikebana is flower arranging.", "correctAnswer": True}]},
    {"title": "Zen in the West",
     "body_html": r"""<p>D.T. Suzuki, Shunryu Suzuki, and Philip Kapleau opened Zen to American and European students in the 20th century. <em>Zen Mind, Beginner's Mind</em> (Shunryu Suzuki) remains a classic.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Author of Zen Mind, Beginner's Mind: ___ Suzuki.", "answer": "Shunryu"},
         {"type": "multiple-choice", "question": "Other Western pioneer: ", "options": ["Philip Kapleau", "Hakuin", "Dogen", "Bodhidharma"], "correctIndex": 0},
         {"type": "true-false", "question": "D.T. Suzuki taught in the West.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Beginner's ___.", "answer": "Mind"},
         {"type": "true-false", "question": "Zen never reached the West.", "correctAnswer": False}]},
    {"title": "Famous Zen Sayings",
     "body_html": r"""<ul><li>"Before enlightenment, chop wood, carry water. After enlightenment, chop wood, carry water."</li><li>"The finger pointing at the moon is not the moon."</li><li>"In the beginner's mind there are many possibilities, in the expert's mind there are few."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Chop wood, carry ___.", "answer": "water"},
         {"type": "multiple-choice", "question": "Finger points at: ", "options": ["sun", "moon", "stars", "self"], "correctIndex": 1},
         {"type": "true-false", "question": "Beginner's mind has many possibilities.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Expert's mind has ___.", "answer": "few"},
         {"type": "true-false", "question": "Sayings rely on poetic concision.", "correctAnswer": True}]},
    {"title": "Daily Zen Practice",
     "body_html": r"""<p>A typical lay routine:</p><ul><li>20–40 minutes of zazen, morning.</li><li>Brief evening sit or chant.</li><li>Awareness during one daily activity (tea, dishes, walking).</li><li>Monthly group sit (zazenkai); annual sesshin if possible.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Daily morning sit: ___ minutes.", "answer": "20"},
         {"type": "multiple-choice", "question": "Group monthly sit: ", "options": ["sesshin", "zazenkai", "dokusan", "oryoki"], "correctIndex": 1},
         {"type": "true-false", "question": "Daily awareness during chores helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Annual intensive: ___.", "answer": "sesshin"},
         {"type": "true-false", "question": "One sit per year is enough.", "correctAnswer": False}]},
    {"title": "Zen Practice Checkpoint",
     "body_html": r"""<ul><li>Zen = direct experience; Soto (just sitting) and Rinzai (koans).</li><li>Zazen posture: precise, upright, hands in cosmic mudra.</li><li>Sesshin retreats deepen practice.</li><li>Zen permeates tea, calligraphy, archery, gardens.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Soto = shikantaza.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Cosmic mudra: ", "options": ["zazen hand position", "a song", "a robe", "a bell"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Rinzai uses ___.", "answer": "koans"},
         {"type": "true-false", "question": "Zazen is sloppy.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Zen comes from Chinese ___.", "answer": "Chan"}]},
]

if __name__ == "__main__":
    render_unit(13, "Zen Practice", 181, LESSONS)
