#!/usr/bin/env python3
"""Burmese Unit 53 — Comedy & Humor (lessons 775-789)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Burmese Sense of Humor",
     "body_html": r"""<p>Burmese humor relies on wordplay, social commentary, exaggeration, and slapstick. Often gentle, occasionally satirical. Political humor is risky publicly but flourishes in private.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Humor: ___.", "answer": "ဟာသ"},
         {"type": "multiple-choice", "question": "Burmese humor includes:", "options": ["aggressive insults only", "wordplay, social commentary, slapstick", "hostile mockery", "no humor"], "correctIndex": 1},
         {"type": "true-false", "question": "Political humor is risky publicly.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Joke: ___.", "answer": "ရယ်စရာ"},
         {"type": "true-false", "question": "Burmese culture lacks any humor tradition.", "correctAnswer": False}]},
    {"title": "Wordplay (Pun)",
     "body_html": r"""<p>Burmese has rich wordplay opportunities thanks to tone differences (ka/kha/ká/ka̰), homophones, and compound words. Skilled comedians twist meanings via tone shifts.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Tone differences enable wordplay in Burmese.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Pun: ", "options": ["စကားလုံးကစား", "ဟာသ", "ရယ်စရာ", "မိုက်"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Word: ___ လုံး.", "answer": "စကား"},
         {"type": "true-false", "question": "Homophones never appear in Burmese.", "correctAnswer": False},
         {"type": "true-false", "question": "Comedians use tone shifts for laughs.", "correctAnswer": True}]},
    {"title": "Slapstick & Visual Comedy",
     "body_html": r"""<p>Physical comedy is universally loved. Burmese vaudeville-style stage shows feature pratfalls, exaggerated gestures, costume gags. Stage comedians are highly trained.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Physical comedy is universally enjoyed.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Vaudeville features:", "options": ["pratfalls and gags", "no movement", "only words", "music only"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Stage: ___.", "answer": "စင်"},
         {"type": "true-false", "question": "Stage comedians are highly trained.", "correctAnswer": True},
         {"type": "true-false", "question": "Slapstick humor doesn't exist in Myanmar.", "correctAnswer": False}]},
    {"title": "Famous Comedians",
     "body_html": r"""<ul><li>Zaganar — political satirist (jailed for jokes about the regime)</li><li>Pa Pa Win Khin — popular comedy actress</li><li>Live comedy at Mandalay's Moustache Brothers troupe (also famously persecuted)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Famous satirist: ___.", "answer": "Zaganar"},
         {"type": "multiple-choice", "question": "Mandalay's troupe:", "options": ["Moustache Brothers", "Beard Brothers", "Long Hair Brothers", "Comedy Sisters"], "correctIndex": 0},
         {"type": "true-false", "question": "Some comedians have been jailed for jokes.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Comedian: ___ ကောင်.", "answer": "ဟာသ"},
         {"type": "true-false", "question": "Comedy in Myanmar is risk-free.", "correctAnswer": False}]},
    {"title": "Comedy in Films & TV",
     "body_html": r"""<p>Burmese comedy films feature ensemble casts; common formula: misunderstanding → escalating chaos → resolution at family dinner. TV sketch shows are also popular.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Comedy films often feature ensemble casts.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Common ending:", "options": ["family dinner", "battle scene", "alien arrival", "musical number"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Misunderstanding: ___.", "answer": "နားလည်မှု လွဲ"},
         {"type": "true-false", "question": "TV sketch shows are popular.", "correctAnswer": True},
         {"type": "true-false", "question": "Burmese comedy films don't exist.", "correctAnswer": False}]},
    {"title": "Burmese Jokes",
     "body_html": r"""<p>Common joke pattern: \"တစ်ယောက်က ___ ပြောလို့...\" — \"One person said ___ because...\". Punchlines often play on social class, region, or marriage stereotypes.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "One person: တစ် ___.", "answer": "ယောက်"},
         {"type": "multiple-choice", "question": "Punchline themes:", "options": ["politics only", "social class, region, marriage", "math only", "nothing"], "correctIndex": 1},
         {"type": "true-false", "question": "Joke pattern: \"X said because...\".", "correctAnswer": True},
         {"type": "fill-blank", "question": "Said: ___ တယ်.", "answer": "ပြော"},
         {"type": "true-false", "question": "Burmese jokes never use stereotypes.", "correctAnswer": False}]},
    {"title": "Children's Humor",
     "body_html": r"""<p>Children love silly rhymes, animal jokes, and exaggerated facial expressions. \"ဖား ဖား\" (frog frog) jokes are classic.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Children love silly rhymes.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Classic kid joke: ", "options": ["frog frog", "tax tax", "war war", "phone phone"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Frog: ___.", "answer": "ဖား"},
         {"type": "true-false", "question": "Animal jokes are popular with kids.", "correctAnswer": True},
         {"type": "true-false", "question": "Children rarely laugh at exaggerated expressions.", "correctAnswer": False}]},
    {"title": "Sarcasm in Burmese",
     "body_html": r"""<p>Sarcasm exists but is often softer than English. Tone of voice and context carry it. Direct sarcastic insult is uncommon — more often gentle teasing.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese sarcasm is often softer than English.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Carries sarcasm in Burmese:", "options": ["volume only", "tone of voice + context", "facial only", "no carriers"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Tease: ___ ပြောင်.", "answer": "နောက်"},
         {"type": "true-false", "question": "Direct sarcastic insults are common in Burmese.", "correctAnswer": False},
         {"type": "true-false", "question": "Tone matters for sarcasm.", "correctAnswer": True}]},
    {"title": "Memes & Internet Humor",
     "body_html": r"""<p>Facebook is the Burmese internet — and meme culture flourishes there. Common meme topics: traffic, water festival mishaps, mother-in-law sketches.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Facebook is the dominant social platform in Myanmar.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Common meme topics: ", "options": ["traffic, water festival, mother-in-law", "math homework", "weather only", "no themes"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Internet: ___.", "answer": "အင်တာနက်"},
         {"type": "true-false", "question": "Meme culture flourishes online.", "correctAnswer": True},
         {"type": "true-false", "question": "Memes are unknown in Myanmar.", "correctAnswer": False}]},
    {"title": "Humor in Storytelling",
     "body_html": r"""<p>Burmese storytellers weave jokes into narratives. Even Buddhist parables sometimes have humorous twists about foolish characters.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Storytellers weave jokes into narratives.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Even Buddhist parables can be:", "options": ["humorous", "boring", "violent", "secret"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Story: ___ ကြောင်း.", "answer": "ဇာတ်"},
         {"type": "true-false", "question": "Foolish characters are common.", "correctAnswer": True},
         {"type": "true-false", "question": "Burmese stories must always be serious.", "correctAnswer": False}]},
    {"title": "Cultural Sensitivities",
     "body_html": r"""<p>Avoid: jokes about Buddha, monks, ethnic groups, or current military. Even private joking can be reported. Stick to safe topics: traffic, weather, family quirks.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Avoid joking about Buddha and monks.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Safe topics: ", "options": ["military politics", "traffic, weather, family", "ethnic stereotypes", "religion"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Be careful: ___ ပါ.", "answer": "သတိ"},
         {"type": "true-false", "question": "Private jokes can have public consequences.", "correctAnswer": True},
         {"type": "true-false", "question": "Anything goes in Burmese humor.", "correctAnswer": False}]},
    {"title": "Funny Phrases",
     "body_html": r"""<ul><li>"ရယ်ရတာပဲ။" — \"It's just funny.\"</li><li>"အရမ်း ရယ်တယ်!" — \"Really hilarious!\"</li><li>"အ မိုက်နေပြီ!" — \"You're being silly!\" (gentle tease)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Funny: ___ စရာ.", "answer": "ရယ်"},
         {"type": "multiple-choice", "question": "Hilarious: ", "options": ["အရမ်း ရယ်တယ်", "အ မိုက်နေပြီ", "ရယ်ရတာပဲ", "ပျော်"], "correctIndex": 0},
         {"type": "true-false", "question": "မိုက် can mean \"silly.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Really: ___.", "answer": "အရမ်း"},
         {"type": "true-false", "question": "\"အ မိုက်နေပြီ!\" is often a gentle tease.", "correctAnswer": True}]},
    {"title": "Comedy at Festivals",
     "body_html": r"""<p>During Thingyan (water festival), comedy troupes perform satirical (\"thanga-yat\") routines on stages around towns. They roast public figures, traditions, and current events.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Water festival: ___.", "answer": "Thingyan"},
         {"type": "multiple-choice", "question": "Festival comedy: ", "options": ["banned", "satirical \"thanga-yat\"", "purely religious", "non-existent"], "correctIndex": 1},
         {"type": "true-false", "question": "Comedy troupes roast public figures during Thingyan.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Festival: ___ ပွဲ.", "answer": "ပွဲတော် (or)"},
         {"type": "true-false", "question": "Thingyan has comedy elements.", "correctAnswer": True}]},
    {"title": "Practice: A Burmese Joke",
     "body_html": r"""<p>Sample (mild) joke:</p><p><em>"တစ်ယောက်က ဆရာဝန် ဆီ သွားတယ်။ \"ဆရာ၊ ကျွန်တော် ပျော် နေတယ်။\" ဆရာက ပြောတယ် — \"ဒီ နေရာက ဆေးခန်း ပါ။ ပျော်တာ မဟုတ်ဘူး၊ ဖျား နေတာ။\""</em></p><p>"A guy went to the doctor: 'Doctor, I'm happy.' Doctor: 'This is a clinic. You're not happy, you're feverish.'\" (Tone-pun: ပျော် ≈ ဖျား in some dialects.)</p>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese jokes can use tone puns.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "ပျော် means: ", "options": ["fever", "happy", "sick", "tired"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Doctor: ___ ဝန်.", "answer": "ဆရာ"},
         {"type": "fill-blank", "question": "Clinic: ___ ခန်း.", "answer": "ဆေး"},
         {"type": "true-false", "question": "ဖျား = fever; ပျော် = happy. Different words.", "correctAnswer": True}]},
    {"title": "Comedy Checkpoint",
     "body_html": r"""<p>Recap of Unit 53:</p><ul><li>Burmese humor: wordplay, slapstick, social commentary.</li><li>Famous: Zaganar, Pa Pa Win Khin, Moustache Brothers.</li><li>Sensitive topics: religion, ethnicity, military.</li><li>Internet humor flourishes on Facebook; common meme themes.</li><li>Festival comedy (thanga-yat) at Thingyan.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Humor: ___.", "answer": "ဟာသ"},
         {"type": "multiple-choice", "question": "Avoid joking about: ", "options": ["traffic", "weather", "religion / military", "family"], "correctIndex": 2},
         {"type": "true-false", "question": "Wordplay relies on tones in Burmese.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Funny: ___ စရာ.", "answer": "ရယ်"},
         {"type": "fill-blank", "question": "Comedian (famous): ___.", "answer": "Zaganar"},
         {"type": "true-false", "question": "Facebook hosts most Burmese internet humor.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Festival: ___.", "answer": "Thingyan"}]},
]

if __name__ == "__main__":
    render_unit(53, "Burmese Comedy & Humor", 775, LESSONS)
