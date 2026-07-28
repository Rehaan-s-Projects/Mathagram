#!/usr/bin/env python3
"""Burmese Unit 52 — Songs & Lyrics (lessons 760-774)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Burmese Music Overview",
     "body_html": r"""<p>Burmese music has classical (saing waing ensemble), folk (regional traditions), and modern pop scenes. Many young singers blend Burmese melodies with Western pop arrangements.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Music: ___.", "answer": "ဂီတ"},
         {"type": "multiple-choice", "question": "Classical orchestra: ", "options": ["saing waing", "K-pop", "marching", "rock"], "correctIndex": 0},
         {"type": "true-false", "question": "Modern Burmese pop blends Western arrangements.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pop: ___.", "answer": "ပေါ့ပ်"},
         {"type": "true-false", "question": "Burmese has only one music genre.", "correctAnswer": False}]},
    {"title": "Traditional Instruments",
     "body_html": r"""<ul><li>စောင်း — saung (harp)</li><li>ပတ်တင် — patala (xylophone)</li><li>ဆိုင်းဝိုင်း — saing waing (drum circle)</li><li>ပလွေ — pa-le (flute)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Burmese harp: ___.", "answer": "စောင်း"},
         {"type": "multiple-choice", "question": "Xylophone: ", "options": ["ဆိုင်းဝိုင်း", "ပတ်တင်", "စောင်း", "ပလွေ"], "correctIndex": 1},
         {"type": "true-false", "question": "Saing waing is a drum circle.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Flute: ___.", "answer": "ပလွေ"},
         {"type": "true-false", "question": "Saung is considered Myanmar's national instrument.", "correctAnswer": True}]},
    {"title": "Folk Songs",
     "body_html": r"""<p>Burmese folk songs (ကျေးလက်တေးချင်း) often celebrate harvest, festivals, love, and longing for home. Each region has distinctive folk traditions.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Folk song: ___ လက်တေးချင်း.", "answer": "ကျေး"},
         {"type": "multiple-choice", "question": "Common folk theme:", "options": ["computers", "harvest, festivals, love", "stocks", "war planes"], "correctIndex": 1},
         {"type": "true-false", "question": "Folk songs vary by region.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Song: ___ ချင်း.", "answer": "တေး"},
         {"type": "true-false", "question": "All Myanmar regions have identical folk songs.", "correctAnswer": False}]},
    {"title": "Kaba Ma Kyei — National Anthem",
     "body_html": r"""<p>The Burmese national anthem is \"Kaba Ma Kyei\" (\"Till the End of the World\"), written 1947. Sung at official ceremonies, schools, and broadcast openings.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "National anthem: ___ Ma Kyei.", "answer": "Kaba"},
         {"type": "multiple-choice", "question": "Anthem written:", "options": ["1820", "1947", "1990", "2010"], "correctIndex": 1},
         {"type": "true-false", "question": "Anthem means \"Till the End of the World.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Anthem: ___ မ ကြွေး.", "answer": "ကမ္ဘာ"},
         {"type": "true-false", "question": "Burmese national anthem dates to 1820.", "correctAnswer": False}]},
    {"title": "Modern Burmese Pop Stars",
     "body_html": r"""<p>Notable: Sai Sai Kham Leng, Phyu Phyu Kyaw Thein, Wai La, R Zarni. They blend romantic ballads, electronic, and Western pop. Online streaming and YouTube launched many careers.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Sai Sai Kham Leng is a Burmese pop star.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Popular launch platform:", "options": ["pirate radio", "YouTube", "vinyl only", "no platforms"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Star: ___.", "answer": "ကြယ်ပွင့်"},
         {"type": "true-false", "question": "Modern Burmese pop is internationally streamed.", "correctAnswer": True},
         {"type": "true-false", "question": "All pop stars are male.", "correctAnswer": False}]},
    {"title": "Karaoke Culture",
     "body_html": r"""<p>Karaoke (\"KTV\") is a major Burmese pastime. Bars and home setups are common; popular songs include slow ballads, K-pop covers, and Burmese hits.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Karaoke is a popular pastime.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "KTV bars often feature:", "options": ["slow ballads", "only metal", "no Burmese songs", "instrumentals only"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Sing: ___ ပါ.", "answer": "သီဆို"},
         {"type": "true-false", "question": "K-pop covers are common.", "correctAnswer": True},
         {"type": "true-false", "question": "Karaoke is rare in Myanmar.", "correctAnswer": False}]},
    {"title": "Lyric Themes",
     "body_html": r"""<p>Common pop lyric themes:</p><ul><li>အချစ် (love)</li><li>လွမ်းဆွတ် (longing)</li><li>စိတ်ပျော် (joy)</li><li>စိတ်ရှုပ် (heartbreak)</li><li>သူငယ်ချင်း (friendship)</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Love: ___.", "answer": "အချစ်"},
         {"type": "multiple-choice", "question": "Heartbreak: ", "options": ["စိတ်ပျော်", "စိတ်ရှုပ်", "လွမ်းဆွတ်", "သူငယ်ချင်း"], "correctIndex": 1},
         {"type": "true-false", "question": "လွမ်းဆွတ် means \"longing.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Friendship: ___ ချင်း.", "answer": "သူငယ်"},
         {"type": "fill-blank", "question": "Joy: စိတ် ___.", "answer": "ပျော်"}]},
    {"title": "Reading Lyrics",
     "body_html": r"""<p>Lyrics often use poetic, slightly archaic Burmese. Don't expect colloquial speech. Imagery: moon, river, longing, the beloved's face.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Lyrics often use poetic Burmese.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Common imagery:", "options": ["robots", "moon, river, beloved's face", "computers", "cars"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Moon: ___.", "answer": "လ"},
         {"type": "true-false", "question": "Lyrics typically use casual slang only.", "correctAnswer": False},
         {"type": "fill-blank", "question": "River: ___.", "answer": "မြစ်"}]},
    {"title": "Hip-Hop & Rap",
     "body_html": r"""<p>Hip-hop has grown in Myanmar; artists like J-Me, Sai Sai (early hits), and others rap in Burmese on social and political themes. The 2010s saw a hip-hop boom.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Hip-hop grew in 2010s Myanmar.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Hip-hop in Burmese: ", "options": ["non-existent", "growing scene", "only English", "purely classical"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Rap: ___.", "answer": "ရတ်ပ်"},
         {"type": "true-false", "question": "Burmese rap covers social themes.", "correctAnswer": True},
         {"type": "true-false", "question": "Hip-hop is alien to Myanmar.", "correctAnswer": False}]},
    {"title": "Album Vocabulary",
     "body_html": r"""<ul><li>အယ်လ်ဘမ် — album</li><li>သီချင်း — song</li><li>သီဆို — to sing</li><li>တေးရေး — songwriter</li><li>စတူဒီယို — studio</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Song: ___.", "answer": "သီချင်း"},
         {"type": "multiple-choice", "question": "Album: ", "options": ["သီချင်း", "အယ်လ်ဘမ်", "တေးရေး", "သီဆို"], "correctIndex": 1},
         {"type": "true-false", "question": "Songwriter is တေးရေး.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Studio: ___ ဒီယို.", "answer": "စတူ"},
         {"type": "fill-blank", "question": "To sing: သီ ___.", "answer": "ဆို"}]},
    {"title": "Religious Music",
     "body_html": r"""<p>Buddhist chants and devotional songs are everyday music. Pali chants are recited at temples; modern devotional pop also exists.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Buddhist chants are part of everyday music.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Pali is used in:", "options": ["pop", "chants at temples", "rap", "K-pop"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Devotional: ___ ရေး.", "answer": "ဘာသာ"},
         {"type": "true-false", "question": "Modern devotional pop exists.", "correctAnswer": True},
         {"type": "true-false", "question": "Religious music is extinct in Myanmar.", "correctAnswer": False}]},
    {"title": "Concert Vocabulary",
     "body_html": r"""<ul><li>ဂီတပွဲ — concert</li><li>ပရိသတ် — audience</li><li>"လက်မှတ် ဘယ်နှ ကျပ်လဲ။" — \"How much is the ticket?\"</li><li>"စင်မြင့်ပေါ်" — onstage</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Concert: ___ ပွဲ.", "answer": "ဂီတ"},
         {"type": "multiple-choice", "question": "Audience: ", "options": ["ပရိသတ်", "လက်မှတ်", "စင်မြင့်", "ဂီတ"], "correctIndex": 0},
         {"type": "true-false", "question": "Burmese has live concerts.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Onstage: စင်မြင့် ___.", "answer": "ပေါ်"},
         {"type": "fill-blank", "question": "How much: ဘယ် ___ လဲ.", "answer": "နှ ကျပ်"}]},
    {"title": "Music Apps",
     "body_html": r"""<ul><li>Joox, Spotify, YouTube Music — popular streaming.</li><li>"လိုင်စင်ရှိ ဆော့ဖ်ဝဲ" — licensed app</li><li>"ဒေါင်းလုပ်" — to download</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Download: ___.", "answer": "ဒေါင်းလုပ်"},
         {"type": "multiple-choice", "question": "Popular streaming:", "options": ["Joox, Spotify, YouTube Music", "Vinyl only", "Cassettes", "Radio only"], "correctIndex": 0},
         {"type": "true-false", "question": "Music streaming is popular.", "correctAnswer": True},
         {"type": "fill-blank", "question": "License: ___.", "answer": "လိုင်စင်"},
         {"type": "true-false", "question": "Burmese stream music online.", "correctAnswer": True}]},
    {"title": "Practice: A Famous Lyric",
     "body_html": r"""<p>Sample line (modern pop):</p><p style="text-align:center;font-size:1.2em;"><em>"လူတိုင်း လို့ ကြိုက်တတ်ပါတယ်၊ မင်း ပျော်ရင် ငါ ပျော်တယ်။"</em></p><p>"Everyone has someone they love; if you're happy, I'm happy."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Everyone: လူ ___.", "answer": "တိုင်း"},
         {"type": "multiple-choice", "question": "Happy: ", "options": ["ပျော်", "ဖျား", "နာ", "ကောင်း"], "correctIndex": 0},
         {"type": "true-false", "question": "မင်း means \"you\" (informal).", "correctAnswer": True},
         {"type": "fill-blank", "question": "I: ___.", "answer": "ငါ"},
         {"type": "true-false", "question": "Pop lyrics often address \"you.\"", "correctAnswer": True}]},
    {"title": "Songs Checkpoint",
     "body_html": r"""<p>Recap of Unit 52:</p><ul><li>Music genres: classical (saing waing), folk, pop, hip-hop.</li><li>Instruments: စောင်း (harp), ပတ်တင် (xylophone), ပလွေ (flute).</li><li>Anthem: \"Kaba Ma Kyei\" (1947).</li><li>Lyrics: love, longing, joy, heartbreak.</li><li>Streaming: Joox, Spotify, YouTube Music.</li><li>Karaoke and hip-hop are growing scenes.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Song: ___.", "answer": "သီချင်း"},
         {"type": "multiple-choice", "question": "Saung is a:", "options": ["xylophone", "harp", "drum", "flute"], "correctIndex": 1},
         {"type": "true-false", "question": "Karaoke is popular.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Anthem: ___ Ma Kyei.", "answer": "Kaba"},
         {"type": "fill-blank", "question": "Album: ___.", "answer": "အယ်လ်ဘမ်"},
         {"type": "true-false", "question": "Burmese has only one musical genre.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Concert: ဂီတ ___.", "answer": "ပွဲ"}]},
]

if __name__ == "__main__":
    render_unit(52, "Burmese Songs & Lyrics", 760, LESSONS)
