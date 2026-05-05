#!/usr/bin/env python3
"""Burmese Unit 48 — Driver-Passenger (lessons 700-714)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Hailing a Taxi",
     "body_html": r"""<ul><li>"တက္ကစီ ခေါ်ပါ။" — \"Call a taxi.\"</li><li>"___ ကို သွားချင်တယ်။" — \"I want to go to ___.\"</li><li>"ဘယ်လောက် ကျသလဲ။" — \"How much will it cost?\"</li><li>Wave at the curb; speak the destination clearly.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Taxi: ___.", "answer": "တက္ကစီ"},
         {"type": "multiple-choice", "question": "Want to go: ", "options": ["သွားချင်တယ်", "ပြန်ချင်တယ်", "နေချင်တယ်", "လာချင်တယ်"], "correctIndex": 0},
         {"type": "true-false", "question": "ဘယ်လောက် ကျသလဲ asks the price.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Call: ___.", "answer": "ခေါ်"},
         {"type": "true-false", "question": "Wave at the curb to hail.", "correctAnswer": True}]},
    {"title": "Giving Directions",
     "body_html": r"""<ul><li>ညာ — right</li><li>ဘယ် — left</li><li>တည့်တည့် — straight</li><li>"___ မှာ ရပ်ပါ။" — \"Stop at ___.\"</li><li>"ရှေ့ဆက်ပါ။" — \"Continue forward.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Right: ___.", "answer": "ညာ"},
         {"type": "multiple-choice", "question": "Straight: ", "options": ["ညာ", "ဘယ်", "တည့်တည့်", "ရပ်"], "correctIndex": 2},
         {"type": "true-false", "question": "ရပ်ပါ means \"please stop.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Left: ___.", "answer": "ဘယ်"},
         {"type": "fill-blank", "question": "Continue forward: ___ ဆက်ပါ.", "answer": "ရှေ့"}]},
    {"title": "Bus Vocabulary",
     "body_html": r"""<ul><li>ဘတ်စ်ကား — bus</li><li>မှတ်တိုင် — bus stop</li><li>လမ်းကြောင်း — route</li><li>"YBS ___ နံပါတ် ဘယ်ကို သွားလဲ။" — \"Where does YBS bus ___ go?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Bus stop: ___ တိုင်.", "answer": "မှတ်"},
         {"type": "multiple-choice", "question": "Route: ", "options": ["ဘတ်စ်ကား", "မှတ်တိုင်", "လမ်းကြောင်း", "နံပါတ်"], "correctIndex": 2},
         {"type": "true-false", "question": "YBS = Yangon Bus Service.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Bus: ___ ကား.", "answer": "ဘတ်စ်"},
         {"type": "true-false", "question": "Burmese cities have organized bus systems.", "correctAnswer": True}]},
    {"title": "At the Train Station",
     "body_html": r"""<ul><li>ရထား — train</li><li>ဘူတာ — station</li><li>လက်မှတ် — ticket</li><li>"___ ကို ရထား ဘယ်အချိန် ထွက်လဲ။" — \"What time does the train to ___ leave?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Train: ___.", "answer": "ရထား"},
         {"type": "multiple-choice", "question": "Station: ", "options": ["ရထား", "လက်မှတ်", "ဘူတာ", "ထွက်"], "correctIndex": 2},
         {"type": "true-false", "question": "လက်မှတ် means \"ticket.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Leave: ___.", "answer": "ထွက်"},
         {"type": "fill-blank", "question": "Train to: ___ ကို.", "answer": "..."}]},
    {"title": "On the Plane",
     "body_html": r"""<ul><li>လေယာဉ် — airplane</li><li>လေဆိပ် — airport</li><li>ကြွေးဆေး — boarding pass</li><li>"လေယာဉ် ဘယ်အချိန် တက်လဲ။" — \"When does the plane leave?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Airplane: ___.", "answer": "လေယာဉ်"},
         {"type": "multiple-choice", "question": "Airport: ", "options": ["လေယာဉ်", "လေဆိပ်", "ကြွေးဆေး", "တက်"], "correctIndex": 1},
         {"type": "true-false", "question": "ကြွေးဆေး means \"boarding pass.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Plane takeoff: ___.", "answer": "တက်"},
         {"type": "true-false", "question": "Yangon has an international airport.", "correctAnswer": True}]},
    {"title": "Boat Travel",
     "body_html": r"""<ul><li>သင်္ဘော — boat / ship</li><li>လှေ — small boat</li><li>ဆိပ်ကမ်း — port</li><li>"Inle Lake သို့ လှေ ငှားနိုင်လား။" — \"Can we rent a boat for Inle Lake?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Boat / ship: ___.", "answer": "သင်္ဘော"},
         {"type": "multiple-choice", "question": "Port: ", "options": ["သင်္ဘော", "လှေ", "ဆိပ်ကမ်း", "ငှား"], "correctIndex": 2},
         {"type": "true-false", "question": "လှေ means a small boat.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Rent: ___.", "answer": "ငှား"},
         {"type": "true-false", "question": "Inle Lake offers boat tours.", "correctAnswer": True}]},
    {"title": "Driver Conversations",
     "body_html": r"""<ul><li>"ဘယ်ကို သွားမလဲ။" — \"Where to?\"</li><li>"အရင်က ဒီနေရာ ရောက်ဖူးလား။" — \"Have you been here before?\"</li><li>"အေးကွန်း ဖွင့်ပါ။" — \"Turn on the AC.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Where to: ဘယ်___ သွားမလဲ.", "answer": "ကို"},
         {"type": "multiple-choice", "question": "AC on: ", "options": ["ဘွင့်ပါ", "ဖွင့်ပါ", "ပိတ်ပါ", "ရပ်ပါ"], "correctIndex": 1},
         {"type": "true-false", "question": "ရောက်ဖူး means \"have been to.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "AC: ___ ကွန်း.", "answer": "အေး"},
         {"type": "true-false", "question": "Drivers often chat with passengers.", "correctAnswer": True}]},
    {"title": "Bargaining a Fare",
     "body_html": r"""<ul><li>"___ ကျပ် ပေးပါမယ်။" — \"I'll pay ___ kyat.\"</li><li>"လျှော့ပေးနိုင်လား။" — \"Can you give a discount?\"</li><li>"တရားသား မပြောကြဘူး။" — \"Don't give an inflated price.\"</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Bargaining is common with no-meter taxis.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Pay: ", "options": ["ပေး", "ယူ", "ပြန်", "ထုတ်"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Inflated price warning: ___ မပြောကြဘူး.", "answer": "တရားသား"},
         {"type": "fill-blank", "question": "Discount: ___ ပေးနိုင်လား.", "answer": "လျှော့"},
         {"type": "true-false", "question": "Meters are universal in Yangon taxis.", "correctAnswer": False}]},
    {"title": "Road Conditions",
     "body_html": r"""<ul><li>လမ်းပြ — pothole</li><li>လမ်းပိတ် — road closed</li><li>ယာဉ်ကြောက — traffic jam</li><li>လမ်းပိတ်ဆို့ — blockade</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Traffic jam: ___ ကြောက.", "answer": "ယာဉ်"},
         {"type": "multiple-choice", "question": "Road closed: ", "options": ["လမ်းပြ", "လမ်းပိတ်", "လမ်းပိတ်ဆို့", "ယာဉ်ကြောက"], "correctIndex": 1},
         {"type": "true-false", "question": "လမ်းပြ means \"pothole.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Blockade: လမ်း ___ ဆို့.", "answer": "ပိတ်"},
         {"type": "true-false", "question": "Yangon has heavy traffic.", "correctAnswer": True}]},
    {"title": "Drivers' Slang",
     "body_html": r"""<ul><li>"လမ်း မဖြောင့်" — bumpy road</li><li>"ပြေး" — speed up</li><li>"ဖျော့လိုက်!" — slow down!</li><li>"အရှိန်" — speed</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Speed: ___.", "answer": "အရှိန်"},
         {"type": "multiple-choice", "question": "Slow down: ", "options": ["ပြေး", "ဖျော့လိုက်", "လမ်းမဖြောင့်", "အရှိန်"], "correctIndex": 1},
         {"type": "true-false", "question": "ပြေး means \"speed up.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Bumpy: လမ်း ___ ဖြောင့်.", "answer": "မ"},
         {"type": "true-false", "question": "ဖျော့လိုက် is a casual command.", "correctAnswer": True}]},
    {"title": "Vehicle Types",
     "body_html": r"""<ul><li>ကား — car</li><li>စက်ဘီး — bicycle</li><li>ဘုတ်ဘီး — motorcycle</li><li>ပစ်ကပ်ကား — pickup truck</li><li>ထရပ်ကား — truck</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Bicycle: ___ ဘီး.", "answer": "စက်"},
         {"type": "multiple-choice", "question": "Motorcycle: ", "options": ["ကား", "စက်ဘီး", "ဘုတ်ဘီး", "ထရပ်ကား"], "correctIndex": 2},
         {"type": "true-false", "question": "ပစ်ကပ်ကား is a pickup truck.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Truck: ___ ကား.", "answer": "ထရပ်"},
         {"type": "fill-blank", "question": "Car: ___.", "answer": "ကား"}]},
    {"title": "Driver's License",
     "body_html": r"""<ul><li>ယာဉ်မောင်းလိုင်စင် — driver's license</li><li>"လိုင်စင် ပြသပါ။" — \"Show your license.\"</li><li>ဒဏ်ငွေ — fine (penalty)</li><li>"အရှိန် ကျော်တယ်။" — \"You exceeded the speed limit.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Driver's license: ယာဉ်မောင်း ___.", "answer": "လိုင်စင်"},
         {"type": "multiple-choice", "question": "Fine: ", "options": ["လိုင်စင်", "ဒဏ်ငွေ", "အရှိန်", "ပြ"], "correctIndex": 1},
         {"type": "true-false", "question": "Speed limit exceeded: အရှိန် ကျော်တယ်.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Show: ___.", "answer": "ပြ"},
         {"type": "true-false", "question": "Police can ask for license.", "correctAnswer": True}]},
    {"title": "Asking About Distance",
     "body_html": r"""<ul><li>"ဘယ်လောက် ဝေးလဲ။" — \"How far?\"</li><li>"ကီလိုမီတာ ဘယ်လောက်လဲ။" — \"How many km?\"</li><li>"ဘယ်လောက် ကြာမလဲ။" — \"How long will it take?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Far: ___.", "answer": "ဝေး"},
         {"type": "multiple-choice", "question": "How long: ", "options": ["ဘယ်လောက် ဝေးလဲ", "ဘယ်လောက် ကြာမလဲ", "ကီလိုမီတာ", "ဘယ်ကို"], "correctIndex": 1},
         {"type": "true-false", "question": "ကြာ means \"to take time.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Kilometer: ___ မီတာ.", "answer": "ကီလို"},
         {"type": "true-false", "question": "Distance and time are common questions.", "correctAnswer": True}]},
    {"title": "Practice: Hail a Taxi",
     "body_html": r"""<p>Sample:</p><p><strong>You:</strong> "Hilton Hotel ကို သွားချင်ပါတယ်။"</p><p><strong>Driver:</strong> "ရပါတယ်။ ဘယ်လမ်းကို သွားမလဲ။"</p><p><strong>You:</strong> "ဆာရှမ်းနဲ့ ပြည်လမ်း က ပိုနီးတယ်။"</p><p><strong>Driver:</strong> "OK. ၁၀ မိနစ် ထဲမှာ ရောက်မယ်။"</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Closer/nearer: ___ နီး.", "answer": "ပို"},
         {"type": "multiple-choice", "question": "Will arrive: ", "options": ["ထွက်မယ်", "ရောက်မယ်", "သွားမယ်", "လာမယ်"], "correctIndex": 1},
         {"type": "true-false", "question": "ရပါတယ် means \"OK / it's possible.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "10 minutes: ___ မိနစ်.", "answer": "၁၀"},
         {"type": "true-false", "question": "Drivers may suggest a route.", "correctAnswer": True}]},
    {"title": "Driver-Passenger Checkpoint",
     "body_html": r"""<p>Recap of Unit 48:</p><ul><li>Vehicles: ကား, ဘတ်စ်ကား, တက္ကစီ, ရထား, လေယာဉ်.</li><li>Directions: ညာ (right), ဘယ် (left), တည့်တည့် (straight), ရပ်ပါ (stop).</li><li>Asking: ဘယ်လောက် ဝေးလဲ, ဘယ်လောက် ကြာမလဲ.</li><li>Bargaining fares with no-meter taxis is common.</li><li>လိုင်စင် (license), ဒဏ်ငွေ (fine).</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Right: ___.", "answer": "ညာ"},
         {"type": "multiple-choice", "question": "Bus stop: ", "options": ["မှတ်တိုင်", "ဘူတာ", "ဆိပ်ကမ်း", "လေဆိပ်"], "correctIndex": 0},
         {"type": "true-false", "question": "ထွက် means \"to leave / depart.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Stop: ___.", "answer": "ရပ်"},
         {"type": "fill-blank", "question": "Train: ___.", "answer": "ရထား"},
         {"type": "true-false", "question": "Yangon has an organized bus system (YBS).", "correctAnswer": True},
         {"type": "fill-blank", "question": "How long: ဘယ်လောက် ___ မလဲ.", "answer": "ကြာ"}]},
]

if __name__ == "__main__":
    render_unit(48, "Burmese Driver-Passenger", 700, LESSONS)
