#!/usr/bin/env python3
"""Burmese Unit 41 — Newspaper Reading (lessons 595-609)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Major Burmese Newspapers",
     "body_html": r"""<ul><li>Myanmar Alin (\"Light of Myanmar\") — state daily</li><li>Kyemon (\"The Mirror\") — state daily</li><li>The Voice — independent</li><li>7Day News — popular weekly</li><li>The Irrawaddy — exile / international focus</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "\"Light of Myanmar\": Myanmar ___.", "answer": "Alin"},
         {"type": "multiple-choice", "question": "Independent paper:", "options": ["Myanmar Alin", "Kyemon", "The Voice", "Government Gazette"], "correctIndex": 2},
         {"type": "true-false", "question": "The Irrawaddy is exile-based.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"The Mirror\": ___.", "answer": "Kyemon"},
         {"type": "true-false", "question": "Myanmar has only one newspaper.", "correctAnswer": False}]},
    {"title": "Newspaper Layout",
     "body_html": r"""<p>Typical Burmese newspaper layout:</p><ul><li>Header with date, edition.</li><li>Front page: top political/national news.</li><li>Inside: international, local, business, sports, opinion.</li><li>Back page: classifieds, ads, entertainment.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Front page typically has top political/national news.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Classifieds usually appear:", "options": ["front page", "back page", "middle", "never printed"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Date: ___.", "answer": "နေ့စွဲ"},
         {"type": "true-false", "question": "Sports has its own section.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Opinion: ___.", "answer": "အမြင်"}]},
    {"title": "Headline Conventions",
     "body_html": r"""<p>Burmese headlines:</p><ul><li>Often verbless or condensed.</li><li>Use loanwords for international concepts (\"COVID\" \"GDP\").</li><li>Quote sources frequently.</li><li>Length: a single line or short two-liner.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Headlines often verbless.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Loanwords appear in headlines:", "options": ["never", "rarely", "frequently for international concepts", "only for politics"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Headline: ___ ခေါင်းစဉ်.", "answer": "သတင်း"},
         {"type": "true-false", "question": "Sources are typically quoted.", "correctAnswer": True},
         {"type": "true-false", "question": "Headlines run several paragraphs.", "correctAnswer": False}]},
    {"title": "Reading the Lead Paragraph",
     "body_html": r"""<p>The lead (ဦးဆောင်စာပိုဒ်) answers the 5 W's: who, what, when, where, why.</p><p>Burmese leads can be longer than English ones, but should give the gist.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Lead paragraph: ___ စာပိုဒ်.", "answer": "ဦးဆောင်"},
         {"type": "multiple-choice", "question": "5 W's:", "options": ["who/what/when/where/why", "who/what/which/where/whose", "who/whom/whose/where/when", "all of these"], "correctIndex": 0},
         {"type": "true-false", "question": "Burmese leads can be longer than English.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Who: ___ သူ.", "answer": "ဘယ်"},
         {"type": "true-false", "question": "Lead should give the gist.", "correctAnswer": True}]},
    {"title": "Quoting Sources",
     "body_html": r"""<p>Quotation patterns:</p><ul><li>"___ လို့ ___က ပြောတယ်။" — \"___ said ___.\"</li><li>"___ အရ" — \"according to ___.\"</li><li>"အရင်းအမြစ်" — source.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "\"According to\": ___ အရ.", "answer": "..."},
         {"type": "multiple-choice", "question": "Source: ", "options": ["သတင်း", "အရင်းအမြစ်", "ခေါင်းစဉ်", "စာပိုဒ်"], "correctIndex": 1},
         {"type": "true-false", "question": "ပြောတယ် means \"said.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Said: ___ တယ်.", "answer": "ပြော"},
         {"type": "true-false", "question": "Source attribution is unimportant in journalism.", "correctAnswer": False}]},
    {"title": "Date & Place Bylines",
     "body_html": r"""<p>"YANGON, March 5 — ..." style is common. Format in Burmese:</p><ul><li>City | date | story body.</li><li>Or: \"___ မြို့မှ — story...\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "City marker: ___ မှ.", "answer": "မြို့"},
         {"type": "multiple-choice", "question": "Byline includes:", "options": ["city + date", "only date", "only city", "footnote"], "correctIndex": 0},
         {"type": "true-false", "question": "Bylines are typical in Burmese newspapers.", "correctAnswer": True},
         {"type": "fill-blank", "question": "March (Burmese): မတ် ___.", "answer": "လ"},
         {"type": "true-false", "question": "Bylines mark where reporting was done.", "correctAnswer": True}]},
    {"title": "Common News Topics",
     "body_html": r"""<ul><li>နိုင်ငံရေး — politics</li><li>စီးပွားရေး — economy</li><li>လူမှုရေး — society</li><li>ပညာရေး — education</li><li>ကျန်းမာရေး — health</li><li>အားကစား — sports</li><li>ရာသီဥတု — weather</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Politics: ___.", "answer": "နိုင်ငံရေး"},
         {"type": "multiple-choice", "question": "Sports: ", "options": ["စီးပွားရေး", "ပညာရေး", "အားကစား", "ရာသီဥတု"], "correctIndex": 2},
         {"type": "true-false", "question": "ပညာရေး means \"education.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Health: ___ ရေး.", "answer": "ကျန်းမာ"},
         {"type": "fill-blank", "question": "Weather: ___ ဥတု.", "answer": "ရာသီ"}]},
    {"title": "Politics Vocabulary",
     "body_html": r"""<ul><li>အစိုးရ — government</li><li>ပါတီ — political party</li><li>ရွေးကောက်ပွဲ — election</li><li>ရွေးချယ် — to choose / elect</li><li>သမ္မတ — president</li><li>ဝန်ကြီး — minister</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Government: ___.", "answer": "အစိုးရ"},
         {"type": "multiple-choice", "question": "President: ", "options": ["ပါတီ", "သမ္မတ", "ဝန်ကြီး", "အစိုးရ"], "correctIndex": 1},
         {"type": "true-false", "question": "ရွေးကောက်ပွဲ means \"election.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Minister: ___ ကြီး.", "answer": "ဝန်"},
         {"type": "fill-blank", "question": "Party: ___.", "answer": "ပါတီ"}]},
    {"title": "Economy Vocabulary",
     "body_html": r"""<ul><li>ငွေကြေး — currency / finance</li><li>ပို့ကုန် — exports</li><li>သွင်းကုန် — imports</li><li>ထုတ်လုပ်မှု — production</li><li>ဈေးကွက် — market</li><li>လုပ်အား — labor</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Exports: ___.", "answer": "ပို့ကုန်"},
         {"type": "multiple-choice", "question": "Imports: ", "options": ["ပို့ကုန်", "သွင်းကုန်", "ဈေးကွက်", "လုပ်အား"], "correctIndex": 1},
         {"type": "true-false", "question": "ထုတ်လုပ်မှု means \"production.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Currency: ___ ကြေး.", "answer": "ငွေ"},
         {"type": "fill-blank", "question": "Market: ___.", "answer": "ဈေးကွက်"}]},
    {"title": "Disaster & Crisis Vocabulary",
     "body_html": r"""<ul><li>ဘေး — disaster</li><li>လှုပ်ခတ် — earthquake</li><li>ရေကြီး — flood</li><li>မိုးကြီး — heavy rain</li><li>သဘာဝဘေး — natural disaster</li><li>ဆုံးရှုံး — to lose / be destroyed</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Earthquake: ___ ခတ်.", "answer": "လှုပ်"},
         {"type": "multiple-choice", "question": "Flood: ", "options": ["မိုးကြီး", "ရေကြီး", "ဆုံးရှုံး", "သဘာဝဘေး"], "correctIndex": 1},
         {"type": "true-false", "question": "သဘာဝဘေး means \"natural disaster.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Disaster: ___.", "answer": "ဘေး"},
         {"type": "fill-blank", "question": "To be destroyed: ___ ရှုံး.", "answer": "ဆုံး"}]},
    {"title": "International Vocabulary",
     "body_html": r"""<ul><li>နိုင်ငံခြား — foreign country</li><li>ကုလသမဂ္ဂ — UN</li><li>သံအမတ် — ambassador</li><li>သဘောတူညီချက် — agreement</li><li>စစ်တပ် — military</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "UN: ___ သမဂ္ဂ.", "answer": "ကုလ"},
         {"type": "multiple-choice", "question": "Ambassador: ", "options": ["စစ်တပ်", "သံအမတ်", "ကုလသမဂ္ဂ", "နိုင်ငံခြား"], "correctIndex": 1},
         {"type": "true-false", "question": "နိုင်ငံခြား means \"foreign country.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Military: ___ တပ်.", "answer": "စစ်"},
         {"type": "fill-blank", "question": "Agreement: သဘော___ ချက်.", "answer": "တူညီ"}]},
    {"title": "Editorial Style",
     "body_html": r"""<p>Editorials (ထင်မြင်ချက်):</p><ul><li>Personal voice OK.</li><li>Argumentative structure: claim → evidence → conclusion.</li><li>End with implications or call-to-action.</li><li>Tone: respectful even when critical.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Editorial: ___ မြင်ချက်.", "answer": "ထင်"},
         {"type": "multiple-choice", "question": "Editorial structure:", "options": ["random", "claim → evidence → conclusion", "no structure", "only opinion"], "correctIndex": 1},
         {"type": "true-false", "question": "Editorials may end with call-to-action.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tone is respectful even when ___.", "answer": "critical"},
         {"type": "true-false", "question": "Personal voice is forbidden in editorials.", "correctAnswer": False}]},
    {"title": "Reading Tips",
     "body_html": r"""<ul><li>Start with the headline and lead paragraph for the gist.</li><li>Skim the rest, focusing on quotes and figures.</li><li>Note unfamiliar words; build vocabulary log.</li><li>Read articles on familiar topics first.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Start with headline and lead.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Reading order:", "options": ["last paragraph first", "skim, then deep-read", "deep-read every word", "skip ahead randomly"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Vocabulary ___.", "answer": "log"},
         {"type": "true-false", "question": "Read articles on familiar topics first.", "correctAnswer": True},
         {"type": "true-false", "question": "Reading skills don't transfer between languages.", "correctAnswer": False}]},
    {"title": "Practice: Read a Headline",
     "body_html": r"""<p>Sample: \"အကြီးအကဲ မြို့တော်မှာ စီမံကိန်း ၃ ခု တင်လိုက်ပြီ။\"</p><p>"Leader announces 3 projects in capital city."</p><p>Decode: အကြီးအကဲ (leader) | မြို့တော် (capital) | စီမံကိန်း (project) | ၃ ခု (3) | တင်လိုက်ပြီ (announced).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Leader: ___ အကဲ.", "answer": "အကြီး"},
         {"type": "multiple-choice", "question": "Capital city: ", "options": ["မြို့တော်", "ရွာ", "စိမံ", "လုပ်ငန်း"], "correctIndex": 0},
         {"type": "true-false", "question": "စီမံကိန်း means \"project.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "3 (numeral): ___.", "answer": "၃"},
         {"type": "true-false", "question": "တင်လိုက်ပြီ implies recent action (announced).", "correctAnswer": True}]},
    {"title": "Newspaper Reading Checkpoint",
     "body_html": r"""<p>Recap of Unit 41:</p><ul><li>Major papers: Myanmar Alin (state), The Voice (independent), Irrawaddy (exile).</li><li>Headlines often verbless, packed with key words.</li><li>Lead paragraph answers the 5 W's.</li><li>Sections: politics, economy, society, sports, weather.</li><li>Reading strategy: skim headline + lead, then deep-read.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Politics: ___ ရေး.", "answer": "နိုင်ငံ"},
         {"type": "multiple-choice", "question": "5 W's are answered in:", "options": ["headline only", "lead paragraph", "footnote", "ad section"], "correctIndex": 1},
         {"type": "true-false", "question": "Source attribution is common.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Election: ___ ပွဲ.", "answer": "ရွေးကောက်"},
         {"type": "fill-blank", "question": "Disaster: ___.", "answer": "ဘေး"},
         {"type": "true-false", "question": "Editorials never have personal voice.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Production: ___ မှု.", "answer": "ထုတ်လုပ်"}]},
]

if __name__ == "__main__":
    render_unit(41, "Burmese Newspaper Reading", 595, LESSONS)
