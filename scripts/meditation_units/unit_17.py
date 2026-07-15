#!/usr/bin/env python3
"""Meditation Unit 17 — Jewish Meditation (lessons 241-255)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Hitbonenut — Contemplation",
     "body_html": r"""<p><em>Hitbonenut</em> is reflective Jewish meditation — sustained contemplation of an idea, verse, or attribute of God until it transforms understanding.</p><ul><li>Hebrew root: <em>binah</em> (understanding).</li><li>Used in Hasidic and Mussar traditions.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Reflective Jewish meditation: ___.", "answer": "hitbonenut"},
         {"type": "multiple-choice", "question": "Root means: ", "options": ["understanding", "fire", "sun", "dance"], "correctIndex": 0},
         {"type": "true-false", "question": "Hitbonenut is sustained contemplation.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Used in Hasidic and ___ traditions.", "answer": "Mussar"},
         {"type": "true-false", "question": "Hitbonenut is fast skim-thinking.", "correctAnswer": False}]},
    {"title": "Hitbodedut — Solitary Talking",
     "body_html": r"""<p>Rebbe Nachman of Breslov taught <em>hitbodedut</em>: spending an hour daily alone, ideally in nature, talking aloud to God in your own words.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Spontaneous prayer: ___.", "answer": "hitbodedut"},
         {"type": "multiple-choice", "question": "Teacher: Rebbe ___ of Breslov.", "options": ["Nachman", "Akiva", "Hillel", "Schneerson"], "correctIndex": 0},
         {"type": "true-false", "question": "It is done aloud.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Often done in ___.", "answer": "nature"},
         {"type": "true-false", "question": "Hitbodedut uses fixed scripted prayers only.", "correctAnswer": False}]},
    {"title": "The Shema",
     "body_html": r"""<p>The Shema is Judaism's central declaration: <em>"Shema Yisrael, Adonai Eloheinu, Adonai Echad"</em> — "Hear O Israel, the Lord our God, the Lord is One." Said morning, evening, and at the moment of death.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hear O ___.", "answer": "Israel"},
         {"type": "multiple-choice", "question": "Final word means: ", "options": ["One", "Many", "Light", "Wisdom"], "correctIndex": 0},
         {"type": "true-false", "question": "Said morning and evening.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Adonai ___.", "answer": "Echad"},
         {"type": "true-false", "question": "The Shema declares many gods.", "correctAnswer": False}]},
    {"title": "Kabbalah — Mystical Tradition",
     "body_html": r"""<p>Kabbalah is the mystical strand of Judaism. Its core text is the <em>Zohar</em> (13th c.). Modern revivers: Isaac Luria of Safed (16th c.), the Hasidic movement (18th c.).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Core text: ___.", "answer": "Zohar"},
         {"type": "multiple-choice", "question": "Reviver of Safed: ", "options": ["Isaac Luria", "Maimonides", "Hillel", "Akiva"], "correctIndex": 0},
         {"type": "true-false", "question": "Kabbalah is mystical Judaism.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Hasidic movement: ___ century.", "answer": "18th"},
         {"type": "true-false", "question": "Zohar is the Quran.", "correctAnswer": False}]},
    {"title": "The Tree of Life — Sefirot",
     "body_html": r"""<p>The Sefirot are 10 divine attributes arranged on the Tree of Life: Keter (Crown), Chochmah (Wisdom), Binah (Understanding), Chesed (Lovingkindness), Gevurah (Strength), Tiferet (Beauty), Netzach (Eternity), Hod (Splendor), Yesod (Foundation), Malkhut (Kingdom).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number of Sefirot: ___.", "answer": "10"},
         {"type": "multiple-choice", "question": "Crown: ", "options": ["Keter", "Binah", "Tiferet", "Yesod"], "correctIndex": 0},
         {"type": "true-false", "question": "Sefirot are divine attributes.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Lovingkindness: ___.", "answer": "Chesed"},
         {"type": "true-false", "question": "Sefirot count is 7.", "correctAnswer": False}]},
    {"title": "Letters & Permutation",
     "body_html": r"""<p>Abraham Abulafia (13th c.) developed letter meditation — chanting and visualizing combinations of Hebrew letters. The 22 letters are seen as creative, reality-shaping forces.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number of Hebrew letters: ___.", "answer": "22"},
         {"type": "multiple-choice", "question": "Teacher: ", "options": ["Abulafia", "Maimonides", "Hillel", "Luria"], "correctIndex": 0},
         {"type": "true-false", "question": "Letters are seen as creative forces.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Letter meditation: ___ century.", "answer": "13th"},
         {"type": "true-false", "question": "Abulafia opposed letter practice.", "correctAnswer": False}]},
    {"title": "Mussar — Soul Traits",
     "body_html": r"""<p>Mussar is a Jewish ethical-spiritual practice: cultivate one soul-trait (<em>middah</em>) at a time — patience, generosity, humility, gratitude. Daily journaling tracks growth.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Soul-trait: ___.", "answer": "middah"},
         {"type": "multiple-choice", "question": "Method: ", "options": ["one trait at a time", "all at once", "no traits", "random"], "correctIndex": 0},
         {"type": "true-false", "question": "Mussar uses journaling.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Plural: ___.", "answer": "middot"},
         {"type": "true-false", "question": "Mussar tackles every trait at once.", "correctAnswer": False}]},
    {"title": "Hasidic Joy",
     "body_html": r"""<p>The Baal Shem Tov (18th-c. founder of Hasidism) taught that joy lifts the soul — singing, dancing, and serving God with simchah. Niggun (wordless melody) carries prayer past words.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Wordless melody: ___.", "answer": "niggun"},
         {"type": "multiple-choice", "question": "Founder of Hasidism: ", "options": ["Baal Shem Tov", "Hillel", "Akiva", "Abulafia"], "correctIndex": 0},
         {"type": "true-false", "question": "Joy lifts the soul.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Joy in Hebrew: ___.", "answer": "simchah"},
         {"type": "true-false", "question": "Hasidism opposes singing.", "correctAnswer": False}]},
    {"title": "Shabbat as Practice",
     "body_html": r"""<p>Shabbat (Friday sundown to Saturday night) is meditation built into time. Stop work, light candles, share meals, sing, study, rest. The week's mind softens and reorders.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Shabbat begins ___ sundown.", "answer": "Friday"},
         {"type": "multiple-choice", "question": "Practice: ", "options": ["work harder", "stop work and rest", "ignore family", "shop more"], "correctIndex": 1},
         {"type": "true-false", "question": "Light candles.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Ends ___ night.", "answer": "Saturday"},
         {"type": "true-false", "question": "Shabbat is a 12-hour rule.", "correctAnswer": False}]},
    {"title": "Tikkun Olam",
     "body_html": r"""<p><em>Tikkun olam</em> = "repair of the world." Lurianic Kabbalah teaches that divine sparks fell into matter; through mitzvot (good acts) we lift them. Meditation feeds action.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Repair: ___ olam.", "answer": "tikkun"},
         {"type": "multiple-choice", "question": "Source: ", "options": ["Lurianic Kabbalah", "Plato", "Aristotle", "Confucius"], "correctIndex": 0},
         {"type": "true-false", "question": "Mitzvot lift sparks.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sparks are fallen into ___.", "answer": "matter"},
         {"type": "true-false", "question": "Meditation is divorced from action here.", "correctAnswer": False}]},
    {"title": "Counting the Omer",
     "body_html": r"""<p>Between Passover and Shavuot, Jews count 49 days, each tied to a combination of Sefirot (e.g., "Chesed within Gevurah"). It is a built-in 7-week meditation.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Days counted: ___.", "answer": "49"},
         {"type": "multiple-choice", "question": "Between which holidays: ", "options": ["Passover and Shavuot", "Hanukkah and Purim", "Rosh Hashanah and Yom Kippur", "Sukkot and Tu BiShvat"], "correctIndex": 0},
         {"type": "true-false", "question": "Each day is tied to Sefirot.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Total weeks: ___.", "answer": "7"},
         {"type": "true-false", "question": "Counting the Omer is 100 days.", "correctAnswer": False}]},
    {"title": "Modern Teachers",
     "body_html": r"""<ul><li>Aryeh Kaplan — bridge between Jewish meditation and modern practitioners.</li><li>Zalman Schachter-Shalomi — Jewish Renewal.</li><li>Rami Shapiro — interspiritual.</li><li>Jonathan Sacks — moral and contemplative writing.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Aryeh ___ wrote on Jewish meditation.", "answer": "Kaplan"},
         {"type": "multiple-choice", "question": "Jewish Renewal: ", "options": ["Schachter-Shalomi", "Akiva", "Maimonides", "Luria"], "correctIndex": 0},
         {"type": "true-false", "question": "Sacks wrote contemplatively.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Interspiritual rabbi: Rami ___.", "answer": "Shapiro"},
         {"type": "true-false", "question": "Modern Jewish meditation has no living teachers.", "correctAnswer": False}]},
    {"title": "Names of God",
     "body_html": r"""<p>Hebrew tradition has many divine names: Adonai, Elohim, El Shaddai, Yah, Hashem, Shekhinah (the indwelling). Each is a meditative entry point.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Indwelling: ___.", "answer": "Shekhinah"},
         {"type": "multiple-choice", "question": "Common name: ", "options": ["Adonai", "Allah", "Brahman", "Tao"], "correctIndex": 0},
         {"type": "true-false", "question": "Each name is a meditative entry point.", "correctAnswer": True},
         {"type": "fill-blank", "question": "El ___.", "answer": "Shaddai"},
         {"type": "true-false", "question": "There is only one Hebrew name for God.", "correctAnswer": False}]},
    {"title": "Daily Jewish Contemplative Practice",
     "body_html": r"""<ul><li>Morning Shema with focused presence.</li><li>20–30 min hitbonenut on a Torah passage.</li><li>Daily Mussar trait check.</li><li>Shabbat as weekly anchor.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hitbonenut length: ___-30 min.", "answer": "20"},
         {"type": "multiple-choice", "question": "Anchor of week: ", "options": ["Shabbat", "Monday meeting", "Tuesday gym", "Friday lunch"], "correctIndex": 0},
         {"type": "true-false", "question": "Mussar trait check is daily.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Morning practice: ___.", "answer": "Shema"},
         {"type": "true-false", "question": "Shabbat happens once a year.", "correctAnswer": False}]},
    {"title": "Jewish Meditation Checkpoint",
     "body_html": r"""<ul><li>Hitbonenut (contemplation), hitbodedut (solitary speech), Mussar (traits).</li><li>Kabbalah, Sefirot, letter meditation.</li><li>Hasidic joy and niggun.</li><li>Shabbat is structural meditation in time.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Hitbodedut is solitary outdoor speech.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Kabbalah's Tree has: ", "options": ["10 Sefirot", "5 Sefirot", "20 Sefirot", "0 Sefirot"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Wordless melody: ___.", "answer": "niggun"},
         {"type": "true-false", "question": "Shabbat is meditation in time.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Soul-trait practice: ___.", "answer": "Mussar"}]},
]

if __name__ == "__main__":
    render_unit(17, "Jewish Meditation", 241, LESSONS)
