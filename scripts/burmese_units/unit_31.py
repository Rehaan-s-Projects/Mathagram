#!/usr/bin/env python3
"""Burmese Unit 31 — Daily Routines (lessons 445-459)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Waking Up Vocabulary",
     "body_html": r"""
<p>Useful words for the start of the day:</p>
<ul>
<li>အိပ်ရာထ — eikya hta — to get up / wake up</li>
<li>နံနက် — nan-net — morning</li>
<li>အိပ်ပျော် — eik-pyaw — to fall asleep</li>
<li>နိုးထ — nó hta — to wake up (alert)</li>
<li>နံနက်စာ — nan-net-sa — breakfast</li>
<li>သွားတိုက် — thwa-toh — brush teeth (lit. "tooth-brush")</li>
</ul>
<p>Phrase: "ငါ မနက် ၆ နာရီ နိုးတယ်။" — "I wake at 6 AM."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "နံနက် means \"___\".", "answer": "morning"},
         {"type": "multiple-choice", "question": "သွားတိုက် means:", "options": ["wake up", "go to sleep", "brush teeth", "eat breakfast"], "correctIndex": 2},
         {"type": "true-false", "question": "အိပ်ရာထ means \"to fall asleep.\"", "correctAnswer": False},
         {"type": "fill-blank", "question": "နံနက်စာ means \"___\".", "answer": "breakfast"},
         {"type": "fill-blank", "question": "နိုးထ means \"to ___ up.\"", "answer": "wake"}]},
    {"title": "Morning Routine",
     "body_html": r"""
<p>Common morning verbs and phrases:</p>
<ul>
<li>ရေချိုး — ye-cho — to take a bath / shower</li>
<li>မျက်နှာသစ် — myet-na-thit — to wash face</li>
<li>သွားတိုက် — thwa-toh — to brush teeth</li>
<li>အ၀တ်လဲ — a-wut-le — to change clothes</li>
<li>စာသွားသင် — sa thwa-thin — to go to school (lit. "go to study")</li>
</ul>
<p>Sample dialog:</p>
<p>"မနက်တိုင်း ဘာလုပ်လဲ။" — "What do you do every morning?"</p>
<p>"ရေချိုးပြီး စာသင်သွားပါတယ်။" — "I bathe and then go to school."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ရေချိုး means \"to take a ___\".", "answer": "shower"},
         {"type": "multiple-choice", "question": "စာသွားသင် literally means:", "options": ["go to sleep", "go to study (school)", "go shopping", "go home"], "correctIndex": 1},
         {"type": "true-false", "question": "မျက်နှာသစ် means \"to wash face.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "အ၀တ်လဲ means to change ___.", "answer": "clothes"},
         {"type": "fill-blank", "question": "သွားတိုက် means \"to brush ___\".", "answer": "teeth"}]},
    {"title": "Breakfast Conversations",
     "body_html": r"""
<p>Burmese breakfast (နံနက်စာ) staples:</p>
<ul>
<li>မုန့်ဟင်းခါး — Mohinga, fish-noodle soup, the unofficial national dish.</li>
<li>ထမင်း — htamin, rice (any meal includes rice).</li>
<li>ခေါက်ဆွဲ — kauk-hsweh, noodles (Shan-style or other).</li>
<li>လက်ဖက်ရည် — la-pet-yei, tea (sweet, milky).</li>
</ul>
<p>Phrase: "မနက်စာ ဘာစားလဲ။" — "What did you eat for breakfast?"</p>
<p>"မုန့်ဟင်းခါး စားတယ်။" — "I ate Mohinga."</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "Burmese unofficial national dish:", "options": ["pho", "Mohinga", "tom yum", "satay"], "correctIndex": 1},
         {"type": "fill-blank", "question": "လက်ဖက်ရည် means ___.", "answer": "tea"},
         {"type": "true-false", "question": "ထမင်း means rice.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Burmese breakfast is called ___.", "answer": "နံနက်စာ (or nan-net-sa)"},
         {"type": "true-false", "question": "Mohinga is a dessert.", "correctAnswer": False}]},
    {"title": "Going to Work or School",
     "body_html": r"""
<p>Words and phrases:</p>
<ul>
<li>အလုပ် — a-louk — work / job</li>
<li>ကျောင်း — kyaung — school</li>
<li>သွားတယ် — thwa de — to go</li>
<li>ဘတ်စ်ကား — bus-kar — bus</li>
<li>ကား — kar — car / vehicle</li>
<li>စက်ဘီး — set-bein — bicycle</li>
</ul>
<p>"အလုပ်ကို ဘတ်စ်ကားနဲ့ သွားတယ်။" — "I go to work by bus."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ကျောင်း means \"___\".", "answer": "school"},
         {"type": "multiple-choice", "question": "ဘတ်စ်ကား means:", "options": ["bicycle", "bus", "boat", "train"], "correctIndex": 1},
         {"type": "true-false", "question": "အလုပ် means \"work\" or \"job.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "စက်ဘီး means \"___\".", "answer": "bicycle"},
         {"type": "fill-blank", "question": "သွားတယ် means \"to ___\".", "answer": "go"}]},
    {"title": "Commuting in Yangon",
     "body_html": r"""
<p>Yangon's commuting realities have unique vocabulary:</p>
<ul>
<li>ယာဉ်ကြောက — yain-kyaw-ka — traffic jam</li>
<li>YBS (Yangon Bus Service) — modern bus system</li>
<li>ဂေါက်ကား — gauk-kar — pickup truck (informal share-taxi)</li>
<li>တက္ကစီ — tek-ka-si — taxi</li>
<li>ဂျေး — Grab — popular ride-share app</li>
</ul>
<p>"ယာဉ်ကြောထဲ နာရီ အကြာ ပိတ်နေတယ်။" — "Stuck in traffic for an hour."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Traffic jam in Burmese: ___.", "answer": "ယာဉ်ကြောက"},
         {"type": "multiple-choice", "question": "Yangon ride-share app:", "options": ["Uber", "Grab", "Lyft", "Ola"], "correctIndex": 1},
         {"type": "true-false", "question": "ဂေါက်ကား means \"taxi.\"", "correctAnswer": False},
         {"type": "fill-blank", "question": "တက္ကစီ means \"___\".", "answer": "taxi"},
         {"type": "true-false", "question": "Yangon has heavy traffic.", "correctAnswer": True}]},
    {"title": "Workday Vocabulary",
     "body_html": r"""
<p>Office and workplace words:</p>
<ul>
<li>ရုံး — yon — office</li>
<li>စားပွဲ — sa-pweh — desk / table</li>
<li>ကွန်ပျူတာ — kun-pyu-ta — computer</li>
<li>စာရွက် — sa-yet — paper / document</li>
<li>လုပ်ဖော်ကိုင်ဖက် — louk-baw kaing-bet — colleague</li>
<li>စည်းဝေး — see-way — meeting</li>
</ul>
<p>"ဒီနေ့ စည်းဝေး ၃ ခုရှိတယ်။" — "I have 3 meetings today."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ရုံး means \"___\".", "answer": "office"},
         {"type": "multiple-choice", "question": "Burmese for \"meeting\":", "options": ["yon", "see-way", "kun-pyu-ta", "sa-yet"], "correctIndex": 1},
         {"type": "true-false", "question": "ကွန်ပျူတာ is borrowed from English.", "correctAnswer": True},
         {"type": "fill-blank", "question": "လုပ်ဖော်ကိုင်ဖက် means \"___\".", "answer": "colleague"},
         {"type": "fill-blank", "question": "စားပွဲ means \"___\".", "answer": "desk"}]},
    {"title": "Lunch Break Phrases",
     "body_html": r"""
<p>Lunch (နေ့လည်စာ) phrases:</p>
<ul>
<li>"ထမင်းစားမယ်။" — "I'm going to eat (lunch)."</li>
<li>"ဘာစားမလဲ။" — "What shall we eat?"</li>
<li>"အတူ စားကြရအောင်။" — "Let's eat together."</li>
<li>"ထမင်းကြွေးမယ်။" — "I'll treat you to lunch."</li>
</ul>
<p>Common lunches: rice + curry (ဟင်း hin), Shan noodles (ရှမ်းခေါက်ဆွဲ), salad (သုပ် thoke). Tea shops are popular spots.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Lunch in Burmese: နေ့___စာ.", "answer": "လည်"},
         {"type": "multiple-choice", "question": "\"အတူ စားကြရအောင်။\" means:", "options": ["I'm full", "Let's eat together", "I'm hungry", "Goodbye"], "correctIndex": 1},
         {"type": "true-false", "question": "ဟင်း means curry.", "correctAnswer": True},
         {"type": "fill-blank", "question": "သုပ် means \"___\".", "answer": "salad"},
         {"type": "fill-blank", "question": "ထမင်းကြွေးမယ်။ means \"I'll ___ you.\"", "answer": "treat"}]},
    {"title": "Afternoon Routine",
     "body_html": r"""
<p>Afternoon (နေ့လည်) words:</p>
<ul>
<li>စိတ်ပင်ပန်း — seik pin-pan — to be tired</li>
<li>ကော်ဖီ — kaw-fee — coffee</li>
<li>လုပ်ဆဲ — louk-sai — still working</li>
<li>အိမ်ပြန် — eim-pyan — to go home</li>
<li>စျေးပွဲ — zay-pweh — market</li>
</ul>
<p>"ဒီနေ့ တော်တော် ပင်ပန်းတယ်။" — "I'm pretty tired today."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ကော်ဖီ means \"___\".", "answer": "coffee"},
         {"type": "multiple-choice", "question": "အိမ်ပြန် means:", "options": ["go to work", "go home", "go shopping", "go to bed"], "correctIndex": 1},
         {"type": "true-false", "question": "စိတ်ပင်ပန်း means \"to be tired.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "နေ့လည် means \"___\".", "answer": "afternoon"},
         {"type": "fill-blank", "question": "စျေးပွဲ means \"___\".", "answer": "market"}]},
    {"title": "Evening Activities",
     "body_html": r"""
<p>Evening (ညနေ) vocabulary:</p>
<ul>
<li>ည — nya — night</li>
<li>ညနေ — nya-nei — evening</li>
<li>ရုပ်ရှင် — yoke-shin — movie</li>
<li>တီဗီ — tee-bee — TV</li>
<li>စောင့် — saung — to wait</li>
<li>ဖုန်းခေါ် — phone-khaw — phone call</li>
</ul>
<p>"ညနေ ရုပ်ရှင် ကြည့်ချင်တယ်။" — "I want to watch a movie this evening."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ည means \"___\".", "answer": "night"},
         {"type": "multiple-choice", "question": "ရုပ်ရှင် means:", "options": ["TV", "movie", "book", "phone"], "correctIndex": 1},
         {"type": "true-false", "question": "ဖုန်းခေါ် means \"phone call.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "ညနေ means \"___\".", "answer": "evening"},
         {"type": "fill-blank", "question": "စောင့် means \"to ___\".", "answer": "wait"}]},
    {"title": "Dinner Conversations",
     "body_html": r"""
<p>Dinner (ညစာ nya-sa):</p>
<ul>
<li>"ညစာ ဘာစားမလဲ။" — "What shall we have for dinner?"</li>
<li>"အိမ်မှာ ထမင်းဟင်း ချက်တယ်။" — "I'm cooking rice and curry at home."</li>
<li>"ဆာတယ်။" — "I'm hungry."</li>
<li>"ကျေနပ်တယ်။" — "I'm satisfied / full."</li>
</ul>
<p>Burmese family dinner is a sit-down affair. Rice is the staple; everyone shares from communal dishes of curries, vegetables, soups.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Dinner in Burmese: ___.", "answer": "ညစာ (or nya-sa)"},
         {"type": "multiple-choice", "question": "ဆာတယ်။ means:", "options": ["I'm full", "I'm hungry", "I'm tired", "I'm cold"], "correctIndex": 1},
         {"type": "true-false", "question": "ကျေနပ်တယ်။ means \"I'm satisfied/full.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "ထမင်းဟင်း means \"rice and ___\".", "answer": "curry"},
         {"type": "true-false", "question": "Burmese family meals share dishes communally.", "correctAnswer": True}]},
    {"title": "Bedtime Routine",
     "body_html": r"""
<p>Going to sleep (အိပ်):</p>
<ul>
<li>သွားတိုက် — thwa-toh — brush teeth (again!)</li>
<li>အိပ်ရာ — eik-ya — bed</li>
<li>စောင် — saung — blanket</li>
<li>စောင်းအိပ်ပါ — saung-eik-pa — sleep on your side</li>
<li>"အိပ်တော့မယ်။" — "I'm going to sleep now."</li>
<li>"ကောင်းသော ည။" — "Good night."</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "အိပ်ရာ means \"___\".", "answer": "bed"},
         {"type": "multiple-choice", "question": "ကောင်းသော ည။ means:", "options": ["Good morning", "Good evening", "Good night", "See you"], "correctIndex": 2},
         {"type": "true-false", "question": "စောင် means \"blanket.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "အိပ်တော့မယ်။ means \"I'm going to ___.\"", "answer": "sleep"},
         {"type": "fill-blank", "question": "သွားတိုက် (in this context) means brush ___.", "answer": "teeth"}]},
    {"title": "Weekend Routines",
     "body_html": r"""
<p>Weekend (စနေ-တနင်္ဂနွေ) is typically:</p>
<ul>
<li>Visit family (မိသားစုကို သွားလည်တယ်).</li>
<li>Go to the temple (ဘုရားကို သွား).</li>
<li>Hang out at tea shops (လက်ဖက်ရည်ဆိုင်).</li>
<li>Shopping at markets (စျေး).</li>
<li>Outdoor recreation: parks, lakes.</li>
</ul>
<p>"စနေနေ့မှာ ဘုရားသွားတယ်။" — "I went to the temple on Saturday."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Saturday: ___ နေ့.", "answer": "စနေ"},
         {"type": "multiple-choice", "question": "Sunday in Burmese:", "options": ["စနေ", "တနင်္ဂနွေ", "သောကြာ", "ကြာသပတေး"], "correctIndex": 1},
         {"type": "true-false", "question": "Going to the temple is a typical weekend activity.", "correctAnswer": True},
         {"type": "fill-blank", "question": "လက်ဖက်ရည်ဆိုင် means \"___ shop.\"", "answer": "tea"},
         {"type": "fill-blank", "question": "ဘုရား means \"___\".", "answer": "temple"}]},
    {"title": "Holiday Routines",
     "body_html": r"""
<p>Public holidays in Myanmar feature distinctive routines:</p>
<ul>
<li><strong>Thingyan (Water Festival):</strong> April; people splash water on each other for days.</li>
<li><strong>Thadingyut (Festival of Lights):</strong> October; lanterns and offerings.</li>
<li><strong>Tazaungdaing:</strong> November; another festival of lights.</li>
<li><strong>Independence Day:</strong> January 4.</li>
</ul>
<p>"သင်္ကြန် မှာ မိသားစုနဲ့ ပျော်တယ်။" — "I have fun with family at Thingyan."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Burmese Water Festival: ___.", "answer": "Thingyan"},
         {"type": "multiple-choice", "question": "Thadingyut is the festival of:", "options": ["water", "lights", "harvest", "fire"], "correctIndex": 1},
         {"type": "true-false", "question": "Independence Day in Myanmar is January 4.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Thingyan is in the month of ___.", "answer": "April"},
         {"type": "true-false", "question": "Tazaungdaing is in November.", "correctAnswer": True}]},
    {"title": "Practice: My Day in Burmese",
     "body_html": r"""
<p>Try assembling a paragraph about your day:</p>
<p><em>"ကျွန်တော် မနက် ၇ နာရီ နိုးတယ်။ ရေချိုးပြီး မုန့်ဟင်းခါး စားတယ်။ ၈ နာရီ အလုပ်ကို သွားတယ်။ စည်းဝေး ၃ ခု ရှိတယ်။ ညနေ ၅ နာရီ အိမ်ပြန်တယ်။ ည ၁၀ နာရီ အိပ်တယ်။"</em></p>
<p>"I wake at 7 AM. After bathing, I eat Mohinga. At 8 AM I go to work. I have 3 meetings. At 5 PM I go home. At 10 PM I sleep."</p>
<p>Now adapt to YOUR routine. Substitute your wake time, your meals, your work pattern.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "နာရီ means \"___ (time unit).\"", "answer": "hour"},
         {"type": "multiple-choice", "question": "မနက် ၇ နာရီ means:", "options": ["7 PM", "7 AM", "7 days", "7 weeks"], "correctIndex": 1},
         {"type": "true-false", "question": "ကျွန်တော် is the polite form of \"I\" used by male speakers.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ည ၁၀ နာရီ means \"___ PM.\"", "answer": "10"},
         {"type": "true-false", "question": "Burmese sentence ends with the punctuation ။.", "correctAnswer": True}]},
    {"title": "Daily Routines Checkpoint",
     "body_html": r"""
<p>Recap of Unit 31:</p>
<ul>
<li>Time-of-day vocabulary: နံနက် (morning), နေ့လည် (afternoon), ညနေ (evening), ည (night).</li>
<li>Three main meals: နံနက်စာ, နေ့လည်စာ, ညစာ.</li>
<li>Common verbs: နိုးထ (wake), ရေချိုး (bathe), စား (eat), အိပ် (sleep).</li>
<li>Transportation: ဘတ်စ်ကား (bus), တက္ကစီ (taxi), စက်ဘီး (bike).</li>
<li>Workplace: ရုံး (office), စည်းဝေး (meeting).</li>
<li>Weekends/holidays bring family, temple, and festival vocabulary.</li>
</ul>""",
     "exercises": [
         {"type": "multiple-choice", "question": "နံနက်စာ means:", "options": ["dinner", "lunch", "breakfast", "tea"], "correctIndex": 2},
         {"type": "fill-blank", "question": "ဘုရား means \"___\".", "answer": "temple"},
         {"type": "true-false", "question": "Thingyan is the Burmese New Year water festival.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ည means \"___\".", "answer": "night"},
         {"type": "multiple-choice", "question": "ထမင်း means:", "options": ["bread", "rice", "noodles", "tea"], "correctIndex": 1},
         {"type": "true-false", "question": "Mohinga is fish-noodle soup.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sunday in Burmese: ___.", "answer": "တနင်္ဂနွေ"}]},
]

if __name__ == "__main__":
    render_unit(31, "Burmese Daily Routines", 445, LESSONS)
