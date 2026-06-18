#!/usr/bin/env python3
"""Burmese Unit 30 — Dialects (lessons 430-444)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Standard Burmese (Yangon)",
     "body_html": r"""
<p>The official, prestige variety is <strong>Standard Burmese</strong> — the dialect of Yangon (formerly Rangoon), spoken in the country's largest city and used in education, broadcasting, and government.</p>
<p>This is the variety taught in most courses and reflected in dictionaries. When Burmese is referenced without qualification, this is what's meant.</p>
<p>Within Yangon there's still informal/formal register variation, plus class and age-based differences. But across regions, Yangon dialect is universally understood.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Standard Burmese is based on the Yangon dialect.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Yangon was formerly known as:", "options": ["Mandalay", "Naypyidaw", "Rangoon", "Bagan"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Standard Burmese is used in education and ___.", "answer": "broadcasting"},
         {"type": "true-false", "question": "Burmese has only one spoken variety.", "correctAnswer": False},
         {"type": "true-false", "question": "Yangon dialect is universally understood across Myanmar.", "correctAnswer": True}]},
    {"title": "Mandalay Dialect",
     "body_html": r"""
<p>Mandalay was Myanmar's last royal capital and is the country's second-largest city. <strong>Mandalay Burmese</strong> differs subtly from Yangon:</p>
<ul>
<li>Slightly more conservative pronunciations (closer to spelling).</li>
<li>Some lexical differences: ဘယ်လို (how) is more commonly bal-lo than bay-lo.</li>
<li>Final glottal stops can be more clearly articulated.</li>
<li>Tone realization can sound flatter to Yangonites.</li>
</ul>
<p>Differences are minor — a Yangonite and a Mandalayan converse without difficulty.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Mandalay was Myanmar's last royal capital.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Mandalay dialect compared to Yangon:", "options": ["wholly unintelligible", "subtly different but mutually intelligible", "identical", "uses different script"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Mandalay is Myanmar's ___-largest city.", "answer": "second"},
         {"type": "true-false", "question": "Mandalay pronunciations are closer to spelling.", "correctAnswer": True},
         {"type": "true-false", "question": "Mandalay uses a different writing system.", "correctAnswer": False}]},
    {"title": "Rakhine (Arakanese)",
     "body_html": r"""
<p><strong>Rakhine</strong> (also called Arakanese) is spoken in the western Rakhine State, along the Bay of Bengal coast. It's the most divergent Burmese dialect — sometimes considered a separate language.</p>
<p>Distinctive features:</p>
<ul>
<li>Preserves the /r/ sound that has merged with /y/ in standard Burmese.</li>
<li>Different tonal system (similar but not identical).</li>
<li>Different lexicon for many everyday words.</li>
<li>Cultural influence from Bangladesh and India.</li>
</ul>
<p>Rakhine speakers can usually understand standard Burmese, but the reverse can be challenging.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Rakhine is also called ___.", "answer": "Arakanese"},
         {"type": "multiple-choice", "question": "Rakhine preserves a sound merged in Standard Burmese:", "options": ["/r/", "/v/", "/z/", "/sh/"], "correctIndex": 0},
         {"type": "true-false", "question": "Rakhine is the most divergent Burmese dialect.", "correctAnswer": True},
         {"type": "true-false", "question": "Rakhine speakers can rarely understand standard Burmese.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Rakhine state is on the ___ coast of Myanmar.", "answer": "western"}]},
    {"title": "Tavoyan (Dawei)",
     "body_html": r"""
<p><strong>Tavoyan</strong> (Dawei) is spoken in the Tanintharyi Region in the south. It preserves several archaic features of older Burmese.</p>
<ul>
<li>Conservative consonant clusters.</li>
<li>Older vowel pronunciations.</li>
<li>Vocabulary borrowed from Mon (a Mon-Khmer language).</li>
</ul>
<p>Tavoyan is mutually intelligible with Standard Burmese, but takes some effort. Speakers often shift to Standard when speaking to outsiders.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Tavoyan preserves archaic features.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tavoyan is spoken in the ___ region.", "answer": "Tanintharyi"},
         {"type": "multiple-choice", "question": "Tavoyan has borrowed vocabulary from:", "options": ["Mandarin", "Mon", "Hindi", "Vietnamese"], "correctIndex": 1},
         {"type": "true-false", "question": "Tavoyan and Standard Burmese are mutually unintelligible.", "correctAnswer": False},
         {"type": "true-false", "question": "Speakers often switch to Standard for outsiders.", "correctAnswer": True}]},
    {"title": "Intha (Inle Lake)",
     "body_html": r"""
<p><strong>Intha</strong> ("sons of the lake") is spoken by the people of Inle Lake in Shan State. Despite living in a Shan-majority area, the Intha speak a Burmese dialect.</p>
<p>Features:</p>
<ul>
<li>Similar to Tavoyan in many ways (theory: the Intha migrated from Tavoy long ago).</li>
<li>Preserves the /r/ where Standard has /y/.</li>
<li>Specific fishing and lake-life vocabulary.</li>
</ul>
<p>Famous Intha cultural feature: leg-rowing fishermen on Inle Lake.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Intha means \"sons of the ___\".", "answer": "lake"},
         {"type": "multiple-choice", "question": "Intha is spoken at:", "options": ["Yangon", "Inle Lake", "Bagan", "Naypyidaw"], "correctIndex": 1},
         {"type": "true-false", "question": "Intha is a Shan dialect, not a Burmese dialect.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Inle Lake is famous for ___-rowing fishermen.", "answer": "leg"},
         {"type": "true-false", "question": "Intha shares features with Tavoyan.", "correctAnswer": True}]},
    {"title": "Yaw Dialect",
     "body_html": r"""
<p><strong>Yaw</strong> dialect is spoken in Magway Region in central Myanmar. It's relatively conservative and shares features with both Standard Burmese and Rakhine.</p>
<p>Distinctive vocabulary in everyday domains: weather words, agricultural terms, kinship terms. Yaw speakers may use particles in slightly different positions than Standard.</p>
<p>Modern media exposure means many Yaw speakers are fully bidialectal — fluent in both Yaw and Standard.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Yaw is spoken in Magway Region.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Yaw shares features with:", "options": ["Yangon only", "Rakhine only", "both Standard and Rakhine", "no other dialects"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Many Yaw speakers are ___ — fluent in Yaw and Standard.", "answer": "bidialectal"},
         {"type": "true-false", "question": "Yaw is the most divergent Burmese dialect.", "correctAnswer": False},
         {"type": "true-false", "question": "Modern media has increased Standard Burmese exposure.", "correctAnswer": True}]},
    {"title": "Mergui (Myeik) Dialect",
     "body_html": r"""
<p><strong>Mergui</strong> (Myeik) is spoken in the southern Mergui Archipelago and surrounding coastal areas. The dialect shares Tavoyan's conservatism but with extra Malay and Thai loanwords from coastal trade.</p>
<p>The Moken (sea nomads) live in this region and speak a different language entirely (Austronesian); Burmese-Mergui dialect is the regional Burmese variety.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mergui is also written as ___.", "answer": "Myeik"},
         {"type": "multiple-choice", "question": "Mergui has loanwords from:", "options": ["Russian and Chinese", "Malay and Thai", "French", "Arabic"], "correctIndex": 1},
         {"type": "true-false", "question": "The Moken speak a different language from Burmese.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Mergui is in the ___ Archipelago.", "answer": "Mergui"},
         {"type": "true-false", "question": "Mergui shares Tavoyan's conservatism.", "correctAnswer": True}]},
    {"title": "Beik Dialect Notes",
     "body_html": r"""
<p>The <strong>Beik</strong> variant is sometimes treated as part of Mergui, sometimes as a separate dialect. It's spoken in coastal villages of the deep south.</p>
<p>Beik shows features:</p>
<ul>
<li>Strong /r/ retention.</li>
<li>Slower speech tempo than Yangon.</li>
<li>Coastal/maritime vocabulary not found in interior dialects.</li>
</ul>
<p>Like all southern Burmese dialects, increasingly merging with Standard via media and migration.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Beik retains the /r/ sound.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Beik is in the:", "options": ["far north", "central plateau", "deep south coast", "western mountains"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Beik has ___ vocabulary not found inland.", "answer": "maritime"},
         {"type": "true-false", "question": "Southern dialects are increasingly merging with Standard.", "correctAnswer": True},
         {"type": "true-false", "question": "Beik speech is faster than Yangon's.", "correctAnswer": False}]},
    {"title": "Tonal Differences Across Dialects",
     "body_html": r"""
<p>While all Burmese dialects have the three-tone system, the realization differs:</p>
<ul>
<li>Yangon: clear high-low distinction; creaky tone is sharply short.</li>
<li>Mandalay: tonal contrasts slightly less stark; high tone less falling.</li>
<li>Rakhine: tones may be realized differently, sometimes with extra register distinctions.</li>
<li>Tavoyan/Mergui: tones are slower, with lengthened vowels.</li>
</ul>
<p>For learners: stick with Yangon-style tones initially. You'll adjust to regional varieties through exposure.</p>""",
     "exercises": [
         {"type": "true-false", "question": "All Burmese dialects use a three-tone system.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Tonal contrasts are slightly less stark in:", "options": ["Yangon", "Mandalay", "Rakhine", "all the same"], "correctIndex": 1},
         {"type": "fill-blank", "question": "For learners, start with ___-style tones.", "answer": "Yangon"},
         {"type": "true-false", "question": "Tavoyan tones tend to be slower.", "correctAnswer": True},
         {"type": "true-false", "question": "Rakhine has fewer tonal distinctions than Yangon.", "correctAnswer": False}]},
    {"title": "Vocabulary Differences",
     "body_html": r"""
<p>Sample vocabulary differences:</p>
<table style="margin:0 auto; border-collapse: collapse;">
<tr><th style="border-bottom:1px solid #ccc; padding:4px 12px;">Meaning</th><th style="border-bottom:1px solid #ccc; padding:4px 12px;">Yangon</th><th style="border-bottom:1px solid #ccc; padding:4px 12px;">Rakhine</th></tr>
<tr><td style="padding:4px 12px;">water</td><td style="padding:4px 12px;">ye (ရေ)</td><td style="padding:4px 12px;">ré</td></tr>
<tr><td style="padding:4px 12px;">man</td><td style="padding:4px 12px;">yauk-kya</td><td style="padding:4px 12px;">rauk-kya</td></tr>
<tr><td style="padding:4px 12px;">good</td><td style="padding:4px 12px;">kaung</td><td style="padding:4px 12px;">kaung (similar)</td></tr>
</table>
<p>Notice the /r/ vs /y/ pattern. This single sound shift accounts for many vocabulary differences between Rakhine and Yangon.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Yangon \"water\" is ___, Rakhine has /r/.", "answer": "ye"},
         {"type": "multiple-choice", "question": "The main sound shift is:", "options": ["/p/ ↔ /b/", "/r/ ↔ /y/", "/k/ ↔ /h/", "/t/ ↔ /d/"], "correctIndex": 1},
         {"type": "true-false", "question": "\"Good\" is similar across dialects.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Rakhine \"man\" is rauk-kya; Yangon is ___-kya.", "answer": "yauk"},
         {"type": "true-false", "question": "Vocabulary differences are usually predictable from sound shifts.", "correctAnswer": True}]},
    {"title": "Grammatical Differences",
     "body_html": r"""
<p>Grammatical differences across dialects are smaller than vocabulary or pronunciation:</p>
<ul>
<li>Particle usage may vary slightly (e.g., subject markers).</li>
<li>Some dialects use older or alternative tense markers.</li>
<li>Honorific particles may differ in formal/informal split.</li>
<li>Word order and sentence structure are virtually identical.</li>
</ul>
<p>If you've learned Standard Burmese grammar, you can read or speak with anyone in Myanmar — vocabulary and accent are the main hurdles.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Word order is virtually the same across Burmese dialects.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Main learner hurdles across dialects:", "options": ["script", "grammar", "vocabulary and accent", "no hurdles"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Standard grammar lets you communicate ___-wide.", "answer": "country"},
         {"type": "true-false", "question": "Burmese grammar varies wildly across dialects.", "correctAnswer": False},
         {"type": "true-false", "question": "Honorific particles can differ across dialects.", "correctAnswer": True}]},
    {"title": "When to Use Standard",
     "body_html": r"""
<p>For learners, Standard Burmese is the default and the right choice for:</p>
<ul>
<li>Formal speech (work, government, school).</li>
<li>Speaking to strangers (especially outside your local area).</li>
<li>Broadcast media and printed publications.</li>
<li>Teaching and learning materials.</li>
</ul>
<p>Use a regional dialect when:</p>
<ul>
<li>Speaking with friends and family from that region.</li>
<li>Identity / community signaling within local communities.</li>
<li>Specific regional cultural events.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Standard Burmese is the default for learners.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "When NOT to use Standard:", "options": ["with strangers", "in formal speech", "with family in your home region (informal)", "in news"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Broadcast media uses ___ Burmese.", "answer": "Standard"},
         {"type": "true-false", "question": "Dialect use is purely incidental, never identity-related.", "correctAnswer": False},
         {"type": "true-false", "question": "Schools teach Standard Burmese.", "correctAnswer": True}]},
    {"title": "Mutual Intelligibility",
     "body_html": r"""
<p>Most Burmese dialects are mutually intelligible with Standard, with some effort:</p>
<ul>
<li>Yangon ↔ Mandalay: very high, almost effortless.</li>
<li>Yangon ↔ Tavoyan/Mergui: medium; takes attention.</li>
<li>Yangon ↔ Rakhine: lower; trained ear needed.</li>
<li>Yangon ↔ Intha: medium.</li>
</ul>
<p>Some scholars consider Rakhine a separate language. The line between "language" and "dialect" is fuzzy and political — speakers of all these varieties identify as Burmese-speakers.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "Yangon ↔ Mandalay intelligibility is:", "options": ["very low", "medium", "very high", "zero"], "correctIndex": 2},
         {"type": "true-false", "question": "Some scholars consider Rakhine a separate language.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Yangon ↔ Rakhine intelligibility requires a trained ___.", "answer": "ear"},
         {"type": "true-false", "question": "All dialect speakers identify as Burmese-speakers.", "correctAnswer": True},
         {"type": "true-false", "question": "Yangon ↔ Tavoyan is effortlessly intelligible.", "correctAnswer": False}]},
    {"title": "Practice: Identify the Dialect",
     "body_html": r"""
<p>Sample sentences. Can you guess the dialect?</p>
<ol>
<li>"ရေ ပေးပါ" (ye pay ba) — "Give me water." → <strong>Standard Yangon</strong>.</li>
<li>"ré pay ba" → <strong>Rakhine</strong> (note /r/ retention).</li>
<li>"Slow, slightly drawled tones, southern coastal lexicon" → likely <strong>Tavoyan or Mergui</strong>.</li>
<li>Crisp, formal, sharp creaky tones → <strong>Yangon educated speech</strong>.</li>
<li>Slightly more conservative, Mandalay-area vocabulary → <strong>Mandalay</strong>.</li>
</ol>""",
     "exercises": [
         {"type": "multiple-choice", "question": "\"ré pay ba\" suggests:", "options": ["Yangon", "Rakhine", "Mandalay", "Tavoyan"], "correctIndex": 1},
         {"type": "true-false", "question": "Conservative vocabulary suggests Mandalay.", "correctAnswer": True},
         {"type": "fill-blank", "question": "/r/ retention is a hallmark of ___.", "answer": "Rakhine"},
         {"type": "true-false", "question": "Crisp formal speech is typical of urban Yangon.", "correctAnswer": True},
         {"type": "true-false", "question": "All these examples are mutually unintelligible.", "correctAnswer": False}]},
    {"title": "Dialects Checkpoint",
     "body_html": r"""
<p>Recap of Unit 30:</p>
<ul>
<li>Standard Burmese (Yangon) is the default; learn it first.</li>
<li>Mandalay is similar but slightly more conservative.</li>
<li>Rakhine is the most divergent — preserves /r/ and has different vocabulary.</li>
<li>Tavoyan, Mergui, Beik, Intha preserve archaic features.</li>
<li>Vocabulary differences are usually predictable from sound shifts.</li>
<li>Grammar is mostly uniform across dialects.</li>
<li>Mutual intelligibility ranges from very high (Mandalay) to medium (Rakhine).</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Standard Burmese is based on Yangon.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Most divergent Burmese dialect:", "options": ["Mandalay", "Rakhine", "Yangon", "Yaw"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Rakhine retains the /___/ sound.", "answer": "r"},
         {"type": "true-false", "question": "Burmese grammar varies dramatically across dialects.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Intha live at ___ Lake.", "answer": "Inle"},
         {"type": "true-false", "question": "Yangon ↔ Mandalay is essentially effortless.", "correctAnswer": True},
         {"type": "true-false", "question": "Tavoyan preserves archaic Burmese features.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(30, "Burmese Dialects", 430, LESSONS)
