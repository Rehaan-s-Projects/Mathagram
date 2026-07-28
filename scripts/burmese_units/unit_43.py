#!/usr/bin/env python3
"""Burmese Unit 43 — Politics & Government (lessons 625-639)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Government Structure",
     "body_html": r"""<p>Myanmar's government has had multiple forms (parliamentary, military). Key structural words:</p><ul><li>အစိုးရ — government</li><li>လွှတ်တော် — parliament</li><li>သမ္မတ — president</li><li>ဝန်ကြီးချုပ် — prime minister</li><li>ပြည်ထောင်စု — Union (federation)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Parliament: ___ တော်.", "answer": "လွှတ်"},
         {"type": "multiple-choice", "question": "Union: ", "options": ["အစိုးရ", "ပြည်ထောင်စု", "သမ္မတ", "ဝန်ကြီး"], "correctIndex": 1},
         {"type": "true-false", "question": "ဝန်ကြီးချုပ် means \"prime minister.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Government: ___ ရ.", "answer": "အစိုး"},
         {"type": "true-false", "question": "Myanmar has only ever had one form of government.", "correctAnswer": False}]},
    {"title": "Branches of Government",
     "body_html": r"""<ul><li>အုပ်ချုပ်ရေး — executive</li><li>ဥပဒေပြု — legislative</li><li>တရားစီရင် — judicial</li><li>စိစစ် — to oversee</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Executive: ___ ချုပ်ရေး.", "answer": "အုပ်"},
         {"type": "multiple-choice", "question": "Judicial: ", "options": ["အုပ်ချုပ်ရေး", "ဥပဒေပြု", "တရားစီရင်", "စိစစ်"], "correctIndex": 2},
         {"type": "true-false", "question": "ဥပဒေပြု means \"legislative.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Oversee: ___ စစ်.", "answer": "စိ"},
         {"type": "true-false", "question": "Three branches: executive, legislative, judicial.", "correctAnswer": True}]},
    {"title": "Elections",
     "body_html": r"""<ul><li>ရွေးကောက်ပွဲ — election</li><li>ကိုယ်စားလှယ် — representative / candidate</li><li>မဲ — vote</li><li>မဲဆန္ဒပြုသူ — voter</li><li>အနိုင်ရ — to win</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Vote: ___.", "answer": "မဲ"},
         {"type": "multiple-choice", "question": "Voter: ", "options": ["ကိုယ်စားလှယ်", "မဲ", "မဲဆန္ဒပြုသူ", "ရွေးကောက်ပွဲ"], "correctIndex": 2},
         {"type": "true-false", "question": "ကိုယ်စားလှယ် means \"representative.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Win: အနိုင် ___.", "answer": "ရ"},
         {"type": "fill-blank", "question": "Election: ___ ပွဲ.", "answer": "ရွေးကောက်"}]},
    {"title": "Political Parties",
     "body_html": r"""<ul><li>NLD (National League for Democracy) — အမျိုးသား ဒီမိုကရေစီ အဖွဲ့ချုပ်</li><li>USDP (Union Solidarity & Development Party)</li><li>SAC (State Administration Council, post-2021 military)</li><li>Others: ethnic-based parties (Shan, Kachin, Mon, Karen).</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "NLD = National League for ___.", "answer": "Democracy"},
         {"type": "multiple-choice", "question": "Post-2021 military body:", "options": ["NLD", "SAC", "USDP", "EU"], "correctIndex": 1},
         {"type": "true-false", "question": "Many ethnic-based parties exist.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Aung San Suu Kyi led the ___.", "answer": "NLD"},
         {"type": "true-false", "question": "Myanmar has only one political party.", "correctAnswer": False}]},
    {"title": "Politics Phrases",
     "body_html": r"""<ul><li>"လူထု ထောက်ခံ" — public support</li><li>"ဆန္ဒပြ" — to protest</li><li>"ပိတ်ဆို့" — to blockade / boycott</li><li>"တရားမဝင်" — illegal</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Public: ___ ထု.", "answer": "လူ"},
         {"type": "multiple-choice", "question": "To protest: ", "options": ["ဆန္ဒပြ", "ပိတ်ဆို့", "တရားမဝင်", "လူထု"], "correctIndex": 0},
         {"type": "true-false", "question": "တရားမဝင် means \"illegal.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Boycott: ___ ဆို့.", "answer": "ပိတ်"},
         {"type": "true-false", "question": "လူထု ထောက်ခံ means \"public support.\"", "correctAnswer": True}]},
    {"title": "Military Vocabulary",
     "body_html": r"""<ul><li>တပ်မတော် — Tatmadaw (Myanmar military)</li><li>စစ်တပ် — military / army</li><li>စစ်သား — soldier</li><li>ဗိုလ် — officer</li><li>စစ်အာဏာ — military power / coup</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Soldier: ___ သား.", "answer": "စစ်"},
         {"type": "multiple-choice", "question": "Officer: ", "options": ["တပ်မတော်", "ဗိုလ်", "စစ်အာဏာ", "စစ်တပ်"], "correctIndex": 1},
         {"type": "true-false", "question": "တပ်မတော် is the Myanmar military.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Military power / coup: စစ်___.", "answer": "အာဏာ"},
         {"type": "fill-blank", "question": "Army: ___ တပ်.", "answer": "စစ်"}]},
    {"title": "Civil Society",
     "body_html": r"""<ul><li>လူ့အခွင့်အရေး — human rights</li><li>လူ့အဖွဲ့အစည်း — civil society</li><li>NGO — အစိုးရ မဟုတ်တဲ့ အဖွဲ့အစည်း</li><li>သတင်းမီဒီယာ — media</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Human rights: လူ့ ___ အရေး.", "answer": "အခွင့်"},
         {"type": "multiple-choice", "question": "Media: ", "options": ["NGO", "သတင်းမီဒီယာ", "လူ့အဖွဲ့အစည်း", "လူ့အခွင့်အရေး"], "correctIndex": 1},
         {"type": "true-false", "question": "လူ့အဖွဲ့အစည်း means \"civil society.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "NGO: အစိုးရ ___ တဲ့ အဖွဲ့.", "answer": "မဟုတ်"},
         {"type": "true-false", "question": "Civil society includes NGOs and media.", "correctAnswer": True}]},
    {"title": "Diplomacy",
     "body_html": r"""<ul><li>သံတမန် — diplomat</li><li>သံရုံး — embassy</li><li>သဘောတူညီချက် — treaty / agreement</li><li>ဆွေးနွေး — to discuss / negotiate</li><li>ဆက်ဆံရေး — relations</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Diplomat: ___ တမန်.", "answer": "သံ"},
         {"type": "multiple-choice", "question": "Embassy: ", "options": ["သံတမန်", "သံရုံး", "ဆွေးနွေး", "ဆက်ဆံရေး"], "correctIndex": 1},
         {"type": "true-false", "question": "ဆွေးနွေး means \"to discuss / negotiate.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Relations: ___ ဆံရေး.", "answer": "ဆက်"},
         {"type": "true-false", "question": "Treaties are agreements between states.", "correctAnswer": True}]},
    {"title": "Public Policy",
     "body_html": r"""<ul><li>မူဝါဒ — policy</li><li>စီမံကိန်း — plan / project</li><li>ပြုပြင်ပြောင်းလဲ — to reform</li><li>ရင်းနှီးမြှုပ်နှံ — to invest</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Policy: ___.", "answer": "မူဝါဒ"},
         {"type": "multiple-choice", "question": "Reform: ", "options": ["မူဝါဒ", "စီမံကိန်း", "ပြုပြင်ပြောင်းလဲ", "ရင်းနှီး"], "correctIndex": 2},
         {"type": "true-false", "question": "ရင်းနှီးမြှုပ်နှံ means \"to invest.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Project: စီ ___ ကိန်း.", "answer": "မံ"},
         {"type": "true-false", "question": "Public policy never changes.", "correctAnswer": False}]},
    {"title": "Sensitive Topics",
     "body_html": r"""<p>For learners: be cautious about discussing certain topics in public:</p><ul><li>2021 coup and aftermath</li><li>Rohingya crisis</li><li>Ethnic conflict</li><li>Aung San Suu Kyi's status</li></ul><p>Read these in news but be careful in conversation.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Some Burmese political topics are sensitive.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Best practice:", "options": ["push opinions on locals", "read news, listen, respect", "argue loudly", "ignore politics entirely"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Coup: ___ အာဏာ.", "answer": "စစ်"},
         {"type": "true-false", "question": "Discussing politics openly is uniformly safe.", "correctAnswer": False},
         {"type": "true-false", "question": "Listening respectfully is the best approach.", "correctAnswer": True}]},
    {"title": "Reading Political News",
     "body_html": r"""<p>Tips:</p><ul><li>Identify primary actors first.</li><li>Note source carefully — state vs independent press differ in tone.</li><li>Translate key terms before reading whole article.</li><li>Triangulate via multiple sources.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Triangulating across sources is recommended.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "First step:", "options": ["read whole article", "identify primary actors", "translate every word", "skip headlines"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Source: ___ မြစ်.", "answer": "အရင်းအ"},
         {"type": "true-false", "question": "State vs independent media often have different tones.", "correctAnswer": True},
         {"type": "true-false", "question": "Skipping context is fine.", "correctAnswer": False}]},
    {"title": "Local Government",
     "body_html": r"""<ul><li>မြို့နယ်အုပ်ချုပ်ရေး — township administration</li><li>ရပ်ကွက်ဥက္ကဋ္ဌ — ward chair</li><li>ရွာသူကြီး — village headman</li><li>လမ်းမှာ ပြသနာ — \"problem on the road\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Village headman: ရွာ ___ ကြီး.", "answer": "သူ"},
         {"type": "multiple-choice", "question": "Ward chair: ", "options": ["မြို့နယ်", "ရပ်ကွက်ဥက္ကဋ္ဌ", "ရွာသူကြီး", "စစ်တပ်"], "correctIndex": 1},
         {"type": "true-false", "question": "Local government has multiple levels.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Township administration: မြို့နယ် ___ ချုပ်ရေး.", "answer": "အုပ်"},
         {"type": "true-false", "question": "Village headmen exist in Myanmar.", "correctAnswer": True}]},
    {"title": "Constitutional Vocabulary",
     "body_html": r"""<ul><li>ဖွဲ့စည်းပုံ အခြေခံ — constitution</li><li>အခွင့်အရေး — rights</li><li>တာဝန် — duty / responsibility</li><li>ပြင်ဆင်ချက် — amendment</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Constitution: ဖွဲ့စည်းပုံ ___ ခြေခံ.", "answer": "အ"},
         {"type": "multiple-choice", "question": "Amendment: ", "options": ["အခွင့်အရေး", "တာဝန်", "ပြင်ဆင်ချက်", "ဖွဲ့စည်းပုံ"], "correctIndex": 2},
         {"type": "true-false", "question": "တာဝန် means \"duty.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Rights: အခွင့် ___.", "answer": "အရေး"},
         {"type": "true-false", "question": "Constitutions are amendable.", "correctAnswer": True}]},
    {"title": "Practice: Decode a Headline",
     "body_html": r"""<p>Sample: \"လွှတ်တော်တွင် ဥပဒေသစ် မဲခွဲဆုံးဖြတ်ခဲ့သည်။\"</p><p>"Parliament voted on a new law."</p><p>လွှတ်တော် (parliament) | တွင် (in/at) | ဥပဒေသစ် (new law) | မဲခွဲ (vote) | ဆုံးဖြတ် (decide) | ခဲ့သည် (past tense formal).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "New law: ဥပဒေ ___.", "answer": "သစ်"},
         {"type": "multiple-choice", "question": "Vote (verb): ", "options": ["မဲခွဲ", "ပြန်ပေး", "လုပ်ပြီး", "ပြင်ဆင်"], "correctIndex": 0},
         {"type": "true-false", "question": "ဆုံးဖြတ်ခဲ့သည် is past tense formal.", "correctAnswer": True},
         {"type": "fill-blank", "question": "In/at: ___.", "answer": "တွင်"},
         {"type": "true-false", "question": "ဥပဒေ means \"law.\"", "correctAnswer": True}]},
    {"title": "Politics Checkpoint",
     "body_html": r"""<p>Recap of Unit 43:</p><ul><li>Government: အစိုးရ; Parliament: လွှတ်တော်; President: သမ္မတ.</li><li>Three branches: executive, legislative, judicial.</li><li>Elections: ရွေးကောက်ပွဲ; vote: မဲ.</li><li>Military: တပ်မတော် (Tatmadaw); coup: စစ်အာဏာ.</li><li>Civil society: NGOs, media, human rights.</li><li>Sensitive topics — use restraint in conversation.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Election: ___ ပွဲ.", "answer": "ရွေးကောက်"},
         {"type": "multiple-choice", "question": "Tatmadaw is:", "options": ["a religion", "the Myanmar military", "an opposition party", "a journalist's union"], "correctIndex": 1},
         {"type": "true-false", "question": "လွှတ်တော် means \"parliament.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Vote: ___.", "answer": "မဲ"},
         {"type": "fill-blank", "question": "Constitution: ___ စည်းပုံ အခြေခံ.", "answer": "ဖွဲ့"},
         {"type": "true-false", "question": "Politics is universally safe to discuss in Myanmar.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Reform: ___ ပြောင်းလဲ.", "answer": "ပြုပြင်"}]},
]

if __name__ == "__main__":
    render_unit(43, "Burmese Politics & Government", 625, LESSONS)
