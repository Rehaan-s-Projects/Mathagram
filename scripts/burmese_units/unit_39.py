#!/usr/bin/env python3
"""Burmese Unit 39 — Folk Tales (lessons 565-579)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "The Tortoise & the Eagle",
     "body_html": r"""<p>A tortoise begs an eagle to teach him to fly. The eagle reluctantly carries him aloft, but the tortoise wriggles, falls, and dies. <strong>Moral:</strong> Be content with what you are.</p>""",
     "exercises": [
         {"type": "true-false", "question": "The tortoise survives in this tale.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "Moral:", "options": ["fly high", "trust eagles", "be content with what you are", "never give up"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Tortoise: ___ ပြာ.", "answer": "လိပ်"},
         {"type": "fill-blank", "question": "Eagle: ___.", "answer": "လင်းယုန်"},
         {"type": "true-false", "question": "Burmese folktales often feature animal characters.", "correctAnswer": True}]},
    {"title": "The Clever Rabbit",
     "body_html": r"""<p>A rabbit (ယုန်) outwits a tiger by tricking him into seeing his own reflection in a well, convincing the tiger that another (stronger) tiger lives there. The tiger leaps in and drowns.</p><p><strong>Moral:</strong> Wits beat strength.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Rabbit: ___.", "answer": "ယုန်"},
         {"type": "multiple-choice", "question": "Moral:", "options": ["strength wins", "wits beat strength", "luck matters", "always run"], "correctIndex": 1},
         {"type": "true-false", "question": "Tiger drowns in the well.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tiger: ___.", "answer": "ကျား"},
         {"type": "fill-blank", "question": "Well: ___.", "answer": "ရေတွင်း"}]},
    {"title": "The Greedy Crocodile",
     "body_html": r"""<p>A crocodile (မိချောက်) tries to eat a monkey by tricking him onto its back. The monkey escapes by claiming his heart is hidden in a tree.</p><p><strong>Moral:</strong> Greed leads to losing what you already have.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Crocodile: ___.", "answer": "မိချောက်"},
         {"type": "multiple-choice", "question": "Monkey says his heart is in a:", "options": ["river", "cave", "tree", "stone"], "correctIndex": 2},
         {"type": "true-false", "question": "Moral concerns greed.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Monkey: ___.", "answer": "မျောက်"},
         {"type": "true-false", "question": "Crocodile gets the monkey.", "correctAnswer": False}]},
    {"title": "The Wise Mongoose",
     "body_html": r"""<p>A mongoose (ပြိုက်) protects a sleeping baby from a snake. The mother returns to find the mongoose covered in blood and wrongly assumes it killed the baby. She kills the mongoose, then finds the dead snake.</p><p><strong>Moral:</strong> Don't act on appearances; gather facts first.</p>""",
     "exercises": [
         {"type": "true-false", "question": "The mongoose actually saved the baby.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Moral:", "options": ["love mongooses", "don't act on appearances", "snakes are good", "babies sleep deeply"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Mongoose: ___.", "answer": "ပြိုက်"},
         {"type": "fill-blank", "question": "Snake: ___.", "answer": "မြွေ"},
         {"type": "true-false", "question": "Mother gathers facts before acting.", "correctAnswer": False}]},
    {"title": "The Magic Mango Tree",
     "body_html": r"""<p>A poor woodcutter plants a magic mango seed; it grows golden mangoes. Greedy neighbors steal the tree but it dies in their garden — only the original kind owner can grow it.</p><p><strong>Moral:</strong> Kindness brings prosperity.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mango: ___.", "answer": "သရက်"},
         {"type": "multiple-choice", "question": "Moral:", "options": ["greed wins", "kindness brings prosperity", "magic isn't real", "trees move"], "correctIndex": 1},
         {"type": "true-false", "question": "The tree thrives in the greedy neighbor's garden.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Woodcutter: သစ် ___ သမား.", "answer": "ခုတ်"},
         {"type": "fill-blank", "question": "Golden: ___.", "answer": "ရွှေ"}]},
    {"title": "The Foolish Donkey",
     "body_html": r"""<p>A donkey wants to play with the master's lap dog. He runs in, knocks things over, ruins everything. The master beats him.</p><p><strong>Moral:</strong> Don't try to be what you aren't.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Donkey: ___.", "answer": "မြင်းကောင်း (or 'donkey')"},
         {"type": "multiple-choice", "question": "Moral:", "options": ["be yourself", "always play", "imitate masters", "knock things over"], "correctIndex": 0},
         {"type": "true-false", "question": "The donkey gets the affection he wanted.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Lap dog: ___.", "answer": "ခွေး"},
         {"type": "true-false", "question": "Trying to be what you aren't causes trouble.", "correctAnswer": True}]},
    {"title": "The Princess & the Naga",
     "body_html": r"""<p>A princess falls in love with a Naga (mythical serpent prince). They marry; their children become the founders of a Burmese royal line. (Many southeast-Asian dynasties claim Naga ancestry.)</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mythical serpent: ___.", "answer": "Naga"},
         {"type": "multiple-choice", "question": "What dynasties claim Naga ancestry?", "options": ["European royals", "Southeast Asian dynasties", "African kings", "Polynesian chiefs"], "correctIndex": 1},
         {"type": "true-false", "question": "Princess marries the Naga.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Princess: ___ မင်းသမီး.", "answer": "မ"},
         {"type": "true-false", "question": "Nagas are common in SE Asian mythology.", "correctAnswer": True}]},
    {"title": "The Forest Hermit",
     "body_html": r"""<p>A hermit (ရသေ့) lives in the forest, gaining wisdom through meditation. Kings and lords seek his counsel. Common motif in Burmese folklore: the worldly powerful must humble themselves before the truly wise.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hermit: ___.", "answer": "ရသေ့"},
         {"type": "multiple-choice", "question": "Common motif:", "options": ["powerful seek the wise", "wise serve the powerful", "hermits avoid all", "kings rule absolutely"], "correctIndex": 0},
         {"type": "true-false", "question": "Hermits live in solitude.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Wisdom: ___.", "answer": "ဉာဏ်"},
         {"type": "true-false", "question": "Hermits never appear in folklore.", "correctAnswer": False}]},
    {"title": "Folktale Structure",
     "body_html": r"""<p>Typical Burmese folktale structure:</p><ol><li>Opening: "ရှေးအခါက" — "Long ago..."</li><li>Setup: introduce characters and setting.</li><li>Conflict: usually involving greed, wisdom, or kindness.</li><li>Resolution: moral consequence.</li><li>Closing: explicit moral lesson.</li></ol>""",
     "exercises": [
         {"type": "fill-blank", "question": "Opening: ရှေးအခါ___ .", "answer": "က"},
         {"type": "multiple-choice", "question": "Common conflict themes:", "options": ["math problems", "greed/wisdom/kindness", "war strategy", "love triangles"], "correctIndex": 1},
         {"type": "true-false", "question": "Burmese folktales usually end with a moral.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"Long ago\": ___ အခါက.", "answer": "ရှေး"},
         {"type": "true-false", "question": "Burmese tales lack a structured moral closing.", "correctAnswer": False}]},
    {"title": "Common Animal Characters",
     "body_html": r"""<ul><li>ကျား (kya) — tiger: power, sometimes foolish</li><li>ယုန် (yon) — rabbit: cleverness</li><li>လိပ် (leip) — turtle: patience</li><li>မျောက် (myauk) — monkey: trickery</li><li>ကျီး (kyi) — vulture/crow: opportunism</li><li>မြွေ (myway) — snake: danger or wisdom</li><li>ကြောင် (kyaung) — cat: independence</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tiger: ___.", "answer": "ကျား"},
         {"type": "multiple-choice", "question": "Symbol of cleverness:", "options": ["tiger", "rabbit", "turtle", "vulture"], "correctIndex": 1},
         {"type": "true-false", "question": "Turtle = patience.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Snake: ___.", "answer": "မြွေ"},
         {"type": "fill-blank", "question": "Cat: ___.", "answer": "ကြောင်"}]},
    {"title": "Moral Lessons",
     "body_html": r"""<p>Common Burmese folktale morals:</p><ul><li>Greed brings ruin.</li><li>Cleverness can defeat strength.</li><li>Don't judge by appearances.</li><li>Be true to yourself.</li><li>Generosity is rewarded.</li><li>Patience wins.</li><li>Hubris falls.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Greed brings ruin is a common moral.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Cleverness vs:", "options": ["strength", "love", "wealth", "weather"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Don't judge by ___.", "answer": "appearances"},
         {"type": "true-false", "question": "\"Hubris falls\" is a common Burmese moral.", "correctAnswer": True},
         {"type": "true-false", "question": "Burmese folktales emphasize cynicism over virtue.", "correctAnswer": False}]},
    {"title": "Storytelling Phrases",
     "body_html": r"""<ul><li>"ရှေးအခါက" — "Long ago..."</li><li>"တစ်နေ့မှာ" — "One day..."</li><li>"ဘုရားသခင်က" — "The deity / spirit said..." (in some tales)</li><li>"အဲ့ဒါကြောင့်" — "Therefore / for that reason..."</li><li>"အဆုံးမှာ" — "In the end..."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "\"One day\": ___ နေ့မှာ.", "answer": "တစ်"},
         {"type": "multiple-choice", "question": "\"In the end\":", "options": ["ရှေးအခါက", "အဆုံးမှာ", "အဲ့ဒါကြောင့်", "တစ်နေ့မှာ"], "correctIndex": 1},
         {"type": "true-false", "question": "ရှေးအခါက = \"Long ago.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"Therefore\": ___ ကြောင့်.", "answer": "အဲ့ဒါ"},
         {"type": "true-false", "question": "Storytelling phrases set up structure.", "correctAnswer": True}]},
    {"title": "Comparing with Western Tales",
     "body_html": r"""<p>Some parallels:</p><ul><li>Tortoise & Eagle ≈ Aesop's Tortoise & Hare (different lessons)</li><li>Wise Mongoose ≈ The Brave Dog (Llewellyn's Gelert)</li><li>Magic Mango ≈ The Goose that Laid Golden Eggs (greed punished)</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Cross-cultural moral parallels exist.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Tortoise & Hare is from:", "options": ["Burmese", "Aesop's", "Grimms'", "Vietnamese"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Wise Mongoose ≈ The Brave ___.", "answer": "Dog"},
         {"type": "true-false", "question": "Greed-punished tales appear in many cultures.", "correctAnswer": True},
         {"type": "true-false", "question": "Burmese folklore has no parallels with Western.", "correctAnswer": False}]},
    {"title": "Practice: Tell a Story",
     "body_html": r"""<p>Compose a brief tale in Burmese style:</p><p><em>ရှေးအခါက မြင်းတစ်ကောင်နဲ့ နွားတစ်ကောင် ရှိကြတယ်။ မြင်းက ပြေးဖို့ ဂုဏ်ယူတယ်။ နွားက လယ်ထွန်ခြင်းနဲ့ ကောင်းတယ်။ တစ်နေ့ ...</em></p><p>"Long ago there was a horse and an ox. The horse boasted of running. The ox was good at plowing. One day..."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Horse: ___.", "answer": "မြင်း"},
         {"type": "multiple-choice", "question": "Ox / cow:", "options": ["မြင်း", "နွား", "ခွေး", "ကျား"], "correctIndex": 1},
         {"type": "true-false", "question": "ပြေး means \"to run.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Plow: လယ် ___ .", "answer": "ထွန်"},
         {"type": "true-false", "question": "ကောင် is the classifier for animals.", "correctAnswer": True}]},
    {"title": "Folk Tales Checkpoint",
     "body_html": r"""<p>Recap of Unit 39:</p><ul><li>Common animals: tiger, rabbit, turtle, monkey, snake — each with archetypal traits.</li><li>Story structure: "Long ago" → setup → conflict → resolution → moral.</li><li>Common morals: greed punished, cleverness wins, don't judge by appearances.</li><li>Naga, hermit, mango tree — characteristic Burmese motifs.</li><li>Storytelling phrases: ရှေးအခါက, တစ်နေ့မှာ, အဆုံးမှာ.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Rabbit symbolizes ___.", "answer": "cleverness"},
         {"type": "multiple-choice", "question": "Common Burmese folktale motif:", "options": ["aliens", "Naga", "vampires", "robots"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Long ago: ___ အခါက.", "answer": "ရှေး"},
         {"type": "true-false", "question": "Most Burmese folktales end with a moral.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tiger: ___.", "answer": "ကျား"},
         {"type": "true-false", "question": "Folktales avoid moral lessons.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Hermit: ___.", "answer": "ရသေ့"}]},
]

if __name__ == "__main__":
    render_unit(39, "Burmese Folk Tales", 565, LESSONS)
