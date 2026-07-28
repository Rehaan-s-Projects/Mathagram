#!/usr/bin/env python3
"""Meditation Unit 15 — Christian & Western Contemplative (lessons 211-225)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Christian Contemplative Roots",
     "body_html": r"""<p>Christian contemplative practice is ancient. The desert fathers and mothers of Egypt and Syria (3rd–5th century) sat in silence, prayed continually, and trained the heart toward God.</p><ul><li>Antony the Great, Pachomius, Mary of Egypt.</li><li>Hesychia = "stillness."</li><li>Foundation of monasticism East and West.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Greek for stillness: ___.", "answer": "hesychia"},
         {"type": "multiple-choice", "question": "Desert fathers/mothers were in: ", "options": ["China", "Egypt and Syria", "Ireland", "Japan"], "correctIndex": 1},
         {"type": "true-false", "question": "Christian contemplation is ancient.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Antony the ___.", "answer": "Great"},
         {"type": "true-false", "question": "Desert practice was loud and busy.", "correctAnswer": False}]},
    {"title": "Lectio Divina",
     "body_html": r"""<p>Lectio Divina ("divine reading") is a four-step contemplative reading of scripture:</p><ul><li>Lectio — read slowly.</li><li>Meditatio — meditate on what stands out.</li><li>Oratio — pray or respond from the heart.</li><li>Contemplatio — rest in God's presence.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Step 1: ___.", "answer": "lectio"},
         {"type": "multiple-choice", "question": "Lectio Divina has how many steps? ", "options": ["3", "4", "5", "12"], "correctIndex": 1},
         {"type": "true-false", "question": "Final step is contemplatio.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pray from heart: ___.", "answer": "oratio"},
         {"type": "true-false", "question": "Lectio Divina is fast skim-reading.", "correctAnswer": False}]},
    {"title": "Centering Prayer",
     "body_html": r"""<p>Developed by Trappist monks Thomas Keating, Basil Pennington, and William Meninger in the 1970s. Method:</p><ul><li>Choose a sacred word (e.g., "Abba," "Jesus," "love").</li><li>Sit silently 20 minutes.</li><li>When thoughts arise, return gently to the word.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Length: ___ minutes.", "answer": "20"},
         {"type": "multiple-choice", "question": "Founders include: ", "options": ["Thomas Keating", "Pope Pius", "John Lennon", "Galileo"], "correctIndex": 0},
         {"type": "true-false", "question": "Use a single sacred word.", "correctAnswer": True},
         {"type": "fill-blank", "question": "When thoughts arise, return to the ___.", "answer": "word"},
         {"type": "true-false", "question": "Centering Prayer was invented in 2010.", "correctAnswer": False}]},
    {"title": "The Jesus Prayer",
     "body_html": r"""<p>The Jesus Prayer is the heart of Eastern Orthodox hesychast practice: <em>"Lord Jesus Christ, Son of God, have mercy on me, a sinner."</em> Repeated continuously, often with breath.</p><ul><li>Tradition: <em>The Way of a Pilgrim</em>.</li><li>Mount Athos monks pray it ceaselessly.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Lord ___ Christ.", "answer": "Jesus"},
         {"type": "multiple-choice", "question": "Tradition source: ", "options": ["The Way of a Pilgrim", "Mein Kampf", "Tao Te Ching", "Quran"], "correctIndex": 0},
         {"type": "true-false", "question": "Mount Athos monks pray it.", "correctAnswer": True},
         {"type": "fill-blank", "question": "...have ___ on me.", "answer": "mercy"},
         {"type": "true-false", "question": "Prayer is said only on Sundays.", "correctAnswer": False}]},
    {"title": "The Cloud of Unknowing",
     "body_html": r"""<p>14th-century English text by an anonymous monk. Teaches that God is approached not by knowledge but by love — a "cloud of unknowing." Use a single short word as anchor.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Country of origin: ___.", "answer": "England"},
         {"type": "multiple-choice", "question": "God is approached by: ", "options": ["knowledge", "love", "money", "force"], "correctIndex": 1},
         {"type": "true-false", "question": "The author is anonymous.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Cloud of ___.", "answer": "unknowing"},
         {"type": "true-false", "question": "It dates from ancient Egypt.", "correctAnswer": False}]},
    {"title": "Teresa of Avila",
     "body_html": r"""<p>16th-century Spanish Carmelite. Her <em>Interior Castle</em> describes seven mansions of the soul, moving from beginner's prayer to mystical union with God.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Country: ___.", "answer": "Spain"},
         {"type": "multiple-choice", "question": "Number of mansions: ", "options": ["3", "5", "7", "9"], "correctIndex": 2},
         {"type": "true-false", "question": "Teresa was a Carmelite.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Famous book: Interior ___.", "answer": "Castle"},
         {"type": "true-false", "question": "Teresa wrote in the 19th century.", "correctAnswer": False}]},
    {"title": "John of the Cross",
     "body_html": r"""<p>Spanish Carmelite, Teresa's contemporary and reformer. Wrote <em>The Dark Night of the Soul</em> and <em>The Ascent of Mount Carmel</em>. Coined "dark night" for purifying suffering on the spiritual path.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Famous text: Dark Night of the ___.", "answer": "Soul"},
         {"type": "multiple-choice", "question": "Order: ", "options": ["Jesuit", "Franciscan", "Carmelite", "Benedictine"], "correctIndex": 2},
         {"type": "true-false", "question": "John knew Teresa.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Ascent of Mount ___.", "answer": "Carmel"},
         {"type": "true-false", "question": "Dark night = purifying suffering.", "correctAnswer": True}]},
    {"title": "Meister Eckhart",
     "body_html": r"""<p>13th–14th century German Dominican mystic. Spoke of <em>Gelassenheit</em> (releasement, letting-be) and the birth of God in the soul. Bold language got him in trouble; his work influences Christian and interspiritual mysticism today.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Country: ___.", "answer": "Germany"},
         {"type": "multiple-choice", "question": "Order: ", "options": ["Dominican", "Carmelite", "Cistercian", "Benedictine"], "correctIndex": 0},
         {"type": "true-false", "question": "Gelassenheit means letting-be.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Eckhart was German and ___.", "answer": "Dominican"},
         {"type": "true-false", "question": "Eckhart's language was timid.", "correctAnswer": False}]},
    {"title": "Quaker Silence",
     "body_html": r"""<p>The Religious Society of Friends (Quakers) gathers in silent worship. Anyone may speak when "moved by the Spirit." This is a Protestant contemplative practice.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Religious Society of ___.", "answer": "Friends"},
         {"type": "multiple-choice", "question": "Worship is: ", "options": ["loud singing", "silence with occasional speaking", "shouting", "video sermons"], "correctIndex": 1},
         {"type": "true-false", "question": "Quakers are a Protestant group.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Speak when moved by the ___.", "answer": "Spirit"},
         {"type": "true-false", "question": "Only the pastor may speak.", "correctAnswer": False}]},
    {"title": "Ignatian Examen",
     "body_html": r"""<p>The Examen is a five-step daily prayer of Ignatius of Loyola:</p><ul><li>Become aware of God's presence.</li><li>Review the day with gratitude.</li><li>Pay attention to emotions.</li><li>Choose one feature to pray about.</li><li>Look toward tomorrow.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Founder: ___ of Loyola.", "answer": "Ignatius"},
         {"type": "multiple-choice", "question": "Number of steps: ", "options": ["3", "5", "7", "10"], "correctIndex": 1},
         {"type": "true-false", "question": "Examen is daily prayer.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Review the day with ___.", "answer": "gratitude"},
         {"type": "true-false", "question": "Examen is centered on tomorrow only.", "correctAnswer": False}]},
    {"title": "Thomas Merton",
     "body_html": r"""<p>20th-century Trappist monk. <em>The Seven Storey Mountain</em>, <em>New Seeds of Contemplation</em>. Bridge-builder to Buddhism, especially Zen. Met the Dalai Lama in 1968.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Order: ___.", "answer": "Trappist"},
         {"type": "multiple-choice", "question": "Bridged with: ", "options": ["Buddhism (especially Zen)", "Hinduism alone", "atheism", "Wicca"], "correctIndex": 0},
         {"type": "true-false", "question": "Merton met the Dalai Lama.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Book: The Seven Storey ___.", "answer": "Mountain"},
         {"type": "true-false", "question": "Merton was a 17th-century mystic.", "correctAnswer": False}]},
    {"title": "Henri Nouwen & Spiritual Direction",
     "body_html": r"""<p>Henri Nouwen (1932–1996), Dutch Catholic priest and writer. <em>The Return of the Prodigal Son</em>. Popularized spiritual direction — meeting regularly with a guide to discern God's movement in your life.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Country: ___.", "answer": "Netherlands"},
         {"type": "multiple-choice", "question": "Practice popularized: ", "options": ["spiritual direction", "yoga", "fasting only", "fortune telling"], "correctIndex": 0},
         {"type": "true-false", "question": "Nouwen was a Catholic priest.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Book: Return of the ___ Son.", "answer": "Prodigal"},
         {"type": "true-false", "question": "Spiritual direction is meditative dialogue.", "correctAnswer": True}]},
    {"title": "Modern Christian Mindfulness",
     "body_html": r"""<p>Authors like Cynthia Bourgeault, James Finley, and Richard Rohr blend contemplative Christianity with insights from Buddhism, depth psychology, and the Enneagram.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Author: Richard ___.", "answer": "Rohr"},
         {"type": "multiple-choice", "question": "Other voice: ", "options": ["Cynthia Bourgeault", "Hakuin", "Mother Teresa only", "Plato"], "correctIndex": 0},
         {"type": "true-false", "question": "Modern Christian mindfulness draws on Buddhism.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Author: James ___.", "answer": "Finley"},
         {"type": "true-false", "question": "Modern Christian contemplation is closed to other traditions.", "correctAnswer": False}]},
    {"title": "Daily Christian Contemplative Practice",
     "body_html": r"""<ul><li>20 minutes Centering Prayer or Jesus Prayer.</li><li>Lectio Divina with a passage of scripture.</li><li>Examen at the end of the day.</li><li>Sunday community + monthly spiritual direction.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Length of Centering Prayer: ___ min.", "answer": "20"},
         {"type": "multiple-choice", "question": "Daily review: ", "options": ["Examen", "Tonglen", "Mantra", "Koan"], "correctIndex": 0},
         {"type": "true-false", "question": "Sunday community helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Read scripture via ___ Divina.", "answer": "Lectio"},
         {"type": "true-false", "question": "Once-yearly practice is enough.", "correctAnswer": False}]},
    {"title": "Christian Contemplative Checkpoint",
     "body_html": r"""<ul><li>Long lineage: desert fathers/mothers, medieval mystics, modern Trappists.</li><li>Methods: Lectio Divina, Centering Prayer, Jesus Prayer, Examen.</li><li>Mystics: Teresa, John of the Cross, Eckhart, Merton, Nouwen.</li><li>Quakers contribute silent worship.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Centering Prayer uses a sacred word.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Cloud of Unknowing comes from: ", "options": ["England", "Spain", "Egypt", "Russia"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Anglican-influenced silent worship: ___.", "answer": "Quaker"},
         {"type": "true-false", "question": "Examen looks at the day.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Teresa of ___.", "answer": "Avila"}]},
]

if __name__ == "__main__":
    render_unit(15, "Christian & Western Contemplative", 211, LESSONS)
