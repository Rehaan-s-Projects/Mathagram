#!/usr/bin/env python3
"""Burmese Unit 47 — Teacher-Student Dialogues (lessons 685-699)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Classroom Vocabulary",
     "body_html": r"""<ul><li>စာသင်ခန်း — classroom</li><li>ကျောင်းသား — student</li><li>ဆရာ — teacher (m)</li><li>ဆရာမ — teacher (f)</li><li>စာအုပ် — book</li><li>ခဲတံ — pencil</li><li>ဘောပင် — pen</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Classroom: စာသင် ___.", "answer": "ခန်း"},
         {"type": "multiple-choice", "question": "Pen: ", "options": ["စာအုပ်", "ခဲတံ", "ဘောပင်", "ဆရာ"], "correctIndex": 2},
         {"type": "true-false", "question": "ဆရာမ is a female teacher.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Student: ___ သား.", "answer": "ကျောင်း"},
         {"type": "fill-blank", "question": "Pencil: ___ တံ.", "answer": "ခဲ"}]},
    {"title": "Greeting the Teacher",
     "body_html": r"""<ul><li>"မင်္ဂလာပါ ဆရာ။" — \"Hello, teacher.\"</li><li>"မင်္ဂလာပါ ဆရာမ။" — for female</li><li>Stand when greeting; bow slightly.</li><li>Add ပါ for politeness in all responses.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Stand when greeting the teacher.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Politeness particle: ", "options": ["ပါ", "က", "မ", "ဘယ်"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Hello: ___ ပါ.", "answer": "မင်္ဂလာ"},
         {"type": "true-false", "question": "Sitting through teacher greeting is fine.", "correctAnswer": False},
         {"type": "true-false", "question": "Honorifics are important in school.", "correctAnswer": True}]},
    {"title": "Asking Questions",
     "body_html": r"""<ul><li>"မေးခွင့် ပေးပါ။" — \"May I ask?\"</li><li>"ဒါ ဘာဖြစ်လို့လဲ။" — \"Why is this?\"</li><li>"ပြန်ရှင်းပြပါ။" — \"Please explain again.\"</li><li>"နားမလည်ဘူး။" — \"I don't understand.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "May I ask: ___ ခွင့် ပေးပါ.", "answer": "မေး"},
         {"type": "multiple-choice", "question": "I don't understand: ", "options": ["နားမလည်ဘူး", "ပြန်ရှင်းပြ", "မေးခွင့်", "ဘယ်လိုလဲ"], "correctIndex": 0},
         {"type": "true-false", "question": "ပြန်ရှင်းပြပါ means \"Please explain again.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Why: ဘာ___ လို့.", "answer": "ဖြစ်"},
         {"type": "fill-blank", "question": "Understand: နား ___.", "answer": "လည်"}]},
    {"title": "Answering",
     "body_html": r"""<ul><li>"အဖြေက ___ ပါ။" — \"The answer is ___.\"</li><li>"ဒါ ___ ပါ။" — \"This is ___.\"</li><li>"မသိပါဘူး။" — \"I don't know.\"</li><li>"ထင်တယ်။" — \"I think (it is).\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Answer: ___ .", "answer": "အဖြေ"},
         {"type": "multiple-choice", "question": "I don't know: ", "options": ["မသိပါဘူး", "သိပါတယ်", "ဒါ ___", "ထင်တယ်"], "correctIndex": 0},
         {"type": "true-false", "question": "ထင်တယ် means \"I think.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "I think: ___ တယ်.", "answer": "ထင်"},
         {"type": "true-false", "question": "Saying \"I don't know\" is allowed.", "correctAnswer": True}]},
    {"title": "Subjects",
     "body_html": r"""<ul><li>သင်္ချာ — math</li><li>သိပ္ပံ — science</li><li>ပထဝီ — geography</li><li>သမိုင်း — history</li><li>ဘာသာရပ် — subject</li><li>အင်္ဂလိပ်စာ — English</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Math: ___.", "answer": "သင်္ချာ"},
         {"type": "multiple-choice", "question": "History: ", "options": ["ပထဝီ", "သမိုင်း", "သိပ္ပံ", "သင်္ချာ"], "correctIndex": 1},
         {"type": "true-false", "question": "ဘာသာရပ် means \"subject.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "English: ___ စာ.", "answer": "အင်္ဂလိပ်"},
         {"type": "fill-blank", "question": "Geography: ___.", "answer": "ပထဝီ"}]},
    {"title": "Schedule & Time",
     "body_html": r"""<ul><li>စာသင်ချိန် — class time</li><li>ပေးကာလ — break</li><li>"အချိန်စားရင်း ဘယ်လောက်လဲ။" — \"What's the schedule?\"</li><li>"တနင်္လာနေ့ ဘာရှိလဲ။" — \"What's on Monday?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Class time: စာသင် ___.", "answer": "ချိန်"},
         {"type": "multiple-choice", "question": "Break: ", "options": ["စာသင်ချိန်", "ပေးကာလ", "အချိန်စားရင်း", "တနင်္လာ"], "correctIndex": 1},
         {"type": "true-false", "question": "တနင်္လာနေ့ means \"Monday.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Schedule: ___ စားရင်း.", "answer": "အချိန်"},
         {"type": "true-false", "question": "Burmese week starts Sunday.", "correctAnswer": True}]},
    {"title": "Homework",
     "body_html": r"""<ul><li>အိမ်စာ — homework</li><li>"အိမ်စာ ပေးထားလား။" — \"Did you give homework?\"</li><li>"တင်ဦးမယ်။" — \"I'll submit it.\"</li><li>"ဆရာ၊ အိမ်စာ နောက်ပိုင်း တင်လို့ ရလား။" — \"Teacher, can I submit late?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Homework: ___ စာ.", "answer": "အိမ်"},
         {"type": "multiple-choice", "question": "Submit: ", "options": ["ပေး", "တင်", "ပြန်", "လွှဲ"], "correctIndex": 1},
         {"type": "true-false", "question": "နောက်ပိုင်း means \"later.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Late submission ask: ___ ရလား.", "answer": "လို့"},
         {"type": "true-false", "question": "Asking permission politely is appreciated.", "correctAnswer": True}]},
    {"title": "Tests & Grades",
     "body_html": r"""<ul><li>စာမေးပွဲ — exam</li><li>ရမှတ် — score / mark</li><li>အောင်/ရှုံး — pass/fail</li><li>တန်းကျော် — promotion (next year)</li><li>"မေးခွန်း ဘယ်လောက် ခက်လဲ။" — \"How hard is the exam?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Score: ___ မှတ်.", "answer": "ရ"},
         {"type": "multiple-choice", "question": "Pass: ", "options": ["ရှုံး", "အောင်", "တန်းကျော်", "စာမေးပွဲ"], "correctIndex": 1},
         {"type": "true-false", "question": "တန်းကျော် means \"promote to next year.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Difficult: ___.", "answer": "ခက်"},
         {"type": "fill-blank", "question": "Question: မေး ___.", "answer": "ခွန်း"}]},
    {"title": "Praise & Encouragement",
     "body_html": r"""<ul><li>"တော်တယ်!" — \"You're talented!\"</li><li>"ဆက်လုပ်!" — \"Keep going!\"</li><li>"ကြိုးစားပါ။" — \"Try hard.\"</li><li>"ကောင်းတယ်။" — \"Good.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Talented: ___ တယ်.", "answer": "တော်"},
         {"type": "multiple-choice", "question": "Try hard: ", "options": ["ကြိုးစားပါ", "ဆက်လုပ်", "တော်တယ်", "ကောင်းတယ်"], "correctIndex": 0},
         {"type": "true-false", "question": "ဆက်လုပ် means \"Keep going.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Good: ___ တယ်.", "answer": "ကောင်း"},
         {"type": "true-false", "question": "Praise is common in Burmese teaching.", "correctAnswer": True}]},
    {"title": "Discipline",
     "body_html": r"""<ul><li>"အသံမထွက်ပါနဲ့။" — \"Don't speak (be quiet).\"</li><li>"ထိုင်ရင်းမှာ ထိုင်ပါ။" — \"Sit in your seat.\"</li><li>"ပြန်ရေးပါ။" — \"Rewrite.\"</li><li>"တာဝန်ယူ။" — \"Take responsibility.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Be quiet: အသံ ___ ထွက်ပါနဲ့.", "answer": "မ"},
         {"type": "multiple-choice", "question": "Take responsibility: ", "options": ["ပြန်ရေးပါ", "တာဝန်ယူ", "ထိုင်ပါ", "အသံမထွက်"], "correctIndex": 1},
         {"type": "true-false", "question": "Rewrite: ပြန်ရေးပါ.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sit: ___ ပါ.", "answer": "ထိုင်"},
         {"type": "true-false", "question": "Discipline language can be direct.", "correctAnswer": True}]},
    {"title": "Group Activities",
     "body_html": r"""<ul><li>အဖွဲ့ — group</li><li>လုပ်ဖော်ကိုင်ဖက် — partner</li><li>"အတူ လုပ်ကြရအောင်။" — \"Let's work together.\"</li><li>တင်ပြ — to present</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Group: ___.", "answer": "အဖွဲ့"},
         {"type": "multiple-choice", "question": "Present: ", "options": ["တင်ပြ", "ပြန်ရေး", "ဆက်လုပ်", "ထိုင်"], "correctIndex": 0},
         {"type": "true-false", "question": "လုပ်ဖော်ကိုင်ဖက် means \"partner.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Together: ___ လုပ်ကြရအောင်.", "answer": "အတူ"},
         {"type": "true-false", "question": "Group work is uncommon in Burmese schools.", "correctAnswer": False}]},
    {"title": "Library Vocabulary",
     "body_html": r"""<ul><li>စာကြည့်တိုက် — library</li><li>စာအုပ်ငှား — to borrow a book</li><li>ပြန်အပ် — to return</li><li>"စာအုပ် ဘယ်နှအုပ် ငှားနိုင်လဲ။" — \"How many books can I borrow?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Library: ___ တိုက်.", "answer": "စာကြည့်"},
         {"type": "multiple-choice", "question": "Borrow: ", "options": ["ပြန်အပ်", "စာအုပ်ငှား", "စာကြည့်တိုက်", "ဘယ်နှအုပ်"], "correctIndex": 1},
         {"type": "true-false", "question": "ပြန်အပ် means \"to return.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Book: ___ အုပ်.", "answer": "စာ"},
         {"type": "true-false", "question": "Libraries exist in Myanmar.", "correctAnswer": True}]},
    {"title": "Graduation",
     "body_html": r"""<ul><li>ဘွဲ့နှင်းသဘင် — graduation ceremony</li><li>ဘွဲ့ — degree / diploma</li><li>"အောင်မြင်စွာ ပြီးဆုံးပြီ။" — \"Successfully completed.\"</li><li>"ဂုဏ်ယူပါတယ်။" — \"Congratulations / I'm proud.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Degree: ___.", "answer": "ဘွဲ့"},
         {"type": "multiple-choice", "question": "Congratulations: ", "options": ["ဘွဲ့", "ဂုဏ်ယူပါတယ်", "ပြီးဆုံးပြီ", "အောင်မြင်"], "correctIndex": 1},
         {"type": "true-false", "question": "ဘွဲ့နှင်းသဘင် means \"graduation ceremony.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Successfully: ___ မြင်စွာ.", "answer": "အောင်"},
         {"type": "true-false", "question": "Burmese graduations are ceremonial events.", "correctAnswer": True}]},
    {"title": "Practice: A Class Day",
     "body_html": r"""<p>Sample dialogue:</p><p><strong>Teacher:</strong> "မင်္ဂလာပါ။ ဒီနေ့ သင်္ချာ စာသင်မယ်။"</p><p><strong>Student:</strong> "မင်္ဂလာပါ ဆရာ။"</p><p><strong>Teacher:</strong> "အိမ်စာ ကို ထုတ်ပြပါ။"</p><p><strong>Student:</strong> "ဒါ ကျွန်တော့် အိမ်စာ ပါ။"</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Today: ___.", "answer": "ဒီနေ့"},
         {"type": "multiple-choice", "question": "Show: ", "options": ["ပြ", "ထုတ်", "ထုတ်ပြ", "ထိုင်"], "correctIndex": 2},
         {"type": "true-false", "question": "ကျွန်တော့် means \"my\" (male polite).", "correctAnswer": True},
         {"type": "fill-blank", "question": "Math: ___.", "answer": "သင်္ချာ"},
         {"type": "fill-blank", "question": "Will study: ___ မယ်.", "answer": "သင်"}]},
    {"title": "Teacher-Student Checkpoint",
     "body_html": r"""<p>Recap of Unit 47:</p><ul><li>Teacher: ဆရာ (m) / ဆရာမ (f); student: ကျောင်းသား.</li><li>Subjects: သင်္ချာ, သိပ္ပံ, သမိုင်း, အင်္ဂလိပ်စာ.</li><li>Asking: မေးခွင့်; saying I don't understand: နားမလည်ဘူး.</li><li>Praise: တော်တယ်; encouragement: ကြိုးစားပါ.</li><li>Exam: စာမေးပွဲ; pass/fail: အောင်/ရှုံး.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Teacher (m): ___.", "answer": "ဆရာ"},
         {"type": "multiple-choice", "question": "Library: ", "options": ["စာအုပ်", "စာကြည့်တိုက်", "စာသင်ခန်း", "ကျောင်း"], "correctIndex": 1},
         {"type": "true-false", "question": "ကြိုးစားပါ means \"try hard.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Homework: ___ စာ.", "answer": "အိမ်"},
         {"type": "fill-blank", "question": "Pass: ___.", "answer": "အောင်"},
         {"type": "true-false", "question": "Students stand to greet teachers.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Graduation degree: ___.", "answer": "ဘွဲ့"}]},
]

if __name__ == "__main__":
    render_unit(47, "Burmese Teacher-Student Dialogues", 685, LESSONS)
