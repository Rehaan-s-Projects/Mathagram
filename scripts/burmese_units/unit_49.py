#!/usr/bin/env python3
"""Burmese Unit 49 — Tourism Operators (lessons 715-729)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Welcoming Tourists",
     "body_html": r"""<ul><li>"မင်္ဂလာပါ၊ မြန်မာနိုင်ငံသို့ ကြိုဆိုပါတယ်။" — \"Welcome to Myanmar.\"</li><li>"လာရောက်လည်ပတ်တာကို ကျေးဇူးတင်ပါတယ်။" — \"Thank you for visiting.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Welcome: ___ ဆိုပါတယ်.", "answer": "ကြို"},
         {"type": "multiple-choice", "question": "Visit: ", "options": ["လာရောက်လည်ပတ်", "ပြန်", "သွား", "နား"], "correctIndex": 0},
         {"type": "true-false", "question": "မြန်မာနိုင်ငံ means \"Myanmar.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Country: ___.", "answer": "နိုင်ငံ"},
         {"type": "true-false", "question": "Burmese tourism welcomes foreign visitors.", "correctAnswer": True}]},
    {"title": "Hotel Check-In",
     "body_html": r"""<ul><li>ဟိုတယ် — hotel</li><li>စာရင်းသွင်း — to register / check in</li><li>"ပတ်စ်ပို့ ပြပါ။" — \"Show your passport.\"</li><li>"အခန်းနံပါတ် ___ ပါ။" — \"Room number ___.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hotel: ___.", "answer": "ဟိုတယ်"},
         {"type": "multiple-choice", "question": "Check in: ", "options": ["ပတ်စ်ပို့", "စာရင်းသွင်း", "အခန်းနံပါတ်", "ပြ"], "correctIndex": 1},
         {"type": "true-false", "question": "ပတ်စ်ပို့ means \"passport.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Room: ___ ခန်း.", "answer": "အ"},
         {"type": "true-false", "question": "Hotels require ID/passport at check-in.", "correctAnswer": True}]},
    {"title": "Booking a Tour",
     "body_html": r"""<ul><li>ခရီးသွားလမ်းညွှန်ထုတ်ကုန် — tour package</li><li>"___ ရက် တည်းခို လမ်းညွှန် ရှိလား။" — \"Is there a ___-day tour?\"</li><li>"ခရီးသွားအာမခံ" — travel insurance</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tour package (long): ___ သွားလမ်းညွှန်ထုတ်ကုန်.", "answer": "ခရီး"},
         {"type": "multiple-choice", "question": "Travel insurance: ", "options": ["ခရီးသွားအာမခံ", "ဟိုတယ်", "လမ်းညွှန်", "ခရီးထွက်"], "correctIndex": 0},
         {"type": "true-false", "question": "Tours can be booked in advance.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tour days: ___ ရက်.", "answer": "..."},
         {"type": "true-false", "question": "Travel insurance is recommended.", "correctAnswer": True}]},
    {"title": "Famous Sites",
     "body_html": r"""<ul><li>ရွှေတိဂုံစေတီ — Shwedagon Pagoda</li><li>ပုဂံ — Bagan</li><li>အင်းလေးကန် — Inle Lake</li><li>မြောက်ဦးမြို့ — Mrauk U</li><li>ကျိုက်ထီးရိုး — Kyaiktiyo (Golden Rock)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Inle: ___ လေးကန်.", "answer": "အင်း"},
         {"type": "multiple-choice", "question": "Bagan in Burmese: ", "options": ["ပုဂံ", "ကျိုက်ထီးရိုး", "ရွှေတိဂုံ", "မြောက်ဦး"], "correctIndex": 0},
         {"type": "true-false", "question": "Kyaiktiyo is the Golden Rock pagoda.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Shwedagon: ___ တိဂုံ.", "answer": "ရွှေ"},
         {"type": "fill-blank", "question": "Mrauk U: ___ ဦးမြို့.", "answer": "မြောက်"}]},
    {"title": "Tour Guide Vocabulary",
     "body_html": r"""<ul><li>လမ်းညွှန် — guide</li><li>ဂျိုက်တင်ပြ — to explain</li><li>"ဒီနေရာ ___ နှစ်ကြာ ဝါသနာ ပါ။" — \"This place is ___ years old.\"</li><li>"ဒီကြောင် ဘာကြောင့်ထူးခြားလဲ။" — \"Why is this special?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Guide: ___ ညွှန်.", "answer": "လမ်း"},
         {"type": "multiple-choice", "question": "Explain: ", "options": ["ဂျိုက်တင်ပြ", "ပြန်", "ဆက်", "ထူးခြား"], "correctIndex": 0},
         {"type": "true-false", "question": "Tour guides know historical detail.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Why special: ဘာကြောင့် ___ လဲ.", "answer": "ထူးခြား"},
         {"type": "true-false", "question": "Asking questions is welcomed by guides.", "correctAnswer": True}]},
    {"title": "Photography Etiquette",
     "body_html": r"""<ul><li>"ဓါတ်ပုံ ရိုက်လို့ ရလား။" — \"Can I take a photo?\"</li><li>"ဖျော်ဖြေချက် — flash\"</li><li>Avoid photographing people without permission.</li><li>Some sacred sites prohibit photography inside.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Photo: ___ ပုံ.", "answer": "ဓါတ်"},
         {"type": "multiple-choice", "question": "Take a photo: ", "options": ["ဆွဲ", "ရိုက်", "ပြ", "ထုတ်"], "correctIndex": 1},
         {"type": "true-false", "question": "Permission is polite before photographing people.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Allowed: ___.", "answer": "ရ"},
         {"type": "true-false", "question": "All sites allow photography.", "correctAnswer": False}]},
    {"title": "Souvenir Shopping",
     "body_html": r"""<ul><li>လက်ဆောင်ပစ္စည်း — souvenir</li><li>"ဒါ ဘယ်လောက်လဲ။" — \"How much is this?\"</li><li>လက်ဖွဲ့ — handicraft</li><li>"အရေးတကြီး မဝယ်ချင်ပါဘူး။" — \"I don't want to buy in haste.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Souvenir: ___ ပစ္စည်း.", "answer": "လက်ဆောင်"},
         {"type": "multiple-choice", "question": "Handicraft: ", "options": ["လက်ဆောင်", "လက်ဖွဲ့", "ပစ္စည်း", "ဈေးဝယ်"], "correctIndex": 1},
         {"type": "true-false", "question": "Bargaining is normal in souvenir markets.", "correctAnswer": True},
         {"type": "fill-blank", "question": "How much: ဘယ်လောက် ___.", "answer": "လဲ"},
         {"type": "true-false", "question": "Tourists are expected to bargain in tourist markets.", "correctAnswer": True}]},
    {"title": "Cultural Performance",
     "body_html": r"""<ul><li>ဇာတ်ပွဲ — drama / performance</li><li>အခမ်းအနား — ceremony</li><li>"ရိုးရာ ဘ်ထရုံ — traditional dance</li><li>"အရင်းအနှီး အဆင့် ဘယ်လောက်လဲ။" — \"What's the cover charge?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Drama: ___ ပွဲ.", "answer": "ဇာတ်"},
         {"type": "multiple-choice", "question": "Ceremony: ", "options": ["ရိုးရာ", "အခမ်းအနား", "ဇာတ်ပွဲ", "ဖျော်ဖြေ"], "correctIndex": 1},
         {"type": "true-false", "question": "ရိုးရာ means \"traditional.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Performance: ___.", "answer": "ဖျော်ဖြေ"},
         {"type": "true-false", "question": "Cultural shows charge admission.", "correctAnswer": True}]},
    {"title": "Visa & Immigration",
     "body_html": r"""<ul><li>ဗီဇာ — visa</li><li>လူဝင်မှုကြီးကြပ်ရေး — immigration</li><li>"ရက်ပေါင်း ___ ရက် နေနိုင်ပါတယ်။" — \"You can stay ___ days.\"</li><li>"ဗီဇာ သက်တမ်း ဘယ်အချိန် ကုန်လဲ။" — \"When does the visa expire?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Visa: ___.", "answer": "ဗီဇာ"},
         {"type": "multiple-choice", "question": "Immigration: ", "options": ["လူဝင်မှုကြီးကြပ်ရေး", "ပတ်စ်ပို့", "လူနေထိုင်", "ဗီဇာ"], "correctIndex": 0},
         {"type": "true-false", "question": "သက်တမ်း means \"validity period.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Days (count): ___ ရက်.", "answer": "..."},
         {"type": "true-false", "question": "Visas have expiration dates.", "correctAnswer": True}]},
    {"title": "Traveler Health",
     "body_html": r"""<ul><li>"ရေ မသန့်ရှင်းတဲ့ နေရာ ဘယ်ကို ရှောင်ရမလဲ။" — \"Where to avoid unsafe water?\"</li><li>"ထပ်ပြီး ဖျား နေမလား။" — \"Has the fever returned?\"</li><li>ပိုးကိုက် — insect bite</li><li>ဖျား-ကိုက်ဆေး — fever-cold medicine</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Insect bite: ___ ကိုက်.", "answer": "ပိုး"},
         {"type": "multiple-choice", "question": "To avoid: ", "options": ["ရှောင်", "လုပ်", "သွား", "ဆုံး"], "correctIndex": 0},
         {"type": "true-false", "question": "Drinking unsafe water can cause illness.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Fever: ___.", "answer": "ဖျား"},
         {"type": "true-false", "question": "Travelers sometimes need fever medicine.", "correctAnswer": True}]},
    {"title": "Travel Itineraries",
     "body_html": r"""<ul><li>ခရီးစဉ် — itinerary</li><li>"ပထမနေ့" — first day</li><li>"နောက်နေ့" — next day</li><li>"အစီအစဉ်အရ" — according to plan</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Itinerary: ___ စဉ်.", "answer": "ခရီး"},
         {"type": "multiple-choice", "question": "First day: ", "options": ["ပထမနေ့", "နောက်နေ့", "နောက်ဆုံးနေ့", "ဒီနေ့"], "correctIndex": 0},
         {"type": "true-false", "question": "အစီအစဉ်အရ means \"according to plan.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Next: ___.", "answer": "နောက်"},
         {"type": "true-false", "question": "Tour itineraries are usually fixed.", "correctAnswer": True}]},
    {"title": "Best Times to Visit",
     "body_html": r"""<p>Travel seasons:</p><ul><li>November-February: cool, dry — ideal.</li><li>March-May: hot, dry.</li><li>June-October: rainy season.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Cool/dry: ___ မှ Feb.", "answer": "Nov"},
         {"type": "multiple-choice", "question": "Rainy season: ", "options": ["Nov-Feb", "Mar-May", "Jun-Oct", "all year"], "correctIndex": 2},
         {"type": "true-false", "question": "November-February is ideal for tourism.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Hot dry: ___ မှ May.", "answer": "Mar"},
         {"type": "true-false", "question": "Burma has clear seasonal cycles.", "correctAnswer": True}]},
    {"title": "Tourist Complaints",
     "body_html": r"""<ul><li>"ဒီနေရာ ဆူညံတယ်။" — \"This place is noisy.\"</li><li>"အေးကွန်း မအေးဘူး။" — \"AC isn't cooling.\"</li><li>"ပြင်ပေးနိုင်လား။" — \"Can you fix it?\"</li><li>"ပြောင်းပေးနိုင်လား။" — \"Can you change (the room)?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Noisy: ___ ညံ.", "answer": "ဆူ"},
         {"type": "multiple-choice", "question": "Fix: ", "options": ["ပြောင်း", "ပြင်", "ပိတ်", "ရပ်"], "correctIndex": 1},
         {"type": "true-false", "question": "Polite complaints get better service.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Change room: ___.", "answer": "ပြောင်း"},
         {"type": "true-false", "question": "ဆူညံ means \"noisy.\"", "correctAnswer": True}]},
    {"title": "Practice: Greet a Tourist",
     "body_html": r"""<p>Sample greeting from a tour guide:</p><p><em>"မင်္ဂလာပါ။ မြန်မာနိုင်ငံသို့ ကြိုဆိုပါတယ်။ ကျွန်တော်က ___ ပါ။ ဒီနေ့ ရွှေတိဂုံစေတီ ကို ပြသပေးပါမယ်။"</em></p><p>"Hello, welcome to Myanmar. I'm ___. Today I'll show you Shwedagon Pagoda."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Will show: ___ ပေးပါမယ်.", "answer": "ပြသ"},
         {"type": "multiple-choice", "question": "Today: ", "options": ["ဒီနေ့", "မနေ့က", "မနက်ဖြန်", "နောက်လ"], "correctIndex": 0},
         {"type": "true-false", "question": "ကြိုဆို means \"welcome.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pagoda (Shwedagon ending): ___ စေတီ.", "answer": "တိဂုံ"},
         {"type": "true-false", "question": "Tour guides typically introduce themselves.", "correctAnswer": True}]},
    {"title": "Tourism Checkpoint",
     "body_html": r"""<p>Recap of Unit 49:</p><ul><li>Welcome: ကြိုဆိုပါတယ်; thanks for visiting: ___ ကျေးဇူးတင်.</li><li>Famous: Shwedagon, Bagan, Inle, Mrauk U, Kyaiktiyo.</li><li>Tour: ခရီးသွားလမ်းညွှန်; guide: လမ်းညွှန်.</li><li>Hotel: ဟိုတယ်; check-in: စာရင်းသွင်း.</li><li>Visa: ဗီဇာ; immigration: လူဝင်မှုကြီးကြပ်ရေး.</li><li>Best season: Nov-Feb (cool/dry).</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hotel: ___.", "answer": "ဟိုတယ်"},
         {"type": "multiple-choice", "question": "Famous lake: ", "options": ["ပုဂံ", "အင်းလေးကန်", "ရွှေတိဂုံ", "ကျိုက်ထီးရိုး"], "correctIndex": 1},
         {"type": "true-false", "question": "Nov-Feb is the ideal time to visit.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Guide: ___ ညွှန်.", "answer": "လမ်း"},
         {"type": "fill-blank", "question": "Photo: ___ ပုံ.", "answer": "ဓါတ်"},
         {"type": "true-false", "question": "Visas have time limits.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Welcome: ___ ဆိုပါတယ်.", "answer": "ကြို"}]},
]

if __name__ == "__main__":
    render_unit(49, "Burmese Tourism Operators", 715, LESSONS)
