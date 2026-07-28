#!/usr/bin/env python3
"""Burmese Unit 28 — Pronunciation Drills (lessons 400-414)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "The Three Tones in Detail",
     "body_html": r"""
<p>Burmese is a tonal language. Every vowel carries one of three lexical tones, marked in writing by special symbols.</p>
<ul>
<li><strong>Low tone (level):</strong> ka က — a steady, even pitch, slightly drawn out.</li>
<li><strong>High tone (falling):</strong> ká ကာ — starts high and falls; held longer.</li>
<li><strong>Creaky tone (high checked):</strong> kâ ကား — sharp, short, with vocal-fry creak at the end.</li>
</ul>
<p>Same consonant + vowel, three different words. Mastering the tone difference is the most important pronunciation skill in Burmese.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "How many lexical tones does Burmese have?", "options": ["2", "3", "4", "5"], "correctIndex": 1},
         {"type": "fill-blank", "question": "The tone with vocal-fry creak is called the ___ tone.", "answer": "creaky"},
         {"type": "true-false", "question": "Tones change the meaning of a Burmese word.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Which tone is held longest?", "options": ["low (level)", "high (falling)", "creaky", "all equal"], "correctIndex": 1},
         {"type": "true-false", "question": "Burmese is a tonal language.", "correctAnswer": True}]},
    {"title": "Low Tone Practice",
     "body_html": r"""
<p>The <strong>low tone</strong> is the unmarked default. Pitch stays steady at a mid-low level, the syllable is medium length.</p>
<p>Examples (low tone):</p>
<ul>
<li>က ka — "to dance" (verb stem)</li>
<li>မ ma — used in negation</li>
<li>လ la — "to come"</li>
<li>သ tha — "son"</li>
</ul>
<p><strong>Drill:</strong> Say each syllable with a calm, even voice — no rise, no fall, no creak. Compare to the high and creaky versions in the next lessons.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Low tone has a steady, even pitch.", "correctAnswer": True},
         {"type": "fill-blank", "question": "က in low tone means \"to ___\" (verb stem).", "answer": "dance"},
         {"type": "multiple-choice", "question": "Low tone is:", "options": ["the unmarked default", "always marked with a special character", "a question marker", "a falling tone"], "correctIndex": 0},
         {"type": "true-false", "question": "Low tone has vocal-fry creak.", "correctAnswer": False},
         {"type": "fill-blank", "question": "သ in low tone means \"___\".", "answer": "son"}]},
    {"title": "Creaky Tone Practice",
     "body_html": r"""
<p>The <strong>creaky tone</strong> (sometimes called "high-checked") is short, sharp, and ends with vocal-fry creak — like the English "uh-oh" feeling. Mark in writing: a small dot under the syllable (auk myit).</p>
<p>Examples (creaky tone):</p>
<ul>
<li>က့ ka̰ — used in some words for "I" (informal/female speaker)</li>
<li>မိ mḭ — "mother" (informal)</li>
<li>သ့ tha̰ — "thin" (adjective)</li>
</ul>
<p><strong>Tip:</strong> Imagine cutting the syllable short with a slight glottal squeeze at the end. This is the same kind of creakiness American English sometimes has at the end of phrases.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Creaky tone is short and sharp.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Creaky tone ends with:", "options": ["a rising pitch", "vocal-fry creak", "a long fall", "no special feature"], "correctIndex": 1},
         {"type": "fill-blank", "question": "The diacritic mark for creaky tone is called auk ___.", "answer": "myit"},
         {"type": "true-false", "question": "Creaky tone is the longest of the three tones.", "correctAnswer": False},
         {"type": "fill-blank", "question": "မိ creaky tone means \"___\" (informal).", "answer": "mother"}]},
    {"title": "High Tone Practice",
     "body_html": r"""
<p>The <strong>high tone</strong> (sometimes called "heavy" or "falling") starts at a high pitch and falls, with the syllable held noticeably longer than the others. Mark in writing: a long stroke (visarga) ◌း after the syllable.</p>
<p>Examples (high tone):</p>
<ul>
<li>ကား ká — "car"</li>
<li>မား má — "to be hard"</li>
<li>လား lá — question marker (yes/no questions)</li>
<li>သား thá — "son" (more formal than သ)</li>
</ul>
<p><strong>Drill:</strong> Compare the three: က ka (low) — က့ ka̰ (creaky) — ကား ká (high). Same consonant-vowel, three meanings.</p>""",
     "exercises": [
         {"type": "true-false", "question": "The high tone is held longer than the others.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "ကား means:", "options": ["dance", "car", "come", "mother"], "correctIndex": 1},
         {"type": "fill-blank", "question": "The visarga mark used for high tone looks like ___ vertical dots.", "answer": "two"},
         {"type": "true-false", "question": "လား is a question marker.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Which tone has a clearly falling pitch?", "options": ["low", "creaky", "high", "none"], "correctIndex": 2}]},
    {"title": "Tone-Pair Minimal Pairs",
     "body_html": r"""
<p>Practice telling tones apart with these minimal pairs — same syllable, different tones, different meanings.</p>
<ul>
<li>က ka (dance) / က့ ka̰ (one of) / ကား ká (car)</li>
<li>မ ma (girl) / မ့ ma̰ (mother, informal) / မား má (to be hard)</li>
<li>လ la (come) / လ့ la̰ (moon) / လား lá (?, question marker)</li>
<li>သ tha (son) / သ့ tha̰ (thin) / သား thá (son, formal)</li>
</ul>
<p><strong>Drill:</strong> Repeat each triplet aloud. Record yourself if you can — most learners struggle to hear their own tone errors.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "လ in low tone means:", "options": ["come", "moon", "?", "go"], "correctIndex": 0},
         {"type": "fill-blank", "question": "The high-tone version of \"come\" is the question marker ___.", "answer": "lá"},
         {"type": "true-false", "question": "Same syllable + different tones = different words.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "မား (high tone) means:", "options": ["girl", "to be hard", "mother", "dance"], "correctIndex": 1},
         {"type": "true-false", "question": "Recording yourself helps learn tones.", "correctAnswer": True}]},
    {"title": "Aspirated vs Unaspirated Stops",
     "body_html": r"""
<p>Burmese distinguishes <strong>aspirated</strong> stops (with a puff of air) from <strong>unaspirated</strong> stops (without). This is contrastive — different words.</p>
<p>Pairs:</p>
<ul>
<li>က k vs ခ kh — ka (dance) / kha (bitter)</li>
<li>စ s vs ဆ hs — sa (eat) / hsa (medicine)</li>
<li>တ t vs ထ th — ta (one) / tha (carry)</li>
<li>ပ p vs ဖ ph — pa (go) / pha (frog)</li>
</ul>
<p><strong>Tip:</strong> Hold a tissue in front of your mouth. Aspirated stops should make it flutter; unaspirated stops shouldn't.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Aspirated stops involve a puff of air.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "ခ vs က differ in:", "options": ["aspiration", "tone", "meaning only", "spelling only"], "correctIndex": 0},
         {"type": "fill-blank", "question": "ဖ ph means \"___\".", "answer": "frog"},
         {"type": "true-false", "question": "ka and kha mean the same thing.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Tissue in front of mouth: aspirated makes it ___.", "answer": "flutter"}]},
    {"title": "Voiced vs Voiceless Consonants",
     "body_html": r"""
<p>Burmese distinguishes voiced from voiceless consonants. In some positions, voicing changes meaning.</p>
<p>Pairs:</p>
<ul>
<li>က k (voiceless) vs ဂ g (voiced)</li>
<li>စ s (voiceless) vs ဇ z (voiced)</li>
<li>တ t (voiceless) vs ဒ d (voiced)</li>
<li>ပ p (voiceless) vs ဗ b (voiced)</li>
</ul>
<p>Voicing also occurs naturally between vowels (intervocalic voicing). The unvoiced consonant of one word may become voiced when it sits between vowels in a phrase.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "ဂ vs က differ by:", "options": ["aspiration", "voicing", "tone", "vowel length"], "correctIndex": 1},
         {"type": "true-false", "question": "Voicing can change between vowels.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ဇ is the voiced version of ___.", "answer": "စ"},
         {"type": "true-false", "question": "p (ပ) is voiced.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "Intervocalic voicing means voicing changes:", "options": ["between vowels", "before vowels", "after consonants", "at word start"], "correctIndex": 0}]},
    {"title": "Nasal Consonants",
     "body_html": r"""
<p>Burmese has four nasal consonants:</p>
<ul>
<li>င ng (velar nasal, like English "sing")</li>
<li>ည ny (palatal nasal, "ny" as in "canyon")</li>
<li>န n (alveolar nasal, like English "n")</li>
<li>မ m (bilabial nasal, like English "m")</li>
</ul>
<p>The velar nasal can appear at the start of a word (ငါး ngá "five") — unlike English, where "ng" only occurs at the end.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ငါး means \"___\".", "answer": "five"},
         {"type": "multiple-choice", "question": "Burmese has __ nasal consonants.", "options": ["2", "3", "4", "5"], "correctIndex": 2},
         {"type": "true-false", "question": "Velar nasal can begin a word in Burmese.", "correctAnswer": True},
         {"type": "fill-blank", "question": "မ is the ___ nasal.", "answer": "bilabial"},
         {"type": "true-false", "question": "English allows word-initial \"ng-\".", "correctAnswer": False}]},
    {"title": "Glottal Stop (Final ʔ)",
     "body_html": r"""
<p>Many Burmese syllables end with a <strong>glottal stop</strong>, written with the asat ်  on a stop consonant (က်, တ်, ပ်). The vowel is cut off abruptly.</p>
<p>Examples:</p>
<ul>
<li>မက် meʔ — "to like"</li>
<li>ထိပ် theiʔ — "tip / top"</li>
<li>လုပ် louʔ — "to do / make"</li>
</ul>
<p>The asat suppresses the consonant's inherent vowel. This is one of the most common ways Burmese syllables end.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "The asat suppresses the consonant's inherent ___.", "answer": "vowel"},
         {"type": "multiple-choice", "question": "လုပ် means:", "options": ["to like", "tip", "to do", "to come"], "correctIndex": 2},
         {"type": "true-false", "question": "Glottal stops cut off the vowel abruptly.", "correctAnswer": True},
         {"type": "fill-blank", "question": "မက် means \"to ___\".", "answer": "like"},
         {"type": "true-false", "question": "Asat is written above the consonant.", "correctAnswer": True}]},
    {"title": "Vowel Length",
     "body_html": r"""
<p>Burmese vowels can be short or long, and length sometimes distinguishes words. Long vowels are typically marked with the diacritic ◌ါ or the doubling implied by the high tone.</p>
<p>Examples:</p>
<ul>
<li>က ka (short) vs ကာ kaa (long)</li>
<li>စ sa (short) vs စာ saa "letter, document" (long)</li>
<li>လ la (short) vs လာ laa "to come" (long)</li>
</ul>
<p>Length interacts with tone — long vowels are typical of high and creaky tones, short of low tones, but the system isn't perfectly clean.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Vowel length can change a word's meaning in Burmese.", "correctAnswer": True},
         {"type": "fill-blank", "question": "စာ means \"___\".", "answer": "letter"},
         {"type": "multiple-choice", "question": "Long vowels are typically associated with:", "options": ["low tone", "high or creaky tones", "no tone", "loudness"], "correctIndex": 1},
         {"type": "fill-blank", "question": "The Burmese letter for long /aa/ is written with a ___-shaped extender.", "answer": "vertical"},
         {"type": "true-false", "question": "Vowel length and tone always match perfectly.", "correctAnswer": False}]},
    {"title": "Diphthongs",
     "body_html": r"""
<p>A diphthong is a vowel sound that glides from one position to another. Burmese has several:</p>
<ul>
<li>ai — as in ကိုက် kaiʔ "to bite"</li>
<li>au — as in ကောင် kaung "good (used in compounds)"</li>
<li>ei — as in ကေး "to give" (varies by dialect)</li>
<li>ou — as in ဂုဏ် goun "honor"</li>
</ul>
<p>Diphthongs are written with combinations of vowel marks — for example, the ◌ို + asat structure produces /ai/.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ကိုက် means \"to ___\".", "answer": "bite"},
         {"type": "multiple-choice", "question": "ဂုဏ် means:", "options": ["good", "honor", "five", "bite"], "correctIndex": 1},
         {"type": "true-false", "question": "Diphthongs glide from one vowel position to another.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ကောင် is a vowel diphthong written ___.", "answer": "au"},
         {"type": "true-false", "question": "Burmese has no diphthongs.", "correctAnswer": False}]},
    {"title": "Consonant Clusters & Medials",
     "body_html": r"""
<p>Burmese has limited consonant clusters; most are <strong>medials</strong> — modifications to a base consonant. The four medials are:</p>
<ul>
<li>◌ျ (yapin): adds /-y-/. ကျ kya "to fall"</li>
<li>◌ြ (yayit): adds /-r-/ in older words, often /-y-/ in modern. ကြ kya/kra</li>
<li>◌ွ (wahsway): adds /-w-/. ကွ kwa</li>
<li>◌ှ (hahto): adds aspiration or /h/. ကှ kha</li>
</ul>
<p>Medials stack onto the base consonant. They don't create independent syllables.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "The medial that adds /-w-/ is called ___ (Burmese name).", "answer": "wahsway"},
         {"type": "multiple-choice", "question": "ကျ means:", "options": ["come", "fall", "go", "bite"], "correctIndex": 1},
         {"type": "true-false", "question": "Medials create independent syllables.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Burmese has __ medial signs.", "answer": "four"},
         {"type": "true-false", "question": "Yapin adds a /y/ sound.", "correctAnswer": True}]},
    {"title": "Word-Level Stress",
     "body_html": r"""
<p>Word stress in Burmese is largely determined by tone and syllable structure rather than free placement (as in English). Heavy syllables (with a long vowel or final stop) attract emphasis.</p>
<p>In compound words, the second element is usually <strong>weakened</strong>: its tone may shift to a neutral schwa-like sound. This is called the "weak schwa" or "minor syllable."</p>
<p>For example, မိန်းကလေး mein-kaleh "girl" — the first syllable is fully stressed, the kaleh "child" suffix becomes a quick weakened ka-leh.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Heavy syllables attract emphasis in Burmese.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Weak vowels in compound words are sometimes called ___ syllables.", "answer": "minor"},
         {"type": "multiple-choice", "question": "မိန်းကလေး means:", "options": ["boy", "girl", "child", "woman"], "correctIndex": 1},
         {"type": "true-false", "question": "Stress in Burmese is fully free, like English.", "correctAnswer": False},
         {"type": "true-false", "question": "Weak schwa appears in compound words.", "correctAnswer": True}]},
    {"title": "Sandhi (Sound Changes)",
     "body_html": r"""
<p>Sandhi refers to sound changes when words combine. Common Burmese sandhi:</p>
<ul>
<li><strong>Voicing of initial stops:</strong> a voiceless consonant may become voiced after a sonorant. e.g., ka → ga in some compound contexts.</li>
<li><strong>Tone changes:</strong> the second element of a compound often loses tone or becomes creaky.</li>
<li><strong>Assimilation:</strong> nasals adapt to following consonants (n + p → m + p).</li>
</ul>
<p>You won't always be told these rules explicitly — you'll absorb them by listening to native speakers. Awareness of sandhi prevents you from sounding "robotic" when reading aloud.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Sandhi describes sound changes when words combine.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "A common sandhi pattern:", "options": ["voiceless → voiced after sonorant", "voiced → voiceless always", "no changes occur", "tones become uniform"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Nasals can ___ to following consonants.", "answer": "assimilate"},
         {"type": "true-false", "question": "Sandhi is fully explicit and predictable in writing.", "correctAnswer": False},
         {"type": "true-false", "question": "Sandhi awareness helps natural reading.", "correctAnswer": True}]},
    {"title": "Pronunciation Checkpoint",
     "body_html": r"""
<p>Recap of Unit 28:</p>
<ul>
<li>Three tones: low (steady), creaky (short, glottal), high (long, falling).</li>
<li>Aspirated vs unaspirated stops are contrastive.</li>
<li>Voiced vs voiceless consonants matter; intervocalic voicing happens.</li>
<li>Four nasals: ng, ny, n, m. Word-initial ng is allowed in Burmese.</li>
<li>Glottal stop endings (asat) are extremely common.</li>
<li>Vowel length matters; medials create modified consonants.</li>
<li>Compound words feature minor (weakened) syllables.</li>
<li>Sandhi smooths pronunciation in connected speech.</li>
</ul>""",
     "exercises": [
         {"type": "multiple-choice", "question": "How many tones does Burmese have?", "options": ["2", "3", "4", "6"], "correctIndex": 1},
         {"type": "true-false", "question": "Aspiration is contrastive in Burmese.", "correctAnswer": True},
         {"type": "fill-blank", "question": "The diacritic that creates a glottal-stop ending is called ___.", "answer": "asat"},
         {"type": "multiple-choice", "question": "လား is most often used as:", "options": ["a noun for road", "a question marker", "the verb to come", "a tone diacritic"], "correctIndex": 1},
         {"type": "true-false", "question": "Voicing can change between vowels in connected speech.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Long vowels typically pair with high or ___ tones.", "answer": "creaky"},
         {"type": "true-false", "question": "Medials create independent syllables.", "correctAnswer": False}]},
]

if __name__ == "__main__":
    render_unit(28, "Burmese Pronunciation Drills", 400, LESSONS)
