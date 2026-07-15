#!/usr/bin/env python3
"""Meditation Unit 24 — Trauma-Sensitive Meditation (lessons 346-360)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Trauma in the Body",
     "body_html": r"""<p>Bessel van der Kolk's <em>The Body Keeps the Score</em> popularized the view that trauma stores in the body. Mindfulness can both help and harm depending on how it's offered.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Author: Bessel van der ___.", "answer": "Kolk"},
         {"type": "multiple-choice", "question": "Body Keeps the: ", "options": ["Score", "Watch", "Time", "Hour"], "correctIndex": 0},
         {"type": "true-false", "question": "Mindfulness can help and harm.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Trauma stores in the ___.", "answer": "body"},
         {"type": "true-false", "question": "Trauma lives only in thoughts.", "correctAnswer": False}]},
    {"title": "Window of Tolerance",
     "body_html": r"""<p>Dan Siegel's window of tolerance: a zone where we can feel and think clearly. Above (hyperarousal): anxiety, anger. Below (hypoarousal): numbness, dissociation. Practice expands the window.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Above: ___-arousal.", "answer": "hyper"},
         {"type": "multiple-choice", "question": "Below: ", "options": ["numbness/dissociation", "panic", "rage", "joy"], "correctIndex": 0},
         {"type": "true-false", "question": "Practice expands the window.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Author: Dan ___.", "answer": "Siegel"},
         {"type": "true-false", "question": "Above the window is calm.", "correctAnswer": False}]},
    {"title": "Choice Points in Practice",
     "body_html": r"""<p>For trauma survivors, give choice:</p><ul><li>Eyes open or closed.</li><li>Sitting or lying.</li><li>Object: breath, sound, or external sight.</li><li>Length: 1, 5, or 20 minutes.</li><li>Stop anytime.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Stop ___ time.", "answer": "any"},
         {"type": "multiple-choice", "question": "Object choice: ", "options": ["breath/sound/sight", "breath only", "must be sound", "must be breath"], "correctIndex": 0},
         {"type": "true-false", "question": "Eyes open is allowed.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Length options: 1, 5, or ___ min.", "answer": "20"},
         {"type": "true-false", "question": "No choice should ever be offered.", "correctAnswer": False}]},
    {"title": "Grounding Skills",
     "body_html": r"""<p>Before any inward-focused practice, build grounding:</p><ul><li>Feel feet on floor.</li><li>Press palms together.</li><li>Look around the room and name 5 colors.</li><li>Hold a cool object.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Feel feet on the ___.", "answer": "floor"},
         {"type": "multiple-choice", "question": "Sight-based: ", "options": ["name 5 colors", "close eyes hard", "imagine", "deny seeing"], "correctIndex": 0},
         {"type": "true-false", "question": "Cool object can ground.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Press ___ together.", "answer": "palms"},
         {"type": "true-false", "question": "Grounding is not useful.", "correctAnswer": False}]},
    {"title": "Resourcing",
     "body_html": r"""<p>Resourcing means deliberately strengthening pleasant or neutral states. Examples: visualize a safe place, recall a beloved person, hold a smooth stone. Build the resource <em>before</em> processing distress.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Build resource ___ distress.", "answer": "before"},
         {"type": "multiple-choice", "question": "Example: ", "options": ["safe place visualization", "stew on worst memory", "skip food", "argue"], "correctIndex": 0},
         {"type": "true-false", "question": "Resourcing strengthens pleasant states.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Recall a beloved ___.", "answer": "person"},
         {"type": "true-false", "question": "Resourcing means staying with distress only.", "correctAnswer": False}]},
    {"title": "Pendulation",
     "body_html": r"""<p>Peter Levine's somatic experiencing teaches pendulation: oscillate attention between activation and resource. Build tolerance gradually instead of flooding.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Teacher: Peter ___.", "answer": "Levine"},
         {"type": "multiple-choice", "question": "Pattern: ", "options": ["oscillate", "flood", "freeze", "pile on"], "correctIndex": 0},
         {"type": "true-false", "question": "Builds tolerance gradually.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Modality: somatic ___.", "answer": "experiencing"},
         {"type": "true-false", "question": "Flooding is the goal.", "correctAnswer": False}]},
    {"title": "Titration",
     "body_html": r"""<p>Touch difficult content briefly, then return to safety. The dose matters: a teaspoon of trauma at a time, not a flood. Many short doses metabolize what one long flood overwhelms.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Teaspoon, not ___.", "answer": "flood"},
         {"type": "multiple-choice", "question": "Approach: ", "options": ["short doses", "long sessions only", "never engage", "all at once"], "correctIndex": 0},
         {"type": "true-false", "question": "Many short doses can metabolize trauma.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Return to ___.", "answer": "safety"},
         {"type": "true-false", "question": "Titration means dump everything at once.", "correctAnswer": False}]},
    {"title": "Embodied Self-Compassion",
     "body_html": r"""<p>Place hand on heart or cheek. Say: "This is hard. May I be kind to myself." Touch + words activate caregiving systems and lower threat response.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Hand on ___ or cheek.", "answer": "heart"},
         {"type": "multiple-choice", "question": "Effect: ", "options": ["lower threat", "raise threat", "freeze", "amplify panic"], "correctIndex": 0},
         {"type": "true-false", "question": "Touch + words help.", "correctAnswer": True},
         {"type": "fill-blank", "question": "May I be ___ to myself.", "answer": "kind"},
         {"type": "true-false", "question": "Touch raises threat for everyone.", "correctAnswer": False}]},
    {"title": "Trauma & Long Sits",
     "body_html": r"""<p>Long silent retreats can flood survivors with material. Better: shorter daily practice, work with a teacher, choose programs explicitly trauma-informed.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Choose ___-informed programs.", "answer": "trauma"},
         {"type": "multiple-choice", "question": "Long silent retreats: ", "options": ["can flood survivors", "always safe", "always best", "always required"], "correctIndex": 0},
         {"type": "true-false", "question": "Shorter daily practice often suits.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Work with a ___.", "answer": "teacher"},
         {"type": "true-false", "question": "Long retreats are mandatory for everyone.", "correctAnswer": False}]},
    {"title": "Dissociation Watch",
     "body_html": r"""<p>Signs of dissociating during practice:</p><ul><li>Time loss.</li><li>Numbness, "I'm not in my body."</li><li>Floating sensation.</li></ul><p>If noticed: open eyes, ground in senses, end the sit, take a walk.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "If dissociating: open ___.", "answer": "eyes"},
         {"type": "multiple-choice", "question": "Sign: ", "options": ["time loss", "calm joy", "alertness", "playful focus"], "correctIndex": 0},
         {"type": "true-false", "question": "End the sit if dissociating.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Take a ___.", "answer": "walk"},
         {"type": "true-false", "question": "Dissociation should be deepened.", "correctAnswer": False}]},
    {"title": "Trauma-Sensitive Yoga",
     "body_html": r"""<p>Trauma Center Trauma-Sensitive Yoga (TCTSY) by Emerson and van der Kolk emphasizes choice, present-moment focus, non-coercive language. No adjustments without consent.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Acronym: ___.", "answer": "TCTSY"},
         {"type": "multiple-choice", "question": "No adjustments without: ", "options": ["consent", "money", "uniforms", "music"], "correctIndex": 0},
         {"type": "true-false", "question": "Language is non-coercive.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Co-developer: van der ___.", "answer": "Kolk"},
         {"type": "true-false", "question": "Trauma-sensitive yoga is rough and pushy.", "correctAnswer": False}]},
    {"title": "Working with Veterans",
     "body_html": r"""<p>Veterans often combine PTSD, traumatic brain injury, moral injury. Programs (Mindful Warrior, Warriors at Ease, VA mindfulness) tailor practices and pair with clinical care.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Combination includes PTSD, TBI, ___ injury.", "answer": "moral"},
         {"type": "multiple-choice", "question": "Program: ", "options": ["Mindful Warrior", "Loud Warrior", "No Warrior", "TV Warrior"], "correctIndex": 0},
         {"type": "true-false", "question": "Pair with clinical care.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tailored ___.", "answer": "practices"},
         {"type": "true-false", "question": "All veterans need identical practice.", "correctAnswer": False}]},
    {"title": "Adverse Childhood Experiences",
     "body_html": r"""<p>The ACE Study (Felitti, Anda) showed lasting effects of early trauma. Mindful awareness can reduce reactivity, but body-based, relational therapy is often the deeper layer.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Acronym: ___.", "answer": "ACE"},
         {"type": "multiple-choice", "question": "Researchers: ", "options": ["Felitti, Anda", "Kabat-Zinn", "Linehan", "Hayes"], "correctIndex": 0},
         {"type": "true-false", "question": "Mindful awareness can reduce reactivity.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Adverse ___ Experiences.", "answer": "Childhood"},
         {"type": "true-false", "question": "Childhood trauma has no lasting effects.", "correctAnswer": False}]},
    {"title": "Combining with Therapy",
     "body_html": r"""<p>Best outcomes pair meditation with one or more of: somatic experiencing, EMDR, IFS, sensorimotor psychotherapy, or psychodynamic work. Meditation alone is rarely enough for serious trauma.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "EMDR = Eye Movement ___ and Reprocessing.", "answer": "Desensitization"},
         {"type": "multiple-choice", "question": "Modality: ", "options": ["IFS", "TV", "yoga only", "fasting"], "correctIndex": 0},
         {"type": "true-false", "question": "Meditation alone is rarely enough for serious trauma.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sensorimotor ___.", "answer": "psychotherapy"},
         {"type": "true-false", "question": "Pairing therapies is unhelpful.", "correctAnswer": False}]},
    {"title": "Trauma-Sensitive Checkpoint",
     "body_html": r"""<ul><li>Trauma stores in the body; the window of tolerance frames care.</li><li>Choice, grounding, resourcing, titration, pendulation.</li><li>Watch for dissociation; eyes-open and shorter sits are valid.</li><li>Pair with somatic and clinical therapies for serious trauma.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Trauma can store in the body.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Concept by Dan Siegel: ", "options": ["window of tolerance", "ladder of fear", "circle of love", "wheel of pain"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Touch difficult content briefly: ___ .", "answer": "titration"},
         {"type": "true-false", "question": "Long retreats suit all trauma survivors.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Modality: somatic ___.", "answer": "experiencing"}]},
]

if __name__ == "__main__":
    render_unit(24, "Trauma-Sensitive Meditation", 346, LESSONS)
