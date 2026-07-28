#!/usr/bin/env python3
"""Burmese Unit 35 — Real Estate (lessons 505-519)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Apartments vs Houses",
     "body_html": r"""<p>Yangon especially has both:</p><ul><li>တိုက်ခန်း — taik-khan — apartment</li><li>အိမ် — eim — house</li><li>ကွန်ဒို — kun-do — condo</li><li>ဗီလာ — vee-la — villa</li></ul><p>Older buildings are walk-up flats; newer condos have elevators (ဓာတ်လှေကား).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Apartment: ___.", "answer": "တိုက်ခန်း"},
         {"type": "multiple-choice", "question": "House: ", "options": ["တိုက်ခန်း", "အိမ်", "ကွန်ဒို", "ဗီလာ"], "correctIndex": 1},
         {"type": "true-false", "question": "Newer condos often have elevators.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Elevator: ___.", "answer": "ဓာတ်လှေကား"},
         {"type": "fill-blank", "question": "Condo: ___.", "answer": "ကွန်ဒို"}]},
    {"title": "Buying vs Renting",
     "body_html": r"""<p>Key terms:</p><ul><li>ဝယ် — wai — to buy</li><li>ငှား — hnga — to rent</li><li>ပိုင်ဆိုင်မှု — paing-saing-mhu — ownership</li><li>လုပ်ငန်းခွင် — louk-ngan-khwin — workplace</li></ul><p>Foreigners face restrictions on owning property in Myanmar; renting is more common for non-citizens.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ငှား means \"to ___\".", "answer": "rent"},
         {"type": "multiple-choice", "question": "ဝယ် means:", "options": ["sell", "buy", "rent", "own"], "correctIndex": 1},
         {"type": "true-false", "question": "Foreigners face restrictions on owning Burmese property.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Ownership: ___ ဆိုင်မှု.", "answer": "ပိုင်"},
         {"type": "true-false", "question": "Renting is uncommon for non-citizens.", "correctAnswer": False}]},
    {"title": "Rooms of a House",
     "body_html": r"""<ul><li>ဧည့်ခန်း — eh-khan — living room</li><li>အိပ်ခန်း — eik-khan — bedroom</li><li>မီးဖိုခန်း — mi-bo-khan — kitchen</li><li>ရေချိုးခန်း — yei-cho-khan — bathroom</li><li>စားပွဲခန်း — sa-pweh-khan — dining room</li><li>လေသာ — leh-tha — balcony</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Bedroom: ___ ခန်း.", "answer": "အိပ်"},
         {"type": "multiple-choice", "question": "Kitchen: ", "options": ["ဧည့်ခန်း", "အိပ်ခန်း", "မီးဖိုခန်း", "လေသာ"], "correctIndex": 2},
         {"type": "true-false", "question": "ရေချိုးခန်း means \"bathroom.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Living room: ___ ခန်း.", "answer": "ဧည့်"},
         {"type": "fill-blank", "question": "Balcony: ___.", "answer": "လေသာ"}]},
    {"title": "Furnishings",
     "body_html": r"""<ul><li>ကုလားထိုင် — ku-la-htaing — chair</li><li>စားပွဲ — sa-pweh — table</li><li>အိပ်ရာ — eik-ya — bed</li><li>တီဗီ — tee-bee — TV</li><li>ဗီရို — vi-yo — wardrobe</li><li>ရေခဲသေတ္တာ — yei-ke thit-ta — refrigerator</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Chair: ___ ထိုင်.", "answer": "ကုလား"},
         {"type": "multiple-choice", "question": "Refrigerator: ", "options": ["ဗီရို", "ရေခဲသေတ္တာ", "တီဗီ", "ကုလားထိုင်"], "correctIndex": 1},
         {"type": "true-false", "question": "ဗီရို means \"wardrobe.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Table: ___.", "answer": "စားပွဲ"},
         {"type": "fill-blank", "question": "Bed: ___.", "answer": "အိပ်ရာ"}]},
    {"title": "Lease Terms",
     "body_html": r"""<ul><li>လခ — la-kha — monthly rent</li><li>သက်တမ်း — thet-tan — duration</li><li>အပ်ငွေ — at-ngwe — deposit</li><li>ကန်ထရိုက် — kan-htraik — contract</li></ul><p>Leases are often paid 6-12 months upfront in cash. Always confirm what's included (utilities, maintenance).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Monthly rent: ___.", "answer": "လခ"},
         {"type": "multiple-choice", "question": "Deposit: ", "options": ["လခ", "သက်တမ်း", "အပ်ငွေ", "ကန်ထရိုက်"], "correctIndex": 2},
         {"type": "true-false", "question": "Leases are typically paid upfront for 6-12 months.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Contract: ___.", "answer": "ကန်ထရိုက်"},
         {"type": "true-false", "question": "Always confirm what's included.", "correctAnswer": True}]},
    {"title": "Utilities",
     "body_html": r"""<ul><li>လျှပ်စစ် — hlyat-sit — electricity</li><li>ရေ — yei — water</li><li>ဂိုဒေါင် — go-daung — internet</li><li>ဖုန်း — phone — phone</li><li>"ဘယ်ဟာတွေ ပါသလဲ။" — "What's included?"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Electricity: ___.", "answer": "လျှပ်စစ်"},
         {"type": "multiple-choice", "question": "Water: ", "options": ["လျှပ်စစ်", "ရေ", "ဖုန်း", "ဂိုဒေါင်"], "correctIndex": 1},
         {"type": "true-false", "question": "ဂိုဒေါင် (a generic loanword) means internet.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"What's included?\" ဘယ်ဟာတွေ ___ သလဲ။", "answer": "ပါ"},
         {"type": "fill-blank", "question": "Phone: ___.", "answer": "ဖုန်း"}]},
    {"title": "Neighborhood Vocabulary",
     "body_html": r"""<ul><li>ရပ်ကွက် — yat-kwet — ward / neighborhood</li><li>လမ်း — lan — street / road</li><li>ဈေး — zay — market</li><li>ကျောင်း — kyaung — school</li><li>ဆေးရုံ — say-yon — hospital</li><li>ဘုရား — paya — pagoda</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Ward: ___.", "answer": "ရပ်ကွက်"},
         {"type": "multiple-choice", "question": "Hospital: ", "options": ["ကျောင်း", "ဆေးရုံ", "ဘုရား", "ဈေး"], "correctIndex": 1},
         {"type": "true-false", "question": "လမ်း means \"street.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pagoda: ___.", "answer": "ဘုရား"},
         {"type": "fill-blank", "question": "Market: ___.", "answer": "ဈေး"}]},
    {"title": "Brokers & Agents",
     "body_html": r"""<ul><li>ပွဲစား — pweh-sa — broker / middleman</li><li>"ပွဲခ ဘယ်လောက်လဲ။" — "What's the broker fee?"</li></ul><p>Burmese real estate brokers typically charge 1 month's rent as commission. Some are independent; some work for agencies.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Broker: ___ စား.", "answer": "ပွဲ"},
         {"type": "multiple-choice", "question": "Typical broker fee:", "options": ["1 month rent", "1 year rent", "0.5%", "fixed"], "correctIndex": 0},
         {"type": "true-false", "question": "Some brokers work independently.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ပွဲခ means broker ___.", "answer": "fee"},
         {"type": "true-false", "question": "Broker fees are usually 5% of property value.", "correctAnswer": False}]},
    {"title": "Property Inspection",
     "body_html": r"""<ul><li>"ဒီအိမ် ကြည့်ချင်တယ်။" — "I want to see this house."</li><li>"ရေ စစ်ကြည့်လို့ ရလား။" — "Can I check the water?"</li><li>"ပြင်ဆင်ဖို့ လိုလား။" — "Does it need repairs?"</li><li>"ဒီခြံအနီး အသံ ဘယ်လို လဲ။" — "How is the noise around?"</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "ပြင်ဆင် means \"to repair.\"", "correctAnswer": True},
         {"type": "multiple-choice", "question": "ကြည့်ချင်တယ် means:", "options": ["I want to leave", "I want to see", "I want to wait", "I want to think"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Check water: ရေ စစ်___ .", "answer": "ကြည့်"},
         {"type": "fill-blank", "question": "ခြံ means \"___ / compound.\"", "answer": "yard"},
         {"type": "true-false", "question": "Asking about noise is reasonable when inspecting.", "correctAnswer": True}]},
    {"title": "Signing the Lease",
     "body_html": r"""<ul><li>"ကန်ထရိုက် ထိုးကြရအောင်။" — "Let's sign the contract."</li><li>"ဘယ်နေ့မှာ ပြောင်းနိုင်လဲ။" — "When can I move in?"</li><li>"အတွက် တစ်နှစ်ပဲ ထိုးချင်တယ်။" — "I want a 1-year lease only."</li></ul><p>Read every clause. Watch for: utility responsibilities, repair clause, deposit-return conditions.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sign contract: လက်မှတ် ___.", "answer": "ထိုး"},
         {"type": "multiple-choice", "question": "When move-in question:", "options": ["ဘယ်နေ့မှာ ပြောင်းနိုင်လဲ", "ဘယ်လောက်လဲ", "ဘာဖြစ်တာလဲ", "ဘယ်လို လဲ"], "correctIndex": 0},
         {"type": "true-false", "question": "Read every clause.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Lease duration: ___ တမ်း.", "answer": "သက်"},
         {"type": "true-false", "question": "Watching for repair clauses is sensible.", "correctAnswer": True}]},
    {"title": "Roommate Vocabulary",
     "body_html": r"""<ul><li>လူနေဖော် — lu-nei-baw — roommate</li><li>"အိပ်ခန်း ခြားနေတာလား။" — "Are bedrooms separate?"</li><li>"အစားစရိတ် မျှလို့ ရလား။" — "Can we split groceries?"</li></ul><p>Sharing in Burmese culture often emphasizes communal cooking and meals.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Roommate: လူ___ ဖော်.", "answer": "နေ"},
         {"type": "multiple-choice", "question": "မျှ in this context:", "options": ["receive", "share / split", "sell", "wait"], "correctIndex": 1},
         {"type": "true-false", "question": "Sharing groceries is common with roommates.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Bedrooms separate: အိပ်ခန်း ___ နေတာ.", "answer": "ခြား"},
         {"type": "true-false", "question": "Burmese culture emphasizes communal meals.", "correctAnswer": True}]},
    {"title": "Apartment Problems",
     "body_html": r"""<ul><li>ရေယိုနေတယ် — water leak</li><li>လျှပ်စစ် ပြတ်တယ် — power's out</li><li>အေးကွန်း မလုပ်ဘူး — AC isn't working</li><li>"ပြင်ပေးပါ။" — "Please fix it."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "ရေယိုနေတယ် means \"___ leak.\"", "answer": "water"},
         {"type": "multiple-choice", "question": "Power's out: လျှပ်စစ် ___ တယ်.", "options": ["ဖွင့်", "ပိတ်", "ပြတ်", "ရှိ"], "correctIndex": 2},
         {"type": "true-false", "question": "ပြင်ပေးပါ means \"please fix it.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "AC: အေး___.", "answer": "ကွန်း"},
         {"type": "true-false", "question": "Reporting problems quickly is wise.", "correctAnswer": True}]},
    {"title": "Moving In & Out",
     "body_html": r"""<ul><li>ပြောင်း — pyaung — to move</li><li>"ဒီနေ့ ပြောင်းမယ်။" — "I'm moving today."</li><li>လက်ဆောင် — lek-saung — housewarming gift</li><li>"အပ်ငွေ ပြန်ရနိုင်လား။" — "Can I get my deposit back?"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "To move: ___.", "answer": "ပြောင်း"},
         {"type": "multiple-choice", "question": "Housewarming gift:", "options": ["ပွဲ", "လက်ဆောင်", "ပြင်ဆင်", "ပြန်ပေး"], "correctIndex": 1},
         {"type": "true-false", "question": "Asking for deposit return is reasonable.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"Can I get back deposit?\" အပ်ငွေ ___ ရနိုင်လား။", "answer": "ပြန်"},
         {"type": "true-false", "question": "Burmese friends sometimes give housewarming gifts.", "correctAnswer": True}]},
    {"title": "Practice: House Hunting",
     "body_html": r"""<p>Sample dialogue:</p><p><strong>You:</strong> "ဒီတိုက်ခန်းမှာ အိပ်ခန်း ဘယ်နှခန်းရှိလဲ။" — "How many bedrooms?"</p><p><strong>Agent:</strong> "နှစ်ခန်းပါ။"</p><p><strong>You:</strong> "လခ ဘယ်လောက်လဲ။"</p><p><strong>Agent:</strong> "လခ ၈ သိန်း။"</p><p><strong>You:</strong> "လျှော့ပေးနိုင်လား။"</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "How many: ___ နှ ?", "answer": "ဘယ်"},
         {"type": "multiple-choice", "question": "နှစ်ခန်း means:", "options": ["1 room", "2 rooms", "20 rooms", "200 rooms"], "correctIndex": 1},
         {"type": "true-false", "question": "လခ asks about monthly rent.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Discount question: လျှော့___ နိုင်လား။", "answer": "ပေး"},
         {"type": "fill-blank", "question": "8 lakh: ___ သိန်း.", "answer": "၈"}]},
    {"title": "Real Estate Checkpoint",
     "body_html": r"""<p>Recap of Unit 35:</p><ul><li>Property types: တိုက်ခန်း (apartment), အိမ် (house), ကွန်ဒို (condo).</li><li>Verbs: ဝယ် (buy), ငှား (rent), ပြောင်း (move).</li><li>Lease: လခ (rent), အပ်ငွေ (deposit), ကန်ထရိုက် (contract).</li><li>Brokers: ပွဲစား charge ~1 month rent.</li><li>Foreigners face ownership restrictions; renting is more common.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Apartment: ___.", "answer": "တိုက်ခန်း"},
         {"type": "multiple-choice", "question": "Buy: ", "options": ["ငှား", "ဝယ်", "ပြောင်း", "ထိုင်"], "correctIndex": 1},
         {"type": "true-false", "question": "Foreigners can freely buy property.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Deposit: ___.", "answer": "အပ်ငွေ"},
         {"type": "fill-blank", "question": "Broker: ___ စား.", "answer": "ပွဲ"},
         {"type": "true-false", "question": "Bedrooms = အိပ်ခန်း.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Move: ___.", "answer": "ပြောင်း"}]},
]

if __name__ == "__main__":
    render_unit(35, "Burmese Real Estate", 505, LESSONS)
