#!/usr/bin/env python3
"""Burmese Unit 44 — Law & Legal Vocabulary (lessons 640-654)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Legal System Overview",
     "body_html": r"""<p>Myanmar's law system is civil-law tradition with British colonial influence (1885–1948). Codified in: Penal Code, Civil Procedure Code, Contract Act, etc. Customary law applies in some ethnic communities.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Penal: ___ ဥပဒေ.", "answer": "ပြစ်မှု"},
         {"type": "true-false", "question": "British colonial law influenced Myanmar's legal system.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Customary law applies in:", "options": ["all areas", "no areas", "some ethnic communities", "courts only"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Civil procedure: ___.", "answer": "ဆိုင်ရာဥပဒေ"},
         {"type": "true-false", "question": "Myanmar uses common-law tradition primarily.", "correctAnswer": False}]},
    {"title": "Court Hierarchy",
     "body_html": r"""<ul><li>တရားရုံးချုပ် — Supreme Court</li><li>တိုင်းတရားရုံး — Region/State Court</li><li>ခရိုင်တရားရုံး — District Court</li><li>မြို့နယ်တရားရုံး — Township Court</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Supreme Court: တရားရုံး ___.", "answer": "ချုပ်"},
         {"type": "multiple-choice", "question": "District Court: ", "options": ["တရားရုံးချုပ်", "ခရိုင်တရားရုံး", "မြို့နယ်တရားရုံး", "တိုင်းတရားရုံး"], "correctIndex": 1},
         {"type": "true-false", "question": "Township courts are the lowest level.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Region/State court: ___ တရားရုံး.", "answer": "တိုင်း"},
         {"type": "true-false", "question": "There is only one level of court in Myanmar.", "correctAnswer": False}]},
    {"title": "Lawyer Vocabulary",
     "body_html": r"""<ul><li>တရားလွှတ်တော်ရှေ့နေ — High Court advocate</li><li>ရှေ့နေ — lawyer</li><li>တရားခံ — defendant</li><li>တရားလို — plaintiff</li><li>တရားသူကြီး — judge</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Lawyer: ___.", "answer": "ရှေ့နေ"},
         {"type": "multiple-choice", "question": "Judge: ", "options": ["တရားခံ", "တရားလို", "တရားသူကြီး", "ရှေ့နေ"], "correctIndex": 2},
         {"type": "true-false", "question": "တရားခံ means \"defendant.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Plaintiff: တရား ___.", "answer": "လို"},
         {"type": "fill-blank", "question": "High Court advocate: တရားလွှတ်တော် ___.", "answer": "ရှေ့နေ"}]},
    {"title": "Criminal Procedure",
     "body_html": r"""<ul><li>ဖမ်းဆီး — to arrest</li><li>စုံစမ်း — to investigate</li><li>စွဲချက်တင် — to file charges</li><li>တရားရင်ဆိုင် — to face trial</li><li>ပြစ်ဒဏ်ချ — to sentence</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Investigate: ___ စမ်း.", "answer": "စုံ"},
         {"type": "multiple-choice", "question": "File charges: ", "options": ["ဖမ်းဆီး", "စုံစမ်း", "စွဲချက်တင်", "ပြစ်ဒဏ်ချ"], "correctIndex": 2},
         {"type": "true-false", "question": "ပြစ်ဒဏ်ချ means \"to sentence.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Arrest: ___ ဆီး.", "answer": "ဖမ်း"},
         {"type": "fill-blank", "question": "Trial: တရား ___ ဆိုင်.", "answer": "ရင်"}]},
    {"title": "Civil Procedure",
     "body_html": r"""<ul><li>တရားစွဲ — to file a lawsuit</li><li>တောင်းခံ — to claim / demand</li><li>သက်သေခံ — evidence / testimony</li><li>စီရင်ချက် — verdict / decision</li><li>အယူခံ — appeal</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "File lawsuit: တရား ___.", "answer": "စွဲ"},
         {"type": "multiple-choice", "question": "Evidence: ", "options": ["တောင်းခံ", "သက်သေခံ", "စီရင်ချက်", "အယူခံ"], "correctIndex": 1},
         {"type": "true-false", "question": "အယူခံ means \"appeal.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Verdict: စီရင် ___.", "answer": "ချက်"},
         {"type": "fill-blank", "question": "Claim: ___ ခံ.", "answer": "တောင်း"}]},
    {"title": "Common Crimes",
     "body_html": r"""<ul><li>ခိုးယူ — theft</li><li>လုယက် — robbery</li><li>သတ်ဖြတ် — murder</li><li>လိမ်လည် — fraud</li><li>လာဘ်ပေး — bribery</li><li>မူးယစ် — drug-related</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Theft: ___ ယူ.", "answer": "ခိုး"},
         {"type": "multiple-choice", "question": "Bribery: ", "options": ["ခိုးယူ", "လိမ်လည်", "လာဘ်ပေး", "မူးယစ်"], "correctIndex": 2},
         {"type": "true-false", "question": "လိမ်လည် means \"fraud.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Murder: ___ ဖြတ်.", "answer": "သတ်"},
         {"type": "fill-blank", "question": "Drug-related: ___ ယစ်.", "answer": "မူး"}]},
    {"title": "Punishments",
     "body_html": r"""<ul><li>ထောင်ဒဏ် — prison sentence</li><li>ငွေဒဏ် — fine</li><li>သေဒဏ် — death penalty</li><li>စာအုပ်ဖြုတ် — to expunge / cancel record</li><li>ကာလအတွင်း — within (time period)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Fine: ___ ဒဏ်.", "answer": "ငွေ"},
         {"type": "multiple-choice", "question": "Prison sentence: ", "options": ["ထောင်ဒဏ်", "ငွေဒဏ်", "သေဒဏ်", "ကာလ"], "correctIndex": 0},
         {"type": "true-false", "question": "သေဒဏ် means \"death penalty.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Within: ___ အတွင်း.", "answer": "ကာလ"},
         {"type": "true-false", "question": "Punishments include only fines.", "correctAnswer": False}]},
    {"title": "Property Law",
     "body_html": r"""<ul><li>ပိုင်ဆိုင်မှု — ownership</li><li>ပိုင်ရှင် — owner</li><li>လွှဲပြောင်း — to transfer</li><li>အပ်နှံ — to deposit / entrust</li><li>တရားဝင် — legitimate / legal</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Owner: ___ ရှင်.", "answer": "ပိုင်"},
         {"type": "multiple-choice", "question": "Transfer: ", "options": ["လွှဲပြောင်း", "အပ်နှံ", "တရားဝင်", "ပိုင်ဆိုင်မှု"], "correctIndex": 0},
         {"type": "true-false", "question": "တရားဝင် means \"legitimate.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Ownership: ပိုင်ဆိုင် ___.", "answer": "မှု"},
         {"type": "fill-blank", "question": "Deposit / entrust: ___ နှံ.", "answer": "အပ်"}]},
    {"title": "Contracts",
     "body_html": r"""<ul><li>စာချုပ် — contract</li><li>သဘောတူ — to agree</li><li>ပျက်ကွက် — to default / breach</li><li>လျော်ကြေး — compensation</li><li>စည်းကမ်း — terms / conditions</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Contract: ___.", "answer": "စာချုပ်"},
         {"type": "multiple-choice", "question": "Compensation: ", "options": ["သဘောတူ", "ပျက်ကွက်", "လျော်ကြေး", "စည်းကမ်း"], "correctIndex": 2},
         {"type": "true-false", "question": "ပျက်ကွက် means \"to breach.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Terms: စည်း ___.", "answer": "ကမ်း"},
         {"type": "fill-blank", "question": "To agree: သဘော ___.", "answer": "တူ"}]},
    {"title": "Family Law",
     "body_html": r"""<ul><li>လက်ထပ် — to marry</li><li>ကွာရှင်း — to divorce</li><li>ကလေးထိန်းသိမ်းမှု — child custody</li><li>အမွေ — inheritance</li><li>ပြောင်းရွှေ့ — to migrate / relocate</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Marry: လက် ___.", "answer": "ထပ်"},
         {"type": "multiple-choice", "question": "Inheritance: ", "options": ["လက်ထပ်", "ကွာရှင်း", "အမွေ", "ပြောင်းရွှေ့"], "correctIndex": 2},
         {"type": "true-false", "question": "ကွာရှင်း means \"to divorce.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Child custody: ကလေး ___ မှု.", "answer": "ထိန်းသိမ်း"},
         {"type": "true-false", "question": "Family law covers marriage and divorce.", "correctAnswer": True}]},
    {"title": "Constitutional Rights",
     "body_html": r"""<ul><li>လွတ်လပ်စွာ ပြောဆိုခွင့် — freedom of speech</li><li>စည်းရုံးခွင့် — freedom of assembly</li><li>ဘာသာရေး လွတ်လပ်ခွင့် — religious freedom</li><li>တန်းတူရည်တူ — equality</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Freedom of speech: လွတ်လပ်စွာ ___ ဆိုခွင့်.", "answer": "ပြော"},
         {"type": "multiple-choice", "question": "Equality: ", "options": ["စည်းရုံးခွင့်", "ဘာသာရေး", "တန်းတူရည်တူ", "လွတ်လပ်စွာ"], "correctIndex": 2},
         {"type": "true-false", "question": "ဘာသာရေး လွတ်လပ်ခွင့် means \"religious freedom.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Assembly: စည်း ___.", "answer": "ရုံးခွင့်"},
         {"type": "true-false", "question": "Constitutional rights protect citizens.", "correctAnswer": True}]},
    {"title": "Police Interaction",
     "body_html": r"""<ul><li>ရဲ — police</li><li>ရဲစခန်း — police station</li><li>တုတ်ထမ်း — police baton</li><li>"အကူအညီ ပေးပါ။" — \"Please help.\"</li><li>ID: မှတ်ပုံတင် — national ID</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Police: ___.", "answer": "ရဲ"},
         {"type": "multiple-choice", "question": "ID card: ", "options": ["ရဲ", "မှတ်ပုံတင်", "တုတ်ထမ်း", "ရဲစခန်း"], "correctIndex": 1},
         {"type": "true-false", "question": "ရဲစခန်း means \"police station.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Please help: အကူအညီ ___ ပါ.", "answer": "ပေး"},
         {"type": "true-false", "question": "Carrying ID is required in Myanmar.", "correctAnswer": True}]},
    {"title": "Legal Documents",
     "body_html": r"""<ul><li>စာရွက်စာတမ်း — documents</li><li>လက်မှတ် — signature</li><li>တံဆိပ် — seal / stamp</li><li>သက်သေထောက်ခံ — to certify</li><li>မိတ္တူ — copy</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Stamp: ___.", "answer": "တံဆိပ်"},
         {"type": "multiple-choice", "question": "Copy: ", "options": ["လက်မှတ်", "မိတ္တူ", "တံဆိပ်", "သက်သေထောက်ခံ"], "correctIndex": 1},
         {"type": "true-false", "question": "Documents in Myanmar often need stamps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Certify: သက်သေ ___ ခံ.", "answer": "ထောက်"},
         {"type": "fill-blank", "question": "Signature: ___.", "answer": "လက်မှတ်"}]},
    {"title": "Practice: Legal Terms",
     "body_html": r"""<p>Match terms:</p><ol><li>တရားသူကြီး = judge</li><li>ထောင်ဒဏ် = prison sentence</li><li>လက်ထပ် = to marry</li><li>လျော်ကြေး = compensation</li><li>လိမ်လည် = fraud</li></ol>""",
     "exercises": [
         {"type": "fill-blank", "question": "Judge: တရား ___ ကြီး.", "answer": "သူ"},
         {"type": "multiple-choice", "question": "Marry: ", "options": ["ထောင်ဒဏ်", "လက်ထပ်", "လိမ်လည်", "လျော်ကြေး"], "correctIndex": 1},
         {"type": "true-false", "question": "လျော်ကြေး means \"compensation.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Fraud: လိမ် ___.", "answer": "လည်"},
         {"type": "fill-blank", "question": "Prison sentence: ___ ဒဏ်.", "answer": "ထောင်"}]},
    {"title": "Law Checkpoint",
     "body_html": r"""<p>Recap of Unit 44:</p><ul><li>Civil-law tradition with British colonial influence.</li><li>Court hierarchy: Township → District → Region → Supreme.</li><li>Players: ရှေ့နေ (lawyer), တရားသူကြီး (judge), တရားခံ (defendant), တရားလို (plaintiff).</li><li>Crime types: ခိုးယူ (theft), လုယက် (robbery), လိမ်လည် (fraud).</li><li>Contracts: စာချုပ်; signature: လက်မှတ်; seal: တံဆိပ်.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Lawyer: ___.", "answer": "ရှေ့နေ"},
         {"type": "multiple-choice", "question": "Highest court: ", "options": ["Township", "District", "Supreme", "Region"], "correctIndex": 2},
         {"type": "true-false", "question": "သေဒဏ် means \"death penalty.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Defendant: တရား ___.", "answer": "ခံ"},
         {"type": "fill-blank", "question": "Marriage: လက် ___.", "answer": "ထပ်"},
         {"type": "true-false", "question": "Documents often require stamps in Myanmar.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Bribery: ___ ပေး.", "answer": "လာဘ်"}]},
]

if __name__ == "__main__":
    render_unit(44, "Burmese Law & Legal Vocabulary", 640, LESSONS)
