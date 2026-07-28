#!/usr/bin/env python3
"""Unit 34 — Maxwell's Equations as Vectors (lessons 496-510)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Electric Fields as Vector Fields",
     "body_html": r"""
<p>The electric field \(\vec{E}(\vec{r})\) is a vector field: at each point in space, an arrow telling you the force per unit charge on a small test charge placed there.</p>
<div class="math-block">$$\vec{F} = q\vec{E}$$</div>
<p>For a point charge \(Q\) at the origin, the field is</p>
<div class="math-block">$$\vec{E}(\vec{r}) = \frac{Q}{4\pi\epsilon_0 |\vec{r}|^2}\hat{r}$$</div>
<p>It's radial and falls off as \(1/r^2\). Multiple charges: superpose linearly. Continuous distributions: integrate.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Electric field is a vector field.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Force on charge \(q\): \(\vec{F} = q\) ___.", "answer": "E"},
         {"type": "multiple-choice", "question": "Point charge field falls off as:", "options": ["1/r", "1/r²", "1/r³", "constant"], "correctIndex": 1},
         {"type": "true-false", "question": "Electric fields obey superposition.", "correctAnswer": True},
         {"type": "true-false", "question": "Field of a positive charge points radially outward.", "correctAnswer": True}]},
    {"title": "Magnetic Fields as Vector Fields",
     "body_html": r"""
<p>The magnetic field \(\vec{B}(\vec{r})\) is also a vector field. Force on a charge moving with velocity \(\vec{v}\):</p>
<div class="math-block">$$\vec{F} = q\vec{v} \times \vec{B}$$</div>
<p>That cross product means: magnetic force is perpendicular to both \(\vec{v}\) and \(\vec{B}\), and zero on stationary charges. Combined with electric force:</p>
<div class="math-block">$$\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$$</div>
<p>This is the <strong>Lorentz force law</strong> — the bridge between fields and mechanics.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Magnetic force: \(q\vec{v}\) ___ \(\vec{B}\).", "answer": "x"},
         {"type": "true-false", "question": "Magnetic force on a stationary charge is zero.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Lorentz force law:", "options": [r"\(q\vec{E}\)", r"\(q(\vec{E} + \vec{v}\times\vec{B})\)", r"\(\vec{v}\times\vec{B}\)", r"\(q\vec{B}\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Magnetic force is parallel to velocity.", "correctAnswer": False},
         {"type": "true-false", "question": "B is a vector field on space.", "correctAnswer": True}]},
    {"title": "Gauss's Law for Electric Fields",
     "body_html": r"""
<p>Maxwell's first equation:</p>
<div class="math-block">$$\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$$</div>
<p>Integrated: total electric flux through any closed surface = enclosed charge over \(\epsilon_0\). Charges are sources of \(\vec{E}\) flux.</p>
<p>Use cases: spherical symmetry → field of point charge, cylindrical symmetry → field of line charge, planar symmetry → field of charged plane. Each yields a clean closed-form expression for \(\vec{E}\) without doing nasty integrals.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Gauss for \(\vec{E}\): \(\nabla \cdot \vec{E} = \rho /\) ___.", "answer": "epsilon_0"},
         {"type": "multiple-choice", "question": r"Gauss's law in integral form: \(\oiint \vec{E}\cdot d\vec{S} =\)", "options": [r"\(Q_\text{enc}/\epsilon_0\)", r"0", r"\(\rho V\)", r"\(\mu_0 \vec{J}\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Charges are sources of E-field flux.", "correctAnswer": True},
         {"type": "true-false", "question": "Gauss's law is most useful when there's symmetry.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Field of a point charge \(Q\) at the origin: \(\vec{E} \propto 1/r^?\). Fill: ___.", "answer": "2"}]},
    {"title": "Gauss's Law for Magnetism",
     "body_html": r"""
<p>Maxwell's second equation:</p>
<div class="math-block">$$\nabla \cdot \vec{B} = 0$$</div>
<p>Integrated: total magnetic flux through any closed surface is zero. <strong>There are no magnetic monopoles.</strong></p>
<p>Magnetic field lines have no beginnings or endings — they're closed loops. Every "outflow" of \(\vec{B}\) somewhere is matched by an "inflow" elsewhere. This is a universal experimental fact: no isolated magnetic charges have ever been observed.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\nabla \cdot \vec{B} = 0\) means no magnetic monopoles.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Total magnetic flux through any closed surface:", "options": ["depends on enclosed magnetism", "is zero", "is infinite", "depends on charge"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Magnetic field lines are ___ loops.", "answer": "closed"},
         {"type": "true-false", "question": "Isolated magnetic charges have been observed in nature.", "correctAnswer": False},
         {"type": "true-false", "question": "Magnetic field lines have starting and ending points.", "correctAnswer": False}]},
    {"title": "Faraday's Law in Detail",
     "body_html": r"""
<p>Maxwell's third equation:</p>
<div class="math-block">$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$</div>
<p>A changing magnetic field induces a circulation in the electric field — an EMF.</p>
<p>This explains: generators (rotating magnet → AC voltage), transformers (changing primary current → changing secondary voltage), inductors (changing current → back-EMF). Faraday's law is the foundation of essentially all electrical power technology.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Changing B induces EMF.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Faraday's law in differential form: \(\nabla \times \vec{E} =\)", "options": ["0", r"\(\rho/\epsilon_0\)", r"\(-\partial \vec{B}/\partial t\)", r"\(\mu_0\vec{J}\)"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"\(\oint \vec{E}\cdot d\vec{r} = -d\Phi_B/d\) ___.", "answer": "t"},
         {"type": "true-false", "question": "Faraday's law underlies generators and transformers.", "correctAnswer": True},
         {"type": "true-false", "question": "The minus sign is Lenz's law (induced EMF opposes the flux change).", "correctAnswer": True}]},
    {"title": "Ampère's Law (Static)",
     "body_html": r"""
<p>Maxwell's fourth equation, in its original (static) form:</p>
<div class="math-block">$$\nabla \times \vec{B} = \mu_0 \vec{J}$$</div>
<p>where \(\vec{J}\) is the current density. Currents are sources of \(\vec{B}\) curl. Integrated:</p>
<div class="math-block">$$\oint_C \vec{B} \cdot d\vec{r} = \mu_0 I_\text{enc}$$</div>
<p>This is Ampère's circuital law — useful for symmetric current distributions: long wire, solenoid, toroid.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Ampère's law: \(\nabla \times \vec{B} = \mu_0\) ___.", "answer": "J"},
         {"type": "multiple-choice", "question": "Currents are sources of B's:", "options": ["divergence", "curl", "magnitude", "color"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(\oint \vec{B}\cdot d\vec{r} = \mu_0 I_\text{enc}\) is the integral form.", "correctAnswer": True},
         {"type": "true-false", "question": "Solenoids and toroids fit Ampère's law nicely.", "correctAnswer": True},
         {"type": "true-false", "question": "Static Ampère's law is incomplete (Maxwell needed to fix it).", "correctAnswer": True}]},
    {"title": "Maxwell's Correction",
     "body_html": r"""
<p>Static Ampère's law breaks for time-varying currents (the displacement current is missing). Maxwell's correction:</p>
<div class="math-block">$$\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t}$$</div>
<p>The new term is the <strong>displacement current</strong>. Without it, charge wouldn't be conserved across a charging capacitor (no real \(\vec{J}\) flows through the gap, but \(\partial \vec{E}/\partial t\) is nonzero).</p>
<p>This addition makes Maxwell's equations symmetric: changing \(\vec{B}\) creates \(\vec{E}\) (Faraday), and changing \(\vec{E}\) creates \(\vec{B}\) (Maxwell's correction). Result: <strong>EM waves</strong>.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Maxwell's correction adds the displacement current.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Without displacement current:", "options": ["EM waves still exist", "charge isn't conserved across capacitors", "energy is lost", "no effect"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Displacement current: \(\mu_0 \epsilon_0\) ___.", "answer": "dE/dt"},
         {"type": "true-false", "question": "Maxwell's correction makes the equations symmetric for E and B.", "correctAnswer": True},
         {"type": "true-false", "question": "EM waves emerge from this symmetry.", "correctAnswer": True}]},
    {"title": "The Four Equations Together",
     "body_html": r"""
<p>Maxwell's equations in vacuum (no charges, no currents):</p>
<div class="math-block">$$\nabla \cdot \vec{E} = 0, \quad \nabla \cdot \vec{B} = 0$$</div>
<div class="math-block">$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \quad \nabla \times \vec{B} = \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t}$$</div>
<p>Eight scalar equations in six unknowns. These describe all of classical electromagnetism: light, radio, X-rays, microwaves. The most beautiful and consequential set of equations in physics.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Maxwell's equations describe all of classical electromagnetism.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Number of Maxwell equations:", "options": ["2", "3", "4", "6"], "correctIndex": 2},
         {"type": "true-false", "question": "In vacuum, divergences are zero.", "correctAnswer": True},
         {"type": "true-false", "question": "Light is described by Maxwell's equations.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Speed of light from Maxwell: \(c = 1/\sqrt{\mu_0\) ___\()\).", "answer": "epsilon_0"}]},
    {"title": "EM Waves from Maxwell",
     "body_html": r"""
<p>Take the curl of Faraday's law:</p>
<div class="math-block">$$\nabla \times (\nabla \times \vec{E}) = -\partial_t (\nabla \times \vec{B}) = -\mu_0\epsilon_0 \partial_t^2 \vec{E}$$</div>
<p>Using the identity \(\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla\cdot\vec{E}) - \nabla^2 \vec{E}\) and \(\nabla \cdot \vec{E} = 0\) in vacuum:</p>
<div class="math-block">$$\nabla^2 \vec{E} = \mu_0\epsilon_0 \partial_t^2 \vec{E}$$</div>
<p>The wave equation. Wave speed: \(c = 1/\sqrt{\mu_0\epsilon_0} \approx 3 \times 10^8\) m/s — the speed of light. Maxwell deduced this in 1865, predicting EM waves before they were observed.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Maxwell's equations imply E (and B) satisfy a wave equation.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(c = 1/\sqrt{\mu_0\) ___\()\).", "answer": "epsilon_0"},
         {"type": "multiple-choice", "question": "Maxwell predicted EM waves in:", "options": ["1820", "1865", "1905", "1932"], "correctIndex": 1},
         {"type": "true-false", "question": "EM waves were observed before Maxwell's prediction.", "correctAnswer": False},
         {"type": "true-false", "question": "The wave equation comes from combining Faraday's and Maxwell's-corrected-Ampère's laws.", "correctAnswer": True}]},
    {"title": "Light as an EM Wave",
     "body_html": r"""
<p>Plane-wave solutions of Maxwell:</p>
<div class="math-block">$$\vec{E} = \vec{E}_0 \cos(\vec{k} \cdot \vec{r} - \omega t)$$</div>
<p>with \(\vec{B} = \hat{k} \times \vec{E}/c\) and \(\omega = c|\vec{k}|\). Direction \(\hat{k}\) is the propagation, \(\vec{E}_0\) is the polarization (perpendicular to \(\hat{k}\)).</p>
<p>Light, X-rays, microwaves, radio — all the same kind of wave, just at different frequencies. The "spectrum" is the range of \(\omega\) values.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"In a plane wave, \(\vec{E} \perp \vec{B} \perp \vec{k}\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(\omega =\)", "options": [r"\(c|\vec{k}|\)", r"\(c^2 |\vec{k}|\)", r"\(|\vec{k}|/c\)", r"\(\vec{E}_0\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Light, radio, and X-rays are all EM waves.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\vec{B}\) of a plane wave: \(\hat k \times \vec{E}/\) ___.", "answer": "c"},
         {"type": "true-false", "question": "Polarization is perpendicular to propagation.", "correctAnswer": True}]},
    {"title": "The Poynting Vector",
     "body_html": r"""
<p>The <strong>Poynting vector</strong>:</p>
<div class="math-block">$$\vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B}$$</div>
<p>It represents the directional <strong>energy flux density</strong> (energy per area per time) of the EM field. Magnitude: how much power crosses a unit area per second. Direction: where the energy is flowing.</p>
<p>For a plane wave, \(\vec{S}\) points along \(\hat{k}\) (the wave direction). For a flashlight, \(\vec{S}\) tells you what direction the light goes.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\vec{S} = \vec{E} \times \vec{B}/\mu_0\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Poynting vector represents:", "options": ["force", "energy flux density", "charge", "frequency"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"For a plane wave, \(\vec{S}\) points along \(\hat\) ___.", "answer": "k"},
         {"type": "true-false", "question": "Poynting vector tells you where EM energy is flowing.", "correctAnswer": True},
         {"type": "true-false", "question": "Units of S are W/m².", "correctAnswer": True}]},
    {"title": "Lorentz Force Law Recap",
     "body_html": r"""
<p>The full Lorentz force law:</p>
<div class="math-block">$$\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$$</div>
<p>This is the bridge between fields (described by Maxwell) and matter (described by Newton). For continuous charge/current distributions, the force per unit volume is \(\rho\vec{E} + \vec{J} \times \vec{B}\).</p>
<p>Together, Maxwell's equations + Lorentz force constitute classical electromagnetism — a complete theory of electromagnetic phenomena until you reach quantum scales.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\vec{F} = q\vec{E} + q\vec{v} \times \vec{B}\) is the Lorentz force.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Force per unit volume: \(\rho \vec{E} + \vec{J} \times\) ___.", "answer": "B"},
         {"type": "multiple-choice", "question": "Maxwell + Lorentz =", "options": ["thermodynamics", "classical electromagnetism", "quantum mechanics", "general relativity"], "correctIndex": 1},
         {"type": "true-false", "question": "Lorentz force connects fields and matter.", "correctAnswer": True},
         {"type": "true-false", "question": "Classical EM holds at all scales.", "correctAnswer": False}]},
    {"title": "Vector & Scalar Potentials",
     "body_html": r"""
<p>Since \(\nabla \cdot \vec{B} = 0\), \(\vec{B} = \nabla \times \vec{A}\) for some <strong>vector potential</strong> \(\vec{A}\). Substituting into Faraday and using a scalar potential \(\varphi\):</p>
<div class="math-block">$$\vec{E} = -\nabla\varphi - \frac{\partial \vec{A}}{\partial t}$$</div>
<p>Working with \((\varphi, \vec{A})\) instead of \((\vec{E}, \vec{B})\) often simplifies problems and is the natural language for quantum and relativistic EM. Gauge freedom: \(\vec{A} \to \vec{A} + \nabla \chi\) leaves \(\vec{B}\) unchanged.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\vec{B} = \nabla \times\) ___.", "answer": "A"},
         {"type": "multiple-choice", "question": r"\(\vec{E} =\)", "options": [r"\(-\nabla \varphi\)", r"\(-\nabla\varphi - \partial \vec{A}/\partial t\)", r"\(\nabla \times \vec{A}\)", r"\(\partial \vec{A}/\partial t\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Gauge transformations leave fields unchanged.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Gauge transformation: \(\vec{A} \to \vec{A} + \nabla\) ___.", "answer": "chi"},
         {"type": "true-false", "question": "Potentials are the natural language for quantum EM.", "correctAnswer": True}]},
    {"title": "Practice: Apply Maxwell",
     "body_html": r"""
<p>Quick problems:</p>
<ol>
<li>Field of an infinite line charge \(\lambda\) at distance \(r\): use Gauss with cylindrical symmetry. \(E = \lambda/(2\pi\epsilon_0 r)\).</li>
<li>Field inside a long solenoid with \(n\) turns/length and current \(I\): use Ampère. \(B = \mu_0 n I\), uniform along the axis.</li>
<li>Field of an infinite charged plane with surface density \(\sigma\): \(E = \sigma/(2\epsilon_0)\), perpendicular to the plane.</li>
<li>The "speed of light" \(c\) is determined by \(\mu_0\) and \(\epsilon_0\), not measured separately.</li>
</ol>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Field of infinite line charge \(\lambda\) at distance \(r\): \(\lambda/(2\pi\epsilon_0\) ___\()\).", "answer": "r"},
         {"type": "multiple-choice", "question": "Field inside a solenoid:", "options": [r"\(\mu_0 nI\)", r"\(\mu_0 I/r\)", r"0", r"\(\mu_0 I^2\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Field of an infinite charged plane is uniform on either side.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(c = 1/\) ___.", "answer": "sqrt(mu_0 epsilon_0)"},
         {"type": "true-false", "question": "Symmetric distributions are easier with Gauss/Ampère.", "correctAnswer": True}]},
    {"title": "Maxwell Checkpoint",
     "body_html": r"""
<p>Recap of Unit 34:</p>
<ul>
<li>Maxwell's equations: \(\nabla\cdot\vec{E}=\rho/\epsilon_0\), \(\nabla\cdot\vec{B}=0\), \(\nabla\times\vec{E}=-\partial_t\vec{B}\), \(\nabla\times\vec{B}=\mu_0\vec{J}+\mu_0\epsilon_0\partial_t\vec{E}\).</li>
<li>Lorentz force: \(\vec{F} = q(\vec{E} + \vec{v}\times\vec{B})\).</li>
<li>EM waves emerge from the equations; speed \(c = 1/\sqrt{\mu_0\epsilon_0}\).</li>
<li>Poynting vector \(\vec{S} = \vec{E}\times\vec{B}/\mu_0\) gives energy flux.</li>
<li>Vector & scalar potentials \((\varphi, \vec{A})\) provide an alternative formulation; gauge freedom leaves fields unchanged.</li>
<li>The big vector calculus theorems are the language Maxwell speaks.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\nabla \cdot \vec{B} = 0\) means no magnetic monopoles.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Maxwell predicted:", "options": ["protons", "EM waves", "atoms", "neutrinos"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\vec{S} = \vec{E}\times\vec{B}/\) ___.", "answer": "mu_0"},
         {"type": "true-false", "question": "Lorentz force is part of Maxwell's equations.", "correctAnswer": False},
         {"type": "true-false", "question": "Light is described by Maxwell's equations.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(c \approx\) ___ \(\times 10^8\) m/s.", "answer": "3"},
         {"type": "true-false", "question": "Without displacement current, EM waves wouldn't exist.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(34, "Maxwell's Equations as Vectors", 496, LESSONS)
