#!/usr/bin/env python3
"""Burmese Unit 32 — Business (lessons 460-474)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Business Card Vocabulary",
     "body_html": r"""
<p>Burmese business cards (လုပ်ငန်းကတ်) typically include:</p>
<ul>
<li>အမည် — a-myi — name</li>
<li>ရာထူး — ya-htu — position / title</li>
<li>ကုမ္ပဏီ — kum-pa-ni — company</li>
<li>ဖုန်းနံပါတ် — phone-nan-pat — phone number</li>
<li>အီးမေးလ် — e-mail — email</li>
<li>လိပ်စာ — leik-sa — address</li>
</ul>
<p>Hand cards with both hands as a sign of respect.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ရာထူး means \"___ / title.\"", "answer": "position"},
         {"type": "multiple-choice", "question": "Hand business cards using:", "options": ["left hand only", "right hand only", "both hands", "thumb only"], "correctIndex": 2},
         {"type": "true-false", "question": "ကုမ္ပဏီ means \"company.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "ဖုန်းနံပါတ် means \"___ number.\"", "answer": "phone"},
         {"type": "fill-blank", "question": "လိပ်စာ means \"___\".", "answer": "address"}]},
    {"title": "Greeting a Client",
     "body_html": r"""
<p>Polite, formal greetings:</p>
<ul>
<li>"မင်္ဂလာပါ။" — "Hello" (formal/standard)</li>
<li>"ကျွန်တော့်ကို ___ လို့ ခေါ်ပါ။" — "Call me ___."</li>
<li>"တွေ့ရတာ ဝမ်းသာပါတယ်။" — "Pleased to meet you."</li>
<li>"ပထမဆုံးပဲလား။" — "Is this our first meeting?"</li>
</ul>
<p>Burmese business culture values politeness and indirectness; avoid being too direct in initial conversations.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "\"Pleased to meet you\" in Burmese:", "options": ["မင်္ဂလာပါ", "တွေ့ရတာ ဝမ်းသာပါတယ်", "သွားတော့မယ်", "ဆာတယ်"], "correctIndex": 1},
         {"type": "true-false", "question": "Burmese business culture values politeness and indirectness.", "correctAnswer": True},
         {"type": "fill-blank", "question": "မင်္ဂလာပါ means \"___\".", "answer": "Hello"},
         {"type": "true-false", "question": "Direct, blunt approaches are preferred in initial Burmese business meetings.", "correctAnswer": False},
         {"type": "fill-blank", "question": "ပထမဆုံးပဲလား။ asks if this is the ___ time.", "answer": "first"}]},
    {"title": "Job Titles",
     "body_html": r"""
<p>Common job titles in Burmese:</p>
<ul>
<li>စီအီးအို / လုပ်ငန်းရှင် — CEO / business owner</li>
<li>မန်နေဂျာ — manager</li>
<li>ဝန်ထမ်း — wun-htan — staff / employee</li>
<li>အင်ဂျင်နီယာ — engineer</li>
<li>ဆရာ၀န် — sa-ya-wun — doctor</li>
<li>ဆရာ — sa-ya — teacher</li>
<li>လယ်သမား — le-tha-ma — farmer</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "ဝန်ထမ်း means \"___\".", "answer": "staff"},
         {"type": "multiple-choice", "question": "ဆရာ means:", "options": ["doctor", "teacher", "engineer", "farmer"], "correctIndex": 1},
         {"type": "true-false", "question": "ဆရာ၀န် means \"doctor.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "လယ်သမား means \"___\".", "answer": "farmer"},
         {"type": "fill-blank", "question": "မန်နေဂျာ is borrowed from English ___.", "answer": "manager"}]},
    {"title": "Business Hours",
     "body_html": r"""
<p>Talking about business hours:</p>
<ul>
<li>"ဘယ်အချိန် ဖွင့်လဲ။" — "What time do you open?"</li>
<li>"ဘယ်အချိန် ပိတ်လဲ။" — "What time do you close?"</li>
<li>"စနေ-တနင်္ဂနွေ ပိတ်တယ်။" — "Closed Saturday-Sunday."</li>
<li>"အလုပ်ချိန် မနက် ၉ ကနေ ည ၅ ထိ။" — "Working hours from 9 AM to 5 PM."</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "ဖွင့် means \"to ___\".", "answer": "open"},
         {"type": "multiple-choice", "question": "ပိတ် means:", "options": ["open", "close", "wait", "leave"], "correctIndex": 1},
         {"type": "true-false", "question": "အလုပ်ချိန် means \"working hours.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "မနက် ၉ နာရီ means \"___ AM\".", "answer": "9"},
         {"type": "fill-blank", "question": "Saturday is စနေ; Sunday is ___.", "answer": "တနင်္ဂနွေ"}]},
    {"title": "Banking Basics",
     "body_html": r"""
<p>Banking words:</p>
<ul>
<li>ဘဏ် — ban — bank</li>
<li>ငွေစုစာရင်း — ngwe-su-sa-yin — savings account</li>
<li>ငွေသွင်း — ngwe-thwin — to deposit</li>
<li>ငွေထုတ် — ngwe-htouk — to withdraw</li>
<li>ATM — အေတီအမ် — ATM</li>
<li>ငွေလွှဲ — ngwe-hlweh — money transfer</li>
<li>ကျပ် — kyat — Burmese kyat (currency)</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Currency of Myanmar: ___.", "answer": "kyat"},
         {"type": "multiple-choice", "question": "ငွေထုတ် means:", "options": ["deposit", "withdraw", "transfer", "bank"], "correctIndex": 1},
         {"type": "true-false", "question": "ဘဏ် means \"bank.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "ငွေလွှဲ means money ___.", "answer": "transfer"},
         {"type": "fill-blank", "question": "ငွေစုစာရင်း means ___ account.", "answer": "savings"}]},
    {"title": "Negotiating Prices",
     "body_html": r"""
<p>Bargaining (ဈေးကြောင်း) is common in markets and informal trading. In formal business, prices are usually fixed but discounts can be discussed.</p>
<p>Phrases:</p>
<ul>
<li>"ဈေး လျှော့ပေးနိုင်လား။" — "Can you lower the price?"</li>
<li>"ဒါ ဈေးကြီးတယ်။" — "This is expensive."</li>
<li>"အရမ်း ဈေးပေါတယ်။" — "This is very cheap."</li>
<li>"နောက်ဆုံးဈေး ဘယ်လောက်လဲ။" — "What's the final price?"</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "ဈေးကြောင်း means \"to bargain.\"", "correctAnswer": True},
         {"type": "multiple-choice", "question": "\"ဈေး လျှော့ပေးနိုင်လား။\" asks:", "options": ["What's the address?", "Can you lower the price?", "What's your name?", "Are you open?"], "correctIndex": 1},
         {"type": "fill-blank", "question": "ဈေးကြီး means \"___\".", "answer": "expensive"},
         {"type": "true-false", "question": "ဈေးပေါ means \"cheap.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "နောက်ဆုံးဈေး means \"___ price.\"", "answer": "final"}]},
    {"title": "Closing a Deal",
     "body_html": r"""
<p>Phrases for finalizing:</p>
<ul>
<li>"သဘောတူတယ်။" — "I agree."</li>
<li>"ဒါပဲ ဖြစ်ပါစေ။" — "Let it be so / agreed."</li>
<li>"လက်မှတ်ထိုးကြရအောင်။" — "Let's sign."</li>
<li>"ကျေးဇူးတင်ပါတယ်။" — "Thank you."</li>
</ul>
<p>Handshake or both-hands gesture upon agreement is common. In traditional contexts, agreement may be sealed with a small ceremonial drink or shared meal.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "သဘောတူတယ် means \"I ___.\"", "answer": "agree"},
         {"type": "multiple-choice", "question": "လက်မှတ်ထိုးကြရအောင် means:", "options": ["Let's go", "Let's eat", "Let's sign", "Let's wait"], "correctIndex": 2},
         {"type": "true-false", "question": "Burmese tradition may seal agreements with food.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ဒါပဲ ဖြစ်ပါစေ means \"Let it be ___\".", "answer": "so"},
         {"type": "fill-blank", "question": "ကျေးဇူးတင်ပါတယ် means \"___ you.\"", "answer": "thank"}]},
    {"title": "Contracts & Agreements",
     "body_html": r"""
<p>Contract vocabulary:</p>
<ul>
<li>စာချုပ် — sa-chouk — contract</li>
<li>လက်မှတ် — let-hmat — signature</li>
<li>သက်တမ်း — thet-tan — duration / term</li>
<li>ပျက်ကွက် — pyet-kwet — to default / breach</li>
<li>တာဝန် — ta-wun — responsibility / duty</li>
<li>လျော်ကြေးငွေ — lyaw-kyay-ngwe — compensation</li>
</ul>
<p>Burmese law follows a civil-law tradition modified by colonial-era British law.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "စာချုပ် means:", "options": ["receipt", "contract", "tax", "salary"], "correctIndex": 1},
         {"type": "fill-blank", "question": "လက်မှတ် means \"___\".", "answer": "signature"},
         {"type": "true-false", "question": "ပျက်ကွက် means \"to default/breach.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "သက်တမ်း means \"___ / term.\"", "answer": "duration"},
         {"type": "fill-blank", "question": "လျော်ကြေးငွေ means \"___\".", "answer": "compensation"}]},
    {"title": "Email & Business Letters",
     "body_html": r"""
<p>A formal Burmese business email:</p>
<p><strong>လေးစားရပါသော ___ ရှင့်,</strong> "Dear ___,"</p>
<p>Body...</p>
<p><strong>လေးစားစွာဖြင့်,</strong> "Sincerely,"</p>
<p><strong>[Name]</strong></p>
<p>Modern business in Myanmar often uses English emails alongside Burmese, especially in international firms. Domestic-only firms generally use Burmese.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "လေးစားရပါသော means \"___\" (formal salutation).", "answer": "Dear"},
         {"type": "multiple-choice", "question": "လေးစားစွာဖြင့် means:", "options": ["Hello", "Dear", "Sincerely", "Goodbye"], "correctIndex": 2},
         {"type": "true-false", "question": "International firms in Myanmar often use English emails.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ရှင့် is a polite ___ particle.", "answer": "address"},
         {"type": "true-false", "question": "Burmese business letters never have salutations.", "correctAnswer": False}]},
    {"title": "Phone Etiquette",
     "body_html": r"""
<p>Phone basics:</p>
<ul>
<li>"ဟယ်လို။" — Hello (when answering).</li>
<li>"ဘယ်သူပါလဲ။" — "Who is calling?"</li>
<li>"ခဏစောင့်ပါ။" — "Please wait a moment."</li>
<li>"ပြန်ဖုန်းခေါ်ပေးပါ။" — "Please call back."</li>
<li>"ဖုန်းချလိုက်တယ်။" — "I'll hang up now."</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "ဟယ်လို means \"Hello\" on phone.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "ခဏစောင့်ပါ means:", "options": ["Hello", "Goodbye", "Please wait a moment", "Sorry"], "correctIndex": 2},
         {"type": "fill-blank", "question": "ပြန်ဖုန်းခေါ်ပေးပါ means \"Please ___ back.\"", "answer": "call"},
         {"type": "true-false", "question": "ဖုန်း is borrowed from English \"phone.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "ဘယ်သူပါလဲ means \"___ is calling?\"", "answer": "who"}]},
    {"title": "Networking Events",
     "body_html": r"""
<p>Networking event vocabulary:</p>
<ul>
<li>ပွဲ — pweh — event / party</li>
<li>စားသောက်ဖွယ် — sa-thauk-pwe — refreshments</li>
<li>လုပ်ဖော်ကိုင်ဖက် — colleague (from earlier)</li>
<li>ချိတ်ဆက် — chait-set — to network / connect</li>
<li>"စကားပြောချင်ပါတယ်။" — "I'd like to talk with you."</li>
</ul>
<p>Networking in Myanmar often happens at tea shops or business lunches rather than formal cocktail events.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ပွဲ means \"___ / party.\"", "answer": "event"},
         {"type": "multiple-choice", "question": "ချိတ်ဆက် means:", "options": ["to wait", "to network", "to leave", "to sleep"], "correctIndex": 1},
         {"type": "true-false", "question": "Networking in Myanmar often happens at tea shops.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Refreshments: ___သောက်ဖွယ်.", "answer": "စား"},
         {"type": "true-false", "question": "Burmese business prefers formal cocktail events over informal venues.", "correctAnswer": False}]},
    {"title": "Industry Vocabulary",
     "body_html": r"""
<p>Major sectors of Myanmar's economy:</p>
<ul>
<li>စိုက်ပျိုးရေး — sait-pyo-yei — agriculture</li>
<li>ကုန်သွယ်ရေး — kun-thwe-yei — trade</li>
<li>စက်မှု — set-mu — industry / manufacturing</li>
<li>ခရီးသွားလုပ်ငန်း — k'yi-thwa louk-ngan — tourism</li>
<li>ပင်လယ်ထွက်ပစ္စည်း — pin-leh htwet pit-si — marine products</li>
<li>သတ္တုတွင်း — that-tu-twin — mining</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "စိုက်ပျိုးရေး means \"___\".", "answer": "agriculture"},
         {"type": "multiple-choice", "question": "ခရီးသွားလုပ်ငန်း means:", "options": ["agriculture", "tourism", "mining", "fishing"], "correctIndex": 1},
         {"type": "true-false", "question": "သတ္တုတွင်း means \"mining.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "ကုန်သွယ်ရေး means \"___\".", "answer": "trade"},
         {"type": "fill-blank", "question": "စက်မှု means \"___\".", "answer": "industry"}]},
    {"title": "Burmese Economy Overview",
     "body_html": r"""
<p>Myanmar's economy historically depended on:</p>
<ul>
<li>Rice exports — Myanmar was once the world's biggest rice exporter.</li>
<li>Teak and timber.</li>
<li>Gemstones — rubies, jade, sapphires.</li>
<li>Agriculture — beans, pulses, fruit.</li>
<li>Increasing services and tourism since the 2010s.</li>
</ul>
<p>Modern challenges include political instability, sanctions, and uneven development between Yangon/Mandalay and rural areas.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Myanmar was once the world's biggest rice exporter.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Myanmar's most famous gemstone:", "options": ["diamonds", "rubies", "emeralds", "amethysts"], "correctIndex": 1},
         {"type": "fill-blank", "question": "A major Burmese export: ___ (wood).", "answer": "teak"},
         {"type": "true-false", "question": "Yangon and rural areas have similar levels of development.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Tourism grew especially since the ___s.", "answer": "2010"}]},
    {"title": "Practice: Business Dialogue",
     "body_html": r"""
<p>Sample short dialogue:</p>
<p><strong>A:</strong> "မင်္ဂလာပါ။ ကျွန်တော် ___ ပါ။" — "Hello, I am ___."</p>
<p><strong>B:</strong> "မင်္ဂလာပါ။ တွေ့ရတာ ဝမ်းသာပါတယ်။"</p>
<p><strong>A:</strong> "ဒီစီမံကိန်းအကြောင်း ပြောရအောင်။" — "Let's discuss this project."</p>
<p><strong>B:</strong> "ဆုံးဖြတ်ချက် ဘယ်အချိန်လောက် ရပါမလဲ။" — "When can we have a decision?"</p>
<p><strong>A:</strong> "နောက်ပတ်လောက် အဖြေပေးနိုင်ပါမယ်။" — "I'll have an answer next week."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "စီမံကိန်း means \"___\".", "answer": "project"},
         {"type": "multiple-choice", "question": "ဆုံးဖြတ်ချက် means:", "options": ["meeting", "decision", "lunch", "memo"], "correctIndex": 1},
         {"type": "true-false", "question": "ပြောရအောင် means \"let's talk.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "နောက်ပတ် means \"next ___\".", "answer": "week"},
         {"type": "true-false", "question": "ကျွန်တော် is the polite \"I\" used by male speakers.", "correctAnswer": True}]},
    {"title": "Business Checkpoint",
     "body_html": r"""
<p>Recap of Unit 32:</p>
<ul>
<li>Business cards (လုပ်ငန်းကတ်): handed with both hands.</li>
<li>Polite greetings prevail; indirectness is valued.</li>
<li>Job titles: ဆရာ၀န် (doctor), ဆရာ (teacher), မန်နေဂျာ (manager).</li>
<li>Banking: ဘဏ်, ငွေသွင်း (deposit), ငွေထုတ် (withdraw), ကျပ် (kyat).</li>
<li>Bargaining is common informally; price questions: ဈေးကြီး/ပေါ.</li>
<li>Contracts (စာချုပ်) require signature (လက်မှတ်).</li>
<li>Major industries: agriculture, trade, tourism, mining.</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Currency: ___.", "answer": "kyat"},
         {"type": "multiple-choice", "question": "How to hand business cards:", "options": ["one hand", "both hands", "throw across", "via assistant"], "correctIndex": 1},
         {"type": "true-false", "question": "Indirectness is valued in Burmese business culture.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ဈေးကြီး means \"___\".", "answer": "expensive"},
         {"type": "fill-blank", "question": "ဆရာ၀န် means \"___\".", "answer": "doctor"},
         {"type": "true-false", "question": "Tea shops are common networking venues.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Contract: ___.", "answer": "စာချုပ်"}]},
]

if __name__ == "__main__":
    render_unit(32, "Burmese in Business", 460, LESSONS)
