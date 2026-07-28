#!/usr/bin/env python3
"""Burmese Unit 33 — Etiquette & Manners (lessons 475-489)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Honorifics & Address",
     "body_html": r"""
<p>Burmese has specific honorific particles you use in front of names:</p>
<ul>
<li>ဦး (U) — older man (e.g., U Thant)</li>
<li>ဒေါ် (Daw) — older woman (e.g., Daw Aung San Suu Kyi)</li>
<li>ကို (Ko) — younger man (peer)</li>
<li>မ (Ma) — younger woman</li>
<li>မောင် (Maung) — boy / very young man</li>
</ul>
<p>Always use these in formal settings. Calling an elder by name without ဦး or ဒေါ် is rude.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Honorific for older man: ___ (one syllable).", "answer": "ဦး"},
         {"type": "multiple-choice", "question": "ဒေါ် is used for:", "options": ["younger man", "younger woman", "older woman", "boy"], "correctIndex": 2},
         {"type": "true-false", "question": "Calling an elder by bare name is impolite.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ကို is used for ___ man.", "answer": "younger"},
         {"type": "fill-blank", "question": "Honorific for very young boy: ___.", "answer": "Maung"}]},
    {"title": "Greeting Elders",
     "body_html": r"""
<p>When meeting older relatives, neighbors, or community elders:</p>
<ul>
<li>Slight bow with hands clasped together (anjali mudra style).</li>
<li>"မင်္ဂလာပါ ဦးကြီး။" — "Hello, Uncle (older man)."</li>
<li>Don't sit higher than them.</li>
<li>Speak softly; don't interrupt.</li>
</ul>
<p>The cultural value of respect for elders runs deep. Younger people kneel to greet revered teachers (gadaw ceremony).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Don't sit higher than elders.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Burmese show respect with hands:", "options": ["one hand raised", "fist on chest", "clasped together (anjali)", "behind back"], "correctIndex": 2},
         {"type": "fill-blank", "question": "ဦးကြီး means \"___\".", "answer": "uncle"},
         {"type": "true-false", "question": "Interrupting elders is acceptable.", "correctAnswer": False},
         {"type": "fill-blank", "question": "The respectful kneeling for teachers is called ___.", "answer": "gadaw"}]},
    {"title": "Temple Etiquette",
     "body_html": r"""
<p>At Buddhist pagodas (ဘုရား) and monasteries (ကျောင်း):</p>
<ul>
<li>Remove shoes AND socks at the entrance.</li>
<li>Wear modest clothing — shoulders and knees covered.</li>
<li>Walk clockwise around stupas.</li>
<li>Don't point your feet at Buddha images.</li>
<li>Lower your voice; turn off phones.</li>
</ul>
<p>Some sites prohibit women from certain inner sanctums (Mahamuni, Kyaiktiyo). Respect local customs.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Remove shoes AND socks at temples.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Direction to walk around stupas:", "options": ["counter-clockwise", "clockwise", "either", "no walking"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Burmese temple: ___.", "answer": "ဘုရား"},
         {"type": "true-false", "question": "It's fine to point your feet at Buddha images.", "correctAnswer": False},
         {"type": "true-false", "question": "Some inner sanctums restrict women.", "correctAnswer": True}]},
    {"title": "Dining Etiquette",
     "body_html": r"""
<p>Burmese meal customs:</p>
<ul>
<li>Eldest sits and eats first; younger wait.</li>
<li>Eat with right hand or fork+spoon (chopsticks for noodles).</li>
<li>Don't waste rice — symbolic of disrespect to farmers.</li>
<li>Burping isn't taboo; slurping noodles is fine.</li>
<li>Common toast: "ကျန်းမာရေး အတွက်။" — "To your health."</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Eat with the ___ hand if eating by hand.", "answer": "right"},
         {"type": "multiple-choice", "question": "Wasting rice is:", "options": ["fine", "symbolic of disrespect", "encouraged", "considered lucky"], "correctIndex": 1},
         {"type": "true-false", "question": "Younger people eat first.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Toast: \"ကျန်းမာရေး အတွက်။\" (\"To your ___\").", "answer": "health"},
         {"type": "true-false", "question": "Slurping noodles is acceptable.", "correctAnswer": True}]},
    {"title": "Gift Giving",
     "body_html": r"""
<p>Gifts in Burmese culture:</p>
<ul>
<li>Give and receive with both hands (or right hand supported by left).</li>
<li>Avoid gifts in sets of 4 (associated with death, similar to East Asian taboo).</li>
<li>Wrap gifts attractively; modest gifts are fine.</li>
<li>Don't open gifts in front of the giver (similar to Asian customs).</li>
<li>For elders: tea, flowers, fruit are appropriate.</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Use ___ hands to give and receive.", "answer": "both"},
         {"type": "multiple-choice", "question": "Avoid sets of:", "options": ["3", "4", "5", "7"], "correctIndex": 1},
         {"type": "true-false", "question": "Open gifts immediately in front of giver.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Common elder gift: tea or ___.", "answer": "flowers"},
         {"type": "true-false", "question": "Modest gifts are fine.", "correctAnswer": True}]},
    {"title": "Speaking Politely",
     "body_html": r"""
<p>Politeness particles soften speech:</p>
<ul>
<li>ပါ (pa) — adds politeness to verbs/imperatives.</li>
<li>ခင်ဗျား (khin-bya) — male-speaker polite "you."</li>
<li>ရှင် (shin) — female-speaker polite particle.</li>
<li>"___ ပေးပါ" — "Please ___."</li>
</ul>
<p>Direct demands without pa or appropriate particles can sound rude. When in doubt, add pa.</p>""",
     "exercises": [
         {"type": "true-false", "question": "ပါ adds politeness.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Male-speaker polite \"you\":", "options": ["ရှင်", "ခင်ဗျား", "မင်း", "ငါ"], "correctIndex": 1},
         {"type": "fill-blank", "question": "\"Please give\" → ___ ပေးပါ.", "answer": "..."},
         {"type": "true-false", "question": "Direct demands without ပါ can sound rude.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Female-speaker polite particle: ___.", "answer": "ရှင်"}]},
    {"title": "Body Language",
     "body_html": r"""
<p>Burmese body language norms:</p>
<ul>
<li><strong>Head:</strong> sacred — never pat someone on the head, even children.</li>
<li><strong>Feet:</strong> lowest part — don't point feet at people or Buddha images. Don't step over books.</li>
<li><strong>Hands:</strong> use both hands or right hand (not left alone) for important objects.</li>
<li><strong>Eye contact:</strong> some, but not aggressive. Looking down with elders is respectful.</li>
<li><strong>Pointing:</strong> use whole hand, not single finger.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Don't pat anyone's head, including children.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Pointing should use:", "options": ["index finger", "whole hand", "middle finger", "feet"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Don't ___ over books.", "answer": "step"},
         {"type": "true-false", "question": "Pointing feet at Buddha images is acceptable.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Use ___ hands for important objects.", "answer": "both"}]},
    {"title": "Public Behavior",
     "body_html": r"""
<p>Public conduct expectations:</p>
<ul>
<li>Loud public behavior is frowned upon.</li>
<li>Public displays of affection (PDA) are minimal — keep it modest.</li>
<li>Pushing in queues is normal in busy markets, less so in formal settings.</li>
<li>Smoking in public spaces is common but receding.</li>
<li>Photographing strangers without permission is impolite.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Loud public behavior is generally frowned upon.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "PDA in Myanmar is:", "options": ["enthusiastic", "minimal", "encouraged", "required"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Photographing strangers without ___ is rude.", "answer": "permission"},
         {"type": "true-false", "question": "Markets often have orderly queues.", "correctAnswer": False},
         {"type": "true-false", "question": "Smoking in public is now becoming less common.", "correctAnswer": True}]},
    {"title": "Conversational Topics: OK",
     "body_html": r"""
<p>Safe conversational topics with Burmese friends:</p>
<ul>
<li>Family (always opening question).</li>
<li>Food — Burmese love discussing food.</li>
<li>Festivals and holidays.</li>
<li>Travel within Myanmar.</li>
<li>Sports — football is huge.</li>
<li>Buddhism (gently and respectfully).</li>
</ul>""",
     "exercises": [
         {"type": "multiple-choice", "question": "Most popular sport in Myanmar:", "options": ["cricket", "football", "rugby", "baseball"], "correctIndex": 1},
         {"type": "true-false", "question": "Family is a universal opening topic.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Burmese love discussing ___.", "answer": "food"},
         {"type": "true-false", "question": "Buddhism can be discussed if approached respectfully.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Travel within ___ is common topic.", "answer": "Myanmar"}]},
    {"title": "Conversational Topics: Avoid",
     "body_html": r"""
<p>Topics to handle carefully or avoid:</p>
<ul>
<li>Politics — current and historical (extremely sensitive).</li>
<li>Military government / coup.</li>
<li>Rohingya crisis.</li>
<li>Personal income unless specifically appropriate.</li>
<li>Direct criticism of Buddhist monks.</li>
<li>Comparing Myanmar unfavorably to other countries.</li>
</ul>
<p>Politics in particular has been dangerous to discuss; let your Burmese friends lead any such conversation.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Politics is extremely sensitive in Myanmar.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Best practice on politics:", "options": ["bring it up first", "let Burmese friends lead", "demand opinions", "avoid Burmese altogether"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Avoid criticizing ___ monks directly.", "answer": "Buddhist"},
         {"type": "true-false", "question": "Asking about personal income is always fine.", "correctAnswer": False},
         {"type": "true-false", "question": "Comparing Myanmar unfavorably to other countries can offend.", "correctAnswer": True}]},
    {"title": "Apology & Forgiveness",
     "body_html": r"""
<p>Apologizing in Burmese:</p>
<ul>
<li>"တောင်းပန်ပါတယ်။" — "I apologize." (formal)</li>
<li>"ဆောရီး။" — "Sorry" (informal, English loan)</li>
<li>"ခွင့်လွှတ်ပါ။" — "Please forgive me."</li>
<li>"အပြစ် မရှိပါဘူး။" — "It's not your fault / no problem."</li>
</ul>
<p>Burmese culture values harmony; apologies are common to smooth small conflicts even when no one is clearly at fault.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Formal \"I apologize\": ___ ပါတယ်။", "answer": "တောင်းပန်"},
         {"type": "multiple-choice", "question": "ခွင့်လွှတ်ပါ means:", "options": ["Hello", "Goodbye", "Forgive me", "Thanks"], "correctIndex": 2},
         {"type": "true-false", "question": "Burmese culture values harmony.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ဆောရီး is borrowed from ___.", "answer": "English"},
         {"type": "fill-blank", "question": "\"အပြစ် မရှိပါဘူး။\" means \"It's not your ___.\"", "answer": "fault"}]},
    {"title": "Saying No Politely",
     "body_html": r"""
<p>Direct "no" can feel rude. Soften:</p>
<ul>
<li>"အင်း... မဖြစ်ဘူးထင်တယ်။" — "Hmm... I don't think it's possible."</li>
<li>"စဉ်းစားကြည့်မယ်။" — "I'll think about it." (often a polite no)</li>
<li>"ပေးနိုင်မယ်ဆိုရင် တော်တယ်။" — "If I could, that would be great." (polite no)</li>
<li>"ခက်တယ်။" — "It's difficult." (polite no)</li>
</ul>
<p>Reading these signals is part of cultural competence. Pushing past a polite no can damage relationships.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Direct \"no\" can feel rude in Burmese.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "\"စဉ်းစားကြည့်မယ်။\" often means:", "options": ["yes", "polite no / I'll think about it", "definitely", "I'm hungry"], "correctIndex": 1},
         {"type": "fill-blank", "question": "ခက်တယ် means \"it's ___ \" (a polite no).", "answer": "difficult"},
         {"type": "true-false", "question": "Pushing past a polite no can damage relationships.", "correctAnswer": True},
         {"type": "true-false", "question": "All Burmese sentences must end with no.", "correctAnswer": False}]},
    {"title": "Compliments & Reactions",
     "body_html": r"""
<p>Burmese reactions to compliments are typically modest:</p>
<ul>
<li>Deflect: "ဘာမှ မဟုတ်ပါဘူး။" — "It's nothing special."</li>
<li>Credit others: "သူက သင်ပေးတာ။" — "He/she taught me."</li>
<li>Polite shy smile.</li>
</ul>
<p>Westerners' direct "Thanks!" responses to compliments can feel boastful. Modesty signals good upbringing.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Modesty signals good upbringing.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Burmese typically respond to compliments by:", "options": ["accepting boldly", "deflecting modestly", "ignoring", "asking for more"], "correctIndex": 1},
         {"type": "fill-blank", "question": "\"It's nothing special\": ဘာမှ ___ ပါဘူး။", "answer": "မဟုတ်"},
         {"type": "true-false", "question": "Direct \"Thanks!\" responses can feel boastful.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"He taught me\" credits ___.", "answer": "others"}]},
    {"title": "Practice: Polite Conversation",
     "body_html": r"""
<p>Sample polite exchange:</p>
<p><strong>A (visitor):</strong> "မင်္ဂလာပါ ဦး။ ကျွန်တော် တော်တော် ပျော်ပါတယ်။" — "Hello uncle, I'm very happy (to meet you)."</p>
<p><strong>B (older man):</strong> "ကောင်းပါတယ်။ နေထိုင် ပြပါ။" — "Good. Have a seat."</p>
<p><strong>A:</strong> "မီးနင်ပိုင်လား။ ပေးနိုင်လား။" — "Can I get some water?" (or similar polite request)</p>
<p>The pattern: greet → use honorific → soften request with politeness particle ပါ.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Use honorifics like ဦး in polite conversation.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Politeness particle: ___.", "answer": "ပါ"},
         {"type": "multiple-choice", "question": "ကောင်းပါတယ် means:", "options": ["bad", "good / I'm fine", "sorry", "no"], "correctIndex": 1},
         {"type": "true-false", "question": "Soften requests with politeness particles.", "correctAnswer": True},
         {"type": "fill-blank", "question": "\"Have a seat\": နေထိုင် ___ ပါ။", "answer": "ပြ"}]},
    {"title": "Etiquette Checkpoint",
     "body_html": r"""
<p>Recap of Unit 33:</p>
<ul>
<li>Honorifics: ဦး, ဒေါ်, ကို, မ, မောင် — always use with names of elders.</li>
<li>Temples: shoes off, modest dress, walk clockwise, don't point feet.</li>
<li>Body: head sacred, feet lowest, both hands for important objects.</li>
<li>Speech: politeness particles ပါ, ခင်ဗျား, ရှင်; avoid direct \"no.\"</li>
<li>Public conduct: modest, low-key, no PDA.</li>
<li>Topics: family/food fine; politics very sensitive.</li>
<li>Modesty in receiving compliments is the norm.</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Honorific for older woman: ___.", "answer": "ဒေါ်"},
         {"type": "multiple-choice", "question": "Direction around stupas:", "options": ["counter-clockwise", "clockwise", "either", "spiral"], "correctIndex": 1},
         {"type": "true-false", "question": "Politics is generally a safe topic.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Politeness particle: ___.", "answer": "ပါ"},
         {"type": "true-false", "question": "Burmese head-pat is fine for kids.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Apology: ___ပန်ပါတယ်။.", "answer": "တောင်း"},
         {"type": "true-false", "question": "Use both hands for important objects.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(33, "Burmese Etiquette & Manners", 475, LESSONS)
