#!/usr/bin/env python3
"""Meditation Unit 14 — Tibetan Buddhist Meditation (lessons 196-210)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Vajrayana — Diamond Vehicle",
     "body_html": r"""<p>Tibetan Buddhism is a form of <em>Vajrayana</em>, the "diamond vehicle." It draws on Indian Mahayana, Tantra, and indigenous Bon traditions.</p><ul><li>Vajra = diamond / thunderbolt.</li><li>Three vehicles: Theravada, Mahayana, Vajrayana.</li><li>Famous for vivid imagery, mantras, and rituals.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Vajra means ___ / thunderbolt.", "answer": "diamond"},
         {"type": "multiple-choice", "question": "Tibetan tradition is: ", "options": ["Theravada", "Vajrayana", "Sufi", "Zen"], "correctIndex": 1},
         {"type": "true-false", "question": "Vajrayana includes mantras and ritual.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Indigenous tradition: ___.", "answer": "Bon"},
         {"type": "true-false", "question": "There is one vehicle only.", "correctAnswer": False}]},
    {"title": "Four Schools",
     "body_html": r"""<p>Four major Tibetan schools:</p><ul><li>Nyingma — oldest; Padmasambhava lineage.</li><li>Kagyu — Marpa, Milarepa, Karmapa.</li><li>Sakya — scholarly; Sakya Trizin.</li><li>Gelug — Dalai Lama's school; Tsongkhapa founder.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Dalai Lama school: ___.", "answer": "Gelug"},
         {"type": "multiple-choice", "question": "Oldest school: ", "options": ["Sakya", "Nyingma", "Kagyu", "Gelug"], "correctIndex": 1},
         {"type": "true-false", "question": "Milarepa is in the Kagyu lineage.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Founder of Gelug: ___.", "answer": "Tsongkhapa"},
         {"type": "true-false", "question": "There is only one Tibetan school.", "correctAnswer": False}]},
    {"title": "Refuge & Bodhicitta",
     "body_html": r"""<p>Every session begins with two motivations:</p><ul><li><strong>Refuge</strong> in Buddha, Dharma, Sangha.</li><li><strong>Bodhicitta</strong> — the wish to become enlightened for the sake of all beings.</li></ul><p>These set the heart-direction of the practice.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Wish for all beings' awakening: ___.", "answer": "bodhicitta"},
         {"type": "multiple-choice", "question": "Refuge is in: ", "options": ["money", "Buddha-Dharma-Sangha", "self", "rituals only"], "correctIndex": 1},
         {"type": "true-false", "question": "These open every session.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sangha = ___.", "answer": "community"},
         {"type": "true-false", "question": "Bodhicitta is selfish.", "correctAnswer": False}]},
    {"title": "Ngondro — Foundational Practices",
     "body_html": r"""<p>Most schools require <em>ngondro</em> — preliminary practices done 100,000 times each:</p><ul><li>Refuge prostrations.</li><li>Vajrasattva mantra.</li><li>Mandala offering.</li><li>Guru yoga.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Each ngondro practice: ___ times.", "answer": "100,000"},
         {"type": "multiple-choice", "question": "Not part of ngondro: ", "options": ["prostrations", "Vajrasattva", "playing video games", "guru yoga"], "correctIndex": 2},
         {"type": "true-false", "question": "Ngondro means foundational.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Mandala ___.", "answer": "offering"},
         {"type": "true-false", "question": "Ngondro is a quick warmup.", "correctAnswer": False}]},
    {"title": "Visualization of Deities",
     "body_html": r"""<p>Tibetan practice visualizes deities — Tara, Avalokiteshvara, Manjushri, Vajrayogini — as embodiments of qualities (compassion, wisdom, fierce protection). Visualization purifies and trains the mind.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Compassion deity: ___.", "answer": "Avalokiteshvara"},
         {"type": "multiple-choice", "question": "Wisdom deity: ", "options": ["Tara", "Manjushri", "Padmasambhava", "Yama"], "correctIndex": 1},
         {"type": "true-false", "question": "Visualization trains the mind.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Female compassion deity: ___.", "answer": "Tara"},
         {"type": "true-false", "question": "Deities are literal external gods to worship.", "correctAnswer": False}]},
    {"title": "Mantra Practice",
     "body_html": r"""<ul><li>Om Mani Padme Hum — Avalokiteshvara, compassion.</li><li>Om Tare Tuttare Ture Soha — Tara.</li><li>Om Ah Ra Pa Tsa Na Dhi — Manjushri, wisdom.</li><li>Om Ah Hum Vajra Guru Padma Siddhi Hum — Padmasambhava.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Compassion mantra: Om Mani Padme ___.", "answer": "Hum"},
         {"type": "multiple-choice", "question": "Wisdom mantra ends in: ", "options": ["Hum", "Soha", "Dhi", "Hri"], "correctIndex": 2},
         {"type": "true-false", "question": "Tara mantra includes Tuttare.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Padmasambhava mantra ends: ___ Hum.", "answer": "Siddhi"},
         {"type": "true-false", "question": "Mantras are random sounds.", "correctAnswer": False}]},
    {"title": "Tonglen — Giving and Taking",
     "body_html": r"""<p>Tonglen is a Mahayana practice: on the in-breath, take in the suffering of others; on the out-breath, send out warmth, ease, well-being.</p><ul><li>Reverses our usual self-protective instinct.</li><li>Often taught by Pema Chodron and Chogyam Trungpa.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tonglen in-breath: take in ___.", "answer": "suffering"},
         {"type": "multiple-choice", "question": "Out-breath: ", "options": ["warmth", "anger", "boredom", "irritation"], "correctIndex": 0},
         {"type": "true-false", "question": "Tonglen reverses self-protection.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Famous teacher: Pema ___.", "answer": "Chodron"},
         {"type": "true-false", "question": "Tonglen is a Theravada practice.", "correctAnswer": False}]},
    {"title": "Lojong — Mind Training",
     "body_html": r"""<p>Lojong is a set of 59 slogans for everyday awareness, attributed to Atisha and Geshe Chekawa. Examples: "Drive all blames into one," "Be grateful to everyone."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "There are ___ lojong slogans.", "answer": "59"},
         {"type": "multiple-choice", "question": "Slogan: Be grateful to: ", "options": ["yourself", "no one", "everyone", "the rich"], "correctIndex": 2},
         {"type": "true-false", "question": "Lojong = mind training.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Drive all ___ into one.", "answer": "blames"},
         {"type": "true-false", "question": "Lojong applies only on retreat.", "correctAnswer": False}]},
    {"title": "Mahamudra — The Great Seal",
     "body_html": r"""<p>Mahamudra (Kagyu) points directly to the nature of mind: clear, empty, aware. Practice rests in this open awareness without grasping or rejecting.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mahamudra means Great ___.", "answer": "Seal"},
         {"type": "multiple-choice", "question": "Three qualities of mind: ", "options": ["clear, empty, aware", "loud, big, slow", "good, bad, neutral", "red, blue, green"], "correctIndex": 0},
         {"type": "true-false", "question": "Mahamudra is in the Kagyu school.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Open ___.", "answer": "awareness"},
         {"type": "true-false", "question": "Mahamudra clings tightly to thoughts.", "correctAnswer": False}]},
    {"title": "Dzogchen — Great Perfection",
     "body_html": r"""<p>Dzogchen (Nyingma) introduces <em>rigpa</em>: pristine awareness already complete. Practice is recognition, not construction.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Pristine awareness: ___.", "answer": "rigpa"},
         {"type": "multiple-choice", "question": "Dzogchen school: ", "options": ["Nyingma", "Gelug", "Sakya", "Zen"], "correctIndex": 0},
         {"type": "true-false", "question": "Dzogchen = recognition, not construction.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Great ___.", "answer": "Perfection"},
         {"type": "true-false", "question": "Dzogchen is from China.", "correctAnswer": False}]},
    {"title": "Pointing-Out Instructions",
     "body_html": r"""<p>In Mahamudra and Dzogchen, a qualified teacher gives <em>pointing-out</em> instructions — directly indicating the nature of mind to the student. These are kept oral and simple.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Direct teaching: ___-out.", "answer": "pointing"},
         {"type": "multiple-choice", "question": "Style: ", "options": ["written textbook", "oral and simple", "video lecture only", "kept secret forever"], "correctIndex": 1},
         {"type": "true-false", "question": "Pointing-out names the nature of mind.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Given by ___ teacher.", "answer": "qualified"},
         {"type": "true-false", "question": "It is long and ornate.", "correctAnswer": False}]},
    {"title": "Death & Bardo",
     "body_html": r"""<p>The Tibetan Book of the Dead (Bardo Thodol) describes intermediate states (<em>bardos</em>) between death and rebirth. Phowa is the practice of consciousness transference at death.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Intermediate state: ___.", "answer": "bardo"},
         {"type": "multiple-choice", "question": "Consciousness transference: ", "options": ["phowa", "tonglen", "kinhin", "shikantaza"], "correctIndex": 0},
         {"type": "true-false", "question": "Bardo Thodol is the Book of the Dead.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Bardo Thodol is from ___ tradition.", "answer": "Tibetan"},
         {"type": "true-false", "question": "There are no intermediate states in this view.", "correctAnswer": False}]},
    {"title": "Lay Tibetan Practice",
     "body_html": r"""<ul><li>Daily mantra (Om Mani Padme Hum on a mala).</li><li>Tonglen for difficult moments.</li><li>Refuge + bodhicitta at session start.</li><li>Annual or biannual retreat with teacher.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mantra beads: ___.", "answer": "mala"},
         {"type": "multiple-choice", "question": "Daily mantra: ", "options": ["Om Tare", "Om Mani Padme Hum", "Om Ah Hum", "Om Ra"], "correctIndex": 1},
         {"type": "true-false", "question": "Tonglen helps difficult moments.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Open with refuge and ___.", "answer": "bodhicitta"},
         {"type": "true-false", "question": "Lay practice is impossible.", "correctAnswer": False}]},
    {"title": "Working with a Teacher",
     "body_html": r"""<p>In Vajrayana, the teacher (lama) is central. Vet teachers carefully — credentials, lineage, ethics. The relationship is meant to be transformative, not unsafe.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tibetan word for teacher: ___.", "answer": "lama"},
         {"type": "multiple-choice", "question": "Vet teacher for: ", "options": ["lineage and ethics", "wealth", "popularity", "looks"], "correctIndex": 0},
         {"type": "true-false", "question": "Vajrayana has no teacher role.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Relationship should be ___.", "answer": "transformative"},
         {"type": "true-false", "question": "Lineage matters.", "correctAnswer": True}]},
    {"title": "Tibetan Buddhism Checkpoint",
     "body_html": r"""<ul><li>Vajrayana = diamond vehicle.</li><li>Four schools: Nyingma, Kagyu, Sakya, Gelug.</li><li>Practices: ngondro, mantra, visualization, tonglen, lojong, Mahamudra, Dzogchen.</li><li>Teacher relationship is central; vet carefully.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Tibetan Buddhism is Vajrayana.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Mind training slogans: ", "options": ["lojong", "phowa", "ngondro", "mala"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Compassion mantra includes ___ Mani Padme Hum.", "answer": "Om"},
         {"type": "true-false", "question": "Pointing-out instructions are detailed in books only.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Dzogchen = Great ___.", "answer": "Perfection"}]},
]

if __name__ == "__main__":
    render_unit(14, "Tibetan Buddhist Meditation", 196, LESSONS)
