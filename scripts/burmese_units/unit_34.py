#!/usr/bin/env python3
"""Burmese Unit 34 — Negotiation (lessons 490-504)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "When to Negotiate",
     "body_html": r"""<p>Bargaining (ဈေးပြော) is expected at:</p><ul><li>Outdoor markets and street stalls.</li><li>Taxis without meters.</li><li>Independent shops (clothing, electronics, jewelry).</li><li>Hotel rates outside high season.</li></ul><p>Fixed prices apply at: chain stores, supermarkets, restaurants with menus, modern offices.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Bargaining: ___ ပြော.", "answer": "ဈေး"},
         {"type": "multiple-choice", "question": "Where you typically DON'T bargain:", "options": ["street markets", "supermarket chain", "no-meter taxi", "small jewelry shop"], "correctIndex": 1},
         {"type": "true-false", "question": "Hotel rates can be negotiable in low season.", "correctAnswer": True},
         {"type": "true-false", "question": "Restaurants with printed menus typically have fixed prices.", "correctAnswer": True},
         {"type": "true-false", "question": "Bargaining at supermarkets is normal.", "correctAnswer": False}]},
    {"title": "Opening the Negotiation",
     "body_html": r"""<p>Phrases to start:</p><ul><li>"ဒါ ဘယ်လောက်လဲ။" — "How much is this?"</li><li>"ဈေးနဲ့မပေါ်ဘူးနော်။" — "It's not cheap, you know."</li><li>"လျှော့ပေးနိုင်လား။" — "Can you give a discount?"</li></ul><p>Smile. Stay friendly. Bargaining is a social interaction in Myanmar, not a confrontation.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "\"How much is this?\":", "options": ["ဘယ်မှာလဲ", "ဘယ်လောက်လဲ", "ဘယ်နေ့လဲ", "ဘယ်သူလဲ"], "correctIndex": 1},
         {"type": "fill-blank", "question": "လျှော့ပေးနိုင်လား means \"Can you give a ___?\"", "answer": "discount"},
         {"type": "true-false", "question": "Bargaining should be friendly.", "correctAnswer": True},
         {"type": "true-false", "question": "Confrontational bargaining is the norm.", "correctAnswer": False},
         {"type": "fill-blank", "question": "ဈေးနဲ့ မပေါ်ဘူး means \"It's not ___.\"", "answer": "cheap"}]},
    {"title": "Counter-Offers",
     "body_html": r"""<p>Common counter-offer phrases:</p><ul><li>"___ ကျပ်ပဲ ပေးနိုင်ပါတယ်။" — "I can only pay ___ kyat."</li><li>"ဒါထက် နည်းနည်း လျှော့ပါ။" — "Lower it just a bit."</li><li>"ဒီအဆင့်မှာ ဈေးကြီးတယ်။" — "At this level, it's expensive."</li></ul><p>Walk away if the seller won't budge. They often call you back with a better price.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Walking away can be a negotiation tactic.", "correctAnswer": True},
         {"type": "fill-blank", "question": "နည်းနည်း means \"___\".", "answer": "a little"},
         {"type": "multiple-choice", "question": "ဈေးကြီး means:", "options": ["cheap", "expensive", "high quality", "old"], "correctIndex": 1},
         {"type": "fill-blank", "question": "ပေးနိုင်ပါတယ် means \"I can ___\".", "answer": "pay/give"},
         {"type": "true-false", "question": "Sellers never call you back after walk-away.", "correctAnswer": False}]},
    {"title": "Asking for a Better Deal",
     "body_html": r"""<p>Phrases to push price down:</p><ul><li>"အများဆုံး လျှော့ပေးနိုင်တာ ဘယ်လောက်လဲ။" — "What's the maximum discount?"</li><li>"ပိုပြီး လျှော့ပေးပါ။" — "Give a bigger discount."</li><li>"ငွေသား ပေးမယ်။" — "I'll pay cash." (sometimes opens room)</li><li>"အရေအတွက် များများ ဝယ်မယ်။" — "I'll buy a lot."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "ငွေသား means \"___\".", "answer": "cash"},
         {"type": "multiple-choice", "question": "Buying in bulk:", "options": ["might get a discount", "always at full price", "is forbidden", "doesn't help"], "correctIndex": 0},
         {"type": "true-false", "question": "ပိုပြီး means \"more / additionally.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "အရေအတွက် means \"___\".", "answer": "quantity"},
         {"type": "true-false", "question": "Cash payment can sometimes lower price.", "correctAnswer": True}]},
    {"title": "Closing the Sale",
     "body_html": r"""<p>Wrapping up:</p><ul><li>"ကောင်းပါပြီ။" — "OK then." (agreement)</li><li>"ယူမယ်။" — "I'll take it."</li><li>"ပြေစာ ရနိုင်လား။" — "Can I get a receipt?"</li><li>"ထုပ်ပေးပါ။" — "Wrap it up please."</li></ul>""",
     "exercises": [
         {"type": "multiple-choice", "question": "ယူမယ်။ means:", "options": ["I'll leave", "I'll take it", "I'll wait", "I'll think"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Receipt: ___ စာ.", "answer": "ပြေ"},
         {"type": "true-false", "question": "ထုပ်ပေးပါ asks for wrapping.", "correctAnswer": True},
         {"type": "true-false", "question": "ကောင်းပါပြီ signals agreement.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"I'll take it.\": ___ မယ်။", "answer": "ယူ"}]},
    {"title": "Cultural Norms in Bargaining",
     "body_html": r"""<p>Cultural touches:</p><ul><li>Don't bargain over tiny amounts when buying from older or vulnerable sellers.</li><li>It's polite to compliment the goods even when negotiating.</li><li>Avoid public anger or rude tone — bad form and unproductive.</li><li>"Friendship discount" — long-time customers expect special treatment.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Avoid bargaining hard with vulnerable elderly sellers.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Tone in negotiation should be:", "options": ["aggressive", "rude", "polite and friendly", "cold"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Long-time customers may get a ___ discount.", "answer": "friendship"},
         {"type": "true-false", "question": "Public anger is acceptable.", "correctAnswer": False},
         {"type": "true-false", "question": "Complimenting goods while negotiating is polite.", "correctAnswer": True}]},
    {"title": "Negotiating Salary",
     "body_html": r"""<p>Job-salary negotiation:</p><ul><li>"လစာ ဘယ်လောက်လဲ။" — "What's the salary?"</li><li>"ပိုများတဲ့ လစာ ရနိုင်လား။" — "Can I get a higher salary?"</li><li>"အလုပ်တာဝန် ဘာတွေလုပ်ရမလဲ။" — "What are the duties?"</li></ul><p>Modern Burmese employers expect salary discussions, but indirect approach still works better than aggressive demands.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "လစာ means \"___\".", "answer": "salary"},
         {"type": "multiple-choice", "question": "Best approach to salary talk:", "options": ["aggressive demands", "indirect / measured", "no discussion", "shouting"], "correctIndex": 1},
         {"type": "true-false", "question": "Modern Burmese employers expect salary discussions.", "correctAnswer": True},
         {"type": "fill-blank", "question": "အလုပ်တာဝန် means job ___.", "answer": "duties"},
         {"type": "fill-blank", "question": "ပိုများ means \"___\".", "answer": "more"}]},
    {"title": "Negotiating Rent",
     "body_html": r"""<p>Rent (အိမ်လခ) negotiation:</p><ul><li>Discuss the lease term — longer leases unlock lower monthly rents.</li><li>"တစ်နှစ်စာ ပေးရင် လျှော့ပေးနိုင်လား။" — "If I pay a year, can you discount?"</li><li>"အပ်ငွေ ဘယ်လောက် ပေးရမလဲ။" — "How much deposit?"</li><li>Most landlords require 6–12 months upfront.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Rent: အိမ် ___ .", "answer": "လခ"},
         {"type": "multiple-choice", "question": "Burmese landlords often require:", "options": ["1 month deposit", "6–12 months upfront", "no deposit", "just credit card"], "correctIndex": 1},
         {"type": "true-false", "question": "Longer leases can unlock lower rates.", "correctAnswer": True},
         {"type": "fill-blank", "question": "အပ်ငွေ means \"___\".", "answer": "deposit"},
         {"type": "fill-blank", "question": "တစ်နှစ်စာ means \"for one ___\".", "answer": "year"}]},
    {"title": "Bulk Discounts",
     "body_html": r"""<p>Phrases for buying in quantity:</p><ul><li>"ဆယ်ခု ဝယ်ရင် ဈေး ဘယ်လောက်လဲ။" — "What's the price for 10?"</li><li>"အရောင်း သိပ်များတယ်။" — "I'll buy a lot."</li><li>"စုပေးနိုင်လား။" — "Can you set aside / hold them?"</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Bulk buying often unlocks discounts.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ဆယ်ခု means \"___ pieces.\"", "answer": "10"},
         {"type": "multiple-choice", "question": "စုပေးနိုင်လား means:", "options": ["Wrap it", "Set aside / hold", "Discount", "Refund"], "correctIndex": 1},
         {"type": "fill-blank", "question": "\"a lot\" / many: သိပ်___ .", "answer": "များ"},
         {"type": "true-false", "question": "Buying in bulk gives no leverage.", "correctAnswer": False}]},
    {"title": "Refusing Politely",
     "body_html": r"""<p>If the price stays too high:</p><ul><li>"ကျေးဇူးတင်ပါတယ်။ ပြန်ကြည့်ဦးမယ်။" — "Thanks, I'll come back."</li><li>"အခု ဝယ်ဖို့ မဖြစ်နိုင်ပါဘူး။" — "Can't buy now."</li><li>"တခြားနေရာ ကြည့်လိုက်မယ်။" — "I'll look elsewhere."</li></ul><p>Walking away politely keeps the door open — and often the seller will offer a final lower price.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "တခြားနေရာ means \"___ place.\"", "answer": "another"},
         {"type": "multiple-choice", "question": "Polite refusal preserves:", "options": ["nothing", "future relationship", "anger", "credit"], "correctIndex": 1},
         {"type": "true-false", "question": "Walking away can prompt a better offer.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"Thanks, I'll come back\": ပြန် ___ ဦးမယ်။", "answer": "ကြည့်"},
         {"type": "true-false", "question": "Polite refusal is rude.", "correctAnswer": False}]},
    {"title": "Negotiating in Burmese vs English",
     "body_html": r"""<p>Speaking Burmese (even imperfectly) often gets better prices than English. Sellers may give a "tourist price" if they assume you're a foreign visitor with no language skills.</p><p>Even saying "ဈေး လျှော့ပေးနိုင်လား" or numbers in Burmese signals you've spent time in the country and aren't a tourist target.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Speaking Burmese (even imperfectly) often gets better prices.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "\"Tourist price\" means:", "options": ["a discount", "an inflated price", "a free sample", "the local rate"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Saying numbers in ___ signals you're not a tourist.", "answer": "Burmese"},
         {"type": "true-false", "question": "Sellers always give the same price regardless of language.", "correctAnswer": False},
         {"type": "true-false", "question": "Locals get better deals than visibly foreign tourists in markets.", "correctAnswer": True}]},
    {"title": "Money Particles & Numbers",
     "body_html": r"""<p>Burmese has classifier-counter system. For currency:</p><ul><li>တစ်ထောင် — 1,000 kyat</li><li>သုံးထောင် — 3,000 kyat</li><li>တစ်သိန်း — 100,000 kyat (lakh)</li><li>တစ်သန်း — 1,000,000 kyat (million)</li></ul><p>1 USD ≈ several thousand kyat (rate varies wildly with politics). Always check current rate.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "1,000 kyat: တစ်___.", "answer": "ထောင်"},
         {"type": "multiple-choice", "question": "100,000 kyat:", "options": ["သိန်း", "သန်း", "ထောင်", "ရာ"], "correctIndex": 0},
         {"type": "true-false", "question": "Kyat-to-USD rate is stable.", "correctAnswer": False},
         {"type": "fill-blank", "question": "1,000,000 kyat: တစ်___.", "answer": "သန်း"},
         {"type": "true-false", "question": "Always check current exchange rate.", "correctAnswer": True}]},
    {"title": "Documenting the Deal",
     "body_html": r"""<p>For larger transactions, get it in writing:</p><ul><li>ပြေစာ — receipt</li><li>စာချုပ် — contract</li><li>လက်မှတ် — signature</li><li>"ပြေစာ ပြန်ပေးပါ။" — "Please give a receipt."</li></ul><p>Don't be shy about asking for paper trail — Burmese legal disputes hinge on documentation.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ပြေစာ means \"___\".", "answer": "receipt"},
         {"type": "multiple-choice", "question": "စာချုပ် means:", "options": ["receipt", "contract", "discount", "tax"], "correctIndex": 1},
         {"type": "true-false", "question": "Documentation is important for legal disputes.", "correctAnswer": True},
         {"type": "fill-blank", "question": "လက်မှတ် means \"___\".", "answer": "signature"},
         {"type": "true-false", "question": "Asking for receipts is considered rude.", "correctAnswer": False}]},
    {"title": "Practice: Bargain a Longyi",
     "body_html": r"""<p>Walking through a market scenario:</p><p><strong>You:</strong> "ဒီ လုံချည် ဘယ်လောက်လဲ။" "How much is this longyi?"</p><p><strong>Seller:</strong> "နှစ်သောင်း ပြားပါ။" "20,000 kyat."</p><p><strong>You:</strong> "ဈေးကြီးတယ်။ တစ်သောင်း ငါးထောင် ပေးပါ့မယ်။" "It's expensive. I'll pay 15,000."</p><p><strong>Seller:</strong> "တစ်သောင်း ရှစ်ထောင် လော။" "How about 18,000?"</p><p><strong>You:</strong> "တစ်သောင်း ခြောက်ထောင်။" "16,000."</p><p><strong>Seller:</strong> "ကောင်းပါပြီ။" "OK, deal."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Burmese sarong: ___ ချည်.", "answer": "လုံ"},
         {"type": "multiple-choice", "question": "နှစ်သောင်း means:", "options": ["2,000", "20,000", "200,000", "2,000,000"], "correctIndex": 1},
         {"type": "true-false", "question": "Final agreed price was 16,000 kyat.", "correctAnswer": True},
         {"type": "fill-blank", "question": "တစ်သောင်း ငါးထောင် means ___.", "answer": "15,000"},
         {"type": "true-false", "question": "ကောင်းပါပြီ closes the deal.", "correctAnswer": True}]},
    {"title": "Negotiation Checkpoint",
     "body_html": r"""<p>Recap of Unit 34:</p><ul><li>Bargain at markets, indie shops, no-meter taxis. Not at chain stores.</li><li>Open with a friendly tone, ask the price, suggest a discount.</li><li>Walk away if needed; sellers often call back.</li><li>Speaking Burmese gets better prices.</li><li>Numbers: ထောင် = 1,000; သိန်း = 100,000; သန်း = 1,000,000.</li><li>Get receipts (ပြေစာ) for important purchases.</li><li>Maintain politeness — public anger is bad form.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Receipt: ___.", "answer": "ပြေစာ"},
         {"type": "multiple-choice", "question": "Bargaining at supermarkets is:", "options": ["expected", "not done", "rude", "loud"], "correctIndex": 1},
         {"type": "fill-blank", "question": "100,000 kyat: တစ်___.", "answer": "သိန်း"},
         {"type": "true-false", "question": "Politeness gets better deals than aggression.", "correctAnswer": True},
         {"type": "true-false", "question": "Walking away from a high-priced item often prompts a better offer.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Bargaining: ___ ပြော.", "answer": "ဈေး"},
         {"type": "true-false", "question": "1,000,000 = ထောင်.", "correctAnswer": False}]},
]

if __name__ == "__main__":
    render_unit(34, "Burmese Negotiation", 490, LESSONS)
