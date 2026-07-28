#!/usr/bin/env python3
"""Burmese Unit 46 — Doctor-Patient Dialogues (lessons 670-684)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Making an Appointment",
     "body_html": r"""<p>Phrases:</p><ul><li>"ဆရာဝန်နဲ့ တွေ့ချင်ပါတယ်။" — \"I'd like to see the doctor.\"</li><li>"ဘယ်အချိန် လွတ်လဲ။" — \"What time is available?\"</li><li>"ဆရာဝန် နာမည်က ___ ပါ။" — \"The doctor's name is ___.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Doctor: ဆရာ ___.", "answer": "ဝန်"},
         {"type": "multiple-choice", "question": "Available: ", "options": ["လွတ်", "ရှိ", "မလွတ်", "ကောင်း"], "correctIndex": 0},
         {"type": "true-false", "question": "တွေ့ချင်ပါတယ် means \"I'd like to see.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "What time: ဘယ်___ .", "answer": "အချိန်"},
         {"type": "true-false", "question": "Appointments are not used in Myanmar healthcare.", "correctAnswer": False}]},
    {"title": "Describing Symptoms",
     "body_html": r"""<ul><li>"ခေါင်းကိုက်တယ်။" — \"My head hurts.\"</li><li>"ဖျား နေတယ်။" — \"I have a fever.\"</li><li>"ချောင်းဆိုးတယ်။" — \"I'm coughing.\"</li><li>"ဗိုက်အောင့်တယ်။" — \"My stomach hurts.\"</li><li>"အအေးမိတယ်။" — \"I caught a cold.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Headache: ခေါင်း ___ တယ်.", "answer": "ကိုက်"},
         {"type": "multiple-choice", "question": "Fever: ", "options": ["ဖျား နေတယ်", "ခေါင်းကိုက်တယ်", "ဗိုက်အောင့်တယ်", "ချောင်းဆိုးတယ်"], "correctIndex": 0},
         {"type": "true-false", "question": "ချောင်းဆိုးတယ် means \"coughing.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Stomach hurts: ဗိုက် ___ တယ်.", "answer": "အောင့်"},
         {"type": "fill-blank", "question": "Caught a cold: အအေး ___ တယ်.", "answer": "မိ"}]},
    {"title": "Body Parts",
     "body_html": r"""<ul><li>ခေါင်း — head</li><li>လည်ပင်း — neck</li><li>လက် — hand/arm</li><li>ခြေ — foot/leg</li><li>ဗိုက် — stomach</li><li>နှလုံး — heart</li><li>အသည်း — liver</li><li>ကျောက်ကပ် — kidney</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Heart: ___.", "answer": "နှလုံး"},
         {"type": "multiple-choice", "question": "Kidney: ", "options": ["အသည်း", "ကျောက်ကပ်", "ဗိုက်", "ခေါင်း"], "correctIndex": 1},
         {"type": "true-false", "question": "ခြေ means \"foot/leg.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Liver: ___.", "answer": "အသည်း"},
         {"type": "fill-blank", "question": "Hand/arm: ___.", "answer": "လက်"}]},
    {"title": "Pain Description",
     "body_html": r"""<ul><li>သိပ် နာတယ် — really hurts</li><li>တစ်စိမ်းစိမ်း — throbbing</li><li>ပူနေတယ် — burning</li><li>ဆို့ — sharp</li><li>ထူးထူးခြားခြား — unusual</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hurts: ___ တယ်.", "answer": "နာ"},
         {"type": "multiple-choice", "question": "Burning: ", "options": ["သိပ် နာတယ်", "ပူနေတယ်", "ဆို့", "တစ်စိမ်းစိမ်း"], "correctIndex": 1},
         {"type": "true-false", "question": "ဆို့ means \"sharp\" (pain).", "correctAnswer": True},
         {"type": "fill-blank", "question": "Throbbing: တစ်___ စိမ်း.", "answer": "စိမ်း"},
         {"type": "true-false", "question": "Doctors want detailed pain descriptions.", "correctAnswer": True}]},
    {"title": "When Did It Start?",
     "body_html": r"""<ul><li>"ဘယ်အချိန်က စတင်လဲ။" — \"When did it start?\"</li><li>"မနေ့က" — \"yesterday\"</li><li>"တစ်ပတ်ရှိပြီ" — \"It's been a week.\"</li><li>"ပြောင်းလဲမှုရှိလား။" — \"Has it changed?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Start: ___ တင်.", "answer": "စ"},
         {"type": "multiple-choice", "question": "It's been a week: ", "options": ["မနေ့က", "တစ်ပတ်ရှိပြီ", "ပြောင်းလဲ", "ဘယ်အချိန်က"], "correctIndex": 1},
         {"type": "true-false", "question": "ပြောင်းလဲ means \"to change.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "When: ___ အချိန်.", "answer": "ဘယ်"},
         {"type": "fill-blank", "question": "Yesterday: ___ က.", "answer": "မနေ့"}]},
    {"title": "Medical Vocabulary",
     "body_html": r"""<ul><li>ဆရာဝန် — doctor</li><li>သူနာပြု — nurse</li><li>ဆေးရုံ — hospital</li><li>ဆေးခန်း — clinic</li><li>ဆေးဝါး — medicine</li><li>ဆေး — drug / medicine (short)</li><li>ထိုးဆေး — injection</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Nurse: သူနာ ___.", "answer": "ပြု"},
         {"type": "multiple-choice", "question": "Injection: ", "options": ["ဆေး", "ထိုးဆေး", "ဆေးခန်း", "ဆေးရုံ"], "correctIndex": 1},
         {"type": "true-false", "question": "Clinic: ဆေးခန်း.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Medicine (long): ___ ဝါး.", "answer": "ဆေး"},
         {"type": "fill-blank", "question": "Hospital: ဆေး ___.", "answer": "ရုံ"}]},
    {"title": "Common Conditions",
     "body_html": r"""<ul><li>ဆီးချို — diabetes</li><li>သွေးတိုး — high blood pressure</li><li>သွေးနိမ့် — low blood pressure</li><li>နှလုံးရောဂါ — heart disease</li><li>ကင်ဆာ — cancer</li><li>တုပ်ကွေး — flu</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Diabetes: ဆီး ___.", "answer": "ချို"},
         {"type": "multiple-choice", "question": "Flu: ", "options": ["သွေးတိုး", "တုပ်ကွေး", "နှလုံးရောဂါ", "ကင်ဆာ"], "correctIndex": 1},
         {"type": "true-false", "question": "သွေးတိုး means \"high blood pressure.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Cancer: ___.", "answer": "ကင်ဆာ"},
         {"type": "fill-blank", "question": "Heart disease: နှလုံး ___.", "answer": "ရောဂါ"}]},
    {"title": "Tests & Procedures",
     "body_html": r"""<ul><li>သွေးစစ် — blood test</li><li>ဓာတ်မှန်ရိုက် — X-ray</li><li>စမ်းသပ်ချက် — examination</li><li>ခွဲစိတ်မှု — surgery</li><li>စစ်ဆေးခြင်း — checkup</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Blood test: သွေး ___.", "answer": "စစ်"},
         {"type": "multiple-choice", "question": "Surgery: ", "options": ["သွေးစစ်", "ခွဲစိတ်မှု", "စစ်ဆေး", "စမ်းသပ်"], "correctIndex": 1},
         {"type": "true-false", "question": "ဓာတ်မှန်ရိုက် means \"X-ray.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Examination: ___ သပ်ချက်.", "answer": "စမ်း"},
         {"type": "fill-blank", "question": "Checkup: စစ် ___.", "answer": "ဆေး"}]},
    {"title": "Prescriptions",
     "body_html": r"""<ul><li>ဆေးညွှန်း — prescription</li><li>"ဒီဆေး တစ်နေ့ ၃ ကြိမ် ရွှင်ပါ။" — \"Take this medicine 3 times a day.\"</li><li>စားပြီး — after meals</li><li>စားမတိုင်မီ — before meals</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Prescription: ___ ညွှန်း.", "answer": "ဆေး"},
         {"type": "multiple-choice", "question": "After meals: ", "options": ["စားပြီး", "စားမတိုင်မီ", "မစားခင်", "ဆေးညွှန်း"], "correctIndex": 0},
         {"type": "true-false", "question": "ရွှင် means \"to take/swallow.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Before meals: စား ___ မီ.", "answer": "မတိုင်"},
         {"type": "fill-blank", "question": "Times: ___ ကြိမ်.", "answer": "၃"}]},
    {"title": "Allergies",
     "body_html": r"""<ul><li>ဓာတ်မတည့် — allergy</li><li>"ပြင်းထန်တဲ့ ဓာတ်မတည့်မှု ရှိလား။" — \"Severe allergies?\"</li><li>"ပင်နီစီလင် ဓာတ်မတည့်ဘူး။" — \"Allergic to penicillin.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Allergy: ___ မတည့်.", "answer": "ဓာတ်"},
         {"type": "multiple-choice", "question": "Severe: ", "options": ["ပြင်းထန်တဲ့", "ပင်နီစီလင်", "ဓာတ်မတည့်", "ရှိလား"], "correctIndex": 0},
         {"type": "true-false", "question": "ဓာတ်မတည့် means \"allergy.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Penicillin: ___ နီစီလင်.", "answer": "ပင်"},
         {"type": "true-false", "question": "Asking about allergies is standard practice.", "correctAnswer": True}]},
    {"title": "Pediatrics",
     "body_html": r"""<ul><li>ကလေးအထူးကု — pediatrician</li><li>ဖျား နေတယ် — has a fever</li><li>ဆေးထိုး — vaccination</li><li>"ကလေး ဘယ်နှ နှစ် ရှိပြီလဲ။" — \"How old is the child?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Pediatrician: ကလေး ___ ကု.", "answer": "အထူး"},
         {"type": "multiple-choice", "question": "Vaccination: ", "options": ["ဆေးထိုး", "ဖျား", "ဆရာဝန်", "ဆေးခန်း"], "correctIndex": 0},
         {"type": "true-false", "question": "ဆေးထိုး means \"vaccination/injection.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "How old: ဘယ်နှ ___.", "answer": "နှစ်"},
         {"type": "fill-blank", "question": "Has a fever: ဖျား ___ တယ်.", "answer": "နေ"}]},
    {"title": "Mental Health",
     "body_html": r"""<ul><li>စိတ်ကျရောဂါ — depression</li><li>စိုးရိမ်ပူပန် — anxiety</li><li>စိတ်ပျော်ရွှင် — happy / cheerful</li><li>စိတ်ဖိစီးမှု — stress</li><li>စိတ်ပညာရှင် — psychologist</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Depression: စိတ် ___ ရောဂါ.", "answer": "ကျ"},
         {"type": "multiple-choice", "question": "Stress: ", "options": ["စိုးရိမ်", "စိတ်ပျော်ရွှင်", "စိတ်ဖိစီးမှု", "စိတ်ပညာရှင်"], "correctIndex": 2},
         {"type": "true-false", "question": "စိုးရိမ်ပူပန် means \"anxiety.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Psychologist: စိတ် ___ ရှင်.", "answer": "ပညာ"},
         {"type": "true-false", "question": "Mental health is increasingly discussed in Myanmar.", "correctAnswer": True}]},
    {"title": "Emergency Phrases",
     "body_html": r"""<ul><li>"အရေးပေါ်!" — \"Emergency!\"</li><li>"ကူပါ!" — \"Help!\"</li><li>"လူနာတင်ကား ခေါ်ပါ။" — \"Call an ambulance.\"</li><li>"အသက်အန္တရာယ်!" — \"Life-threatening!\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Emergency: ___ ပေါ်.", "answer": "အရေး"},
         {"type": "multiple-choice", "question": "Ambulance: ", "options": ["လူနာတင်ကား", "ဆရာဝန်", "ဆေးရုံ", "ထိုးဆေး"], "correctIndex": 0},
         {"type": "true-false", "question": "ကူပါ means \"Help!\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Life-threatening: အသက် ___ ရာယ်.", "answer": "အန္တ"},
         {"type": "true-false", "question": "Knowing emergency phrases is important.", "correctAnswer": True}]},
    {"title": "Practice: At the Doctor",
     "body_html": r"""<p>Sample dialogue:</p><p><strong>Doctor:</strong> "ဘာဖြစ်လို့ လာတာလဲ။"</p><p><strong>You:</strong> "ခေါင်းကိုက်ပြီး ဖျား နေတယ်။ ၃ ရက်ရှိပြီ။"</p><p><strong>Doctor:</strong> "သွေး စစ်ကြည့်ရအောင်။"</p><p><strong>You:</strong> "ကောင်းပါပြီ။"</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Why come: ဘာ___ လို့ လာတာ.", "answer": "ဖြစ်"},
         {"type": "multiple-choice", "question": "Test the blood: ", "options": ["သွေးစစ်ကြည့်", "ဖျား နေတယ်", "ခေါင်းကိုက်", "နေ ကောင်း"], "correctIndex": 0},
         {"type": "true-false", "question": "၃ ရက်ရှိပြီ means \"It's been 3 days.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Headache: ___ ကိုက်.", "answer": "ခေါင်း"},
         {"type": "fill-blank", "question": "Fever: ___ နေတယ်.", "answer": "ဖျား"}]},
    {"title": "Doctor-Patient Checkpoint",
     "body_html": r"""<p>Recap of Unit 46:</p><ul><li>Symptoms: ခေါင်းကိုက်, ဖျား, ဗိုက်အောင့်.</li><li>Body parts: ခေါင်း, ဗိုက်, နှလုံး, အသည်း, ကျောက်ကပ်.</li><li>Conditions: ဆီးချို (diabetes), သွေးတိုး (hypertension), ကင်ဆာ (cancer).</li><li>Tests: သွေးစစ် (blood), ဓာတ်မှန်ရိုက် (X-ray), ခွဲစိတ် (surgery).</li><li>Allergies: ဓာတ်မတည့်; emergencies: အရေးပေါ်!</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Doctor: ___ ဝန်.", "answer": "ဆရာ"},
         {"type": "multiple-choice", "question": "Hospital: ", "options": ["ဆေးခန်း", "ဆေးရုံ", "ဆေးညွှန်း", "ဆေးထိုး"], "correctIndex": 1},
         {"type": "true-false", "question": "ဖျား means \"fever.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Heart: ___.", "answer": "နှလုံး"},
         {"type": "fill-blank", "question": "Diabetes: ___ ချို.", "answer": "ဆီး"},
         {"type": "true-false", "question": "ဆေးထိုး = vaccination/injection.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Allergy: ___ မတည့်.", "answer": "ဓာတ်"}]},
]

if __name__ == "__main__":
    render_unit(46, "Burmese Doctor-Patient Dialogues", 670, LESSONS)
