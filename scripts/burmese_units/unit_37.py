#!/usr/bin/env python3
"""Burmese Unit 37 — Buddhism in Detail (lessons 535-549)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Theravada Buddhism Overview",
     "body_html": r"""<p>Myanmar is ~88% Buddhist, almost all Theravada (the older school of Buddhism). Distinguishes from Mahayana (China, Japan, Vietnam) and Vajrayana (Tibet).</p><ul><li>Focus on the Pali Canon — earliest Buddhist scriptures.</li><li>Emphasis on individual liberation through meditation and ethics.</li><li>Monks (သံဃာ) are central to community life.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Buddhist school in Myanmar: ___ vada.", "answer": "Thera"},
         {"type": "multiple-choice", "question": "Myanmar's Buddhist population is roughly:", "options": ["50%", "70%", "88%", "99%"], "correctIndex": 2},
         {"type": "true-false", "question": "The Pali Canon is the Theravada scripture.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Monk: ___.", "answer": "ဘုန်းကြီး (or သံဃာ)"},
         {"type": "true-false", "question": "Theravada emphasizes individual liberation.", "correctAnswer": True}]},
    {"title": "The Buddha (ဗုဒ္ဓ)",
     "body_html": r"""<p>Siddhartha Gautama, born in present-day Nepal ~563 BCE. Achieved enlightenment under the Bodhi tree at Bodhgaya. Taught for 45 years, died at 80.</p><ul><li>Burmese term: ဗုဒ္ဓ (Buddha)</li><li>"The awakened one"</li><li>Founder of the Sangha (monastic community)</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Buddha was born around 563 BCE.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Birth name:", "options": ["Siddhartha", "Maitreya", "Ananda", "Kassapa"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Burmese for Buddha: ___.", "answer": "ဗုဒ္ဓ"},
         {"type": "true-false", "question": "Buddha taught for 45 years.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Place of enlightenment: ___ gaya.", "answer": "Bodh"}]},
    {"title": "The Four Noble Truths",
     "body_html": r"""<ol><li>Life involves dukkha (suffering / unsatisfactoriness).</li><li>Dukkha has a cause: tanha (craving).</li><li>Dukkha can cease.</li><li>The Eightfold Path leads to cessation.</li></ol>""",
     "exercises": [
         {"type": "true-false", "question": "Four Noble Truths is a foundational teaching.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The cause of dukkha is:", "options": ["happiness", "tanha (craving)", "wealth", "fate"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Dukkha means ___.", "answer": "suffering"},
         {"type": "true-false", "question": "The path to liberation is the Eightfold Path.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Number of noble truths: ___.", "answer": "4"}]},
    {"title": "The Eightfold Path",
     "body_html": r"""<p>Right View, Right Intention, Right Speech, Right Action, Right Livelihood, Right Effort, Right Mindfulness, Right Concentration.</p><p>Three groupings:</p><ul><li>Wisdom (paññā): View, Intention</li><li>Ethics (sīla): Speech, Action, Livelihood</li><li>Concentration (samādhi): Effort, Mindfulness, Concentration</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number of path factors: ___.", "answer": "8"},
         {"type": "multiple-choice", "question": "Right Speech is in the ___ group.", "options": ["wisdom", "ethics", "concentration", "none"], "correctIndex": 1},
         {"type": "true-false", "question": "Sila refers to ethics.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Wisdom in Pali: ___.", "answer": "panna"},
         {"type": "fill-blank", "question": "Concentration in Pali: ___.", "answer": "samadhi"}]},
    {"title": "The Five Precepts",
     "body_html": r"""<p>Lay Buddhists observe these:</p><ol><li>Refrain from killing.</li><li>Refrain from stealing.</li><li>Refrain from sexual misconduct.</li><li>Refrain from lying.</li><li>Refrain from intoxicants.</li></ol><p>Burmese laypeople take precepts at temple visits and on holy days.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number of precepts: ___.", "answer": "5"},
         {"type": "multiple-choice", "question": "Fifth precept:", "options": ["no anger", "no intoxicants", "no greed", "no envy"], "correctIndex": 1},
         {"type": "true-false", "question": "Laypeople take precepts at temples.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Refrain from ___ (third precept word).", "answer": "sexual misconduct"},
         {"type": "true-false", "question": "Precepts are binding only on monks.", "correctAnswer": False}]},
    {"title": "Karma & Rebirth",
     "body_html": r"""<p>Karma (ကံ kan): intentional action; produces results. Good karma → favorable rebirth; bad karma → unfavorable.</p><p>Rebirth (ပြန်ဖြစ်ပျက်ခြင်း): the cycle of birth-death-birth, called samsara. Liberation (နိဗ္ဗာန်) breaks the cycle.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Karma in Burmese: ___.", "answer": "ကံ"},
         {"type": "multiple-choice", "question": "Liberation is called:", "options": ["samsara", "nibbana / nirvana", "dukkha", "tanha"], "correctIndex": 1},
         {"type": "true-false", "question": "Samsara is the cycle of rebirth.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Burmese nirvana: ___.", "answer": "နိဗ္ဗာန်"},
         {"type": "true-false", "question": "Good karma leads to favorable rebirth.", "correctAnswer": True}]},
    {"title": "The Sangha (Monks)",
     "body_html": r"""<p><strong>သံဃာ</strong> — community of monks. ~500,000 in Myanmar. Wear maroon-and-saffron robes. Strict 227 rules of conduct (Patimokkha).</p><ul><li>Bound by celibacy.</li><li>One meal before noon.</li><li>Daily alms-round at dawn.</li><li>Lifelong or temporary commitment.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Myanmar has ~500,000 monks.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Number of Patimokkha rules:", "options": ["10", "100", "227", "1000"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Sangha in Burmese: ___.", "answer": "သံဃာ"},
         {"type": "true-false", "question": "Monks eat only one meal before noon.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Robe colors: maroon and ___.", "answer": "saffron"}]},
    {"title": "Pagodas & Stupas (ဘုရား)",
     "body_html": r"""<p>Pagodas house Buddha relics. Famous Burmese pagodas:</p><ul><li><strong>Shwedagon</strong> — Yangon's massive gold stupa.</li><li><strong>Mahamuni</strong> — Mandalay's revered Buddha image.</li><li><strong>Kyaiktiyo</strong> — golden boulder.</li><li><strong>Bagan</strong> — over 2,000 ancient pagodas.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Pagoda: ___.", "answer": "ဘုရား"},
         {"type": "multiple-choice", "question": "Most famous Yangon pagoda:", "options": ["Mahamuni", "Shwedagon", "Kyaiktiyo", "Bagan"], "correctIndex": 1},
         {"type": "true-false", "question": "Bagan has over 2,000 ancient pagodas.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Golden boulder pagoda: ___ tiyo.", "answer": "Kyaik"},
         {"type": "true-false", "question": "Pagodas house Buddha relics.", "correctAnswer": True}]},
    {"title": "Meditation Practices",
     "body_html": r"""<p>Two main techniques:</p><ul><li><strong>Samatha</strong> — concentration meditation, focus on breath.</li><li><strong>Vipassana</strong> — insight meditation, observation of phenomena. Made famous globally by Burmese teachers (Mahasi Sayadaw, S.N. Goenka).</li></ul><p>Beginners often start with breath awareness; advanced practitioners attend 10-day silent retreats.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Vipassana is insight meditation.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Concentration meditation:", "options": ["vipassana", "samatha", "mantra", "yoga"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Famous Burmese teacher: ___ Sayadaw.", "answer": "Mahasi"},
         {"type": "true-false", "question": "Vipassana is a Burmese export.", "correctAnswer": True},
         {"type": "fill-blank", "question": "10-day silent ___ are common.", "answer": "retreats"}]},
    {"title": "Buddhist Holidays",
     "body_html": r"""<ul><li><strong>Vesak (ကဆုန်လ ဖူးပူး)</strong> — May, celebrates Buddha's birth/enlightenment/death.</li><li><strong>Thadingyut</strong> — October, end of Buddhist Lent, festival of lights.</li><li><strong>Tazaungdaing</strong> — November, robes-offering festival.</li><li><strong>Waso</strong> — July, beginning of Buddhist Lent.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "End of Lent festival: ___.", "answer": "Thadingyut"},
         {"type": "multiple-choice", "question": "Vesak month (Burmese calendar):", "options": ["Waso", "Thadingyut", "Kason", "Tazaungdaing"], "correctIndex": 2},
         {"type": "true-false", "question": "Buddhist Lent runs roughly July-October.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Robe-offering festival: ___ daing.", "answer": "Tazaung"},
         {"type": "true-false", "question": "Vesak commemorates Buddha's birth, enlightenment, and death.", "correctAnswer": True}]},
    {"title": "Offering Vocabulary",
     "body_html": r"""<ul><li>လှူ — hlu — to offer / donate</li><li>ဒါန — da-na — generosity / charity</li><li>ဆွမ်း — hsun — food offered to monks</li><li>ပေါင်း — paung — alms bowl</li><li>"ဆွမ်း လှူပါ။" — "Offer food (to monks)."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "To offer: ___.", "answer": "လှူ"},
         {"type": "multiple-choice", "question": "Generosity:", "options": ["dana", "karma", "samadhi", "metta"], "correctIndex": 0},
         {"type": "true-false", "question": "ဆွမ်း means food offered to monks.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Alms bowl: ___.", "answer": "ပေါင်း"},
         {"type": "fill-blank", "question": "Charity in Burmese: ___ ဒါ.", "answer": "ပါ"}]},
    {"title": "Common Buddhist Phrases",
     "body_html": r"""<ul><li>"အသိဉာဏ်ရှိပါစေ။" — "May you have wisdom."</li><li>"မေတ္တာ ပါစေ။" — "May you have loving-kindness."</li><li>"ကိုယ်စိတ် ၂ ပါး ကျန်းမာပါစေ။" — "May body and mind be healthy."</li><li>"သာဓု သာဓု သာဓု။" — "Sadhu, sadhu, sadhu" (Well-said! well-done! shouted at end of merit-making).</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Loving-kindness: ___.", "answer": "မေတ္တာ"},
         {"type": "multiple-choice", "question": "Sadhu means:", "options": ["hello", "thanks", "well done / well said", "goodbye"], "correctIndex": 2},
         {"type": "true-false", "question": "\"အသိဉာဏ်\" means wisdom.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Body: ___ စိတ် ၂ ပါး.", "answer": "ကိုယ်"},
         {"type": "true-false", "question": "Sadhu is shouted three times.", "correctAnswer": True}]},
    {"title": "Buddhism & Daily Life",
     "body_html": r"""<p>Buddhist practice woven into daily life:</p><ul><li>Daily alms-giving to monks at dawn.</li><li>Bowing 3x to Buddha images.</li><li>Reciting the 5 precepts before meals.</li><li>Visiting pagodas on full-moon days.</li><li>Sharing merit (ကုသိုလ်) with deceased relatives.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Merit: ___ သိုလ်.", "answer": "ကု"},
         {"type": "multiple-choice", "question": "Pagoda visits common on:", "options": ["new moon", "full moon", "any day", "Sundays"], "correctIndex": 1},
         {"type": "true-false", "question": "Burmese Buddhists share merit with deceased relatives.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Daily alms at ___.", "answer": "dawn"},
         {"type": "true-false", "question": "Buddhism plays a marginal role in daily Burmese life.", "correctAnswer": False}]},
    {"title": "Practice: Visit a Pagoda",
     "body_html": r"""<p>Steps:</p><ol><li>Remove shoes and socks at entrance.</li><li>Wear modest clothing (long pants/skirt; covered shoulders).</li><li>Walk clockwise around the stupa.</li><li>Bow 3x at the main shrine.</li><li>Offer flowers, candles, or money to the pagoda fund.</li><li>Recite or silently reflect.</li><li>Don't point feet at Buddha images when sitting.</li></ol>""",
     "exercises": [
         {"type": "true-false", "question": "Walk clockwise around the stupa.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Number of bows at main shrine:", "options": ["1", "2", "3", "5"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Remove shoes AND ___.", "answer": "socks"},
         {"type": "true-false", "question": "Tank tops and shorts are fine at pagodas.", "correctAnswer": False},
         {"type": "true-false", "question": "Pointing feet at Buddha images is acceptable.", "correctAnswer": False}]},
    {"title": "Buddhism Checkpoint",
     "body_html": r"""<p>Recap of Unit 37:</p><ul><li>Theravada Buddhism dominates (~88% of Myanmar).</li><li>Buddha (ဗုဒ္ဓ) taught Four Noble Truths and the Eightfold Path.</li><li>Five Precepts for laypeople; 227 rules for monks.</li><li>Karma (ကံ), rebirth, samsara, and nibbana (နိဗ္ဗာန်) frame the worldview.</li><li>Sangha (သံဃာ) — monastic community of ~500,000.</li><li>Famous pagodas: Shwedagon, Mahamuni, Kyaiktiyo, Bagan.</li><li>Vipassana meditation is a major Burmese export.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Buddhist school in Myanmar: ___ vada.", "answer": "Thera"},
         {"type": "multiple-choice", "question": "Number of precepts for laypeople:", "options": ["3", "5", "8", "227"], "correctIndex": 1},
         {"type": "true-false", "question": "Vipassana is concentration meditation.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Liberation: ___.", "answer": "နိဗ္ဗာန်"},
         {"type": "fill-blank", "question": "Karma: ___.", "answer": "ကံ"},
         {"type": "true-false", "question": "Bagan has over 2,000 pagodas.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sadhu shouted ___ times.", "answer": "3"}]},
]

if __name__ == "__main__":
    render_unit(37, "Burmese Buddhism in Detail", 535, LESSONS)
