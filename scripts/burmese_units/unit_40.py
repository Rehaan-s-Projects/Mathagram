#!/usr/bin/env python3
"""Burmese Unit 40 — Children's Stories (lessons 580-594)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "What Children's Stories Teach",
     "body_html": r"""<p>Burmese children's stories blend Buddhist morals, animal characters, and language teaching. Most are short, repetitive, and rhymed for memory.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese children's stories often use rhyme.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Children's stories teach:", "options": ["only language", "only morals", "morals + language", "no real content"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Children: ___.", "answer": "ကလေးများ"},
         {"type": "true-false", "question": "Repetition aids memory.", "correctAnswer": True},
         {"type": "true-false", "question": "Burmese children's stories never feature animals.", "correctAnswer": False}]},
    {"title": "The Little Frog",
     "body_html": r"""<p>A small frog (ဖား) wants to be as big as a buffalo (ကျွဲ). It puffs itself up and up until it bursts.</p><p><strong>Moral:</strong> Don't try to be what you aren't.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Frog: ___.", "answer": "ဖား"},
         {"type": "multiple-choice", "question": "Buffalo: ", "options": ["ကျွဲ", "နွား", "မြင်း", "ခွေး"], "correctIndex": 0},
         {"type": "true-false", "question": "Moral: don't try to be what you aren't.", "correctAnswer": True},
         {"type": "fill-blank", "question": "To burst: ___.", "answer": "ပေါက်"},
         {"type": "true-false", "question": "Frog succeeds in becoming as big as a buffalo.", "correctAnswer": False}]},
    {"title": "The Boy Who Cried Tiger",
     "body_html": r"""<p>Burmese version of "Boy Who Cried Wolf" — boy keeps shouting \"Tiger!\" as a joke. When a real tiger appears, no one believes him.</p><p><strong>Moral:</strong> Liars aren't trusted when telling the truth.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese version uses tiger, not wolf.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Moral:", "options": ["lying is fun", "liars aren't trusted", "tigers don't exist", "shout louder"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Tiger: ___.", "answer": "ကျား"},
         {"type": "fill-blank", "question": "Liar: ___ သမား.", "answer": "လိမ်"},
         {"type": "true-false", "question": "When a real tiger comes, the boy is believed.", "correctAnswer": False}]},
    {"title": "The Helpful Elephant",
     "body_html": r"""<p>An elephant (ဆင်) helps a man cross a flooded river. Years later the man, now rich, refuses to help when the elephant is hurt. Karma punishes him.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Elephant: ___.", "answer": "ဆင်"},
         {"type": "multiple-choice", "question": "Moral:", "options": ["wealth wins", "ingratitude leads to bad karma", "elephants are useless", "always cross rivers"], "correctIndex": 1},
         {"type": "true-false", "question": "Elephant helps a man cross a river.", "correctAnswer": True},
         {"type": "fill-blank", "question": "River: ___.", "answer": "မြစ်"},
         {"type": "true-false", "question": "The man's gratitude grows over time.", "correctAnswer": False}]},
    {"title": "The Stolen Drum",
     "body_html": r"""<p>A child steals a drum (ဗုံ) from the temple. Hides it. Each night the drum mysteriously plays itself, exposing the thief.</p><p>Moral: You can't hide wrongdoing forever.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Drum: ___.", "answer": "ဗုံ"},
         {"type": "multiple-choice", "question": "Where stolen from:", "options": ["market", "temple", "school", "home"], "correctIndex": 1},
         {"type": "true-false", "question": "Drum plays itself.", "correctAnswer": True},
         {"type": "fill-blank", "question": "To steal: ___.", "answer": "ခိုး"},
         {"type": "true-false", "question": "The thief is never exposed.", "correctAnswer": False}]},
    {"title": "The Twelve Friends",
     "body_html": r"""<p>Twelve friends representing the months of the year travel together. Each has a different gift; they help each other through challenges. Lesson on cooperation and the seasonal cycle.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number of friends: ___.", "answer": "12"},
         {"type": "multiple-choice", "question": "They represent:", "options": ["zodiac signs", "months of year", "Buddha's lives", "kings"], "correctIndex": 1},
         {"type": "true-false", "question": "Each has a different gift.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Friend: ___.", "answer": "သူငယ်ချင်း"},
         {"type": "true-false", "question": "Story emphasizes individual achievement over cooperation.", "correctAnswer": False}]},
    {"title": "Min Min the Naughty Boy",
     "body_html": r"""<p>Min Min is a naughty boy who pulls dogs' tails, throws rocks at chickens. After hurting a baby naga, he's transformed into a frog as punishment. Repents over time and is restored to human form.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Punished by being turned into a ___.", "answer": "frog"},
         {"type": "multiple-choice", "question": "Min Min's transgression:", "options": ["honesty", "cruelty to animals", "kindness", "studying hard"], "correctIndex": 1},
         {"type": "true-false", "question": "Min Min is restored to human form.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Naughty: ___.", "answer": "မိုက်"},
         {"type": "true-false", "question": "Repentance plays a role.", "correctAnswer": True}]},
    {"title": "The Magic Pot",
     "body_html": r"""<p>A poor potter (သက်ပတ်) finds a magic pot that produces rice forever. He shares with neighbors. A greedy man steals it but the pot only works for the kind owner.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Potter: ___ .", "answer": "သက်ပတ်"},
         {"type": "multiple-choice", "question": "What does the pot produce?", "options": ["gold", "rice", "money", "tea"], "correctIndex": 1},
         {"type": "true-false", "question": "Pot works for greedy thief.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Magic: ___.", "answer": "မ္ဂူ"},
         {"type": "true-false", "question": "Generosity is rewarded in the tale.", "correctAnswer": True}]},
    {"title": "Reading Skills",
     "body_html": r"""<p>Children's books in Myanmar teach via:</p><ul><li>Picture-with-letter (\"က is for ကြောင်\" — \"k is for cat\").</li><li>Repetition of common words.</li><li>Simple sentences with one new vocabulary word per page.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Repetition is a teaching tool.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "\"က is for ___\":", "options": ["dog", "cat (ကြောင်)", "cow", "horse"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Picture: ___.", "answer": "ပုံ"},
         {"type": "fill-blank", "question": "Simple: ___.", "answer": "ရိုး"},
         {"type": "true-false", "question": "One new word per page is common.", "correctAnswer": True}]},
    {"title": "Rhymes & Songs",
     "body_html": r"""<p>Common children's rhymes:</p><ul><li>"ဆင်ဆင် ဆင်ဆင် ပိန်တယ်နော်" — \"Elephant elephant, you're skinny.\" (silly rhyme)</li><li>"ထမင်းစား ထမင်းစား" — counting rhyme</li><li>Lullabies with metta themes</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "ဆင် means ___.", "answer": "elephant"},
         {"type": "multiple-choice", "question": "Lullabies often use:", "options": ["politics", "metta themes", "horror", "math"], "correctIndex": 1},
         {"type": "true-false", "question": "ပိန် means \"skinny.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Eat rice: ___ စား.", "answer": "ထမင်း"},
         {"type": "true-false", "question": "Children's rhymes use silly themes.", "correctAnswer": True}]},
    {"title": "Common Vocabulary in Children's Books",
     "body_html": r"""<ul><li>ကြောင် (cat), ခွေး (dog), ဖား (frog), ဆင် (elephant), ကျား (tiger)</li><li>အမေ (mom), အဖေ (dad), ဖြူ (white), နက် (black)</li><li>သေး (small), ကြီး (big)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mom: ___.", "answer": "အမေ"},
         {"type": "multiple-choice", "question": "Big: ", "options": ["သေး", "ကြီး", "ဖြူ", "နက်"], "correctIndex": 1},
         {"type": "true-false", "question": "ဖြူ means \"white.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Small: ___.", "answer": "သေး"},
         {"type": "fill-blank", "question": "Dad: ___.", "answer": "အဖေ"}]},
    {"title": "Moral Through Story",
     "body_html": r"""<p>Burmese children's literature explicitly teaches:</p><ul><li>Sharing (ခွဲဝေ)</li><li>Honesty (ရိုးသား)</li><li>Respect for elders (ကြီးသူကို လေးစား)</li><li>Buddha's teachings via simplified Jataka tales</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sharing: ___ ဝေ.", "answer": "ခွဲ"},
         {"type": "multiple-choice", "question": "Respect for ___ is emphasized.", "options": ["self", "elders", "wealth", "fame"], "correctIndex": 1},
         {"type": "true-false", "question": "Simplified Jataka tales appear in children's books.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Honesty: ___ သား.", "answer": "ရိုး"},
         {"type": "true-false", "question": "Stories avoid moral lessons.", "correctAnswer": False}]},
    {"title": "Modern Children's Authors",
     "body_html": r"""<p>Modern authors like Lay Ko Tin and Maung Maung Lay have written contemporary children's stories blending traditional themes with modern situations: school, family, friendship.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Modern authors blend traditional and modern themes.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Common modern themes:", "options": ["alien invasions", "school, family, friendship", "wars only", "pure fantasy"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Author: ___ ရေးသား.", "answer": "စာ"},
         {"type": "true-false", "question": "Modern Burmese children's lit doesn't exist.", "correctAnswer": False},
         {"type": "true-false", "question": "Themes include school, family, friendship.", "correctAnswer": True}]},
    {"title": "Practice: Read a Short Story",
     "body_html": r"""<p>Read along (slowly):</p><p><em>တစ်နေ့မှာ မြို့ထဲမှာ ကြောင်ကလေးတစ်ကောင် ပျောက်နေတယ်။ မိန်းကလေးတစ်ယောက်က ရှာတွေ့ပြီး အိမ်ပြန်ပို့ပေးတယ်။ ကြောင်ရဲ့ ပိုင်ရှင်က ကျေးဇူးတင်ပါတယ်လို့ ပြောတယ်။</em></p><p>"One day in the city a kitten was lost. A girl found and brought it home. The cat's owner thanked her."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Kitten: ကြောင် ___.", "answer": "ကလေး"},
         {"type": "multiple-choice", "question": "Girl found the:", "options": ["kitten", "puppy", "elephant", "snake"], "correctIndex": 0},
         {"type": "true-false", "question": "ပျောက် means \"to be lost.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "City: ___.", "answer": "မြို့"},
         {"type": "true-false", "question": "ကျေးဇူးတင်ပါတယ် means \"thank you.\"", "correctAnswer": True}]},
    {"title": "Children's Stories Checkpoint",
     "body_html": r"""<p>Recap of Unit 40:</p><ul><li>Burmese children's stories teach morals, language, and culture together.</li><li>Common animals: cat, dog, frog, elephant, tiger.</li><li>Lessons: sharing, honesty, respect, kindness.</li><li>Modern authors blend traditional themes with contemporary settings.</li><li>Rhymes and lullabies often use metta themes.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Cat: ___.", "answer": "ကြောင်"},
         {"type": "multiple-choice", "question": "Common moral:", "options": ["winning at all costs", "kindness/sharing", "ignore parents", "pursue wealth alone"], "correctIndex": 1},
         {"type": "true-false", "question": "Lullabies use metta themes.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Frog: ___.", "answer": "ဖား"},
         {"type": "fill-blank", "question": "Elephant: ___.", "answer": "ဆင်"},
         {"type": "true-false", "question": "Children's stories often have explicit moral lessons.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Big: ___.", "answer": "ကြီး"}]},
]

if __name__ == "__main__":
    render_unit(40, "Burmese Children's Stories", 580, LESSONS)
