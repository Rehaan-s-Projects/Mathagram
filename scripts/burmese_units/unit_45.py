#!/usr/bin/env python3
"""Burmese Unit 45 — Banking & Finance (lessons 655-669)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Banking System Overview",
     "body_html": r"""<p>Major Burmese banks include KBZ Bank, AYA Bank, CB Bank, Yoma Bank. Most operate in Burmese with English option for expats. Limited international wire transfers due to sanctions.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Bank: ___.", "answer": "ဘဏ်"},
         {"type": "multiple-choice", "question": "Major Myanmar bank:", "options": ["KBZ", "Wells Fargo", "Chase", "HSBC India"], "correctIndex": 0},
         {"type": "true-false", "question": "International wires are limited due to sanctions.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sanctions: ___ ပိတ်ဆို့မှု.", "answer": "ဒဏ်ခတ်"},
         {"type": "true-false", "question": "Most Burmese banks operate only in English.", "correctAnswer": False}]},
    {"title": "Account Types",
     "body_html": r"""<ul><li>ငွေစုစာရင်း — savings account</li><li>လက်ရှိစာရင်း — current account</li><li>သုံးစွဲမှုကတ် — credit/debit card</li><li>လစာရှင်စာရင်း — payroll account</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Savings: ငွေ ___ စာရင်း.", "answer": "စု"},
         {"type": "multiple-choice", "question": "Credit/debit card: ", "options": ["ငွေစုစာရင်း", "လက်ရှိစာရင်း", "သုံးစွဲမှုကတ်", "လစာရှင်စာရင်း"], "correctIndex": 2},
         {"type": "true-false", "question": "လစာရှင်စာရင်း is a payroll account.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Current account: ___ ရှိ စာရင်း.", "answer": "လက်"},
         {"type": "fill-blank", "question": "Account: ___ ရင်း.", "answer": "စာ"}]},
    {"title": "Common Transactions",
     "body_html": r"""<ul><li>ငွေသွင်း — to deposit</li><li>ငွေထုတ် — to withdraw</li><li>ငွေလွှဲ — to transfer</li><li>ဘဏ်ထုတ်စာ — bank statement</li><li>လက်ကျန် — balance</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Withdraw: ငွေ ___.", "answer": "ထုတ်"},
         {"type": "multiple-choice", "question": "Balance: ", "options": ["ငွေလွှဲ", "လက်ကျန်", "ငွေသွင်း", "ဘဏ်ထုတ်စာ"], "correctIndex": 1},
         {"type": "true-false", "question": "ဘဏ်ထုတ်စာ means \"bank statement.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Transfer: ငွေ ___.", "answer": "လွှဲ"},
         {"type": "fill-blank", "question": "Deposit: ငွေ ___.", "answer": "သွင်း"}]},
    {"title": "Currency",
     "body_html": r"""<ul><li>ကျပ် — kyat (Myanmar currency, code MMK)</li><li>ဒေါ်လာ — US dollar</li><li>ယူရို — euro</li><li>"လဲလှယ်နှုန်း" — exchange rate</li></ul><p>Kyat exchange rate has been volatile. Many transactions still favor cash.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Currency code: ___.", "answer": "MMK"},
         {"type": "multiple-choice", "question": "Exchange rate: ", "options": ["လဲလှယ်နှုန်း", "ဒေါ်လာ", "ယူရို", "ကျပ်"], "correctIndex": 0},
         {"type": "true-false", "question": "Kyat exchange rate has been volatile.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Dollar: ___ လာ.", "answer": "ဒေါ်"},
         {"type": "true-false", "question": "Cash is rarely used in Myanmar.", "correctAnswer": False}]},
    {"title": "ATM & Mobile Banking",
     "body_html": r"""<ul><li>အေတီအမ် — ATM</li><li>ကတ်ထည့် — to insert card</li><li>လျှို့ဝှက်နံပါတ် — PIN</li><li>"လက်ကျန်ကြည့်ပါ" — \"Check balance.\"</li><li>KBZ Pay, AYA Pay, Wave Pay — mobile money</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "PIN: ___ ဝှက်နံပါတ်.", "answer": "လျှို့"},
         {"type": "multiple-choice", "question": "Mobile money apps:", "options": ["KBZ Pay, AYA Pay, Wave", "Venmo, Cash App", "Apple Pay only", "no mobile money"], "correctIndex": 0},
         {"type": "true-false", "question": "Mobile money is widely used.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Insert card: ကတ် ___.", "answer": "ထည့်"},
         {"type": "fill-blank", "question": "Check balance: လက်ကျန် ___.", "answer": "ကြည့်ပါ"}]},
    {"title": "Loans",
     "body_html": r"""<ul><li>ချေးငွေ — loan</li><li>အတိုး — interest</li><li>ပြန်ဆပ် — to repay</li><li>"ချေးဖို့ ရနိုင်လား။" — \"Can I get a loan?\"</li><li>အာမခံပစ္စည်း — collateral</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Interest: ___.", "answer": "အတိုး"},
         {"type": "multiple-choice", "question": "Collateral: ", "options": ["ချေးငွေ", "ပြန်ဆပ်", "အာမခံပစ္စည်း", "အတိုး"], "correctIndex": 2},
         {"type": "true-false", "question": "ပြန်ဆပ် means \"to repay.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Loan: ___ ငွေ.", "answer": "ချေး"},
         {"type": "true-false", "question": "Loans don't accrue interest.", "correctAnswer": False}]},
    {"title": "Investment",
     "body_html": r"""<ul><li>ရင်းနှီးမြှုပ်နှံ — to invest</li><li>စတော့ — stock</li><li>ပစ္စည်း — asset</li><li>အရှုံး — loss</li><li>အမြတ် — profit</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Profit: ___.", "answer": "အမြတ်"},
         {"type": "multiple-choice", "question": "Loss: ", "options": ["ပစ္စည်း", "အမြတ်", "အရှုံး", "စတော့"], "correctIndex": 2},
         {"type": "true-false", "question": "ရင်းနှီးမြှုပ်နှံ means \"to invest.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Stock: ___.", "answer": "စတော့"},
         {"type": "fill-blank", "question": "Asset: ___.", "answer": "ပစ္စည်း"}]},
    {"title": "Insurance",
     "body_html": r"""<ul><li>အာမခံ — insurance</li><li>အသက်အာမခံ — life insurance</li><li>ကျန်းမာရေးအာမခံ — health insurance</li><li>ကားအာမခံ — car insurance</li><li>ပရီမီယံ — premium</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Insurance: ___.", "answer": "အာမခံ"},
         {"type": "multiple-choice", "question": "Health insurance: ", "options": ["အသက်အာမခံ", "ကျန်းမာရေးအာမခံ", "ကားအာမခံ", "ပရီမီယံ"], "correctIndex": 1},
         {"type": "true-false", "question": "Premium uses an English loanword.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Life insurance: အသက် ___.", "answer": "အာမခံ"},
         {"type": "true-false", "question": "Insurance market in Myanmar is fully mature.", "correctAnswer": False}]},
    {"title": "Tax",
     "body_html": r"""<ul><li>အခွန် — tax</li><li>ဝင်ငွေခွန် — income tax</li><li>ကုန်ထုတ်ခွန် — production tax</li><li>VAT — တန်ဖိုးပေါင်းခွန်</li><li>အခွန်ပေး — to pay tax</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tax: ___.", "answer": "အခွန်"},
         {"type": "multiple-choice", "question": "Income tax: ", "options": ["ဝင်ငွေခွန်", "ကုန်ထုတ်ခွန်", "VAT", "ပေး"], "correctIndex": 0},
         {"type": "true-false", "question": "VAT in Burmese: တန်ဖိုးပေါင်းခွန်.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pay tax: အခွန် ___.", "answer": "ပေး"},
         {"type": "fill-blank", "question": "Production tax: ___ ထုတ်ခွန်.", "answer": "ကုန်"}]},
    {"title": "Salary & Payroll",
     "body_html": r"""<ul><li>လစာ — monthly salary</li><li>စရိတ် — expense</li><li>ဆုကြေး — bonus</li><li>ပညာရေးထောက်ပံ့ — education subsidy</li><li>"ဘယ်နေ့ ပေးမလဲ။" — \"When will (you) pay?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Bonus: ___ ကြေး.", "answer": "ဆု"},
         {"type": "multiple-choice", "question": "Salary: ", "options": ["စရိတ်", "လစာ", "ဆုကြေး", "ပညာရေးထောက်ပံ့"], "correctIndex": 1},
         {"type": "true-false", "question": "ပညာရေးထောက်ပံ့ means \"education subsidy.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Expense: ___.", "answer": "စရိတ်"},
         {"type": "fill-blank", "question": "When will pay: ဘယ်နေ့ ___ မလဲ.", "answer": "ပေး"}]},
    {"title": "Budgeting",
     "body_html": r"""<ul><li>ဘတ်ဂျက် — budget (loanword)</li><li>စီစဉ် — to plan</li><li>စုဆောင်း — to save</li><li>သုံးစွဲ — to spend</li><li>လိုအပ်ချက် — needs</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Budget: ___.", "answer": "ဘတ်ဂျက်"},
         {"type": "multiple-choice", "question": "To save: ", "options": ["သုံးစွဲ", "စုဆောင်း", "စီစဉ်", "လိုအပ်ချက်"], "correctIndex": 1},
         {"type": "true-false", "question": "သုံးစွဲ means \"to spend.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "To plan: ___.", "answer": "စီစဉ်"},
         {"type": "fill-blank", "question": "Needs: လို ___ ချက်.", "answer": "အပ်"}]},
    {"title": "Hyperinflation Vocabulary",
     "body_html": r"""<p>Myanmar has experienced inflation cycles:</p><ul><li>ငွေဖောင်းပွ — inflation</li><li>ဈေးနှုန်းတက် — price rise</li><li>ဈေးနှုန်းကျ — price drop</li><li>ဝယ်ယူနိုင်စွမ်း — purchasing power</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Inflation: ငွေ ___ ပွ.", "answer": "ဖောင်း"},
         {"type": "multiple-choice", "question": "Price rise: ", "options": ["ဈေးနှုန်းတက်", "ဈေးနှုန်းကျ", "ဝယ်ယူနိုင်စွမ်း", "ငွေဖောင်းပွ"], "correctIndex": 0},
         {"type": "true-false", "question": "ဝယ်ယူနိုင်စွမ်း means \"purchasing power.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Price drop: ဈေးနှုန်း ___.", "answer": "ကျ"},
         {"type": "true-false", "question": "Myanmar has had inflation cycles.", "correctAnswer": True}]},
    {"title": "Foreign Exchange",
     "body_html": r"""<ul><li>ငွေလဲ — foreign exchange</li><li>လဲလှယ် — to exchange</li><li>"ယနေ့ နှုန်း ဘယ်လောက်လဲ။" — \"What's today's rate?\"</li><li>ဘယ်လောက်ထိ — \"How much (limit)?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Exchange (verb): ___.", "answer": "လဲလှယ်"},
         {"type": "multiple-choice", "question": "\"Today's rate\":", "options": ["ဒီနေ့ နှုန်း", "ဈေးမနက်ဖြန်", "ယနေ့ နှုန်း", "ယနေ့ ဈေး"], "correctIndex": 2},
         {"type": "true-false", "question": "ငွေလဲ relates to currency exchange.", "correctAnswer": True},
         {"type": "fill-blank", "question": "How much (limit): ဘယ်လောက် ___.", "answer": "ထိ"},
         {"type": "true-false", "question": "Foreign exchange rates change daily.", "correctAnswer": True}]},
    {"title": "Practice: At the Bank",
     "body_html": r"""<p>Sample dialogue:</p><p><strong>You:</strong> "မင်္ဂလာပါ။ ငွေသွင်းချင်ပါတယ်။"</p><p><strong>Teller:</strong> "စာရင်းနံပါတ် ပြောပြပါ။"</p><p><strong>You:</strong> "နံပါတ် ၁၂၃၄၅၆ ပါ။"</p><p><strong>Teller:</strong> "ဘယ်လောက် သွင်းမလဲ။"</p><p><strong>You:</strong> "နှစ်သိန်း သွင်းမယ်။"</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Account number: ___ နံပါတ်.", "answer": "စာရင်း"},
         {"type": "multiple-choice", "question": "Deposit (verb): ", "options": ["ထုတ်", "သွင်း", "လွှဲ", "လဲ"], "correctIndex": 1},
         {"type": "true-false", "question": "နှစ်သိန်း means 200,000.", "correctAnswer": True},
         {"type": "fill-blank", "question": "How much: ဘယ်___ .", "answer": "လောက်"},
         {"type": "fill-blank", "question": "I want to deposit: ငွေသွင်း ___ ပါတယ်.", "answer": "ချင်"}]},
    {"title": "Banking Checkpoint",
     "body_html": r"""<p>Recap of Unit 45:</p><ul><li>Major banks: KBZ, AYA, CB, Yoma.</li><li>Account types: ငွေစုစာရင်း, လက်ရှိစာရင်း.</li><li>Transactions: ငွေသွင်း (deposit), ငွေထုတ် (withdraw), ငွေလွှဲ (transfer).</li><li>Currency: kyat (MMK); volatile exchange rate.</li><li>Mobile money: KBZ Pay, AYA Pay, Wave Pay.</li><li>Loans: ချေးငွေ; interest: အတိုး.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Deposit: ငွေ ___.", "answer": "သွင်း"},
         {"type": "multiple-choice", "question": "Mobile money examples:", "options": ["KBZ/AYA Pay", "Venmo", "PayPal", "Apple Pay"], "correctIndex": 0},
         {"type": "true-false", "question": "Withdraw is ငွေထုတ်.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Currency: ___.", "answer": "ကျပ်"},
         {"type": "fill-blank", "question": "Interest: ___.", "answer": "အတိုး"},
         {"type": "true-false", "question": "Inflation is ငွေဖောင်းပွ.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Insurance: ___.", "answer": "အာမခံ"}]},
]

if __name__ == "__main__":
    render_unit(45, "Burmese Banking & Finance", 655, LESSONS)
