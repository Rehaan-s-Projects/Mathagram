#!/usr/bin/env python3
"""Burmese Unit 42 — News Vocabulary (lessons 610-624)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "News Reporting Verbs",
     "body_html": r"""<ul><li>ပြော — pyaw — to say</li><li>ကြေညာ — kyei-nya — to announce</li><li>တိုင်ကြား — taing-kya — to report</li><li>သတင်းပို့ — tha-din-pou — to file a story</li><li>ဖော်ထုတ် — phaw-htouk — to expose</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Announce: ___ ညာ.", "answer": "ကြေ"},
         {"type": "multiple-choice", "question": "Expose: ", "options": ["ပြော", "ကြေညာ", "ဖော်ထုတ်", "တိုင်ကြား"], "correctIndex": 2},
         {"type": "true-false", "question": "သတင်းပို့ means \"file a story.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Say: ___.", "answer": "ပြော"},
         {"type": "fill-blank", "question": "Report: ___ ကြား.", "answer": "တိုင်"}]},
    {"title": "Time Expressions in News",
     "body_html": r"""<ul><li>မနေ့က — yesterday</li><li>ဒီနေ့ — today</li><li>မနက်ဖြန် — tomorrow</li><li>လအတွင်း — within a month</li><li>မကြာသေးခင်က — recently</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Yesterday: ___ က.", "answer": "မနေ့"},
         {"type": "multiple-choice", "question": "Tomorrow: ", "options": ["မနေ့က", "ဒီနေ့", "မနက်ဖြန်", "လအတွင်း"], "correctIndex": 2},
         {"type": "true-false", "question": "မကြာသေးခင်က means \"recently.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Today: ___.", "answer": "ဒီနေ့"},
         {"type": "fill-blank", "question": "Within a month: လ___.", "answer": "အတွင်း"}]},
    {"title": "Quantity & Statistics",
     "body_html": r"""<ul><li>အရေအတွက် — quantity</li><li>ပျမ်းမျှ — average</li><li>ရာခိုင်နှုန်း — percent</li><li>တိုးလာ — to increase</li><li>လျော့ကျ — to decrease</li><li>ထောင်းချ — to plummet</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Percent: ရာ ___ နှုန်း.", "answer": "ခိုင်"},
         {"type": "multiple-choice", "question": "Decrease: ", "options": ["တိုးလာ", "လျော့ကျ", "ထောင်းချ", "ပျမ်းမျှ"], "correctIndex": 1},
         {"type": "true-false", "question": "ပျမ်းမျှ means \"average.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Plummet: ___ ချ.", "answer": "ထောင်း"},
         {"type": "fill-blank", "question": "Increase: ___ လာ.", "answer": "တိုး"}]},
    {"title": "Reporting Numbers",
     "body_html": r"""<p>Numbers in news often use Burmese numerals or both:</p><ul><li>၁၀၀ — 100</li><li>၁၀၀၀ — 1,000</li><li>၁၀၀၀၀ — 10,000 (also: တစ်သောင်း)</li><li>၁၀၀၀၀၀ — 100,000 (one lakh / တစ်သိန်း)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "100 in Burmese numeral: ___.", "answer": "၁၀၀"},
         {"type": "multiple-choice", "question": "1 lakh:", "options": ["1,000", "10,000", "100,000", "1,000,000"], "correctIndex": 2},
         {"type": "true-false", "question": "10,000 = တစ်သောင်း.", "correctAnswer": True},
         {"type": "fill-blank", "question": "1,000: တစ်___.", "answer": "ထောင်"},
         {"type": "true-false", "question": "Burmese newspapers always use Arabic numerals.", "correctAnswer": False}]},
    {"title": "Geographic Terms",
     "body_html": r"""<ul><li>တိုင်း — region</li><li>ပြည်နယ် — state</li><li>မြို့နယ် — township</li><li>ရပ်ကွက် — ward</li><li>ရွာ — village</li><li>တောင်ပိုင်း / မြောက်ပိုင်း — south / north</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "State (admin): ___ နယ်.", "answer": "ပြည်"},
         {"type": "multiple-choice", "question": "Township: ", "options": ["တိုင်း", "မြို့နယ်", "ရွာ", "ရပ်ကွက်"], "correctIndex": 1},
         {"type": "true-false", "question": "ရွာ means \"village.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "South: ___ ပိုင်း.", "answer": "တောင်"},
         {"type": "fill-blank", "question": "North: ___ ပိုင်း.", "answer": "မြောက်"}]},
    {"title": "Health News",
     "body_html": r"""<ul><li>ကျန်းမာရေး — health</li><li>ကပ်ရောဂါ — epidemic</li><li>ကာကွယ်ဆေး — vaccine</li><li>ဆေးရုံ — hospital</li><li>ဆရာဝန် — doctor</li><li>လူနာ — patient</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Vaccine: ___ ဆေး.", "answer": "ကာကွယ်"},
         {"type": "multiple-choice", "question": "Epidemic: ", "options": ["ကျန်းမာရေး", "ကပ်ရောဂါ", "ဆေးရုံ", "လူနာ"], "correctIndex": 1},
         {"type": "true-false", "question": "လူနာ means \"patient.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Hospital: ___ ရုံ.", "answer": "ဆေး"},
         {"type": "fill-blank", "question": "Doctor: ဆရာ ___.", "answer": "ဝန်"}]},
    {"title": "Sports News",
     "body_html": r"""<ul><li>ဘောလုံး — football</li><li>ပြိုင်ပွဲ — competition</li><li>အောင်ပွဲခံ — to win / triumph</li><li>ရှုံးနိမ့် — to lose</li><li>ပန်းတိုင် — finish line / goal</li><li>အပိုင်း — round / stage</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Football: ___ လုံး.", "answer": "ဘော"},
         {"type": "multiple-choice", "question": "To lose: ", "options": ["အောင်ပွဲခံ", "ရှုံးနိမ့်", "အပိုင်း", "ပန်းတိုင်"], "correctIndex": 1},
         {"type": "true-false", "question": "ပြိုင်ပွဲ means \"competition.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Goal: ___ တိုင်.", "answer": "ပန်း"},
         {"type": "fill-blank", "question": "Round: ___.", "answer": "အပိုင်း"}]},
    {"title": "Weather Reports",
     "body_html": r"""<ul><li>ရာသီဥတု — weather</li><li>မိုး — rain</li><li>လေပြင်း — strong wind</li><li>အပူချိန် — temperature</li><li>စိုစွတ် — humidity</li><li>တိမ်ထူ — cloudy</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Temperature: ___ ချိန်.", "answer": "အပူ"},
         {"type": "multiple-choice", "question": "Strong wind: ", "options": ["မိုး", "လေပြင်း", "စိုစွတ်", "တိမ်ထူ"], "correctIndex": 1},
         {"type": "true-false", "question": "တိမ်ထူ means \"cloudy.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Rain: ___.", "answer": "မိုး"},
         {"type": "fill-blank", "question": "Humidity: ___ စွတ်.", "answer": "စို"}]},
    {"title": "Crime & Justice",
     "body_html": r"""<ul><li>ရာဇဝတ်မှု — crime</li><li>ဖမ်းဆီး — to arrest</li><li>တရားရုံး — court</li><li>ပြစ်ဒဏ် — sentence/punishment</li><li>တရားစီရင် — to judge</li><li>သက်သေ — witness</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Crime: ___ ဝတ်မှု.", "answer": "ရာဇ"},
         {"type": "multiple-choice", "question": "Arrest: ", "options": ["ဖမ်းဆီး", "တရားရုံး", "သက်သေ", "ပြစ်ဒဏ်"], "correctIndex": 0},
         {"type": "true-false", "question": "တရားရုံး means \"court.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Witness: ___ သေ.", "answer": "သက်"},
         {"type": "fill-blank", "question": "Sentence: ___ ဒဏ်.", "answer": "ပြစ်"}]},
    {"title": "Technology News",
     "body_html": r"""<ul><li>နည်းပညာ — technology</li><li>အင်တာနက် — internet</li><li>ဖုန်း / လက်ကိုင်ဖုန်း — phone / mobile phone</li><li>ဆော့ဖ်ဝဲ — software</li><li>ဟက်ကာ — hacker</li><li>ဒေတာ — data</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Technology: နည်း ___.", "answer": "ပညာ"},
         {"type": "multiple-choice", "question": "Mobile phone: ", "options": ["ဆော့ဖ်ဝဲ", "လက်ကိုင်ဖုန်း", "ဒေတာ", "အင်တာနက်"], "correctIndex": 1},
         {"type": "true-false", "question": "ဟက်ကာ is borrowed from English.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Internet: ___.", "answer": "အင်တာနက်"},
         {"type": "fill-blank", "question": "Data: ___.", "answer": "ဒေတာ"}]},
    {"title": "Education News",
     "body_html": r"""<ul><li>ပညာရေး — education</li><li>တက္ကသိုလ် — university</li><li>ကျောင်းသား — student</li><li>ဆရာ — teacher</li><li>စာမေးပွဲ — exam</li><li>စာမေးပွဲ အောင် — to pass an exam</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "University: တက္က___ .", "answer": "သိုလ်"},
         {"type": "multiple-choice", "question": "Exam: ", "options": ["ပညာရေး", "စာမေးပွဲ", "တက္ကသိုလ်", "ကျောင်းသား"], "correctIndex": 1},
         {"type": "true-false", "question": "ကျောင်းသား means \"student.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pass exam: စာမေးပွဲ ___.", "answer": "အောင်"},
         {"type": "fill-blank", "question": "Teacher: ___.", "answer": "ဆရာ"}]},
    {"title": "Environment News",
     "body_html": r"""<ul><li>ပတ်ဝန်းကျင် — environment</li><li>သစ်တော — forest</li><li>သစ်ပင်ခုတ် — deforestation</li><li>ရာသီဥတု ပြောင်းလဲ — climate change</li><li>ထိန်းသိမ်း — to conserve</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Environment: ___ ဝန်းကျင်.", "answer": "ပတ်"},
         {"type": "multiple-choice", "question": "Forest: ", "options": ["သစ်တော", "ပတ်ဝန်းကျင်", "ထိန်းသိမ်း", "ရာသီဥတု"], "correctIndex": 0},
         {"type": "true-false", "question": "ထိန်းသိမ်း means \"to conserve.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Deforestation: သစ်ပင် ___.", "answer": "ခုတ်"},
         {"type": "fill-blank", "question": "Climate: ___ ဥတု.", "answer": "ရာသီ"}]},
    {"title": "Culture & Arts",
     "body_html": r"""<ul><li>ယဉ်ကျေးမှု — culture</li><li>အနုပညာ — art</li><li>ဂီတ — music</li><li>ပန်းချီ — painting</li><li>ရုပ်ရှင် — film</li><li>စာပေ — literature</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Culture: ___ ကျေးမှု.", "answer": "ယဉ်"},
         {"type": "multiple-choice", "question": "Painting: ", "options": ["ဂီတ", "ပန်းချီ", "ရုပ်ရှင်", "စာပေ"], "correctIndex": 1},
         {"type": "true-false", "question": "ဂီတ means \"music.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Literature: ___ ပေ.", "answer": "စာ"},
         {"type": "fill-blank", "question": "Art: ___ ပညာ.", "answer": "အနု"}]},
    {"title": "Practice: Match Topics to Vocabulary",
     "body_html": r"""<p>Identify the news topic from the keyword:</p><ol><li>ဖမ်းဆီး, တရားရုံး — Crime/Justice</li><li>ကာကွယ်ဆေး, လူနာ — Health</li><li>ပြိုင်ပွဲ, ဘောလုံး — Sports</li><li>ပါတီ, ရွေးကောက်ပွဲ — Politics</li><li>သစ်ပင်ခုတ်, ပတ်ဝန်းကျင် — Environment</li></ol>""",
     "exercises": [
         {"type": "fill-blank", "question": "ကာကွယ်ဆေး, လူနာ → ___.", "answer": "Health"},
         {"type": "multiple-choice", "question": "ပါတီ, ရွေးကောက်ပွဲ:", "options": ["Sports", "Politics", "Health", "Environment"], "correctIndex": 1},
         {"type": "true-false", "question": "ပြိုင်ပွဲ relates to sports.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Crime keyword: ___ ဆီး.", "answer": "ဖမ်း"},
         {"type": "fill-blank", "question": "Environment keyword: ___ ဝန်းကျင်.", "answer": "ပတ်"}]},
    {"title": "News Vocabulary Checkpoint",
     "body_html": r"""<p>Recap of Unit 42:</p><ul><li>Reporting verbs: ပြော, ကြေညာ, တိုင်ကြား, ဖော်ထုတ်.</li><li>Time: မနေ့က / ဒီနေ့ / မနက်ဖြန် + လအတွင်း.</li><li>Sectors: politics, economy, sports, weather, health, tech, environment.</li><li>Stats: တိုးလာ, လျော့ကျ, ပျမ်းမျှ, ရာခိုင်နှုန်း.</li><li>Crime: ဖမ်းဆီး, တရားရုံး, ပြစ်ဒဏ်.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tomorrow: ___ ဖြန်.", "answer": "မနက်"},
         {"type": "multiple-choice", "question": "Vaccine: ", "options": ["ဆေးရုံ", "ကာကွယ်ဆေး", "ဆရာဝန်", "လူနာ"], "correctIndex": 1},
         {"type": "true-false", "question": "လျော့ကျ means \"to decrease.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Court: တရား ___.", "answer": "ရုံး"},
         {"type": "fill-blank", "question": "Football: ___ လုံး.", "answer": "ဘော"},
         {"type": "true-false", "question": "Numbers in newspapers may use Burmese numerals.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Climate change: ရာသီဥတု ___ လဲ.", "answer": "ပြောင်း"}]},
]

if __name__ == "__main__":
    render_unit(42, "Burmese News Vocabulary", 610, LESSONS)
