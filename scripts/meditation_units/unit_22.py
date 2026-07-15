#!/usr/bin/env python3
"""Meditation Unit 22 — Pain & Chronic Illness (lessons 316-330)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "Pain vs Suffering",
     "body_html": r"""<p>Buddhist teachers distinguish:</p><ul><li>Pain — the bare physical sensation.</li><li>Suffering — the layer of resistance, fear, story we add.</li></ul><p>"Pain × resistance = suffering." Mindfulness can reduce the second factor.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Suffering = pain × ___.", "answer": "resistance"},
         {"type": "multiple-choice", "question": "Mindfulness reduces: ", "options": ["resistance", "tissue", "blood pressure permanently", "weight"], "correctIndex": 0},
         {"type": "true-false", "question": "Pain is bare sensation.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Suffering adds ___, fear, story.", "answer": "resistance"},
         {"type": "true-false", "question": "All pain is equal to all suffering.", "correctAnswer": False}]},
    {"title": "Mindfulness for Chronic Pain",
     "body_html": r"""<p>Long studies show MBSR reduces pain intensity ratings, opioid use, and depression in chronic pain patients. Practice doesn't remove pain; it changes the relationship.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "MBSR reduces ___ use.", "answer": "opioid"},
         {"type": "multiple-choice", "question": "Practice changes: ", "options": ["the relationship to pain", "the bone", "DNA", "body shape"], "correctIndex": 0},
         {"type": "true-false", "question": "MBSR can reduce pain ratings.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Reduces also ___.", "answer": "depression"},
         {"type": "true-false", "question": "Practice removes all pain.", "correctAnswer": False}]},
    {"title": "Investigating Sensation",
     "body_html": r"""<p>Bring careful attention to a painful area. Note: location, size, edges, texture (sharp, dull, throbbing), temperature, change. Sensation usually shifts under steady gaze.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Note the ___ of pain.", "answer": "edges"},
         {"type": "multiple-choice", "question": "Quality: ", "options": ["sharp/dull/throbbing", "good/bad", "hot/cold only", "static"], "correctIndex": 0},
         {"type": "true-false", "question": "Sensation often shifts under attention.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Note location, size, ___.", "answer": "edges"},
         {"type": "true-false", "question": "Pain is always perfectly stable.", "correctAnswer": False}]},
    {"title": "Soft Belly Practice",
     "body_html": r"""<p>Stephen Levine's practice for chronic pain: place hand on belly and let it soften with the in-breath. Soft belly tells the nervous system: "It's safe."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Teacher: Stephen ___.", "answer": "Levine"},
         {"type": "multiple-choice", "question": "Hand placement: ", "options": ["belly", "head", "knee", "spine"], "correctIndex": 0},
         {"type": "true-false", "question": "Soft belly signals safety.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Belly softens with the ___-breath.", "answer": "in"},
         {"type": "true-false", "question": "Hard belly is the goal.", "correctAnswer": False}]},
    {"title": "Imagery for Pain",
     "body_html": r"""<p>Visualize warmth flowing through the painful area, or color shifting from red to blue, or pain dissolving into mist. Some find imagery more accessible than direct attention.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Color shift: red to ___.", "answer": "blue"},
         {"type": "multiple-choice", "question": "Imagery: ", "options": ["warmth flowing", "pain hardening", "skin tightening", "screaming"], "correctIndex": 0},
         {"type": "true-false", "question": "Imagery can be accessible.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pain dissolves into ___.", "answer": "mist"},
         {"type": "true-false", "question": "Imagery is forbidden in pain practice.", "correctAnswer": False}]},
    {"title": "Working with Fatigue",
     "body_html": r"""<p>Chronic illness often brings fatigue. Practice softer, briefer:</p><ul><li>5–10 minute sits.</li><li>Lying down is fine.</li><li>Body scan instead of breath focus.</li><li>Self-compassion phrases.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Sit length: ___–10 min.", "answer": "5"},
         {"type": "multiple-choice", "question": "Posture: ", "options": ["lying is fine", "must stand", "must full lotus", "must run"], "correctIndex": 0},
         {"type": "true-false", "question": "Body scan replaces breath focus.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Use self-___ phrases.", "answer": "compassion"},
         {"type": "true-false", "question": "Forced 60-minute sits are best.", "correctAnswer": False}]},
    {"title": "Doctor-Patient Mindfulness",
     "body_html": r"""<p>Before appointments:</p><ul><li>Write 3 questions to ask.</li><li>5 minutes of breath beforehand.</li><li>Bring a friend or take notes.</li><li>Pause if rushed; ask for slower pace.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Write ___ questions to ask.", "answer": "3"},
         {"type": "multiple-choice", "question": "Before: ", "options": ["5 min breath", "double caffeine", "skip meals", "argue"], "correctIndex": 0},
         {"type": "true-false", "question": "Bringing a friend helps.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Ask for slower ___.", "answer": "pace"},
         {"type": "true-false", "question": "Never take notes.", "correctAnswer": False}]},
    {"title": "Loving-Kindness for the Body",
     "body_html": r"""<p>For an ill or aging body: send metta to body parts that hurt.</p><ul><li>"May this knee be at ease."</li><li>"May this back find peace."</li><li>"May my body be safe."</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "May this ___ be at ease.", "answer": "knee"},
         {"type": "multiple-choice", "question": "Metta target: ", "options": ["body parts", "enemies only", "abstract ideas", "the past"], "correctIndex": 0},
         {"type": "true-false", "question": "Metta can address the body.", "correctAnswer": True},
         {"type": "fill-blank", "question": "May my body be ___.", "answer": "safe"},
         {"type": "true-false", "question": "Metta forbids body wishes.", "correctAnswer": False}]},
    {"title": "Cancer & Mindfulness",
     "body_html": r"""<p>Programs like MBCR (Mindfulness-Based Cancer Recovery, Linda Carlson) and MBSR for cancer patients reduce anxiety and improve sleep through diagnosis, treatment, and survivorship.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Program: ___.", "answer": "MBCR"},
         {"type": "multiple-choice", "question": "Researcher: ", "options": ["Linda Carlson", "Tara Brach", "Pema Chodron", "Hakuin"], "correctIndex": 0},
         {"type": "true-false", "question": "Programs improve sleep.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Helps through diagnosis, ___, survivorship.", "answer": "treatment"},
         {"type": "true-false", "question": "Mindfulness replaces oncology.", "correctAnswer": False}]},
    {"title": "Surgery & Recovery",
     "body_html": r"""<p>Pre-op breath practice and guided imagery improve recovery. Post-op: short body scans, self-compassion, gentle movement when cleared.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Pre-op: ___ practice.", "answer": "breath"},
         {"type": "multiple-choice", "question": "Post-op practice: ", "options": ["short body scans", "loud yoga", "running", "kickboxing"], "correctIndex": 0},
         {"type": "true-false", "question": "Practice can improve recovery.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Movement when ___.", "answer": "cleared"},
         {"type": "true-false", "question": "Forced workouts post-op are wise.", "correctAnswer": False}]},
    {"title": "Long Covid & Energy Pacing",
     "body_html": r"""<p>For long covid, ME/CFS, and similar: avoid push-crash cycles. Use energy envelopes — the day's allotment. Mindfulness helps notice early-warning fatigue cues.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Avoid push-___ cycles.", "answer": "crash"},
         {"type": "multiple-choice", "question": "Daily allotment: ", "options": ["energy envelope", "infinite battery", "power cap unknown", "nothing"], "correctIndex": 0},
         {"type": "true-false", "question": "Mindfulness notices early fatigue.", "correctAnswer": True},
         {"type": "fill-blank", "question": "ME/CFS = myalgic encephalomyelitis / chronic ___ syndrome.", "answer": "fatigue"},
         {"type": "true-false", "question": "Push past every fatigue signal.", "correctAnswer": False}]},
    {"title": "Mental Illness & Mindfulness",
     "body_html": r"""<p>Mindfulness can support but not replace clinical treatment. Specific cautions:</p><ul><li>Bipolar — long sits can destabilize during mania.</li><li>Schizophrenia — visualization may exacerbate symptoms; consult clinician.</li><li>OCD — mindful exposure differs from rumination.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Replaces clinical care: ___ (yes/no).", "answer": "no"},
         {"type": "multiple-choice", "question": "Bipolar caution: ", "options": ["destabilize during mania", "always safe", "dose up", "skip sleep"], "correctIndex": 0},
         {"type": "true-false", "question": "OCD distinguishes mindful exposure from rumination.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Schizophrenia: consult ___.", "answer": "clinician"},
         {"type": "true-false", "question": "All conditions handle meditation identically.", "correctAnswer": False}]},
    {"title": "Caregiver Mindfulness",
     "body_html": r"""<p>Caregivers often burn out. Practice priorities:</p><ul><li>Self-compassion daily.</li><li>Small breaks — 3-minute breathing space.</li><li>Permission to feel anger and grief.</li><li>Community — caregiver groups.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "3-minute ___ space.", "answer": "breathing"},
         {"type": "multiple-choice", "question": "Permission to feel: ", "options": ["anger and grief", "only joy", "only calm", "nothing"], "correctIndex": 0},
         {"type": "true-false", "question": "Caregivers burn out without practice.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Self-___ daily.", "answer": "compassion"},
         {"type": "true-false", "question": "Caregivers should ignore their own emotions.", "correctAnswer": False}]},
    {"title": "End-of-Life Practice",
     "body_html": r"""<p>Frank Ostaseski's "Five Invitations" guide end-of-life work: don't wait, welcome everything, bring your whole self, find a place of rest, cultivate don't-know mind.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Number of invitations: ___.", "answer": "5"},
         {"type": "multiple-choice", "question": "Author: ", "options": ["Frank Ostaseski", "Tara Brach", "Hakuin", "Aurobindo"], "correctIndex": 0},
         {"type": "true-false", "question": "Welcome everything is one of them.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Don't-___ mind.", "answer": "know"},
         {"type": "true-false", "question": "End-of-life practice is unimportant.", "correctAnswer": False}]},
    {"title": "Pain & Illness Checkpoint",
     "body_html": r"""<ul><li>Pain × resistance = suffering; mindfulness reduces resistance.</li><li>Investigate sensation; soft belly; metta for the body.</li><li>Adapt: shorter sits, lying posture, energy pacing.</li><li>Caregivers and end-of-life work matter; consult clinicians for serious conditions.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Mindfulness reduces resistance.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Caregiver tool: ", "options": ["3-min breathing space", "16-hour shift", "no breaks", "no community"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Soft ___.", "answer": "belly"},
         {"type": "true-false", "question": "Practice replaces medical care.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Stephen ___ taught soft belly.", "answer": "Levine"}]},
]

if __name__ == "__main__":
    render_unit(22, "Pain & Chronic Illness", 316, LESSONS)
