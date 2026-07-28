#!/usr/bin/env python3
"""Burmese Unit 51 — TV Shows (lessons 745-759)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Burmese TV Channels",
     "body_html": r"""<ul><li>MRTV (state)</li><li>Channel 7 (entertainment)</li><li>MWD (military-affiliated)</li><li>DVB (exile-based, news)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "State channel: ___.", "answer": "MRTV"},
         {"type": "multiple-choice", "question": "Exile news channel: ", "options": ["MRTV", "Channel 7", "MWD", "DVB"], "correctIndex": 3},
         {"type": "true-false", "question": "Channel 7 is entertainment-focused.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Military-affiliated: ___.", "answer": "MWD"},
         {"type": "true-false", "question": "Myanmar has multiple TV channels.", "correctAnswer": True}]},
    {"title": "TV Show Genres",
     "body_html": r"""<ul><li>ဇာတ်လမ်းတွဲ — drama series</li><li>သတင်း — news</li><li>တေးမြူးသီချင်း — music show</li><li>ဟာသ — comedy</li><li>စစ်ဇာတ် — military / action</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "News: ___.", "answer": "သတင်း"},
         {"type": "multiple-choice", "question": "Drama series: ", "options": ["သတင်း", "ဇာတ်လမ်းတွဲ", "တေးမြူး", "စစ်ဇာတ်"], "correctIndex": 1},
         {"type": "true-false", "question": "ဟာသ means \"comedy.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Music show: ___ မြူးသီချင်း.", "answer": "တေး"},
         {"type": "fill-blank", "question": "Action: ___ ဇာတ်.", "answer": "စစ်"}]},
    {"title": "Soap Operas",
     "body_html": r"""<p>Burmese soaps (\"melodramas\") follow long-running family / romantic plots, often with sudden plot twists. Common tropes: secret family ties, love triangles, evil mother-in-law.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese soaps run long episodes.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Common trope:", "options": ["space adventures", "love triangle / family secrets", "sci-fi epics", "no romance"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Family: ___ စု.", "answer": "မိသား"},
         {"type": "true-false", "question": "Soaps are heavily plot-driven.", "correctAnswer": True},
         {"type": "true-false", "question": "Burmese soaps lack romance.", "correctAnswer": False}]},
    {"title": "Game Shows",
     "body_html": r"""<ul><li>ပြိုင်ပွဲ — competition</li><li>ဆုရရှိ — to win a prize</li><li>"ထဲက ကိုယ်စားလှယ် ___" — \"Contestant from ___\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Win prize: ___ ရရှိ.", "answer": "ဆု"},
         {"type": "multiple-choice", "question": "Competition: ", "options": ["ပြိုင်ပွဲ", "ဆု", "ကိုယ်စားလှယ်", "ဇာတ်လမ်း"], "correctIndex": 0},
         {"type": "true-false", "question": "Burmese has game shows.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Contestant: ___ စားလှယ်.", "answer": "ကိုယ်"},
         {"type": "true-false", "question": "Burmese game shows lack prizes.", "correctAnswer": False}]},
    {"title": "Reality TV",
     "body_html": r"""<ul><li>ရီယယ်လီတီ — reality TV</li><li>စင်မြင့် — stage</li><li>တာဝန်ပေး — challenge / task</li></ul><p>Reality singing/dance shows have grown in popularity, including talent contests modeled on international franchises.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Stage: ___ မြင့်.", "answer": "စင်"},
         {"type": "multiple-choice", "question": "Challenge: ", "options": ["ရီယယ်လီတီ", "တာဝန်ပေး", "စင်မြင့်", "ဆု"], "correctIndex": 1},
         {"type": "true-false", "question": "Reality singing shows are popular.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Reality TV: ___ လီတီ.", "answer": "ရီယယ်"},
         {"type": "true-false", "question": "International franchises have inspired local versions.", "correctAnswer": True}]},
    {"title": "TV News",
     "body_html": r"""<ul><li>သတင်းတင်ဆက်သူ — news anchor</li><li>"ဒီနေ့ ထူးထူးခြားခြား သတင်းများ:" — \"Today's headline news:\"</li><li>"စတိုဒီယိုတွင် ___ နှင့် ဆက်လိုက်ပါ။" — \"In the studio with ___, stay tuned.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Anchor: ___ တင်ဆက်သူ.", "answer": "သတင်း"},
         {"type": "multiple-choice", "question": "Studio: ", "options": ["စတိုဒီယို", "သတင်း", "တင်ဆက်", "ထူးခြား"], "correctIndex": 0},
         {"type": "true-false", "question": "Anchors present TV news.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Today: ___.", "answer": "ဒီနေ့"},
         {"type": "true-false", "question": "TV news has scheduled broadcasts.", "correctAnswer": True}]},
    {"title": "Korean Drama Influence",
     "body_html": r"""<p>K-dramas (Korean dramas) are massively popular in Myanmar. Many are dubbed or subtitled in Burmese. Burmese productions imitate certain K-drama tropes (slow-burn romance, fashion).</p>""",
     "exercises": [
         {"type": "true-false", "question": "K-dramas are popular in Myanmar.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "K-drama features: ", "options": ["slow-burn romance, fashion", "alien invasions", "westerns", "musicals only"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Korean: ___.", "answer": "ကိုရီးယား"},
         {"type": "true-false", "question": "Burmese productions imitate K-drama tropes.", "correctAnswer": True},
         {"type": "true-false", "question": "K-dramas are absent from Myanmar.", "correctAnswer": False}]},
    {"title": "Streaming Services",
     "body_html": r"""<ul><li>Netflix, YouTube, Viu — popular in Myanmar.</li><li>"အွန်လိုင်း ကြည့်တယ်။" — \"I watch online.\"</li><li>"အပ်တ်ပ်ဒိတ်" — update / new episode</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Online: ___ လိုင်း.", "answer": "အွန်"},
         {"type": "multiple-choice", "question": "Update: ", "options": ["အွန်လိုင်း", "အပ်တ်ပ်ဒိတ်", "ကြည့်", "Netflix"], "correctIndex": 1},
         {"type": "true-false", "question": "Streaming services are increasingly used.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Watch: ___ တယ်.", "answer": "ကြည့်"},
         {"type": "true-false", "question": "All streaming requires cable.", "correctAnswer": False}]},
    {"title": "TV Schedules",
     "body_html": r"""<ul><li>"ဘယ်အချိန် ထုတ်လွှင့်လဲ။" — \"What time does it air?\"</li><li>ထုတ်လွှင့် — to broadcast</li><li>ပရိုဂရမ် — program (loanword)</li><li>အပိုင်း — episode</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Broadcast: ___ လွှင့်.", "answer": "ထုတ်"},
         {"type": "multiple-choice", "question": "Episode: ", "options": ["ပရိုဂရမ်", "အပိုင်း", "သတင်း", "ဇာတ်လမ်း"], "correctIndex": 1},
         {"type": "true-false", "question": "ပရိုဂရမ် is borrowed from English.", "correctAnswer": True},
         {"type": "fill-blank", "question": "What time: ဘယ်___ .", "answer": "အချိန်"},
         {"type": "true-false", "question": "Burmese TV uses English program loanword.", "correctAnswer": True}]},
    {"title": "TV Commercials",
     "body_html": r"""<ul><li>ကြော်ငြာ — advertisement</li><li>"ကြော်ငြာ ပျက်" — ad break</li><li>"ဈေးနှုန်း ကြေငြာ" — price announcement</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Advertisement: ___.", "answer": "ကြော်ငြာ"},
         {"type": "multiple-choice", "question": "Ad break: ", "options": ["ကြော်ငြာ ပျက်", "ဈေးနှုန်း", "ကြေငြာ", "ကြော်ငြာ"], "correctIndex": 0},
         {"type": "true-false", "question": "TV ads are common in Myanmar.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Announcement: ___ ငြာ.", "answer": "ကြေ"},
         {"type": "true-false", "question": "Burmese TV has no commercials.", "correctAnswer": False}]},
    {"title": "Sports Broadcasting",
     "body_html": r"""<ul><li>"ဘောလုံးပွဲ ထုတ်လွှင့်" — football broadcast</li><li>"အသံပြောတူ" — commentator</li><li>"ထူးထူးခြားခြား ပွဲ" — special match</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Football match: ဘောလုံး ___.", "answer": "ပွဲ"},
         {"type": "multiple-choice", "question": "Commentator: ", "options": ["ဘောလုံး", "အသံပြောတူ", "ထုတ်လွှင့်", "ပွဲ"], "correctIndex": 1},
         {"type": "true-false", "question": "Sports broadcasting is popular.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Special: ___ ထူးခြား.", "answer": "ထူး"},
         {"type": "true-false", "question": "Football is a popular sport in Myanmar.", "correctAnswer": True}]},
    {"title": "Talk Shows",
     "body_html": r"""<ul><li>"ပြောဆိုရွေး" — talk show</li><li>"ဧည့်သည်" — guest</li><li>"တင်ဆက်သူ" — host</li><li>"စိတ်ဝင်စားဖို့ မေးခွန်း" — interesting question</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Talk show: ___ ဆိုရွေး.", "answer": "ပြော"},
         {"type": "multiple-choice", "question": "Host: ", "options": ["ဧည့်သည်", "တင်ဆက်သူ", "စိတ်ဝင်စား", "မေးခွန်း"], "correctIndex": 1},
         {"type": "true-false", "question": "Talk shows have hosts and guests.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Guest: ___ သည်.", "answer": "ဧည့်"},
         {"type": "true-false", "question": "Burmese has its own talk shows.", "correctAnswer": True}]},
    {"title": "Children's TV",
     "body_html": r"""<ul><li>ကာတွန်း — cartoon</li><li>ပညာပေး ပရိုဂရမ် — educational program</li><li>"ကလေးငယ် တွေ ကြိုက်တယ်။" — \"Kids love it.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Cartoon: ___.", "answer": "ကာတွန်း"},
         {"type": "multiple-choice", "question": "Educational: ", "options": ["ကာတွန်း", "ပညာပေး", "ဇာတ်လမ်း", "သတင်း"], "correctIndex": 1},
         {"type": "true-false", "question": "Children's TV exists in Myanmar.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Kids love: ကလေးငယ် တွေ ___ တယ်.", "answer": "ကြိုက်"},
         {"type": "true-false", "question": "Children prefer adult news.", "correctAnswer": False}]},
    {"title": "Practice: Talking About TV",
     "body_html": r"""<p>Sample dialogue:</p><p><strong>A:</strong> "ဒီအခါ ဘယ် ဇာတ်လမ်းတွဲ ကြည့်နေလဲ။"</p><p><strong>B:</strong> "ငါ ___ ကို ကြည့်နေတယ်။ မင်းရော။"</p><p><strong>A:</strong> "ငါ K-drama ပိုကြိုက်တယ်။"</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Drama series: ___ လမ်းတွဲ.", "answer": "ဇာတ်"},
         {"type": "multiple-choice", "question": "Now / these days: ", "options": ["ဒီအခါ", "မနေ့က", "မနက်ဖြန်", "နောက်လ"], "correctIndex": 0},
         {"type": "true-false", "question": "ပိုကြိုက် means \"prefer / like more.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Watching: ___ နေတယ်.", "answer": "ကြည့်"},
         {"type": "true-false", "question": "Burmese friends discuss TV preferences.", "correctAnswer": True}]},
    {"title": "TV Shows Checkpoint",
     "body_html": r"""<p>Recap of Unit 51:</p><ul><li>Channels: MRTV, Channel 7, MWD, DVB.</li><li>Genres: ဇာတ်လမ်းတွဲ, သတင်း, ဟာသ, ကာတွန်း.</li><li>K-drama is hugely popular and influences local productions.</li><li>Streaming: Netflix, YouTube, Viu.</li><li>Talk show: တင်ဆက်သူ (host), ဧည့်သည် (guest).</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "News: ___.", "answer": "သတင်း"},
         {"type": "multiple-choice", "question": "K-drama: ", "options": ["Korean", "Chinese", "Japanese", "Indian"], "correctIndex": 0},
         {"type": "true-false", "question": "ကာတွန်း means \"cartoon.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Drama series: ___ လမ်းတွဲ.", "answer": "ဇာတ်"},
         {"type": "fill-blank", "question": "Episode: ___.", "answer": "အပိုင်း"},
         {"type": "true-false", "question": "Streaming services are popular.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Game show prize: ___.", "answer": "ဆု"}]},
]

if __name__ == "__main__":
    render_unit(51, "Burmese TV Shows", 745, LESSONS)
