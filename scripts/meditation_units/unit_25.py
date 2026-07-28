#!/usr/bin/env python3
"""Meditation Unit 25 — Addiction & Recovery (lessons 361-375)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Addiction & the Brain",
     "body_html": r"""<p>Addiction hijacks the dopamine reward system. Cues trigger craving; craving narrows attention; relief from craving relieves and reinforces. Mindfulness inserts a pause.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "System hijacked: ___.", "answer": "dopamine"},
         {"type": "multiple-choice", "question": "Mindfulness inserts a: ", "options": ["pause", "shout", "fight", "fast"], "correctIndex": 0},
         {"type": "true-false", "question": "Craving narrows attention.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Relief reinforces ___.", "answer": "craving"},
         {"type": "true-false", "question": "Addiction is purely moral failure.", "correctAnswer": False}]},
    {"title": "Mindfulness-Based Relapse Prevention",
     "body_html": r"""<p>MBRP (Bowen, Chawla, Marlatt) is an 8-week program combining MBCT-style practices with relapse prevention skills. Reduces relapse and substance use.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Acronym: ___.", "answer": "MBRP"},
         {"type": "multiple-choice", "question": "Length: ", "options": ["8 weeks", "1 day", "1 year", "5 weeks"], "correctIndex": 0},
         {"type": "true-false", "question": "Reduces relapse.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Co-developer: ___, Chawla, Marlatt.", "answer": "Bowen"},
         {"type": "true-false", "question": "MBRP is unstudied.", "correctAnswer": False}]},
    {"title": "Urge Surfing",
     "body_html": r"""<p>Coined by Alan Marlatt: urges crest like waves and pass within 20–30 minutes. Don't fight; ride them. Notice intensity, peak, decline. Practice changes the relationship.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Coined by Alan ___.", "answer": "Marlatt"},
         {"type": "multiple-choice", "question": "Wave duration: ", "options": ["20–30 min", "infinite", "5 sec", "1 day"], "correctIndex": 0},
         {"type": "true-false", "question": "Don't fight, ride.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Notice intensity, peak, ___.", "answer": "decline"},
         {"type": "true-false", "question": "Urges last forever.", "correctAnswer": False}]},
    {"title": "12-Step & Contemplation",
     "body_html": r"""<p>AA's Step 11 explicitly seeks "knowledge of His will and the power to carry that out" through "prayer and meditation." Many recovery groups now include sitting practice.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Step ___ mentions meditation.", "answer": "11"},
         {"type": "multiple-choice", "question": "Means: ", "options": ["prayer and meditation", "exercise only", "diet only", "shopping"], "correctIndex": 0},
         {"type": "true-false", "question": "AA includes contemplation.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Knowledge of ___ will.", "answer": "His"},
         {"type": "true-false", "question": "AA forbids meditation.", "correctAnswer": False}]},
    {"title": "Refuge Recovery & Buddhist Approaches",
     "body_html": r"""<p>Refuge Recovery (Noah Levine, then community-led) and Recovery Dharma offer Buddhist-flavored peer support. Four Noble Truths reframed for addiction.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Founder: Noah ___.", "answer": "Levine"},
         {"type": "multiple-choice", "question": "Truth count: ", "options": ["4", "2", "8", "12"], "correctIndex": 0},
         {"type": "true-false", "question": "Buddhist-flavored peer support.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Four Noble ___.", "answer": "Truths"},
         {"type": "true-false", "question": "Recovery Dharma rejects Buddhism.", "correctAnswer": False}]},
    {"title": "Smart Recovery & ACT Tools",
     "body_html": r"""<p>SMART Recovery uses cognitive-behavioral and ACT-style tools: cost-benefit analysis, urge logs, values clarification. Compatible with mindfulness practice.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "ACT = Acceptance and ___ Therapy.", "answer": "Commitment"},
         {"type": "multiple-choice", "question": "Tool: ", "options": ["urge log", "ignore everything", "blame self", "shame log"], "correctIndex": 0},
         {"type": "true-false", "question": "Compatible with mindfulness.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Values ___.", "answer": "clarification"},
         {"type": "true-false", "question": "SMART forbids cognitive tools.", "correctAnswer": False}]},
    {"title": "Behavioral Addictions",
     "body_html": r"""<p>Phones, scrolling, gaming, gambling, porn, sugar — all engage similar reward circuits. Same urge-surfing tools apply.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Engages similar ___ circuits.", "answer": "reward"},
         {"type": "multiple-choice", "question": "Behavioral addiction: ", "options": ["scrolling", "vegetables", "exercise rest", "sleep"], "correctIndex": 0},
         {"type": "true-false", "question": "Urge-surfing applies to phones too.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Behaviors: phones, scrolling, ___.", "answer": "gaming"},
         {"type": "true-false", "question": "Behavioral addictions don't exist.", "correctAnswer": False}]},
    {"title": "HALT Awareness",
     "big_html_unused": "",
     "body_html": r"""<p>The HALT acronym helps spot vulnerability:</p><ul><li><strong>H</strong>ungry</li><li><strong>A</strong>ngry</li><li><strong>L</strong>onely</li><li><strong>T</strong>ired</li></ul><p>If you're slipping toward use, check HALT first.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Acronym: ___.", "answer": "HALT"},
         {"type": "multiple-choice", "question": "L stands for: ", "options": ["Lonely", "Lazy", "Loud", "Long"], "correctIndex": 0},
         {"type": "true-false", "question": "Use HALT before relapse.", "correctAnswer": True},
         {"type": "fill-blank", "question": "T: ___.", "answer": "Tired"},
         {"type": "true-false", "question": "Hunger has no role in cravings.", "correctAnswer": False}]},
    {"title": "Self-Compassion in Recovery",
     "body_html": r"""<p>Shame is a powerful relapse driver. Self-compassion (Neff, Germer's Mindful Self-Compassion) reduces shame, builds resilience, and predicts better recovery outcomes.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Researcher: ___ (Mindful Self-Compassion).", "answer": "Germer"},
         {"type": "multiple-choice", "question": "Shame is: ", "options": ["a relapse driver", "a healer", "irrelevant", "absent"], "correctIndex": 0},
         {"type": "true-false", "question": "Self-compassion improves recovery.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Other researcher: ___.", "answer": "Neff"},
         {"type": "true-false", "question": "Shame helps recovery.", "correctAnswer": False}]},
    {"title": "Sober Curious",
     "body_html": r"""<p>Even non-addicted drinkers benefit from sober experiments. Try 30 days alcohol-free; track sleep, mood, energy. Mindfulness reveals what alcohol was numbing.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Try ___ days alcohol-free.", "answer": "30"},
         {"type": "multiple-choice", "question": "Tracks: ", "options": ["sleep, mood, energy", "weight only", "credit score", "social media"], "correctIndex": 0},
         {"type": "true-false", "question": "Reveals what alcohol was numbing.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Even ___-addicted drinkers benefit.", "answer": "non"},
         {"type": "true-false", "question": "Alcohol numbs nothing.", "correctAnswer": False}]},
    {"title": "Detox & Early Recovery",
     "body_html": r"""<p>First weeks are hard: cravings spike, sleep is fragmented, emotions surge. Practice tools: very short sits, body grounding, walking, peer support, professional supervision when needed.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sleep is ___.", "answer": "fragmented"},
         {"type": "multiple-choice", "question": "First weeks: ", "options": ["hard", "easy", "absent", "neutral"], "correctIndex": 0},
         {"type": "true-false", "question": "Peer support helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Sit length: very ___.", "answer": "short"},
         {"type": "true-false", "question": "Detox is always smooth and easy.", "correctAnswer": False}]},
    {"title": "Triggers & Environment",
     "body_html": r"""<p>Identify people, places, times, emotions that trigger use. Modify environment: remove substances, change routes, swap friend groups. Mindfulness sees the trigger; environment design reduces exposure.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Modify ___.", "answer": "environment"},
         {"type": "multiple-choice", "question": "Triggers: ", "options": ["people, places, times", "weather only", "music only", "hair only"], "correctIndex": 0},
         {"type": "true-false", "question": "Environment design reduces exposure.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Remove ___.", "answer": "substances"},
         {"type": "true-false", "question": "Environment doesn't matter.", "correctAnswer": False}]},
    {"title": "Identifying Values",
     "body_html": r"""<p>Use ACT-style values clarification. What do you want this life to be about? Health, family, creativity, contribution? Each meditative pause asks: does this next move align with my values?</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Method: ___-style values.", "answer": "ACT"},
         {"type": "multiple-choice", "question": "Question: ", "options": ["does this align with values", "is this fun now", "is this loud", "is this expensive"], "correctIndex": 0},
         {"type": "true-false", "question": "Values guide moves.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Examples: health, family, ___, contribution.", "answer": "creativity"},
         {"type": "true-false", "question": "Values are irrelevant.", "correctAnswer": False}]},
    {"title": "Long-Term Sobriety",
     "body_html": r"""<p>After early recovery, the work continues:</p><ul><li>Daily practice habit.</li><li>Continued group connection.</li><li>Service to others.</li><li>Ongoing self-inquiry.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Daily practice ___.", "answer": "habit"},
         {"type": "multiple-choice", "question": "Element: ", "options": ["service to others", "isolation", "secrecy", "perfection"], "correctIndex": 0},
         {"type": "true-false", "question": "Group connection supports.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Ongoing self-___.", "answer": "inquiry"},
         {"type": "true-false", "question": "Long-term recovery requires no practice.", "correctAnswer": False}]},
    {"title": "Addiction & Recovery Checkpoint",
     "body_html": r"""<ul><li>Addiction = hijacked reward circuits; mindfulness inserts a pause.</li><li>MBRP, Refuge Recovery, SMART, 12-Step Step 11.</li><li>Tools: urge surfing, HALT, self-compassion, environment design.</li><li>Sobriety is daily practice + community + values + service.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Urge surfing rides craving waves.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "AA contemplative step: ", "options": ["11", "1", "5", "8"], "correctIndex": 0},
         {"type": "fill-blank", "question": "HALT: Hungry, Angry, Lonely, ___.", "answer": "Tired"},
         {"type": "true-false", "question": "Shame helps recovery.", "correctAnswer": False},
         {"type": "fill-blank", "question": "MBRP = Mindfulness-Based ___ Prevention.", "answer": "Relapse"}]},
]

if __name__ == "__main__":
    render_unit(25, "Addiction & Recovery", 361, LESSONS)
