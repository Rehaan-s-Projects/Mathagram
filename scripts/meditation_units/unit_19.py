#!/usr/bin/env python3
"""Meditation Unit 19 — Mindfulness in Therapy (lessons 271-285)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Jon Kabat-Zinn & MBSR",
     "body_html": r"""<p>In 1979, Jon Kabat-Zinn launched the Mindfulness-Based Stress Reduction (MBSR) program at the University of Massachusetts. He stripped Buddhist meditation of religion to deliver it in clinics.</p><ul><li>8-week structured program.</li><li>Body scan, sitting, mindful yoga.</li><li>One full day silent retreat.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Founder of MBSR: Jon ___-Zinn.", "answer": "Kabat"},
         {"type": "multiple-choice", "question": "Program length: ", "options": ["3 weeks", "8 weeks", "1 year", "2 days"], "correctIndex": 1},
         {"type": "true-false", "question": "MBSR was launched in 1979.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Includes one full ___ silent retreat.", "answer": "day"},
         {"type": "true-false", "question": "MBSR is Buddhist religious instruction.", "correctAnswer": False}]},
    {"title": "MBCT — for Depression",
     "body_html": r"""<p>Mindfulness-Based Cognitive Therapy (MBCT) was developed by Segal, Williams, and Teasdale to prevent depressive relapse. Combines MBSR with cognitive therapy.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "MBCT prevents ___ relapse.", "answer": "depressive"},
         {"type": "multiple-choice", "question": "Builds on: ", "options": ["MBSR", "EMDR", "DBT", "ACT"], "correctIndex": 0},
         {"type": "true-false", "question": "Combines mindfulness with cognitive therapy.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Authors: Segal, Williams, ___.", "answer": "Teasdale"},
         {"type": "true-false", "question": "MBCT is for high blood pressure only.", "correctAnswer": False}]},
    {"title": "ACT — Acceptance and Commitment",
     "body_html": r"""<p>Steven Hayes's Acceptance and Commitment Therapy uses mindfulness to defuse from thoughts and act on values. Six core processes form the "hexaflex."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Founder: Steven ___.", "answer": "Hayes"},
         {"type": "multiple-choice", "question": "Diagram name: ", "options": ["hexaflex", "octohex", "tritium", "trifold"], "correctIndex": 0},
         {"type": "true-false", "question": "ACT acts on values.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Defuse from ___.", "answer": "thoughts"},
         {"type": "true-false", "question": "ACT ignores values.", "correctAnswer": False}]},
    {"title": "DBT — Dialectical Behavior Therapy",
     "body_html": r"""<p>Marsha Linehan developed DBT for borderline personality disorder. Mindfulness is one of four modules: mindfulness, distress tolerance, emotion regulation, interpersonal effectiveness.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Founder: Marsha ___.", "answer": "Linehan"},
         {"type": "multiple-choice", "question": "Modules count: ", "options": ["3", "4", "6", "8"], "correctIndex": 1},
         {"type": "true-false", "question": "DBT was developed for borderline.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Module: distress ___.", "answer": "tolerance"},
         {"type": "true-false", "question": "DBT excludes mindfulness.", "correctAnswer": False}]},
    {"title": "Self-Compassion — Kristin Neff",
     "body_html": r"""<p>Kristin Neff's self-compassion has three components:</p><ul><li>Self-kindness rather than self-judgment.</li><li>Common humanity rather than isolation.</li><li>Mindfulness rather than over-identification.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Researcher: Kristin ___.", "answer": "Neff"},
         {"type": "multiple-choice", "question": "Components count: ", "options": ["2", "3", "4", "5"], "correctIndex": 1},
         {"type": "true-false", "question": "Common humanity is one component.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Self-kindness vs self-___.", "answer": "judgment"},
         {"type": "true-false", "question": "Self-compassion = self-pity.", "correctAnswer": False}]},
    {"title": "Trauma-Sensitive Mindfulness",
     "body_html": r"""<p>David Treleaven's <em>Trauma-Sensitive Mindfulness</em> warns that long sits can trigger flashbacks. Adaptations: shorter durations, eyes open, choice of object, grounding strategies, working with a trauma-informed teacher.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Author: David ___.", "answer": "Treleaven"},
         {"type": "multiple-choice", "question": "Adaptation: ", "options": ["eyes open", "lock door", "darken room", "no breaks"], "correctIndex": 0},
         {"type": "true-false", "question": "Long sits can trigger flashbacks.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Use a trauma-___ teacher.", "answer": "informed"},
         {"type": "true-false", "question": "All meditators handle trauma the same way.", "correctAnswer": False}]},
    {"title": "Polyvagal Theory & Meditation",
     "body_html": r"""<p>Stephen Porges's polyvagal theory describes three nervous system states:</p><ul><li>Ventral vagal — social, calm.</li><li>Sympathetic — fight or flight.</li><li>Dorsal vagal — freeze, shutdown.</li></ul><p>Mindfulness can help shift toward the ventral state.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Researcher: Stephen ___.", "answer": "Porges"},
         {"type": "multiple-choice", "question": "Calm state: ", "options": ["ventral vagal", "sympathetic", "dorsal vagal", "hyper-aroused"], "correctIndex": 0},
         {"type": "true-false", "question": "Sympathetic = fight or flight.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Freeze: ___ vagal.", "answer": "dorsal"},
         {"type": "true-false", "question": "There are 10 NS states in polyvagal theory.", "correctAnswer": False}]},
    {"title": "Internal Family Systems",
     "body_html": r"""<p>Richard Schwartz's IFS sees the mind as a family of "parts" plus an underlying Self. Meditation can resemble IFS — meeting parts with curiosity, calm, and compassion.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Founder: Richard ___.", "answer": "Schwartz"},
         {"type": "multiple-choice", "question": "Underlying core: ", "options": ["Self", "Parts", "Ego", "Brain"], "correctIndex": 0},
         {"type": "true-false", "question": "IFS uses parts work.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Self qualities include curiosity, calm, ___.", "answer": "compassion"},
         {"type": "true-false", "question": "IFS denies parts entirely.", "correctAnswer": False}]},
    {"title": "RAIN — Tara Brach",
     "body_html": r"""<p>Tara Brach teaches RAIN for difficult emotions:</p><ul><li><strong>R</strong>ecognize what is happening.</li><li><strong>A</strong>llow it to be there.</li><li><strong>I</strong>nvestigate with curiosity.</li><li><strong>N</strong>urture with self-compassion.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Acronym: ___.", "answer": "RAIN"},
         {"type": "multiple-choice", "question": "I stands for: ", "options": ["Investigate", "Imagine", "Imitate", "Inspect"], "correctIndex": 0},
         {"type": "true-false", "question": "Tara Brach teaches RAIN.", "correctAnswer": True},
         {"type": "fill-blank", "question": "N: ___.", "answer": "Nurture"},
         {"type": "true-false", "question": "Step A means Argue.", "correctAnswer": False}]},
    {"title": "Common Humanity",
     "body_html": r"""<p>Difficult emotions feel isolating. Reminding yourself that others suffer the same way ("just like me") is itself meditation. It softens shame and shifts perspective.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Phrase: \"___ like me.\"", "answer": "just"},
         {"type": "multiple-choice", "question": "It softens: ", "options": ["shame", "joy", "kindness", "courage"], "correctIndex": 0},
         {"type": "true-false", "question": "Difficult emotions feel isolating.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Practice is itself ___.", "answer": "meditation"},
         {"type": "true-false", "question": "Common humanity worsens shame.", "correctAnswer": False}]},
    {"title": "Working with Anxiety",
     "body_html": r"""<p>Anxiety in the body: tight chest, shallow breath, racing thoughts. Practice:</p><ul><li>Exhale longer than inhale.</li><li>Name three things you see, two you hear, one you feel.</li><li>Soften shoulders and jaw.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Exhale longer than ___.", "answer": "inhale"},
         {"type": "multiple-choice", "question": "Grounding: name 3 you ___ ", "options": ["see", "smell", "taste", "imagine"], "correctIndex": 0},
         {"type": "true-false", "question": "Anxiety often shows in the chest.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Soften shoulders and ___.", "answer": "jaw"},
         {"type": "true-false", "question": "Holding breath calms anxiety best.", "correctAnswer": False}]},
    {"title": "Working with Depression",
     "body_html": r"""<p>Depression often pulls attention into rumination. Mindfulness widens the focus: notice rumination, label it ("thinking, thinking"), shift to body and breath. Behavioral activation (small actions) supports practice.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Label thinking: ___, thinking.", "answer": "thinking"},
         {"type": "multiple-choice", "question": "Behavioral activation = ", "options": ["small actions", "bigger meds", "more sleep alone", "fasting"], "correctIndex": 0},
         {"type": "true-false", "question": "Depression pulls into rumination.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Shift to body and ___.", "answer": "breath"},
         {"type": "true-false", "question": "Mindfulness alone replaces clinical care.", "correctAnswer": False}]},
    {"title": "Mindfulness Apps & Programs",
     "body_html": r"""<p>Common modern entry points:</p><ul><li>Headspace, Calm, Waking Up, Insight Timer, Ten Percent Happier.</li><li>Free university programs (Oxford Mindfulness, Mindful Schools).</li><li>Hospital-based MBSR.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sam Harris-affiliated app: Waking ___.", "answer": "Up"},
         {"type": "multiple-choice", "question": "App: ", "options": ["Headspace", "Excel", "Photoshop", "Outlook"], "correctIndex": 0},
         {"type": "true-false", "question": "Hospital-based MBSR exists.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Free program: ___ Mindfulness (Oxford).", "answer": "Oxford"},
         {"type": "true-false", "question": "Apps eliminate need for any teacher.", "correctAnswer": False}]},
    {"title": "Limits of Therapy-Mindfulness",
     "body_html": r"""<p>Mindfulness is not a cure-all. It can:</p><ul><li>Worsen dissociation if applied carelessly to trauma.</li><li>Be co-opted as productivity hack and miss its ethical roots.</li><li>Mask deeper issues that need clinical care.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Risk: worsen ___ in trauma.", "answer": "dissociation"},
         {"type": "multiple-choice", "question": "Risk: ", "options": ["productivity hack only", "great for everyone", "no risk", "only positive"], "correctIndex": 0},
         {"type": "true-false", "question": "It can mask deeper issues.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Be aware of ___ roots.", "answer": "ethical"},
         {"type": "true-false", "question": "Mindfulness is a complete cure for everything.", "correctAnswer": False}]},
    {"title": "Therapy & Mindfulness Checkpoint",
     "body_html": r"""<ul><li>MBSR (Kabat-Zinn), MBCT (Segal et al.), ACT (Hayes), DBT (Linehan).</li><li>Self-compassion (Neff), trauma-sensitive (Treleaven), IFS (Schwartz).</li><li>RAIN, polyvagal awareness, common humanity.</li><li>Apps and programs are entry points; clinical care matters.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "MBCT prevents depressive relapse.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "RAIN's R: ", "options": ["Recognize", "Refuse", "React", "Run"], "correctIndex": 0},
         {"type": "fill-blank", "question": "ACT: Acceptance and ___ Therapy.", "answer": "Commitment"},
         {"type": "true-false", "question": "Self-compassion has three components.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Polyvagal: ___ vagal = social/calm.", "answer": "ventral"}]},
]

if __name__ == "__main__":
    render_unit(19, "Mindfulness in Therapy", 271, LESSONS)
