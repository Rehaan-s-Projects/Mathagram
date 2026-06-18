#!/usr/bin/env python3
"""Burmese Unit 36 — Cooking & Recipes (lessons 520-534)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Kitchen Tools",
     "body_html": r"""<ul><li>ဒယ်အိုး — daih-o — wok</li><li>ထိုးထား — htui-hta — ladle</li><li>ဓား — dah — knife</li><li>ပြတ်ထုတ် — pyat-htouk — cutting board</li><li>မီးဖို — mi-bo — stove</li><li>ဂျုံ — gyon — pot</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Wok: ___ အိုး.", "answer": "ဒယ်"},
         {"type": "multiple-choice", "question": "Knife: ", "options": ["ဓား", "ဂျုံ", "ထိုးထား", "မီးဖို"], "correctIndex": 0},
         {"type": "true-false", "question": "မီးဖို means \"stove.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Cutting board: ___ ထုတ်.", "answer": "ပြတ်"},
         {"type": "fill-blank", "question": "Pot: ___.", "answer": "ဂျုံ"}]},
    {"title": "Cooking Verbs",
     "body_html": r"""<ul><li>ချက် — chet — to cook (general)</li><li>ကြော် — kyaw — to fry</li><li>ပြုတ် — pyout — to boil</li><li>ထမင်းချက် — htamin-chet — to cook rice</li><li>လှော် — hlaw — to stir-fry</li><li>ဖုတ် — phout — to bake / steam</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "To fry: ___.", "answer": "ကြော်"},
         {"type": "multiple-choice", "question": "To boil: ", "options": ["ချက်", "ကြော်", "ပြုတ်", "လှော်"], "correctIndex": 2},
         {"type": "true-false", "question": "ထမင်းချက် means \"to cook rice.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Stir-fry: ___.", "answer": "လှော်"},
         {"type": "fill-blank", "question": "Bake or steam: ___.", "answer": "ဖုတ်"}]},
    {"title": "Spices & Flavorings",
     "body_html": r"""<ul><li>ဆား — sa — salt</li><li>သကြား — tha-kyar — sugar</li><li>ငရုပ်သီး — nga-yot-thi — chili</li><li>ဆနပ် — hsa-nat — onion</li><li>ကြက်သွန်ဖြူ — kyek-thun-byu — garlic</li><li>ငံပြာရည် — ngan-pya-yei — fish sauce</li><li>ပလာတ — pa-la-ta — cilantro</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Salt: ___.", "answer": "ဆား"},
         {"type": "multiple-choice", "question": "Garlic: ", "options": ["ဆနပ်", "ကြက်သွန်ဖြူ", "ငရုပ်သီး", "သကြား"], "correctIndex": 1},
         {"type": "true-false", "question": "ငံပြာရည် is fish sauce.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sugar: ___ ကြား.", "answer": "သ"},
         {"type": "fill-blank", "question": "Chili: ___ သီး.", "answer": "ငရုပ်"}]},
    {"title": "Common Ingredients",
     "body_html": r"""<ul><li>ဆန် — hsan — uncooked rice</li><li>ထမင်း — htamin — cooked rice</li><li>ကြက် — kyek — chicken</li><li>ဝက် — wek — pork</li><li>အမဲ — a-meh — beef</li><li>ငါး — nga — fish</li><li>ဥ — u — egg</li><li>ဟင်းသီးဟင်းရွက် — hin-thi-hin-yet — vegetables</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Cooked rice: ___.", "answer": "ထမင်း"},
         {"type": "multiple-choice", "question": "Chicken: ", "options": ["ဝက်", "ကြက်", "အမဲ", "ငါး"], "correctIndex": 1},
         {"type": "true-false", "question": "ဥ means \"egg.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Vegetables: ဟင်းသီးဟင်း___ .", "answer": "ရွက်"},
         {"type": "fill-blank", "question": "Pork: ___.", "answer": "ဝက်"}]},
    {"title": "Mohinga Recipe",
     "body_html": r"""<p><strong>မုန့်ဟင်းခါး</strong> (national breakfast) needs:</p><ul><li>Catfish broth</li><li>Lemongrass, ginger</li><li>Banana stem (the secret ingredient)</li><li>Chickpea flour for thickening</li><li>Rice vermicelli noodles</li><li>Garnishes: cilantro, lime, fish sauce, fried shallots, hard-boiled egg, crispy lentil</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Mohinga is a fish soup.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Secret ingredient:", "options": ["coconut", "banana stem", "tomato", "potato"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Mohinga uses ___ flour for thickening.", "answer": "chickpea"},
         {"type": "true-false", "question": "Mohinga noodles are rice vermicelli.", "correctAnswer": True},
         {"type": "true-false", "question": "Mohinga is typically eaten for dinner only.", "correctAnswer": False}]},
    {"title": "Tea Leaf Salad (Lahpet Thoke)",
     "body_html": r"""<p><strong>လက်ဖက်သုပ်</strong> features fermented tea leaves with:</p><ul><li>Crispy fried beans (chickpeas, lima)</li><li>Toasted sesame seeds</li><li>Tomato, garlic, cilantro</li><li>Lime, fish sauce, oil</li></ul><p>Traditional Burmese hospitality dish — served at family events and to guests.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Fermented tea leaves: ___ ဖက်.", "answer": "လက်"},
         {"type": "multiple-choice", "question": "Lahpet Thoke is:", "options": ["a soup", "a salad", "a dessert", "a soup"], "correctIndex": 1},
         {"type": "true-false", "question": "It includes crispy fried beans.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sesame seeds: ___ နှမ်း.", "answer": "နှမ်း"},
         {"type": "true-false", "question": "Served at family events and to guests.", "correctAnswer": True}]},
    {"title": "Curry Basics",
     "body_html": r"""<p><strong>ဟင်း</strong> is the umbrella term for Burmese curries — saucy, oily, served over rice.</p><ul><li>Onion-tomato base</li><li>Turmeric for color</li><li>Fish sauce / shrimp paste for umami</li><li>Slow simmer until oil rises to top</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Curry: ___.", "answer": "ဟင်း"},
         {"type": "multiple-choice", "question": "Burmese curries are:", "options": ["dry", "saucy and oily", "fermented", "raw"], "correctIndex": 1},
         {"type": "true-false", "question": "Turmeric provides color.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Slow ___ until oil rises.", "answer": "simmer"},
         {"type": "fill-blank", "question": "Umami source: ___ paste.", "answer": "shrimp"}]},
    {"title": "Shan Noodles",
     "body_html": r"""<p><strong>ရှမ်းခေါက်ဆွဲ</strong> is rice noodles in clear or thick chicken broth, with marinated tomato and garlic oil. Origin: Shan State.</p><ul><li>Optional: peanut sauce variant</li><li>Common toppings: ground meat, scallion, pickled mustard greens</li><li>Best paired with crispy pork rinds</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Shan noodles: ရှမ်း ___.", "answer": "ခေါက်ဆွဲ"},
         {"type": "multiple-choice", "question": "Shan noodle origin:", "options": ["Yangon", "Shan State", "Mandalay", "India"], "correctIndex": 1},
         {"type": "true-false", "question": "Made with rice noodles.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Peanut sauce ___.", "answer": "variant"},
         {"type": "fill-blank", "question": "Common topping: pickled ___ greens.", "answer": "mustard"}]},
    {"title": "Cooking Methods",
     "body_html": r"""<ul><li>စိမ် — sein — to soak</li><li>လှော် — hlaw — to stir-fry</li><li>ပုပ် — pou — to ferment / pickle</li><li>ကြံ — kyan — to grind / crush</li><li>ထုတ် — htouk — to extract</li><li>ဖျက် — hpyet — to dissolve / mix</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "To soak: ___.", "answer": "စိမ်"},
         {"type": "multiple-choice", "question": "To ferment: ", "options": ["စိမ်", "လှော်", "ပုပ်", "ထုတ်"], "correctIndex": 2},
         {"type": "true-false", "question": "ကြံ means \"to grind.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "To stir-fry: ___.", "answer": "လှော်"},
         {"type": "fill-blank", "question": "To dissolve: ___.", "answer": "ဖျက်"}]},
    {"title": "Recipe Reading",
     "body_html": r"""<p>A recipe (ဟင်းချက်နည်း) lists:</p><ul><li>ပစ္စည်းများ — pi-si-mya — ingredients</li><li>အရေအတွက် — a-ye-a-twet — quantities</li><li>ပြုလုပ်နည်း — pyu-louk-nei — method</li></ul><p>Burmese measurements often use eyeballed amounts. "ပန်းကန်တစ်လက်" = "one bowl's worth." Modern recipes use grams.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Ingredients: ___ များ.", "answer": "ပစ္စည်း"},
         {"type": "multiple-choice", "question": "Method/procedure: ", "options": ["အရေအတွက်", "ပစ္စည်းများ", "ပြုလုပ်နည်း", "ပန်းကန်"], "correctIndex": 2},
         {"type": "true-false", "question": "Modern recipes use grams.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Quantities: အရေ___ .", "answer": "အတွက်"},
         {"type": "true-false", "question": "Traditional Burmese recipes use precise scientific measurements only.", "correctAnswer": False}]},
    {"title": "Eating Vocabulary",
     "body_html": r"""<ul><li>ဆာ — sa — to be hungry</li><li>စား — sa — to eat</li><li>ဝေ — way — to be full</li><li>ကြိုက် — kyaiq — to like</li><li>"အရသာ ရှိတယ်။" — "It's tasty."</li><li>"အင်မတန် ကောင်းတယ်။" — "Excellent."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "To eat: ___.", "answer": "စား"},
         {"type": "multiple-choice", "question": "ဝေ means:", "options": ["hungry", "full", "tired", "thirsty"], "correctIndex": 1},
         {"type": "true-false", "question": "ကြိုက် means \"to like.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tasty: အရသာ ___ တယ်.", "answer": "ရှိ"},
         {"type": "fill-blank", "question": "Excellent: အင်___ တန် ကောင်းတယ်.", "answer": "မ"}]},
    {"title": "Tea Shop Culture",
     "body_html": r"""<p><strong>လက်ဖက်ရည်ဆိုင်</strong> (tea shop) is a Burmese institution: cheap tea, snacks, conversation. Politics historically discussed there.</p><ul><li>Burmese tea: black, sweet, milky</li><li>Snacks: fried bread (paratha), samosas, mohinga</li><li>Plastic stools, low tables</li><li>Open all day</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tea shop: လက်ဖက်___ ဆိုင်.", "answer": "ရည်"},
         {"type": "multiple-choice", "question": "Burmese tea is:", "options": ["green and bitter", "black, sweet, milky", "white", "iced only"], "correctIndex": 1},
         {"type": "true-false", "question": "Tea shops historically hosted political discussions.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Fried bread snack: ___ ratha.", "answer": "pa"},
         {"type": "true-false", "question": "Tea shops are usually open all day.", "correctAnswer": True}]},
    {"title": "Street Food",
     "body_html": r"""<ul><li>ထမင်းကြော် — htamin-kyaw — fried rice</li><li>သုပ် — thoke — salads (countless varieties)</li><li>ဆမူဆာ — hsa-mu-hsa — samosa</li><li>မုန့်ဟင်းခါး — Mohinga (street version)</li><li>"ဒါ ဘယ်လောက်လဲ။" "How much?"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Fried rice: ထမင်း ___.", "answer": "ကြော်"},
         {"type": "multiple-choice", "question": "သုပ် means:", "options": ["soup", "salad", "fried", "boiled"], "correctIndex": 1},
         {"type": "true-false", "question": "ဆမူဆာ is a samosa.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Mohinga: ___ ဟင်းခါး.", "answer": "မုန့်"},
         {"type": "true-false", "question": "Street food is rare in Myanmar.", "correctAnswer": False}]},
    {"title": "Practice: Order a Meal",
     "body_html": r"""<p>Sample order:</p><p><strong>You:</strong> "မုန့်ဟင်းခါး တစ်ပန်းကန် ပေးပါ။"</p><p><strong>Server:</strong> "ဒါပါ ပိုင်ရှင်။"</p><p><strong>You:</strong> "ဆား ပိုပါ ။ ငရုပ်သီး များများ ထည့်ပါ။"</p><p><strong>Server:</strong> "လုပ်ပြီး ပါပြီ။"</p><p>"Bring me a bowl of mohinga... extra salt, lots of chili. — Ready, here you go."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Bowl: ___ ကန်.", "answer": "ပန်း"},
         {"type": "multiple-choice", "question": "More chili: ငရုပ်သီး များ___ ထည့်ပါ.", "options": ["များ", "နည်းနည်း", "ပြန်", "မ"], "correctIndex": 0},
         {"type": "true-false", "question": "ပိုပါ means \"more / extra.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "ထည့်ပါ means \"please ___\".", "answer": "add"},
         {"type": "fill-blank", "question": "လုပ်ပြီး ___ ပြီ. (\"ready\")", "answer": "ပါ"}]},
    {"title": "Cooking Checkpoint",
     "body_html": r"""<p>Recap of Unit 36:</p><ul><li>Tools: ဒယ်အိုး (wok), ဓား (knife), မီးဖို (stove).</li><li>Verbs: ချက် (cook), ကြော် (fry), ပြုတ် (boil).</li><li>Spices: ဆား, ငရုပ်သီး, ငံပြာရည်.</li><li>Famous dishes: Mohinga, Lahpet Thoke, Shan noodles, ဟင်း (curry).</li><li>Tea shop is a Burmese cultural institution.</li><li>Street food everywhere; bargaining and exchanges in Burmese.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Wok: ___ အိုး.", "answer": "ဒယ်"},
         {"type": "multiple-choice", "question": "Fish sauce:", "options": ["ဆား", "သကြား", "ငံပြာရည်", "ငရုပ်သီး"], "correctIndex": 2},
         {"type": "true-false", "question": "Mohinga is the unofficial national breakfast.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Curry: ___.", "answer": "ဟင်း"},
         {"type": "fill-blank", "question": "Salad: ___.", "answer": "သုပ်"},
         {"type": "true-false", "question": "Tea shops have plastic stools and low tables.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Cook (general): ___.", "answer": "ချက်"}]},
]

if __name__ == "__main__":
    render_unit(36, "Burmese Cooking & Recipes", 520, LESSONS)
