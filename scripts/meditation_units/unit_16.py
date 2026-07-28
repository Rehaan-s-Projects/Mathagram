#!/usr/bin/env python3
"""Meditation Unit 16 — Sufi & Islamic Meditation (lessons 226-240)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Sufism — The Heart of Islam",
     "body_html": r"""<p>Sufism (<em>tasawwuf</em>) is the inner, mystical path within Islam. It centers on remembrance of God (<em>dhikr</em>), love, and the polishing of the heart.</p><ul><li>Arabic: <em>tasawwuf</em>.</li><li>Practitioners: Sufis, dervishes, fakirs.</li><li>Major orders: Naqshbandi, Qadiri, Mevlevi, Shadhili.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Arabic for Sufism: ___.", "answer": "tasawwuf"},
         {"type": "multiple-choice", "question": "Major Sufi order: ", "options": ["Mevlevi", "Soto", "Gelug", "Quaker"], "correctIndex": 0},
         {"type": "true-false", "question": "Sufism is the inner path of Islam.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Practitioner term: ___.", "answer": "dervish"},
         {"type": "true-false", "question": "Sufism rejects all of Islam.", "correctAnswer": False}]},
    {"title": "Dhikr — Remembrance",
     "body_html": r"""<p>Dhikr (<em>zikr</em>) is the practice of remembering God through repetition of His names or short phrases:</p><ul><li>La ilaha illa Allah — "There is no god but God."</li><li>Allah hu — "God, He."</li><li>Subhan Allah, Alhamdulillah, Allahu Akbar.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Remembrance: ___.", "answer": "dhikr"},
         {"type": "multiple-choice", "question": "Phrase: ", "options": ["La ilaha illa Allah", "Om Mani Padme Hum", "Hare Krishna", "Shema Yisrael"], "correctIndex": 0},
         {"type": "true-false", "question": "Dhikr can be silent or aloud.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Subhan ___.", "answer": "Allah"},
         {"type": "true-false", "question": "Dhikr means forgetting.", "correctAnswer": False}]},
    {"title": "The 99 Names of God",
     "body_html": r"""<p>Tradition lists 99 Beautiful Names (<em>al-Asma al-Husna</em>): Ar-Rahman (Most Merciful), Ar-Rahim (Most Compassionate), Al-Salaam (Peace), An-Nur (Light). Each can be a meditation focus.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "There are ___ Beautiful Names.", "answer": "99"},
         {"type": "multiple-choice", "question": "Most Merciful: ", "options": ["Ar-Rahman", "Al-Malik", "An-Nur", "As-Salaam"], "correctIndex": 0},
         {"type": "true-false", "question": "Each name can be meditated on.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Light: ___-Nur.", "answer": "An"},
         {"type": "true-false", "question": "There are 9 names.", "correctAnswer": False}]},
    {"title": "Rumi — Poet of Love",
     "body_html": r"""<p>Jalal ad-Din Rumi (1207–1273), Persian Sufi poet. The <em>Masnavi</em> is six volumes of teaching stories. The <em>Divan-e Shams</em> are ecstatic love poems for his teacher Shams of Tabriz.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Rumi's teacher: ___ of Tabriz.", "answer": "Shams"},
         {"type": "multiple-choice", "question": "Major work: ", "options": ["Masnavi", "Quran", "Bible", "Sutras"], "correctIndex": 0},
         {"type": "true-false", "question": "Rumi is Persian.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Divan-e ___.", "answer": "Shams"},
         {"type": "true-false", "question": "Rumi wrote in 1900s.", "correctAnswer": False}]},
    {"title": "Whirling Dervishes — Sema",
     "body_html": r"""<p>The Mevlevi Order (founded by Rumi's followers) practices <em>sema</em> — whirling. The dervish turns counterclockwise, right palm up to receive grace, left palm down to bestow it. A moving meditation.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Whirling ceremony: ___.", "answer": "sema"},
         {"type": "multiple-choice", "question": "Right palm: ", "options": ["up to receive", "down only", "facing self", "behind back"], "correctIndex": 0},
         {"type": "true-false", "question": "Mevlevi Order founded by Rumi's followers.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Direction of turn: ___.", "answer": "counterclockwise"},
         {"type": "true-false", "question": "Sema is a sitting meditation only.", "correctAnswer": False}]},
    {"title": "Muraqaba — Sufi Meditation",
     "body_html": r"""<p>Muraqaba ("watching over") is silent Sufi meditation. The seeker turns the heart toward God, often visualizing a teacher or the Light, and rests there.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sufi meditation: ___.", "answer": "muraqaba"},
         {"type": "multiple-choice", "question": "Often visualizes: ", "options": ["a teacher or Light", "an enemy", "a snack", "a screen"], "correctIndex": 0},
         {"type": "true-false", "question": "Muraqaba is silent.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Muraqaba means ___ over.", "answer": "watching"},
         {"type": "true-false", "question": "Muraqaba is loud and active.", "correctAnswer": False}]},
    {"title": "Salaah & Mindfulness",
     "body_html": r"""<p>The five daily prayers (<em>salaah</em>) are themselves a structured mindfulness: ablution (wudu), standing (qiyam), bowing (ruku), prostration (sujud), sitting (julus). Each posture is a doorway.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number of daily prayers: ___.", "answer": "5"},
         {"type": "multiple-choice", "question": "Prostration: ", "options": ["sujud", "ruku", "julus", "qiyam"], "correctIndex": 0},
         {"type": "true-false", "question": "Salaah is a structured mindfulness.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Ablution: ___.", "answer": "wudu"},
         {"type": "true-false", "question": "There are 12 daily prayers in Islam.", "correctAnswer": False}]},
    {"title": "Stations & States",
     "body_html": r"""<p>Sufi tradition distinguishes <em>maqamat</em> (stations earned by effort) from <em>ahwal</em> (states given by grace). Examples of stations: repentance, patience, gratitude, trust. Examples of states: nearness, awe, love.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Earned stations: ___.", "answer": "maqamat"},
         {"type": "multiple-choice", "question": "Given by grace: ", "options": ["maqamat", "ahwal", "salaah", "wudu"], "correctIndex": 1},
         {"type": "true-false", "question": "Patience is a station.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Love is a ___.", "answer": "state"},
         {"type": "true-false", "question": "All progress is by effort alone.", "correctAnswer": False}]},
    {"title": "The Self — Nafs",
     "body_html": r"""<p>The <em>nafs</em> is the lower self. It moves through stages: commanding (ammara), self-blaming (lawwama), inspired (mulhima), tranquil (mutma'inna). Practice purifies it.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Lower self: ___.", "answer": "nafs"},
         {"type": "multiple-choice", "question": "Tranquil stage: ", "options": ["mutma'inna", "ammara", "lawwama", "mulhima"], "correctIndex": 0},
         {"type": "true-false", "question": "Self-blaming stage: lawwama.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Commanding stage: ___.", "answer": "ammara"},
         {"type": "true-false", "question": "Nafs cannot be transformed.", "correctAnswer": False}]},
    {"title": "Heart Practice — Qalb",
     "body_html": r"""<p>The heart (<em>qalb</em>) is the seat of perception. Sufi practice "polishes" it. A clean heart sees God in all things; a clouded heart sees only itself.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Heart: ___.", "answer": "qalb"},
         {"type": "multiple-choice", "question": "Clouded heart sees: ", "options": ["only self", "all beings", "the moon", "the past"], "correctIndex": 0},
         {"type": "true-false", "question": "Practice polishes the heart.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Clean heart sees ___ in all things.", "answer": "God"},
         {"type": "true-false", "question": "Heart is unimportant in Sufism.", "correctAnswer": False}]},
    {"title": "The Sheikh & the Path",
     "body_html": r"""<p>A Sufi seeker (<em>murid</em>) travels the path (<em>tariqa</em>) under the guidance of a sheikh. The relationship is one of love and discipline.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Seeker: ___.", "answer": "murid"},
         {"type": "multiple-choice", "question": "Path: ", "options": ["tariqa", "salaah", "qalb", "nafs"], "correctIndex": 0},
         {"type": "true-false", "question": "A sheikh guides the path.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tariqa = ___.", "answer": "path"},
         {"type": "true-false", "question": "Sufism has no teacher.", "correctAnswer": False}]},
    {"title": "Famous Sufi Figures",
     "body_html": r"""<ul><li>Rabia al-Adawiyya — early woman saint of Basra.</li><li>Al-Hallaj — martyr who said "I am the Truth."</li><li>Ibn Arabi — Andalusian metaphysician.</li><li>Al-Ghazali — synthesized Sufism with mainstream theology.</li><li>Yunus Emre — Turkish poet of love.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Woman saint of Basra: ___ al-Adawiyya.", "answer": "Rabia"},
         {"type": "multiple-choice", "question": "Synthesizer: ", "options": ["Al-Ghazali", "Al-Hallaj", "Yunus Emre", "Rumi"], "correctIndex": 0},
         {"type": "true-false", "question": "Ibn Arabi was Andalusian.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Al-Hallaj said \"I am the ___.\"", "answer": "Truth"},
         {"type": "true-false", "question": "Yunus Emre wrote in Turkish.", "correctAnswer": True}]},
    {"title": "Sufi Music — Qawwali",
     "body_html": r"""<p>Qawwali is devotional music of the Indian subcontinent — Nusrat Fateh Ali Khan its most famous voice. Sema, Mevlevi music, and the daff drum all serve dhikr.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Famous qawwali singer: ___ Fateh Ali Khan.", "answer": "Nusrat"},
         {"type": "multiple-choice", "question": "Sufi drum: ", "options": ["daff", "tabla", "djembe", "snare"], "correctIndex": 0},
         {"type": "true-false", "question": "Qawwali is devotional.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Music can serve ___.", "answer": "dhikr"},
         {"type": "true-false", "question": "Qawwali rejects God-remembrance.", "correctAnswer": False}]},
    {"title": "Daily Sufi Practice",
     "body_html": r"""<ul><li>Five daily salaah with attention to posture and breath.</li><li>Morning and evening dhikr (10–30 min).</li><li>Reading from Rumi, Hafez, or another Sufi poet.</li><li>Service to others — Sufism stresses serving creation.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Dhikr length: ___ min minimum.", "answer": "10"},
         {"type": "multiple-choice", "question": "Read poetry of: ", "options": ["Rumi or Hafez", "Confucius", "Plato", "Aristotle"], "correctIndex": 0},
         {"type": "true-false", "question": "Service to others matters.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Salaah count: ___ daily.", "answer": "5"},
         {"type": "true-false", "question": "Sufism opposes service.", "correctAnswer": False}]},
    {"title": "Sufi Meditation Checkpoint",
     "body_html": r"""<ul><li>Sufism = Islam's inner path; tasawwuf.</li><li>Dhikr is the central remembrance practice.</li><li>Muraqaba is silent meditation; sema is whirling.</li><li>Sheikh, tariqa, polishing the qalb.</li><li>Famous: Rumi, Rabia, Ibn Arabi, Al-Ghazali.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Dhikr means remembrance.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "99 Beautiful ___ ", "options": ["Names", "Books", "Stars", "Stones"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Whirling ceremony: ___.", "answer": "sema"},
         {"type": "true-false", "question": "Sufism is closed to outsiders forever.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Sufi seeker: ___.", "answer": "murid"}]},
]

if __name__ == "__main__":
    render_unit(16, "Sufi & Islamic Meditation", 226, LESSONS)
