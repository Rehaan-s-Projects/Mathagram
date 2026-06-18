#!/usr/bin/env python3
"""Burmese Unit 54 — Formal Letters (lessons 790-804)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "When to Write Formal Letters",
     "body_html": r"""<p>Formal letters are for: government applications, school admissions, job applications, complaints, official invitations, business proposals. Use proper structure and respectful register.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Formal letters use respectful register.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Formal contexts: ", "options": ["family chat", "government, jobs, official biz", "social media", "casual texts"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Letter: ___ ပို့.", "answer": "စာ"},
         {"type": "true-false", "question": "Formal Burmese letters can be casual.", "correctAnswer": False},
         {"type": "true-false", "question": "Job applications need formal style.", "correctAnswer": True}]},
    {"title": "Letter Structure",
     "body_html": r"""<p>Standard parts:</p><ol><li>Date (top right or top left)</li><li>Recipient address</li><li>Salutation</li><li>Body</li><li>Closing phrase</li><li>Sender's name and signature</li><li>Attachments noted</li></ol>""",
     "exercises": [
         {"type": "true-false", "question": "Standard letters include 7 parts.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Date placement: ", "options": ["bottom", "top right or left", "middle", "no date"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Salutation: ___ ပြုပါသော.", "answer": "လေးစား"},
         {"type": "true-false", "question": "Sender's signature appears at the end.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Attachments: ___ စာများ.", "answer": "ပူးတွဲ"}]},
    {"title": "Salutations",
     "body_html": r"""<ul><li>"လေးစားရပါသော ___ ရှင့်" — \"Dear ___\" (formal)</li><li>"ဦးလေးစားအပ်ပါသော ___" — even more honorific</li><li>"ကြုံရတဲ့သူ ___" — \"To the recipient\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Dear (formal): ___ စားရပါသော.", "answer": "လေး"},
         {"type": "multiple-choice", "question": "Even more honorific: ", "options": ["ဦးလေးစားအပ်", "ကြုံရတဲ့သူ", "လေးစားရပါသော", "ရှင့်"], "correctIndex": 0},
         {"type": "true-false", "question": "Letters often address the reader by title.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Address particle: ___.", "answer": "ရှင့်"},
         {"type": "true-false", "question": "Formal letters drop salutations.", "correctAnswer": False}]},
    {"title": "Opening Lines",
     "body_html": r"""<ul><li>"ဦးစွာ မိမိ ___ ထံ စာရေးရပါသည်။" — \"First, I write to ___.\"</li><li>"ကျွန်တော်/ကျွန်မ ___ မှ ___ အကြောင်း ဆက်သွယ်ပါသည်။"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "First: ___ စွာ.", "answer": "ဦး"},
         {"type": "multiple-choice", "question": "Self (male polite): ", "options": ["ကျွန်တော်", "ကျွန်မ", "ငါ", "မင်း"], "correctIndex": 0},
         {"type": "true-false", "question": "ကျွန်မ is female polite \"I.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Contact: ဆက်___.", "answer": "သွယ်"},
         {"type": "true-false", "question": "Letters often start with self-introduction.", "correctAnswer": True}]},
    {"title": "Stating Purpose",
     "body_html": r"""<ul><li>"___ နှင့်ပတ်သက်၍ စာရေးပါသည်။" — \"I'm writing about ___.\"</li><li>"ထိုသို့ဆိုသောကြောင့်" — \"Therefore...\"</li><li>"လိုအပ်ချက် အဖြစ်" — \"As a need...\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Regarding: ___ ပတ်သက်၍.", "answer": "နှင့်"},
         {"type": "multiple-choice", "question": "Therefore: ", "options": ["ထိုသို့ဆိုသောကြောင့်", "လိုအပ်ချက်", "ဦးစွာ", "ဆက်သွယ်"], "correctIndex": 0},
         {"type": "true-false", "question": "Stating purpose early is good practice.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Need: ___ အပ်ချက်.", "answer": "လို"},
         {"type": "true-false", "question": "Burmese letters never have a clear purpose.", "correctAnswer": False}]},
    {"title": "Body Vocabulary",
     "body_html": r"""<ul><li>တင်ပြ — to submit / present</li><li>ထောက်ခံ — to support</li><li>လျှောက်ထား — to apply</li><li>တောင်းဆို — to request</li><li>ဖြည့်စွက် — to add / supplement</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Submit: ___.", "answer": "တင်ပြ"},
         {"type": "multiple-choice", "question": "Apply: ", "options": ["တင်ပြ", "လျှောက်ထား", "ထောက်ခံ", "ဖြည့်စွက်"], "correctIndex": 1},
         {"type": "true-false", "question": "တောင်းဆို means \"to request.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Support: ___ ခံ.", "answer": "ထောက်"},
         {"type": "fill-blank", "question": "Add: ___ စွက်.", "answer": "ဖြည့်"}]},
    {"title": "Closing Phrases",
     "body_html": r"""<ul><li>"လေးစားစွာဖြင့်" — \"Sincerely\"</li><li>"ကျေးဇူးပြုပါ" — \"Please / kindly\"</li><li>"ဆွေးနွေးနိုင်ပါသည်။" — \"I'm available to discuss.\"</li><li>"တုံ့ပြန်ချက် မျှော်လင့်ပါသည်။" — \"I look forward to your reply.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sincerely: ___ စွာဖြင့်.", "answer": "လေးစား"},
         {"type": "multiple-choice", "question": "Reply: ", "options": ["တုံ့ပြန်ချက်", "မျှော်လင့်", "ကျေးဇူးပြု", "ဆွေးနွေး"], "correctIndex": 0},
         {"type": "true-false", "question": "မျှော်လင့် means \"to look forward.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Available to discuss: ___ ပါသည်.", "answer": "ဆွေးနွေးနိုင်"},
         {"type": "fill-blank", "question": "Kindly: ___ ပြုပါ.", "answer": "ကျေးဇူး"}]},
    {"title": "Cover Letters",
     "body_html": r"""<p>For job applications:</p><ol><li>Position you're applying for.</li><li>Brief background and skills.</li><li>Why you're interested.</li><li>Attached CV reference.</li></ol>""",
     "exercises": [
         {"type": "fill-blank", "question": "Cover letter: ___ ပုံစံ စာ.", "answer": "လျှောက်လွှာ"},
         {"type": "multiple-choice", "question": "Cover letter content: ", "options": ["random", "position, skills, interest, CV mention", "only thanks", "menu"], "correctIndex": 1},
         {"type": "true-false", "question": "Mention attached CV in cover letter.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Position: ___ ထူး.", "answer": "ရာ"},
         {"type": "true-false", "question": "Cover letters should be informal slang.", "correctAnswer": False}]},
    {"title": "Complaint Letters",
     "body_html": r"""<ul><li>"တိုင်ကြားလွှာ" — complaint letter</li><li>State problem clearly.</li><li>Provide evidence (dates, names).</li><li>Request specific resolution.</li><li>Stay polite throughout.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Complaint letter: ___ ကြားလွှာ.", "answer": "တိုင်"},
         {"type": "multiple-choice", "question": "Stay: ", "options": ["angry", "polite throughout", "vague", "loud"], "correctIndex": 1},
         {"type": "true-false", "question": "Provide evidence in complaints.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Resolution / response: ___ ပြန်ချက်.", "answer": "တုံ့"},
         {"type": "true-false", "question": "Complaint letters can be threatening.", "correctAnswer": False}]},
    {"title": "Application Letters",
     "body_html": r"""<ul><li>"လျှောက်လွှာ" — application</li><li>"စာရင်းသွင်း" — to register</li><li>Schools, government services, scholarships use this format.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Application: ___.", "answer": "လျှောက်လွှာ"},
         {"type": "multiple-choice", "question": "Register: ", "options": ["စာရင်းသွင်း", "လျှောက်လွှာ", "တိုင်ကြား", "တင်ပြ"], "correctIndex": 0},
         {"type": "true-false", "question": "Scholarships use formal application letters.", "correctAnswer": True},
         {"type": "fill-blank", "question": "School: ___.", "answer": "ကျောင်း"},
         {"type": "true-false", "question": "Government services don't use formal letters.", "correctAnswer": False}]},
    {"title": "Invitation Letters",
     "body_html": r"""<ul><li>"ဖိတ်ခေါ်လွှာ" — invitation letter</li><li>"___ သို့ ကြိုဆိုပါသည်။" — \"Welcome to ___\"</li><li>State date, time, location, dress code.</li><li>RSVP request.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Invitation letter: ___ ခေါ်လွှာ.", "answer": "ဖိတ်"},
         {"type": "multiple-choice", "question": "Welcome: ", "options": ["ကြိုဆို", "ဖိတ်ခေါ်", "ပြန်ပေး", "လိုအပ်"], "correctIndex": 0},
         {"type": "true-false", "question": "RSVP requests are common.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Date: ___ စွဲ.", "answer": "နေ့"},
         {"type": "true-false", "question": "Invitation letters should omit date.", "correctAnswer": False}]},
    {"title": "Email vs Paper",
     "body_html": r"""<p>Modern Burmese formal communication often uses email, but printed letters with seals/stamps are still required for official documents (government, courts, large transactions).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Government documents often need printed letters.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Modern formal channel: ", "options": ["telegraph only", "email common, paper for official", "WhatsApp only", "no formal channels"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Stamp: ___.", "answer": "တံဆိပ်"},
         {"type": "true-false", "question": "Burmese seals are still legally important.", "correctAnswer": True},
         {"type": "true-false", "question": "Email has fully replaced paper letters.", "correctAnswer": False}]},
    {"title": "Common Errors",
     "body_html": r"""<p>Avoid: casual particles in formal writing, mixing English/Burmese without need, using informal pronouns (မင်း, ငါ), using slang.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Casual \"you\": ___.", "answer": "မင်း"},
         {"type": "multiple-choice", "question": "Avoid in formal writing: ", "options": ["honorifics", "casual pronouns and slang", "polite particles", "official titles"], "correctIndex": 1},
         {"type": "true-false", "question": "Slang fits formal letters.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Casual \"I\": ___.", "answer": "ငါ"},
         {"type": "true-false", "question": "Mixing English unnecessarily is bad in formal writing.", "correctAnswer": True}]},
    {"title": "Practice: Sample Application",
     "body_html": r"""<p>Skeleton:</p><p><em>လေးစားရပါသော ဦးစီးအရာရှိ ရှင့်,<br>ကျွန်တော် (နာမည်) ပါ။ ___ ရာထူးကို လျှောက်ထားလိုသဖြင့် ဤလျှောက်လွှာကို တင်ပြပါသည်။ ပူးတွဲစာများကို စစ်ဆေးပေးပါ။<br>လေးစားစွာဖြင့်,<br>(နာမည်)</em></p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Officer: ဦးစီး ___ ရှိ.", "answer": "အရာ"},
         {"type": "multiple-choice", "question": "Position to apply for: ", "options": ["ရာထူး", "လျှောက်လွှာ", "ပူးတွဲ", "ဦးစီး"], "correctIndex": 0},
         {"type": "true-false", "question": "Attach supporting documents (\"ပူးတွဲစာများ\").", "correctAnswer": True},
         {"type": "fill-blank", "question": "Examine: ___ ဆေး.", "answer": "စစ်"},
         {"type": "true-false", "question": "Closing should match the formal tone.", "correctAnswer": True}]},
    {"title": "Formal Letters Checkpoint",
     "body_html": r"""<p>Recap of Unit 54:</p><ul><li>Structure: date, address, salutation, body, closing, signature.</li><li>Salutations: လေးစားရပါသော ___ ရှင့်.</li><li>Closings: လေးစားစွာဖြင့်, ကျေးဇူးပြုပါ.</li><li>Letter types: cover (လျှောက်လွှာ), complaint (တိုင်ကြားလွှာ), invitation (ဖိတ်ခေါ်လွှာ).</li><li>Avoid casual pronouns (မင်း, ငါ) and slang.</li><li>Government docs still need printed letters with seal.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Application: ___.", "answer": "လျှောက်လွှာ"},
         {"type": "multiple-choice", "question": "Closing: ", "options": ["လေးစားစွာဖြင့်", "မင်္ဂလာပါ", "ဆာတယ်", "မိုက်"], "correctIndex": 0},
         {"type": "true-false", "question": "Burmese seals/stamps still matter legally.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Reply: ___ ပြန်ချက်.", "answer": "တုံ့"},
         {"type": "fill-blank", "question": "Sign: ___.", "answer": "လက်မှတ်"},
         {"type": "true-false", "question": "Slang fits formal letters.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Invitation letter: ___ ခေါ်လွှာ.", "answer": "ဖိတ်"}]},
]

if __name__ == "__main__":
    render_unit(54, "Burmese Formal Letters", 790, LESSONS)
