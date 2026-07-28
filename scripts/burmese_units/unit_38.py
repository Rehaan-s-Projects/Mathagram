#!/usr/bin/env python3
"""Burmese Unit 38 — Buddhist Texts (lessons 550-564)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "The Tipitaka",
     "body_html": r"""<p>The Pali Canon (Tipitaka) is the core Theravada Buddhist scripture. \"Three baskets\":</p><ul><li>Vinaya — monastic rules</li><li>Sutta — discourses of the Buddha</li><li>Abhidhamma — philosophy</li></ul><p>Burmese monks have memorized full sections (and rare individuals the entire 40+ volumes).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Three baskets in Pali: Ti___.", "answer": "pitaka"},
         {"type": "multiple-choice", "question": "Vinaya covers:", "options": ["philosophy", "discourses", "monastic rules", "poetry"], "correctIndex": 2},
         {"type": "true-false", "question": "Sutta is Buddha's discourses.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Abhidhamma covers ___.", "answer": "philosophy"},
         {"type": "true-false", "question": "Some Burmese monks memorize the entire Tipitaka.", "correctAnswer": True}]},
    {"title": "Pali in Burmese Buddhism",
     "body_html": r"""<p>Pali is the liturgical language. Most chants and many proverbs are in Pali, written in Burmese script.</p><ul><li>Pali letters reuse Burmese script with extra diacritics.</li><li>"Buddhaṃ saraṇaṃ gacchāmi" — "I take refuge in the Buddha." Common chant.</li><li>Monks learn Pali in monasteries from boyhood.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Pali is the liturgical language of Burmese Buddhism.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"I take refuge in the ___.\"", "answer": "Buddha"},
         {"type": "multiple-choice", "question": "Pali letters use:", "options": ["Latin alphabet", "Burmese script + diacritics", "Devanagari", "Tibetan"], "correctIndex": 1},
         {"type": "true-false", "question": "Monks learn Pali in monasteries.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Refuge in Pali: ___.", "answer": "saraṇaṃ"}]},
    {"title": "The Three Refuges",
     "body_html": r"""<p>Common chant before any Buddhist activity:</p><ol><li>Buddhaṃ saraṇaṃ gacchāmi — "I take refuge in the Buddha."</li><li>Dhammaṃ saraṇaṃ gacchāmi — "...the Dhamma (teachings)."</li><li>Saṅghaṃ saraṇaṃ gacchāmi — "...the Sangha (monastic community)."</li></ol>""",
     "exercises": [
         {"type": "fill-blank", "question": "Refuge 2: ___ (the teachings).", "answer": "Dhamma"},
         {"type": "multiple-choice", "question": "Number of refuges:", "options": ["1", "2", "3", "5"], "correctIndex": 2},
         {"type": "true-false", "question": "The third refuge is the Sangha.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sangha = monastic ___.", "answer": "community"},
         {"type": "true-false", "question": "Refuges are recited before activities.", "correctAnswer": True}]},
    {"title": "The Mangala Sutta",
     "body_html": r"""<p>The "Discourse on Blessings" — recited at home blessings, weddings, new-year. Lists 38 blessings: associating with the wise, supporting parents, gentleness, generosity, study, and more.</p><p>Often the first text Burmese children learn.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Mangala Sutta lists 38 blessings.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Mangala Sutta is recited at:", "options": ["funerals only", "weddings, blessings, new year", "battles", "every meal"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Mangala means \"___\".", "answer": "blessing"},
         {"type": "true-false", "question": "Generosity is mentioned as a blessing.", "correctAnswer": True},
         {"type": "true-false", "question": "Burmese children rarely study this text.", "correctAnswer": False}]},
    {"title": "The Metta Sutta",
     "body_html": r"""<p>"Discourse on Loving-Kindness" (မေတ္တာ). Recited daily in many homes. Famous opening: "May all beings be happy and safe; may they be at ease."</p><p>Metta meditation: silently wish goodwill to oneself, loved ones, neutral parties, even adversaries.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Loving-kindness: ___.", "answer": "metta"},
         {"type": "multiple-choice", "question": "Metta meditation includes:", "options": ["only family", "only friends", "all beings including adversaries", "only the meditator"], "correctIndex": 2},
         {"type": "true-false", "question": "Metta Sutta is recited daily in many homes.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"May all beings be ___ and safe.\"", "answer": "happy"},
         {"type": "true-false", "question": "Metta extends to adversaries.", "correctAnswer": True}]},
    {"title": "The Karaniya Sutta",
     "body_html": r"""<p>The Karaniya Sutta describes the qualities one should cultivate: capable, upright, gentle, content, calm, wise. Closely connected to the Metta Sutta.</p><p>Used as a daily aspiration text.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Karaniya Sutta describes desired qualities.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Closely connected to:", "options": ["Mangala Sutta", "Metta Sutta", "Dhammapada", "Vinaya"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Quality: gentle, content, ___.", "answer": "wise"},
         {"type": "true-false", "question": "Used as daily aspiration text.", "correctAnswer": True},
         {"type": "true-false", "question": "Lists qualities to AVOID.", "correctAnswer": False}]},
    {"title": "The Dhammapada",
     "body_html": r"""<p>423 verses of moral wisdom — the most-translated Buddhist text. Verses cover karma, mindfulness, anger, friendship, the wise vs the foolish.</p><p>Famous opening: "All that we are is the result of what we have thought."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number of verses: ___.", "answer": "423"},
         {"type": "multiple-choice", "question": "Dhammapada is:", "options": ["the longest sutta", "423 verses of moral wisdom", "rules for monks", "history"], "correctIndex": 1},
         {"type": "true-false", "question": "It's the most-translated Buddhist text.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"All that we are is the result of what we have ___.\"", "answer": "thought"},
         {"type": "true-false", "question": "Covers karma, mindfulness, anger, friendship.", "correctAnswer": True}]},
    {"title": "Jataka Tales",
     "body_html": r"""<p>547 stories of the Buddha's previous lives — born as kings, animals, hermits, demonstrating virtues and karma in action.</p><p>Famous: the deer king, the monkey king, the hare in the moon. Used to teach children moral lessons.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Jataka tales total 547 stories.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Jataka tales describe:", "options": ["future lives", "Buddha's previous lives", "monk rules", "philosophy"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Famous animal: the deer ___.", "answer": "king"},
         {"type": "true-false", "question": "Used to teach children moral lessons.", "correctAnswer": True},
         {"type": "true-false", "question": "Jataka tales feature only humans.", "correctAnswer": False}]},
    {"title": "The Burmese Pali Tradition",
     "body_html": r"""<p>Myanmar has been a center of Pali Buddhist scholarship for centuries. The 5th Buddhist Council in Mandalay (1871) carved the entire Tipitaka into 729 marble slabs at Kuthodaw Pagoda — \"the world's largest book.\"</p>""",
     "exercises": [
         {"type": "true-false", "question": "Kuthodaw Pagoda houses 729 marble slabs of the Tipitaka.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "5th Buddhist Council location:", "options": ["Yangon", "Mandalay", "Bagan", "Inle"], "correctIndex": 1},
         {"type": "fill-blank", "question": "The world's largest ___ is at Kuthodaw.", "answer": "book"},
         {"type": "true-false", "question": "Year of 5th Council: 1871.", "correctAnswer": True},
         {"type": "true-false", "question": "Burma is a major center of Pali scholarship.", "correctAnswer": True}]},
    {"title": "Reading Pali in Burmese Script",
     "body_html": r"""<p>Pali words use the same Burmese letters but pronunciation follows Pali rules. For example, the conjunction "ca" (and) is written စ but pronounced /tʃa/ (English-like \"cha\") in Pali contexts.</p><p>Aspiration in Pali matters; double consonants are doubled.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Pali uses Burmese script with Pali pronunciation rules.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Pali \"ca\" (and) sounds like:", "options": ["/sa/", "/tʃa/ (cha)", "/ka/", "/ja/"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Aspiration in Pali ___.", "answer": "matters"},
         {"type": "true-false", "question": "Double consonants are pronounced double.", "correctAnswer": True},
         {"type": "true-false", "question": "Pali pronunciation matches modern Burmese exactly.", "correctAnswer": False}]},
    {"title": "Common Pali Phrases",
     "body_html": r"""<ul><li>Sabbe sattā sukhitā hontu — "May all beings be happy."</li><li>Buddhaṃ saraṇaṃ gacchāmi — "I take refuge in the Buddha."</li><li>Anicca, dukkha, anatta — "Impermanence, suffering, non-self." (Three marks of existence.)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Three marks: anicca, dukkha, ___.", "answer": "anatta"},
         {"type": "multiple-choice", "question": "Sabbe sattā:", "options": ["all wisdom", "all beings", "all monks", "all teachings"], "correctIndex": 1},
         {"type": "true-false", "question": "Anicca means impermanence.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Refuge in Pali: ___.", "answer": "saraṇaṃ"},
         {"type": "true-false", "question": "Anatta means \"non-self.\"", "correctAnswer": True}]},
    {"title": "Vipassana & Texts",
     "body_html": r"""<p>The Mahāsatipaṭṭhāna Sutta (\"Great Discourse on the Foundations of Mindfulness\") is the foundational text for vipassana practice. Lists four areas of mindfulness: body, feelings, mind, mental phenomena.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Four areas: body, feelings, mind, mental ___.", "answer": "phenomena"},
         {"type": "multiple-choice", "question": "Sutta name (short):", "options": ["Metta", "Mahasatipatthana", "Mangala", "Karaniya"], "correctIndex": 1},
         {"type": "true-false", "question": "It's the foundational vipassana text.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Mindfulness in Pali: sati___ thāna.", "answer": "paṭ"},
         {"type": "true-false", "question": "Lists 4 foundations of mindfulness.", "correctAnswer": True}]},
    {"title": "Devotional Practice",
     "body_html": r"""<p>Daily devotional practice (devotion) elements:</p><ul><li>Bowing to Buddha image (3x).</li><li>Reciting refuges and precepts.</li><li>Offerings: flowers, water, light.</li><li>Recollection of qualities of Buddha, Dhamma, Sangha.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Bow 3x to Buddha image.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Common offering:", "options": ["weapons", "flowers, water, light", "money only", "meat"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Recollect Buddha, Dhamma, ___.", "answer": "Sangha"},
         {"type": "true-false", "question": "Daily practice is uncommon in Buddhist Myanmar.", "correctAnswer": False},
         {"type": "true-false", "question": "Reciting refuges is part of devotional practice.", "correctAnswer": True}]},
    {"title": "Practice: Recite a Short Sutta",
     "body_html": r"""<p>Practice the opening of the Metta Sutta:</p><p style="font-size:1.2em; text-align:center;">"Sabbe sattā sukhitā hontu, sabbe sattā averā hontu, sabbe sattā abyāpajjhā hontu."</p><p>"May all beings be happy. May all beings be free from enmity. May all beings be free from harm."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sabbe ___ sukhitā hontu.", "answer": "sattā"},
         {"type": "multiple-choice", "question": "averā means:", "options": ["happy", "free from enmity", "wise", "wealthy"], "correctIndex": 1},
         {"type": "true-false", "question": "abyāpajjhā = free from harm.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"May all beings be ___.\" (sukhitā = ?)", "answer": "happy"},
         {"type": "true-false", "question": "Metta phrases extend goodwill broadly.", "correctAnswer": True}]},
    {"title": "Buddhist Texts Checkpoint",
     "body_html": r"""<p>Recap of Unit 38:</p><ul><li>Tipitaka: Vinaya, Sutta, Abhidhamma — the Pali Canon.</li><li>Pali is the liturgical language; written in Burmese script.</li><li>Three Refuges: Buddha, Dhamma, Sangha.</li><li>Famous suttas: Mangala (blessings), Metta (loving-kindness), Karaniya, Mahasatipatthana.</li><li>Dhammapada — 423 verses; Jatakas — 547 past-life stories.</li><li>Kuthodaw Pagoda has the world's largest book (Tipitaka in marble).</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tipitaka = three ___.", "answer": "baskets"},
         {"type": "multiple-choice", "question": "Number of Dhammapada verses:", "options": ["108", "227", "423", "547"], "correctIndex": 2},
         {"type": "true-false", "question": "Vinaya covers monastic rules.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Number of Jataka tales: ___.", "answer": "547"},
         {"type": "fill-blank", "question": "Loving-kindness sutta: ___.", "answer": "Metta"},
         {"type": "true-false", "question": "Pali uses Devanagari script in Myanmar.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Mindfulness sutta: Maha___ patthana.", "answer": "sati"}]},
]

if __name__ == "__main__":
    render_unit(38, "Burmese Buddhist Texts", 550, LESSONS)
