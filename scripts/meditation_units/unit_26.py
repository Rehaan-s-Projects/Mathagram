#!/usr/bin/env python3
"""Meditation Unit 26 — Children & Family (lessons 376-390)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Why Mindfulness for Kids?",
     "body_html": r"""<p>Children's stress, anxiety, and attention struggles are rising. School-based mindfulness programs improve emotion regulation, focus, and pro-social behavior.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Improves ___ regulation.", "answer": "emotion"},
         {"type": "multiple-choice", "question": "Outcome: ", "options": ["pro-social behavior", "more fights", "less sleep", "weight gain"], "correctIndex": 0},
         {"type": "true-false", "question": "School programs help focus.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Stress is ___ in children.", "answer": "rising"},
         {"type": "true-false", "question": "Children cannot meditate.", "correctAnswer": False}]},
    {"title": "Age-Appropriate Length",
     "body_html": r"""<p>Rule of thumb:</p><ul><li>Ages 3–6: 1–3 minutes.</li><li>Ages 7–12: 5–10 minutes.</li><li>Teens: up to 20 minutes.</li></ul><p>Many short practices beat one long one.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Ages 3–6: ___-3 min.", "answer": "1"},
         {"type": "multiple-choice", "question": "Ages 7–12: ", "options": ["5–10 min", "1 hour", "0", "30 min"], "correctIndex": 0},
         {"type": "true-false", "question": "Many short practices beat one long.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Teens up to ___ min.", "answer": "20"},
         {"type": "true-false", "question": "Toddlers should sit 1 hour.", "correctAnswer": False}]},
    {"title": "Anchor Practices for Kids",
     "body_html": r"""<ul><li>Belly breathing: hand on belly, watch it rise.</li><li>Hot cocoa breath: smell, then cool with long exhale.</li><li>Pinwheel breathing: blow gently on a pinwheel.</li><li>Stuffed animal breathing: lie down with toy on belly.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hot ___ breath.", "answer": "cocoa"},
         {"type": "multiple-choice", "question": "Tool: ", "options": ["pinwheel", "saw", "hammer", "phone"], "correctIndex": 0},
         {"type": "true-false", "question": "Stuffed animal sits on the belly.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Hand on ___ for belly breath.", "answer": "belly"},
         {"type": "true-false", "question": "Tools must be expensive.", "correctAnswer": False}]},
    {"title": "Mindful Listening Games",
     "body_html": r"""<p>Use a chime: invite kids to listen until the sound completely fades, then raise a hand. Builds sustained attention and equanimity.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Tool: ___.", "answer": "chime"},
         {"type": "multiple-choice", "question": "When sound fades: ", "options": ["raise hand", "shout", "leave room", "argue"], "correctIndex": 0},
         {"type": "true-false", "question": "Builds sustained attention.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Listen until sound completely ___.", "answer": "fades"},
         {"type": "true-false", "question": "Listening games waste time.", "correctAnswer": False}]},
    {"title": "Gratitude Practice",
     "body_html": r"""<p>Three things at dinner or bedtime: "What's one thing that made you smile today?" Builds noticing, language, and connection.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number: ___ things.", "answer": "3"},
         {"type": "multiple-choice", "question": "Time: ", "options": ["dinner or bedtime", "3am", "midnight", "during a fight"], "correctIndex": 0},
         {"type": "true-false", "question": "Builds connection.", "correctAnswer": True},
         {"type": "fill-blank", "question": "What made you ___ today?", "answer": "smile"},
         {"type": "true-false", "question": "Gratitude is meaningless for kids.", "correctAnswer": False}]},
    {"title": "Naming Feelings",
     "body_html": r"""<p>"Mad," "sad," "scared," "happy," "frustrated," "lonely." Use a feelings wheel. Naming reduces intensity (Lieberman's "name it to tame it").</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Phrase: name it to ___ it.", "answer": "tame"},
         {"type": "multiple-choice", "question": "Tool: ", "options": ["feelings wheel", "abacus", "calculator", "TV"], "correctIndex": 0},
         {"type": "true-false", "question": "Naming reduces intensity.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Researcher: ___.", "answer": "Lieberman"},
         {"type": "true-false", "question": "Kids should suppress all feelings.", "correctAnswer": False}]},
    {"title": "Bedtime Body Scan",
     "body_html": r"""<p>Lying down: "wiggle toes, then relax them, then ankles, knees..." up to head. Slow voice. Most kids fall asleep before the chest.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Direction: ___ to head.", "answer": "toes"},
         {"type": "multiple-choice", "question": "Sleep often: ", "options": ["before the chest", "after head", "never", "during shouting"], "correctIndex": 0},
         {"type": "true-false", "question": "Slow voice helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Wiggle then ___.", "answer": "relax"},
         {"type": "true-false", "question": "Loud voice helps sleep.", "correctAnswer": False}]},
    {"title": "Tantrum Toolkit",
     "body_html": r"""<p>During a tantrum, the child's brain is overwhelmed. Don't reason; co-regulate. Calm voice, lower body, simple words. After the storm passes, name the feeling.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Approach: ___-regulate.", "answer": "co"},
         {"type": "multiple-choice", "question": "Don't: ", "options": ["reason mid-storm", "be calm", "use simple words", "wait"], "correctIndex": 0},
         {"type": "true-false", "question": "Name the feeling after storm.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Lower your ___.", "answer": "body"},
         {"type": "true-false", "question": "Logic works mid-tantrum.", "correctAnswer": False}]},
    {"title": "Mindful Parenting",
     "body_html": r"""<p>Daniel Siegel and Mary Hartzell's <em>Parenting from the Inside Out</em>: parents' own regulation predicts kids' regulation. Self-care isn't selfish; it's the foundation.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Co-author: Mary ___.", "answer": "Hartzell"},
         {"type": "multiple-choice", "question": "Predictor: ", "options": ["parent regulation", "child IQ alone", "school size", "paint color"], "correctIndex": 0},
         {"type": "true-false", "question": "Self-care is foundational.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Book: Parenting from the ___ Out.", "answer": "Inside"},
         {"type": "true-false", "question": "Parent regulation is irrelevant.", "correctAnswer": False}]},
    {"title": "Teen-Specific Practices",
     "body_html": r"""<p>Teens benefit from longer sits (15–20 min), peer-led groups, journaling, and connecting practice to identity work. Avoid coercive framings; offer choice.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Length: ___-20 min.", "answer": "15"},
         {"type": "multiple-choice", "question": "Avoid: ", "options": ["coercive framings", "choice", "journaling", "peer groups"], "correctIndex": 0},
         {"type": "true-false", "question": "Peer-led groups help teens.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Connect to ___ work.", "answer": "identity"},
         {"type": "true-false", "question": "Coercion works for teens.", "correctAnswer": False}]},
    {"title": "Family Sit",
     "body_html": r"""<p>Once a week, sit together for 5–15 minutes, then briefly share one feeling each. Models practice and creates a non-stressful family ritual.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Duration: ___-15 min.", "answer": "5"},
         {"type": "multiple-choice", "question": "Frequency: ", "options": ["weekly", "yearly", "never", "daily mandatory"], "correctIndex": 0},
         {"type": "true-false", "question": "Share one feeling each.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Models ___.", "answer": "practice"},
         {"type": "true-false", "question": "Family sits are forbidden.", "correctAnswer": False}]},
    {"title": "Mindfulness in Schools",
     "body_html": r"""<p>Programs: Mindful Schools (US), MindUP (Canada), .b (UK), Inner Explorer. They train teachers to deliver age-appropriate curricula.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "UK program: ___.", "answer": ".b"},
         {"type": "multiple-choice", "question": "Canada: ", "options": ["MindUP", "Mindful Schools", ".b", "Inner Explorer"], "correctIndex": 0},
         {"type": "true-false", "question": "Programs train teachers.", "correctAnswer": True},
         {"type": "fill-blank", "question": "US: Mindful ___.", "answer": "Schools"},
         {"type": "true-false", "question": "School programs are nonexistent.", "correctAnswer": False}]},
    {"title": "Tech & Family",
     "body_html": r"""<p>Devices fragment attention. Family tech rules:</p><ul><li>No phones at meals.</li><li>Charge phones outside bedrooms.</li><li>Tech-free hour before bed.</li><li>Sunday "tech sabbath."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "No phones at ___.", "answer": "meals"},
         {"type": "multiple-choice", "question": "Charge phones: ", "options": ["outside bedrooms", "in bed", "during meals", "in the kitchen sink"], "correctIndex": 0},
         {"type": "true-false", "question": "Tech-free hour before bed.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sunday tech ___.", "answer": "sabbath"},
         {"type": "true-false", "question": "Phones at every meal is best.", "correctAnswer": False}]},
    {"title": "Difficult Family Dynamics",
     "body_html": r"""<p>Mindfulness reveals family patterns: the same fights, the same triggers. Practice creates a pause where reactivity used to live. Your nervous system change shifts the system.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Practice creates a ___.", "answer": "pause"},
         {"type": "multiple-choice", "question": "Effect: ", "options": ["shifts the system", "freezes it", "ends family", "ignites fights"], "correctIndex": 0},
         {"type": "true-false", "question": "One person's change can shift the system.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Reveals family ___.", "answer": "patterns"},
         {"type": "true-false", "question": "You can't influence family dynamics.", "correctAnswer": False}]},
    {"title": "Children & Family Checkpoint",
     "body_html": r"""<ul><li>Short, playful practices for kids; choice and identity work for teens.</li><li>Naming feelings reduces intensity.</li><li>Parent regulation is the foundation.</li><li>Family sits, gratitude, tech rules support shared practice.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Name it to tame it.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Length for ages 3-6: ", "options": ["1-3 min", "1 hour", "30 min", "0"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Sunday: tech ___.", "answer": "sabbath"},
         {"type": "true-false", "question": "Parents' regulation is irrelevant.", "correctAnswer": False},
         {"type": "fill-blank", "question": "UK schools program: ___.", "answer": ".b"}]},
]

if __name__ == "__main__":
    render_unit(26, "Children & Family", 376, LESSONS)
