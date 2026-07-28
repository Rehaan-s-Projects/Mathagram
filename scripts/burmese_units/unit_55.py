#!/usr/bin/env python3
"""Burmese Unit 55 — Grand Mastery (lessons 805-810). Final unit, 6 lessons."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Script Mastery",
     "body_html": r"""<p>You should now read confidently:</p><ul><li>All 33 base consonants and tone marks.</li><li>Medials (ya-pin, ya-yit, wa-hsway, ha-hto).</li><li>Burmese numerals ၀-၉.</li><li>Punctuation: ၊ phrase break, ။ sentence end.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Burmese has ___ base consonants.", "answer": "33"},
         {"type": "multiple-choice", "question": "Sentence end punctuation: ", "options": ["၊", "။", ".", "!"], "correctIndex": 1},
         {"type": "true-false", "question": "Medials modify base consonants.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Numerals run ၀ to ___.", "answer": "၉"},
         {"type": "fill-blank", "question": "Phrase break: ___.", "answer": "၊"}]},
    {"title": "Vocabulary Mastery",
     "body_html": r"""<p>Core categories you've covered:</p><ul><li>Greetings, family, food, travel, weather, body, emotions.</li><li>Politics, law, finance, medicine, education.</li><li>Cultural domains: Buddhism, calligraphy, dialects, festivals.</li><li>Media domains: news, films, TV, songs.</li></ul><p>Aim: 5,000 high-frequency words for daily fluency.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Family: ___ စု.", "answer": "မိသား"},
         {"type": "multiple-choice", "question": "Daily fluency goal: ", "options": ["100 words", "5,000 words", "50,000 words", "no goal"], "correctIndex": 1},
         {"type": "true-false", "question": "You've covered media domains.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Food: ___ ဟင်း.", "answer": "ထမင်း"},
         {"type": "true-false", "question": "Vocabulary breadth aids fluency.", "correctAnswer": True}]},
    {"title": "Grammar Mastery",
     "body_html": r"""<ul><li>Burmese is SOV (Subject-Object-Verb).</li><li>Particles: ga (subject), ko (object), ka (topic), bu (negation), la (question).</li><li>Tenses: ne (present), khe (past), me (future).</li><li>Politeness: pa added for formality.</li><li>Honorifics: U / Daw / Ko / Ma / Maung.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Word order: S-O-___ .", "answer": "V"},
         {"type": "multiple-choice", "question": "Question particle: ", "options": ["ga", "ko", "la", "bu"], "correctIndex": 2},
         {"type": "true-false", "question": "ပါ adds politeness.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Past tense: ___.", "answer": "khe"},
         {"type": "fill-blank", "question": "Future: ___.", "answer": "me"}]},
    {"title": "Cultural Mastery",
     "body_html": r"""<p>You should now navigate:</p><ul><li>Temple etiquette (shoes off, modest dress, walk clockwise).</li><li>Bargaining at markets.</li><li>Honorifics with elders.</li><li>Buddhism: 4 Noble Truths, 5 Precepts, Sangha, festivals.</li><li>Sensitive political topics — listen more than speak.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Walk around stupas: ___.", "answer": "clockwise"},
         {"type": "multiple-choice", "question": "Number of Burmese precepts (lay): ", "options": ["3", "5", "8", "227"], "correctIndex": 1},
         {"type": "true-false", "question": "Bargaining is normal at markets.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Honorific older man: ___.", "answer": "ဦး"},
         {"type": "true-false", "question": "Politics: listen more than speak.", "correctAnswer": True}]},
    {"title": "Conversation Mastery",
     "body_html": r"""<p>You can hold conversations on:</p><ul><li>Greetings, daily routines, family, food.</li><li>Travel, shopping, work.</li><li>Cultural opinions, festivals, religion.</li><li>News and current events (with care for sensitive topics).</li></ul><p>Practice with native speakers via online communities, language exchanges, or trips to Myanmar (when safe).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Conversation requires practice with native speakers.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Greeting: ", "options": ["မင်္ဂလာပါ", "ဆာတယ်", "ပျော်တယ်", "နာတယ်"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Family question: မိသားစု ___ ဦးလား.", "answer": "ရှိ"},
         {"type": "true-false", "question": "Online communities help practice.", "correctAnswer": True},
         {"type": "true-false", "question": "Avoid native-speaker contact to learn.", "correctAnswer": False}]},
    {"title": "Burmese Grand Mastery",
     "body_html": r"""<p>You've reached the end. From the script to street food, from politics to pop songs — you have a comprehensive foundation in Burmese.</p><p>What you've gained:</p><ul><li>~5,000+ word working vocabulary.</li><li>Reading and writing in the Burmese script.</li><li>Pronunciation including the 3-tone system.</li><li>Cultural fluency: Buddhism, etiquette, regional dialects, festivals.</li><li>Practical fluency: shopping, work, doctor visits, formal letters, conversation.</li></ul><p>ကောင်းကောင်း လေ့လာဖြစ်ခဲ့ပါတယ်။ ဆက်လုပ်ပါ — keep going. Visit Myanmar (safely), watch Burmese films, listen to Burmese music. Every day's exposure is more fluency.</p><p>သာဓု သာဓု သာဓု။</p>""",
     "exercises": [
         {"type": "true-false", "question": "Tone system has 3 tones.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Continued exposure leads to: ", "options": ["fluency", "decay", "no change", "translation"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Keep going: ___ လုပ်ပါ.", "answer": "ဆက်"},
         {"type": "true-false", "question": "သာဓု is shouted three times in Buddhist contexts.", "correctAnswer": True},
         {"type": "true-false", "question": "Daily exposure builds fluency.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Burmese script: ___ စာ.", "answer": "မြန်မာ"},
         {"type": "fill-blank", "question": "Hello: ___ ပါ.", "answer": "မင်္ဂလာ"},
         {"type": "true-false", "question": "Cultural fluency is part of language fluency.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(55, "Burmese Grand Mastery", 805, LESSONS)
