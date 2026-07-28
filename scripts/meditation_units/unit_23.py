#!/usr/bin/env python3
"""Meditation Unit 23 — Grief & Loss (lessons 331-345)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_meditation import render_unit

LESSONS = [
    {"title": "What Is Grief?",
     "body_html": r"""<p>Grief is the natural response to loss — of a person, role, place, ability. It moves in waves and reorganizes a life over months and years. There is no schedule.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Grief moves in ___.", "answer": "waves"},
         {"type": "multiple-choice", "question": "Loss can be: ", "options": ["person/role/place/ability", "only person", "only money", "only objects"], "correctIndex": 0},
         {"type": "true-false", "question": "There is no fixed schedule.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Grief reorganizes a ___.", "answer": "life"},
         {"type": "true-false", "question": "Grief lasts only one week.", "correctAnswer": False}]},
    {"title": "Stages — Kübler-Ross Revisited",
     "body_html": r"""<p>Elisabeth Kübler-Ross's stages — denial, anger, bargaining, depression, acceptance — were observed in dying patients, not bereaved survivors. They are signals, not a path.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Stage list ends with ___.", "answer": "acceptance"},
         {"type": "multiple-choice", "question": "Originally observed in: ", "options": ["dying patients", "bereaved", "doctors", "nurses"], "correctIndex": 0},
         {"type": "true-false", "question": "Stages are signals, not a path.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Stage: ___ (often misunderstood as guilt).", "answer": "bargaining"},
         {"type": "true-false", "question": "Everyone experiences exact stages in order.", "correctAnswer": False}]},
    {"title": "Continuing Bonds",
     "body_html": r"""<p>Modern research (Klass, Silverman, Nickman) finds healthy mourners maintain a relationship with the lost person — talking to them, keeping mementos, marking dates. Not a problem to fix.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Concept name: ___ bonds.", "answer": "continuing"},
         {"type": "multiple-choice", "question": "Healthy mourners: ", "options": ["maintain relationship", "fully detach", "deny loss", "rage forever"], "correctIndex": 0},
         {"type": "true-false", "question": "Talking to the dead can be healthy.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Researcher: ___, Silverman, Nickman.", "answer": "Klass"},
         {"type": "true-false", "question": "Mementos must be discarded.", "correctAnswer": False}]},
    {"title": "Sitting with the Wave",
     "body_html": r"""<p>When grief surges:</p><ul><li>Stop and sit if possible.</li><li>Place hand on chest.</li><li>Breathe slowly through it.</li><li>Name what you feel.</li><li>Let it pass; it will.</li></ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "Place hand on ___.", "answer": "chest"},
         {"type": "multiple-choice", "question": "Strategy: ", "options": ["sit and breathe", "fight it", "deny it", "shop"], "correctIndex": 0},
         {"type": "true-false", "question": "Naming reduces grip.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Let it ___.", "answer": "pass"},
         {"type": "true-false", "question": "Waves never pass.", "correctAnswer": False}]},
    {"title": "Tonglen for Grief",
     "body_html": r"""<p>Adapt tonglen: on the in-breath, take in your own grief and the grief of all who have loved and lost; on the out-breath, send peace and ease. Common humanity included.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "On in-breath: take in ___.", "answer": "grief"},
         {"type": "multiple-choice", "question": "Out-breath: ", "options": ["peace and ease", "more grief", "noise", "nothing"], "correctIndex": 0},
         {"type": "true-false", "question": "Includes others who have lost.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tonglen is from ___ Buddhism.", "answer": "Tibetan"},
         {"type": "true-false", "question": "Tonglen is forbidden in grief.", "correctAnswer": False}]},
    {"title": "Anniversary Reactions",
     "body_html": r"""<p>Birthdays, death-day, holidays, season triggers may bring back grief. Plan something — a candle, a walk, a meal in their honor. Predict and accommodate.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Predict and ___.", "answer": "accommodate"},
         {"type": "multiple-choice", "question": "Trigger types: ", "options": ["dates and seasons", "only Mondays", "only weekdays", "never"], "correctIndex": 0},
         {"type": "true-false", "question": "A candle can mark the day.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Walk or ___ in honor.", "answer": "meal"},
         {"type": "true-false", "question": "Anniversary reactions are imaginary.", "correctAnswer": False}]},
    {"title": "Grief & the Body",
     "body_html": r"""<p>Grief lives in the body: chest tightness, throat lump, heaviness, exhaustion. Body-based practices — gentle yoga, walking, swimming, somatic experiencing — release stuck holding.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Body site: ___ tightness.", "answer": "chest"},
         {"type": "multiple-choice", "question": "Body practice: ", "options": ["gentle yoga", "ignoring body", "fasting only", "fighting"], "correctIndex": 0},
         {"type": "true-false", "question": "Walking releases stuck holding.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Throat ___.", "answer": "lump"},
         {"type": "true-false", "question": "Grief is purely mental.", "correctAnswer": False}]},
    {"title": "Pet Loss",
     "body_html": r"""<p>Grief over pets is real grief. Some friends and family minimize it. Find communities that don't. Rituals — paw print, photo, ceremony — help.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Find communities that ___ .", "answer": "don't"},
         {"type": "multiple-choice", "question": "Useful ritual: ", "options": ["paw print", "ignore", "throw out everything", "lecture friends"], "correctIndex": 0},
         {"type": "true-false", "question": "Pet grief is real.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Some people ___ it.", "answer": "minimize"},
         {"type": "true-false", "question": "Pet grief deserves shame.", "correctAnswer": False}]},
    {"title": "Anticipatory Grief",
     "body_html": r"""<p>When loss is foreseen — terminal illness, dementia, ending of a relationship — grief begins before death. Don't wait for "the right time" to feel it.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Begins before ___.", "answer": "death"},
         {"type": "multiple-choice", "question": "Trigger: ", "options": ["terminal illness", "promotion", "vacation", "rain"], "correctIndex": 0},
         {"type": "true-false", "question": "Anticipatory grief is normal.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Don't wait for the right ___.", "answer": "time"},
         {"type": "true-false", "question": "Anticipatory grief means selfishness.", "correctAnswer": False}]},
    {"title": "Complicated Grief",
     "body_html": r"""<p>When grief intensifies and persists severely past 12 months and impairs function, it may be complicated grief disorder. Therapy (especially Complicated Grief Treatment, Shear) helps.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Past ___ months and impaired.", "answer": "12"},
         {"type": "multiple-choice", "question": "Therapy named: ", "options": ["Shear's CGT", "DBT", "ACT", "Reiki"], "correctIndex": 0},
         {"type": "true-false", "question": "Complicated grief is treatable.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Therapist: ___.", "answer": "Shear"},
         {"type": "true-false", "question": "Severe persistent grief never warrants help.", "correctAnswer": False}]},
    {"title": "Rituals & Memorials",
     "body_html": r"""<p>Wakes, funerals, sitting shiva, ofrenda for Día de los Muertos, Obon — every culture has rituals. They give grief a place to live and a community to share it.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Mexican: ___ for Día de los Muertos.", "answer": "ofrenda"},
         {"type": "multiple-choice", "question": "Japanese: ", "options": ["Obon", "Hanami", "Shogatsu", "Tanabata"], "correctIndex": 0},
         {"type": "true-false", "question": "Rituals share grief with community.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Jewish: sitting ___.", "answer": "shiva"},
         {"type": "true-false", "question": "Rituals are pointless.", "correctAnswer": False}]},
    {"title": "Writing as Practice",
     "body_html": r"""<p>James Pennebaker's research: writing 15–20 minutes about emotional experiences improves immune markers, mood, and sleep. Don't worry about grammar; write for yourself.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Length: ___–20 min.", "answer": "15"},
         {"type": "multiple-choice", "question": "Researcher: ", "options": ["Pennebaker", "Kabat-Zinn", "Linehan", "Hayes"], "correctIndex": 0},
         {"type": "true-false", "question": "Improves mood and sleep.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Don't worry about ___.", "answer": "grammar"},
         {"type": "true-false", "question": "Writing must be perfect.", "correctAnswer": False}]},
    {"title": "Meaning-Making",
     "body_html": r"""<p>Robert Neimeyer's meaning reconstruction: grief is not just emotional management, it is rebuilding a life narrative that includes the loss. Stories, art, service all help.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Researcher: ___.", "answer": "Neimeyer"},
         {"type": "multiple-choice", "question": "Approach: ", "options": ["meaning reconstruction", "loss erasure", "denial", "blame"], "correctIndex": 0},
         {"type": "true-false", "question": "Stories and art help.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Rebuilds a life ___.", "answer": "narrative"},
         {"type": "true-false", "question": "Service has no place in grief.", "correctAnswer": False}]},
    {"title": "Sangha for Grief",
     "body_html": r"""<p>Grief groups — in person, online (e.g., The Dinner Party for younger adults), or via hospice — break the isolation. Shared grief is lighter grief.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Group for younger adults: The ___ Party.", "answer": "Dinner"},
         {"type": "multiple-choice", "question": "Source: ", "options": ["hospice", "lottery", "casino", "spam"], "correctIndex": 0},
         {"type": "true-false", "question": "Shared grief is lighter grief.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Groups break the ___.", "answer": "isolation"},
         {"type": "true-false", "question": "Grief groups don't exist online.", "correctAnswer": False}]},
    {"title": "Grief Checkpoint",
     "body_html": r"""<ul><li>Grief moves in waves; stages are signals, not a path.</li><li>Continuing bonds are healthy.</li><li>Body, ritual, writing, community all matter.</li><li>Complicated grief is treatable; seek help if persistent.</li></ul>""",
     "exercises": [
         {"type": "true-false", "question": "Continuing bonds are healthy.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Pennebaker writing duration: ", "options": ["15–20 min", "1 hour", "5 sec", "10 min"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Mexican ritual: ___.", "answer": "ofrenda"},
         {"type": "true-false", "question": "Complicated grief is untreatable.", "correctAnswer": False},
         {"type": "fill-blank", "question": "Grief moves in ___.", "answer": "waves"}]},
]

if __name__ == "__main__":
    render_unit(23, "Grief & Loss", 331, LESSONS)
