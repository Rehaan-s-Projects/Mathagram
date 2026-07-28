#!/usr/bin/env python3
"""Burmese Unit 50 — Films (lessons 730-744)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_burmese import render_unit

LESSONS = [
    {"title": "Burmese Cinema History",
     "body_html": r"""<p>Burmese cinema dates to 1920s. Golden Age: 1950s-60s with stars like Win Oo and Ye Aye. Industry suffered under military rule but revived post-2010.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Burmese cinema dates to the 1920s.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Golden Age era: ", "options": ["1920s", "1950s-60s", "1990s", "2010s"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Cinema: ___ ရှင်ရုံ.", "answer": "ရုပ်"},
         {"type": "true-false", "question": "The industry is centered in Yangon.", "correctAnswer": True},
         {"type": "true-false", "question": "Military rule helped Burmese cinema flourish.", "correctAnswer": False}]},
    {"title": "Genres",
     "body_html": r"""<ul><li>အချစ်ဇာတ် — romance</li><li>တိုက်ပွဲဇာတ် — action</li><li>ရယ်စရာ — comedy</li><li>သရဲ — horror</li><li>ဇာတ်ကြောင်း — drama</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Romance: ___ ဇာတ်.", "answer": "အချစ်"},
         {"type": "multiple-choice", "question": "Horror: ", "options": ["ရယ်စရာ", "သရဲ", "တိုက်ပွဲ", "ဇာတ်ကြောင်း"], "correctIndex": 1},
         {"type": "true-false", "question": "ရယ်စရာ means \"comedy.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Drama: ___ ကြောင်း.", "answer": "ဇာတ်"},
         {"type": "fill-blank", "question": "Action: တိုက် ___ ဇာတ်.", "answer": "ပွဲ"}]},
    {"title": "Movie Theater",
     "body_html": r"""<ul><li>ရုပ်ရှင်ရုံ — cinema</li><li>လက်မှတ် — ticket</li><li>"လက်မှတ် ၂ စောင် ပေးပါ။" — \"2 tickets please.\"</li><li>"ထိုင်ခုံ ဘယ်နေရာလဲ။" — \"Where's the seat?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Cinema: ___ ရှင်ရုံ.", "answer": "ရုပ်"},
         {"type": "multiple-choice", "question": "Ticket: ", "options": ["ထိုင်ခုံ", "လက်မှတ်", "ဇာတ်ကြောင်း", "ရုပ်ရှင်"], "correctIndex": 1},
         {"type": "true-false", "question": "Burmese cinemas sell tickets.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Seat: ___ ခုံ.", "answer": "ထိုင်"},
         {"type": "fill-blank", "question": "Two tickets: ___ စောင်.", "answer": "၂"}]},
    {"title": "Film Vocabulary",
     "body_html": r"""<ul><li>ဇာတ်ညွှန်း — script</li><li>ဒါရိုက်တာ — director (loanword)</li><li>သရုပ်ဆောင် — actor</li><li>ဇာတ်လမ်း — story / plot</li><li>ဇာတ်ဝင်ခန်း — scene</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Director: ___.", "answer": "ဒါရိုက်တာ"},
         {"type": "multiple-choice", "question": "Actor: ", "options": ["ဒါရိုက်တာ", "သရုပ်ဆောင်", "ဇာတ်ညွှန်း", "ဇာတ်ဝင်ခန်း"], "correctIndex": 1},
         {"type": "true-false", "question": "ဇာတ်လမ်း means \"plot.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "Scene: ___ ဝင်ခန်း.", "answer": "ဇာတ်"},
         {"type": "fill-blank", "question": "Script: ___ ညွှန်း.", "answer": "ဇာတ်"}]},
    {"title": "Famous Burmese Actors",
     "body_html": r"""<p>Notable: Win Oo (golden-age leading man), Ye Aye (actress), Khin Hlaing, Eaindra Kyaw Zin (modern), Kyaw Hsu (modern). Recent stars often act in melodramas and romantic comedies.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Win Oo is a golden-age leading man.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Modern Burmese actress:", "options": ["Win Oo", "Ye Aye", "Eaindra Kyaw Zin", "Khin Hlaing"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Acting (career): ___ ဆောင်.", "answer": "သရုပ်"},
         {"type": "true-false", "question": "Modern Burmese cinema features romantic comedies.", "correctAnswer": True},
         {"type": "true-false", "question": "There are no female Burmese actors.", "correctAnswer": False}]},
    {"title": "Watching at Home",
     "body_html": r"""<ul><li>တီဗီ — TV</li><li>ရုပ်ရှင်ကြည့် — to watch a movie</li><li>"အွန်လိုင်းပေါ်မှာ ကြည့်" — \"watch online\"</li><li>"ဘာ လမ်းကြောင်း ကောင်းသလဲ။" — \"What's a good channel?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Watch: ___.", "answer": "ကြည့်"},
         {"type": "multiple-choice", "question": "Online: ", "options": ["အွန်လိုင်း", "ဇာတ်ကြောင်း", "ထိုင်ခုံ", "ဆီးနီမာ"], "correctIndex": 0},
         {"type": "true-false", "question": "Streaming has grown in Myanmar.", "correctAnswer": True},
         {"type": "fill-blank", "question": "TV: ___.", "answer": "တီဗီ"},
         {"type": "true-false", "question": "Cinemas are the only place to watch films.", "correctAnswer": False}]},
    {"title": "Reviewing a Film",
     "body_html": r"""<ul><li>"ဒီရုပ်ရှင် ကောင်းတယ်။" — \"This movie is good.\"</li><li>"ဇာတ်ကြောင်း ထူးခြားတယ်။" — \"The plot is unique.\"</li><li>"အစ မှာ နှေးတယ်။" — \"Slow at the start.\"</li><li>"အဆုံးမှာ ကြိုက်တယ်။" — \"Liked the ending.\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Good: ___ တယ်.", "answer": "ကောင်း"},
         {"type": "multiple-choice", "question": "Slow: ", "options": ["ထူးခြား", "နှေး", "ကြိုက်", "ကောင်း"], "correctIndex": 1},
         {"type": "true-false", "question": "Reviews can mention pacing.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Ending: ___ ဆုံး.", "answer": "အ"},
         {"type": "fill-blank", "question": "Liked: ___ တယ်.", "answer": "ကြိုက်"}]},
    {"title": "Film Festivals",
     "body_html": r"""<p>Yangon hosts the Yangon Film Festival; international films screen alongside Burmese productions. Independent (\"indie\") films have grown in last decade.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Yangon hosts a film festival.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Indie films are:", "options": ["state-funded", "independent", "imported only", "extinct"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Festival: ___.", "answer": "ပွဲတော်"},
         {"type": "true-false", "question": "International films screen at Yangon's festival.", "correctAnswer": True},
         {"type": "true-false", "question": "Independent Burmese cinema is shrinking.", "correctAnswer": False}]},
    {"title": "Subtitles & Dubbing",
     "body_html": r"""<ul><li>စာတန်းထိုး — subtitles</li><li>အသံသွင်း — dubbing</li><li>"အင်္ဂလိပ်စာတန်း ရှိလား။" — \"Are there English subtitles?\"</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Subtitle: ___ ထိုး.", "answer": "စာတန်း"},
         {"type": "multiple-choice", "question": "Dubbing: ", "options": ["စာတန်းထိုး", "အသံသွင်း", "အင်္ဂလိပ်", "ဇာတ်လမ်း"], "correctIndex": 1},
         {"type": "true-false", "question": "English subtitles may be available.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Voice-track: ___ သွင်း.", "answer": "အသံ"},
         {"type": "true-false", "question": "All foreign films are auto-dubbed in Burmese.", "correctAnswer": False}]},
    {"title": "Children's Films",
     "body_html": r"""<p>Genre: children's animation, often blending Burmese folktales with modern animation. Local studios produce educational shorts on Buddhism, hygiene, civic values.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Children's films often blend folktales and modern animation.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Educational shorts cover:", "options": ["nuclear physics", "Buddhism, hygiene, civic values", "stock trading", "tank battles"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Animation: ___ ကာတွန်း.", "answer": "ရုပ်ရှင်"},
         {"type": "true-false", "question": "Local animation studios exist.", "correctAnswer": True},
         {"type": "true-false", "question": "Burmese children only watch foreign films.", "correctAnswer": False}]},
    {"title": "Documentary Films",
     "body_html": r"""<p>Documentaries on history, ethnic culture, environmental issues — including some controversial works on the 2021 coup, exile communities, and the Rohingya.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Documentaries cover Burmese history and culture.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Some documentaries are:", "options": ["always government-backed", "controversial", "always Burmese-funded", "extinct"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Documentary: ___ ဇာတ်ကြောင်း.", "answer": "မှန်"},
         {"type": "true-false", "question": "Some documentaries cover the 2021 coup.", "correctAnswer": True},
         {"type": "true-false", "question": "Documentaries are unimportant.", "correctAnswer": False}]},
    {"title": "Foreign Films Influence",
     "body_html": r"""<p>Indian Bollywood, Hollywood, Korean dramas (K-drama) all popular. Younger Burmese fluent in English/Korean partly through media. K-pop and K-drama strongly influence youth culture.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Korean K-drama is popular in Myanmar.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Influences:", "options": ["only Burmese", "Bollywood, Hollywood, K-drama", "only Hollywood", "only Chinese"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Bollywood influence: ___ မြင်း.", "answer": "အိန္ဒိ"},
         {"type": "true-false", "question": "K-pop influences Burmese youth.", "correctAnswer": True},
         {"type": "true-false", "question": "Foreign films have no influence on Burmese youth.", "correctAnswer": False}]},
    {"title": "Awards",
     "body_html": r"""<ul><li>အကယ်ဒမီ ဆု — Academy Award (Burmese)</li><li>"ဆုရှင်" — winner</li><li>"အကောင်းဆုံး ရုပ်ရှင်" — best film</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Award: ___.", "answer": "ဆု"},
         {"type": "multiple-choice", "question": "Winner: ", "options": ["ရုပ်ရှင်", "ဆုရှင်", "အကယ်ဒမီ", "အကောင်းဆုံး"], "correctIndex": 1},
         {"type": "true-false", "question": "Burmese has its own Academy Awards.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Best: ___ ဆုံး.", "answer": "အကောင်း"},
         {"type": "true-false", "question": "Awards exist in Burmese cinema.", "correctAnswer": True}]},
    {"title": "Practice: Recommend a Film",
     "body_html": r"""<p>Sample dialogue:</p><p><strong>A:</strong> "မင်းကြိုက်တဲ့ ရုပ်ရှင် ဘာလဲ။"</p><p><strong>B:</strong> "ငါ အချစ်ဇာတ် ကြိုက်တယ်။ မင်း ဘာကြိုက်သလဲ။"</p><p><strong>A:</strong> "ငါက သရဲ ဇာတ်လမ်း ပိုကြိုက်တယ်။"</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "I prefer (more): ___ ကြိုက်.", "answer": "ပို"},
         {"type": "multiple-choice", "question": "Romance films: ", "options": ["သရဲ", "အချစ်ဇာတ်", "ရယ်စရာ", "တိုက်ပွဲ"], "correctIndex": 1},
         {"type": "true-false", "question": "ငါ is informal \"I.\"", "correctAnswer": True},
         {"type": "fill-blank", "question": "What films: ___ ရုပ်ရှင်.", "answer": "ဘာ"},
         {"type": "true-false", "question": "Genres are debated by friends.", "correctAnswer": True}]},
    {"title": "Films Checkpoint",
     "body_html": r"""<p>Recap of Unit 50:</p><ul><li>Cinema since 1920s; Golden Age 1950s-60s.</li><li>Genres: အချစ်ဇာတ် (romance), တိုက်ပွဲဇာတ် (action), ရယ်စရာ (comedy), သရဲ (horror).</li><li>Players: ဒါရိုက်တာ (director), သရုပ်ဆောင် (actor).</li><li>Theater: ရုပ်ရှင်ရုံ; ticket: လက်မှတ်.</li><li>Foreign influences: Bollywood, Hollywood, K-drama.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Cinema: ___ ရုံ.", "answer": "ရုပ်ရှင်"},
         {"type": "multiple-choice", "question": "K-drama is from:", "options": ["China", "India", "Korea", "Japan"], "correctIndex": 2},
         {"type": "true-false", "question": "Golden Age was 1950s-60s.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Romance: ___ ဇာတ်.", "answer": "အချစ်"},
         {"type": "fill-blank", "question": "Director: ___.", "answer": "ဒါရိုက်တာ"},
         {"type": "true-false", "question": "Subtitles can be in English.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Best film: အကောင်းဆုံး ___.", "answer": "ရုပ်ရှင်"}]},
]

if __name__ == "__main__":
    render_unit(50, "Burmese Films", 730, LESSONS)
