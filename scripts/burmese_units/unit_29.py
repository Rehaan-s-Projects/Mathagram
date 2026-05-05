#!/usr/bin/env python3
"""Burmese Unit 29 — Calligraphy (lessons 415-429)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Origins of Burmese Script",
     "body_html": r"""
<p>The Burmese script descends from the <strong>Brahmi family</strong> via Pyu and Mon scripts. Earliest Burmese inscriptions date to the 11th century during the Pagan dynasty.</p>
<p>The distinctive <strong>circular shapes</strong> evolved because palm-leaf manuscripts (the original writing surface) couldn't tolerate straight horizontal strokes — they would split the leaf along its grain. Curved letters preserved the leaf.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Burmese script descends from the ___ script family.", "answer": "Brahmi"},
         {"type": "multiple-choice", "question": "Why are Burmese letters circular?", "options": ["aesthetic preference", "to avoid splitting palm leaves", "religious symbolism", "easier to print"], "correctIndex": 1},
         {"type": "true-false", "question": "Burmese script first appeared in the 11th century.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Burmese script evolved from the ___ and Mon scripts.", "answer": "Pyu"},
         {"type": "true-false", "question": "Burmese was originally written on paper.", "correctAnswer": False}]},
    {"title": "Tools of Calligraphy",
     "body_html": r"""
<p>Traditional Burmese calligraphy uses:</p>
<ul>
<li><strong>Stylus (kanyit):</strong> a sharp metal tool for incising letters into palm leaves.</li>
<li><strong>Charcoal or soot ink:</strong> rubbed into the inscribed marks afterward to make them visible.</li>
<li><strong>Palm leaves (peisa):</strong> dried and treated leaves cut into long strips.</li>
</ul>
<p>Modern calligraphy uses brush, fountain pen, or ballpoint, but the round shapes remain. Bamboo brushes are popular for ceremonial documents.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "The traditional incising tool is called a ___.", "answer": "stylus"},
         {"type": "multiple-choice", "question": "Which is NOT a traditional tool?", "options": ["stylus", "soot ink", "ballpoint pen", "palm leaves"], "correctIndex": 2},
         {"type": "true-false", "question": "Modern calligraphy can use bamboo brushes.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Treated leaves used for writing are called ___.", "answer": "peisa"},
         {"type": "true-false", "question": "Charcoal ink is rubbed in after incising.", "correctAnswer": True}]},
    {"title": "The Round-Letter Aesthetic",
     "body_html": r"""
<p>Burmese letters are built from <strong>circles, arcs, and partial loops</strong>. Beautiful Burmese script has perfectly round circles, even spacing, and consistent stroke thickness.</p>
<p>Examples of circular letters:</p>
<ul>
<li>က (ka) — open at top, closed at bottom</li>
<li>သ (tha) — full circle on right</li>
<li>ဝ (wa) — pure circle</li>
<li>ဎ (dha) — circle with bar</li>
</ul>
<p>Letter ဝ (wa) is the simplest possible Burmese letter: a single perfect circle.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese letters are built from circles and arcs.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The simplest Burmese letter is:", "options": ["က", "သ", "ဝ", "ဎ"], "correctIndex": 2},
         {"type": "fill-blank", "question": "ဝ is pronounced ___.", "answer": "wa"},
         {"type": "true-false", "question": "Beautiful Burmese script has uneven circles.", "correctAnswer": False},
         {"type": "fill-blank", "question": "က is open at the ___.", "answer": "top"}]},
    {"title": "Stroke Order Basics",
     "body_html": r"""
<p>General principles for writing Burmese letters by hand:</p>
<ul>
<li>Most letters start at the upper-left and move counter-clockwise around the loop.</li>
<li>Vertical descending strokes are drawn last.</li>
<li>Diacritics (vowel marks, tones) are added after the base consonant.</li>
<li>Stacked consonants are written from top to bottom.</li>
</ul>
<p>Stroke order matters less for legibility than for speed and consistency. Following standard order makes your writing flow.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "Most Burmese letters start at:", "options": ["lower-right", "upper-left", "center", "anywhere"], "correctIndex": 1},
         {"type": "true-false", "question": "Diacritics are usually added AFTER the base consonant.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Stacked consonants are written ___ to ___.", "answer": "top, bottom"},
         {"type": "true-false", "question": "Stroke order is irrelevant.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "Loops are typically drawn:", "options": ["clockwise", "counter-clockwise", "either", "depends on letter"], "correctIndex": 1}]},
    {"title": "Practicing the Circle Strokes",
     "body_html": r"""
<p>Drill: draw rows of perfect circles. Aim for:</p>
<ul>
<li>Same diameter for each circle.</li>
<li>Consistent line weight.</li>
<li>Even spacing between circles.</li>
<li>Smooth, unbroken lines.</li>
</ul>
<p>Then practice the most common circular letter (ဝ) repeatedly. Then graduate to two-arc letters like သ (tha) and စ (sa). The fundamentals matter; rushing leads to messy script.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Practicing simple circles is a foundational drill.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Which letter is just a circle?", "options": ["က", "ဝ", "သ", "ဎ"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Two-arc letters like ___ build on circle skills.", "answer": "သ"},
         {"type": "true-false", "question": "Inconsistent line weight is fine for calligraphy.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Burmese letter စ is romanized as ___.", "answer": "sa"}]},
    {"title": "Letter Spacing",
     "body_html": r"""
<p>Burmese has no spaces between words within a phrase — only between phrases or sentences. Letters within a syllable nest tightly together.</p>
<p>Spacing principles:</p>
<ul>
<li>Letters of the same syllable touch or overlap slightly.</li>
<li>Different syllables in the same word are separated by a small gap.</li>
<li>Phrases are separated by larger gaps; sentences by larger still.</li>
<li>Punctuation: ၊ (small comma) for phrases, ။ (large square) for sentences.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese has no word spaces within phrases.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The sentence-ending punctuation is:", "options": ["၊", "။", ".", "!"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Phrase-ending punctuation is ___ in Burmese script.", "answer": "၊"},
         {"type": "true-false", "question": "Letters within a syllable can overlap.", "correctAnswer": True},
         {"type": "true-false", "question": "All Burmese punctuation is borrowed from English.", "correctAnswer": False}]},
    {"title": "Writing Numerals 0-9",
     "body_html": r"""
<p>Burmese has its own numerals, related to but distinct from Arabic numerals. They share the underlying decimal system.</p>
<ul>
<li>၀ — 0</li>
<li>၁ — 1</li>
<li>၂ — 2</li>
<li>၃ — 3</li>
<li>၄ — 4</li>
<li>၅ — 5</li>
<li>၆ — 6</li>
<li>၇ — 7</li>
<li>၈ — 8</li>
<li>၉ — 9</li>
</ul>
<p>So 2025 is written ၂၀၂၅ in Burmese numerals. Both Arabic and Burmese numerals are used in modern Myanmar.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "၀ represents the digit ___.", "answer": "0"},
         {"type": "multiple-choice", "question": "The number 2025 in Burmese is:", "options": ["၂၀၂၅", "၂၀၂", "၂၅", "၂၀၂၆"], "correctIndex": 0},
         {"type": "true-false", "question": "Modern Myanmar uses both Burmese and Arabic numerals.", "correctAnswer": True},
         {"type": "fill-blank", "question": "၇ is the digit ___.", "answer": "7"},
         {"type": "true-false", "question": "Burmese numerals don't use the decimal system.", "correctAnswer": False}]},
    {"title": "Writing Common Greetings",
     "body_html": r"""
<p>Practice writing the most common greetings:</p>
<ul>
<li>မင်္ဂလာပါ — Mingalaba (Hello)</li>
<li>ကျေးဇူးတင်ပါတယ် — Kyei zu tin ba de (Thank you)</li>
<li>ဘယ်လိုလဲ — How are you?</li>
<li>ကောင်းပါတယ် — I'm fine.</li>
<li>သွားတော့မယ် — I'm leaving now.</li>
</ul>
<p>Calligraphic versions emphasize circular letters and proper spacing. These greetings are commonly seen on shop signs and letterhead.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "မင်္ဂလာပါ means:", "options": ["Goodbye", "Hello", "Sorry", "Please"], "correctIndex": 1},
         {"type": "fill-blank", "question": "ကျေးဇူးတင်ပါတယ် means \"___ you\".", "answer": "thank"},
         {"type": "true-false", "question": "Greetings are commonly seen on shop signs.", "correctAnswer": True},
         {"type": "fill-blank", "question": "သွားတော့မယ် means \"I'm ___\".", "answer": "leaving"},
         {"type": "true-false", "question": "ကောင်းပါတယ် is a verb meaning \"to come\".", "correctAnswer": False}]},
    {"title": "Writing Names",
     "body_html": r"""
<p>Burmese names follow phonological patterns; you can transliterate any name into Burmese script if you know the sounds. Names are not divided into "first/last" — Burmese personal names are full given names with no surnames in the Western sense.</p>
<p>Examples:</p>
<ul>
<li>Aung — အောင်</li>
<li>San — ဆန်း</li>
<li>Suu Kyi — စုကြည်</li>
<li>Maung — မောင် (used as honorific for younger men)</li>
</ul>
<p>To transliterate a foreign name, find the closest Burmese sounds and write them syllable by syllable.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese names lack Western-style surnames.", "correctAnswer": True},
         {"type": "fill-blank", "question": "မောင် is an honorific for younger ___.", "answer": "men"},
         {"type": "multiple-choice", "question": "Aung in Burmese script is:", "options": ["စု", "အောင်", "ဆန်း", "မောင်"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Suu Kyi in Burmese: ___ .", "answer": "စုကြည်"},
         {"type": "true-false", "question": "Foreign names can be transliterated into Burmese script.", "correctAnswer": True}]},
    {"title": "Palm-Leaf Manuscripts (Parabaik)",
     "body_html": r"""
<p>Before paper, Burmese texts were written on prepared palm leaves bound into <strong>parabaik</strong> (folded books). The accordion-fold structure allowed long texts. Pages were inscribed with stylus, then darkened with soot.</p>
<p>Major surviving works on parabaik include:</p>
<ul>
<li>The Glass Palace Chronicle (Hmannan Yazawin) — royal Burmese history.</li>
<li>The Tipitaka — Buddhist canon, copied for centuries.</li>
<li>Astrology and medical texts.</li>
</ul>
<p>Many ancient palm-leaf manuscripts survive in Myanmar's monasteries today.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Parabaik are folded palm-leaf books.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The Glass Palace Chronicle is:", "options": ["a Buddhist text", "Burmese royal history", "a medical guide", "a poetry collection"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Burmese palm-leaf manuscripts are called ___.", "answer": "parabaik"},
         {"type": "true-false", "question": "Many ancient parabaik survive in monasteries.", "correctAnswer": True},
         {"type": "fill-blank", "question": "The Buddhist canon is called the ___.", "answer": "Tipitaka"}]},
    {"title": "Modern Burmese Fonts",
     "body_html": r"""
<p>Modern computer fonts for Burmese include:</p>
<ul>
<li><strong>Padauk:</strong> open-source standard, named after Myanmar's national flower.</li>
<li><strong>Myanmar3:</strong> common in Microsoft Office.</li>
<li><strong>Pyidaungsu:</strong> the official government font.</li>
<li><strong>Zawgyi:</strong> historical font; non-Unicode-compliant; legacy.</li>
</ul>
<p>For decades, Zawgyi was the de facto Burmese encoding online — but it's incompatible with international Unicode. Myanmar formally migrated to Unicode in 2019.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "Padauk is named after Myanmar's national:", "options": ["flag", "flower", "tree", "river"], "correctIndex": 1},
         {"type": "true-false", "question": "Zawgyi is Unicode-compliant.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Myanmar formally migrated to Unicode in ___.", "answer": "2019"},
         {"type": "true-false", "question": "Pyidaungsu is the official government font.", "correctAnswer": True},
         {"type": "fill-blank", "question": "An open-source standard font is ___.", "answer": "Padauk"}]},
    {"title": "Calligraphy Styles",
     "body_html": r"""
<p>Several Burmese calligraphy styles exist:</p>
<ul>
<li><strong>Manuscript style</strong> (ပိဋက poh-tah-ka): rounded, cursive, found in palm-leaf books.</li>
<li><strong>Modern print style</strong>: sharper, more uniform — designed for clarity in books and signage.</li>
<li><strong>Ceremonial display style</strong>: elaborate flourishes; used on temple inscriptions and royal documents.</li>
<li><strong>Children's primer style</strong>: simplified, oversize letters for young learners.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Different calligraphy styles serve different purposes.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Ceremonial display style is used for:", "options": ["children's books", "temple inscriptions", "newspapers", "modern fiction"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Manuscript style is found on ___-leaf books.", "answer": "palm"},
         {"type": "true-false", "question": "Modern print style emphasizes clarity.", "correctAnswer": True},
         {"type": "true-false", "question": "Children's primer style uses small, complex letters.", "correctAnswer": False}]},
    {"title": "Beautiful Handwriting Tips",
     "body_html": r"""
<p>Practical advice from Burmese calligraphy teachers:</p>
<ul>
<li>Use grid paper or guidelines until your circles are consistent.</li>
<li>Practice slow before fast — speed comes from muscle memory, not hurry.</li>
<li>Keep your hand relaxed; tense fingers produce shaky lines.</li>
<li>Daily 15-minute practice beats weekly hour-long sessions.</li>
<li>Imitate good models: copy from a textbook your script you admire.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Daily 15-minute practice helps more than weekly sessions.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "What helps consistent circles?", "options": ["rushing", "grid paper", "tense fingers", "no practice"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Speed comes from ___ memory.", "answer": "muscle"},
         {"type": "true-false", "question": "Tense fingers produce smoother lines.", "correctAnswer": False},
         {"type": "true-false", "question": "Imitating models is a good way to learn.", "correctAnswer": True}]},
    {"title": "Practice: Copy a Quote",
     "body_html": r"""
<p>Practice copying this Burmese proverb in your best handwriting:</p>
<p style="font-size:1.5em; text-align:center;">အသိဉာဏ်သည် ရွှေထက်အဖိုးတန်သည်။</p>
<p>Romanization: <em>A-thi-nyan thi shwe htet a-pho tan thi.</em></p>
<p>Meaning: "Wisdom is more valuable than gold."</p>
<p>Trace the circular shapes. Notice how the words flow without spaces. End with the sentence-final punctuation ။. This is a classic Burmese proverb — common on temple walls and schoolroom posters.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "The proverb means \"Wisdom is more valuable than ___.\"", "answer": "gold"},
         {"type": "multiple-choice", "question": "Sentence-final punctuation is:", "options": ["၊", "။", ".", "!"], "correctIndex": 1},
         {"type": "true-false", "question": "Burmese words within a sentence have spaces between them.", "correctAnswer": False},
         {"type": "fill-blank", "question": "ရွှေ means ___.", "answer": "gold"},
         {"type": "true-false", "question": "Tracing helps build muscle memory.", "correctAnswer": True}]},
    {"title": "Calligraphy Checkpoint",
     "body_html": r"""
<p>Recap of Unit 29:</p>
<ul>
<li>Burmese script descends from Brahmi via Pyu and Mon, with circular shapes evolved for palm-leaf preservation.</li>
<li>Traditional tools: stylus, palm leaves (peisa), soot ink. Modern: pens and brushes.</li>
<li>Strokes generally start upper-left, loop counter-clockwise, with vertical lines last.</li>
<li>Burmese has its own numerals (၀-၉) and punctuation (၊ for phrase, ။ for sentence).</li>
<li>Modern fonts: Padauk, Pyidaungsu, Myanmar3 — all Unicode. Zawgyi is legacy.</li>
<li>Multiple calligraphy styles: manuscript, print, ceremonial, primer.</li>
<li>Daily short practice beats long, irregular sessions.</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Burmese script descends from the ___ family.", "answer": "Brahmi"},
         {"type": "multiple-choice", "question": "Sentence-final punctuation:", "options": ["၊", "။", ".", "!"], "correctIndex": 1},
         {"type": "true-false", "question": "Zawgyi is Unicode-compliant.", "correctAnswer": False},
         {"type": "fill-blank", "question": "The traditional writing surface was the ___ leaf.", "answer": "palm"},
         {"type": "true-false", "question": "Most Burmese letters are built from circles and arcs.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Burmese digits run from ၀ to ___.", "answer": "၉"},
         {"type": "true-false", "question": "Palm-leaf books are called parabaik.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(29, "Burmese Calligraphy", 415, LESSONS)
