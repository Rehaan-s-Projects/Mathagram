#!/usr/bin/env python3
"""Meditation Unit 18 — Hindu & Yogic Meditation (lessons 256-270)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Roots in the Vedas & Upanishads",
     "body_html": r"""<p>Hindu meditation reaches back to the Vedas (1500 BCE) and the Upanishads (800–200 BCE), which describe Atman (self) and Brahman (ultimate). Meditation is the bridge.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Self: ___.", "answer": "Atman"},
         {"type": "multiple-choice", "question": "Ultimate: ", "options": ["Brahman", "Atman", "Maya", "Karma"], "correctIndex": 0},
         {"type": "true-false", "question": "Vedas date to roughly 1500 BCE.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Upanishads: ___–200 BCE.", "answer": "800"},
         {"type": "true-false", "question": "Meditation is the bridge.", "correctAnswer": True}]},
    {"title": "Patanjali's Yoga Sutras",
     "body_html": r"""<p>The <em>Yoga Sutras</em> (~200 BCE) by Patanjali define yoga as "stilling the fluctuations of the mind." They lay out the 8 limbs (<em>ashtanga</em>): yama, niyama, asana, pranayama, pratyahara, dharana, dhyana, samadhi.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Limbs of yoga: ___.", "answer": "8"},
         {"type": "multiple-choice", "question": "Sixth limb: ", "options": ["dharana", "dhyana", "asana", "samadhi"], "correctIndex": 0},
         {"type": "true-false", "question": "Patanjali defines yoga as stilling the mind.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Eight-limbed: ___.", "answer": "ashtanga"},
         {"type": "true-false", "question": "Sutras are modern (20th century).", "correctAnswer": False}]},
    {"title": "Yama & Niyama",
     "body_html": r"""<p>Foundations:</p><ul><li>Yamas (5 restraints): non-harm, truth, non-stealing, restraint, non-grasping.</li><li>Niyamas (5 observances): cleanliness, contentment, discipline, study, surrender to the divine.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Non-harm: ___.", "answer": "ahimsa"},
         {"type": "multiple-choice", "question": "Niyamas count: ", "options": ["3", "5", "7", "10"], "correctIndex": 1},
         {"type": "true-false", "question": "Truth is a yama.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Contentment: ___.", "answer": "santosha"},
         {"type": "true-false", "question": "Yamas and niyamas are optional decorations.", "correctAnswer": False}]},
    {"title": "Asana & Pranayama",
     "body_html": r"""<p>Asana = posture, originally meant for stable sitting. Pranayama = breath control, the bridge from body to mind. Today, asana also refers to physical yoga postures.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Posture: ___.", "answer": "asana"},
         {"type": "multiple-choice", "question": "Breath control: ", "options": ["pranayama", "dhyana", "asana", "yama"], "correctIndex": 0},
         {"type": "true-false", "question": "Asana originally meant stable sitting.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Bridge from body to ___.", "answer": "mind"},
         {"type": "true-false", "question": "Asana means food.", "correctAnswer": False}]},
    {"title": "Pratyahara — Withdrawal of Senses",
     "body_html": r"""<p>Pratyahara turns the senses inward. Like a tortoise drawing in its limbs, attention is withdrawn from external stimuli to settle inside.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Withdrawal of senses: ___.", "answer": "pratyahara"},
         {"type": "multiple-choice", "question": "Image used: ", "options": ["tortoise", "lion", "tiger", "fish"], "correctIndex": 0},
         {"type": "true-false", "question": "Senses are turned inward.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Senses withdraw from ___ stimuli.", "answer": "external"},
         {"type": "true-false", "question": "Pratyahara amplifies external sounds.", "correctAnswer": False}]},
    {"title": "Dharana, Dhyana, Samadhi",
     "body_html": r"""<p>The triad called <em>samyama</em>:</p><ul><li>Dharana — concentration on one object.</li><li>Dhyana — sustained meditation on it.</li><li>Samadhi — absorption, merging with the object.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Triad name: ___.", "answer": "samyama"},
         {"type": "multiple-choice", "question": "Absorption: ", "options": ["samadhi", "dharana", "dhyana", "asana"], "correctIndex": 0},
         {"type": "true-false", "question": "Concentration: dharana.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sustained meditation: ___.", "answer": "dhyana"},
         {"type": "true-false", "question": "Samadhi is shallow distraction.", "correctAnswer": False}]},
    {"title": "Bhakti Yoga — Devotion",
     "body_html": r"""<p>Bhakti is the path of love and devotion to a chosen deity (<em>ishta-devata</em>): Krishna, Shiva, Devi. Practice: chanting (kirtan), japa (mantra repetition with mala), darshan (seeing the deity).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Chosen deity: ___-devata.", "answer": "ishta"},
         {"type": "multiple-choice", "question": "Communal chanting: ", "options": ["kirtan", "japa", "asana", "darshan"], "correctIndex": 0},
         {"type": "true-false", "question": "Bhakti is the path of devotion.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Mantra repetition: ___.", "answer": "japa"},
         {"type": "true-false", "question": "Bhakti opposes love.", "correctAnswer": False}]},
    {"title": "Jnana Yoga — Knowledge",
     "body_html": r"""<p>Jnana is the path of inquiry: "Who am I?" Ramana Maharshi (1879–1950) is the great modern teacher of self-inquiry (<em>atma-vichara</em>).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Self-inquiry: atma-___.", "answer": "vichara"},
         {"type": "multiple-choice", "question": "Modern teacher: ", "options": ["Ramana Maharshi", "Patanjali", "Vivekananda", "Aurobindo"], "correctIndex": 0},
         {"type": "true-false", "question": "Jnana is the path of inquiry.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Central question: Who am ___ ?", "answer": "I"},
         {"type": "true-false", "question": "Ramana lived in 1500 BCE.", "correctAnswer": False}]},
    {"title": "Karma Yoga — Action",
     "body_html": r"""<p>Karma yoga is selfless action — doing what is required without attachment to results. The Bhagavad Gita is its central text.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Central text: ___ Gita.", "answer": "Bhagavad"},
         {"type": "multiple-choice", "question": "Karma yoga: ", "options": ["selfless action", "passive watching", "no action", "fasting only"], "correctIndex": 0},
         {"type": "true-false", "question": "Action is done without attachment to fruit.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Path of ___ action.", "answer": "selfless"},
         {"type": "true-false", "question": "Karma yoga forbids action.", "correctAnswer": False}]},
    {"title": "Mantra & Japa",
     "body_html": r"""<p>Mantras include Om, So Hum (I am that), Om Namah Shivaya, Hare Krishna. Japa: repeat with a 108-bead mala.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mala beads: ___.", "answer": "108"},
         {"type": "multiple-choice", "question": "I am that: ", "options": ["So Hum", "Om Namah", "Hare Krishna", "Gayatri"], "correctIndex": 0},
         {"type": "true-false", "question": "Japa = mantra repetition.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Mantra to Shiva: Om Namah ___.", "answer": "Shivaya"},
         {"type": "true-false", "question": "Mala has 7 beads.", "correctAnswer": False}]},
    {"title": "Vedanta — Non-Duality",
     "body_html": r"""<p>Advaita Vedanta (Shankara, 8th c.) teaches that Atman is Brahman. The world's apparent separateness is <em>maya</em> — appearance, not lie. Practice culminates in recognition.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Founder of Advaita: ___.", "answer": "Shankara"},
         {"type": "multiple-choice", "question": "Apparent separateness: ", "options": ["maya", "atman", "samsara", "moksha"], "correctIndex": 0},
         {"type": "true-false", "question": "Atman is Brahman.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Advaita = ___-duality.", "answer": "non"},
         {"type": "true-false", "question": "Advaita teaches multiple ultimate selves.", "correctAnswer": False}]},
    {"title": "Kundalini Yoga",
     "body_html": r"""<p>Kundalini practices aim to awaken energy at the base of the spine and lift it through the seven chakras to the crown. Methods: breath, bandhas (locks), mantra, mudra. Not for casual experimentation.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Energy at spine base: ___.", "answer": "kundalini"},
         {"type": "multiple-choice", "question": "Locks: ", "options": ["bandhas", "asanas", "mantras", "mudras"], "correctIndex": 0},
         {"type": "true-false", "question": "Energy moves to the crown.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Number of chakras: ___.", "answer": "7"},
         {"type": "true-false", "question": "Casual experimentation is recommended.", "correctAnswer": False}]},
    {"title": "Famous Modern Teachers",
     "body_html": r"""<ul><li>Swami Vivekananda — brought yoga to the West (1893).</li><li>Paramahansa Yogananda — Autobiography of a Yogi.</li><li>Sri Aurobindo — Integral Yoga.</li><li>Sivananda, Iyengar, Krishnamacharya — modern asana lineage.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Brought yoga to West: ___.", "answer": "Vivekananda"},
         {"type": "multiple-choice", "question": "Autobiography of a Yogi: ", "options": ["Yogananda", "Aurobindo", "Iyengar", "Sivananda"], "correctIndex": 0},
         {"type": "true-false", "question": "Iyengar is in modern asana lineage.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Integral Yoga: ___.", "answer": "Aurobindo"},
         {"type": "true-false", "question": "Vivekananda came to the West in 2020.", "correctAnswer": False}]},
    {"title": "Daily Hindu/Yogic Practice",
     "body_html": r"""<ul><li>Morning asana + pranayama (20–30 min).</li><li>Japa with mala (108 repetitions).</li><li>20 min seated meditation.</li><li>Reading Gita or Yoga Sutras.</li><li>Evening kirtan or arati.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Japa repetitions: ___.", "answer": "108"},
         {"type": "multiple-choice", "question": "Morning includes: ", "options": ["asana + pranayama", "TV", "shopping", "fight"], "correctIndex": 0},
         {"type": "true-false", "question": "Japa uses a mala.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Read the Bhagavad ___.", "answer": "Gita"},
         {"type": "true-false", "question": "Daily practice is unnecessary.", "correctAnswer": False}]},
    {"title": "Hindu/Yogic Checkpoint",
     "body_html": r"""<ul><li>Roots in Vedas/Upanishads, Patanjali's eight limbs.</li><li>Paths: Bhakti (devotion), Jnana (knowledge), Karma (action), Raja (royal yoga).</li><li>Asana, pranayama, mantra, japa, kirtan.</li><li>Advaita Vedanta: Atman is Brahman.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Patanjali wrote the Yoga Sutras.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Path of devotion: ", "options": ["Bhakti", "Jnana", "Karma", "Raja"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Atman is ___.", "answer": "Brahman"},
         {"type": "true-false", "question": "Advaita is non-dual.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Eight-limbed: ___.", "answer": "ashtanga"}]},
]

if __name__ == "__main__":
    render_unit(18, "Hindu & Yogic Meditation", 256, LESSONS)
