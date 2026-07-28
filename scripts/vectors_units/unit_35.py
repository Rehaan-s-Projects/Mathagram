#!/usr/bin/env python3
"""Unit 35 — 4-Vectors & Special Relativity (lessons 511-525)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Frames of Reference",
     "body_html": r"""
<p>An <strong>inertial frame</strong> is a coordinate system in which Newton's first law holds: a free particle moves in a straight line at constant speed. Different inertial frames are related by uniform translations.</p>
<p>Classical mechanics says the laws of physics are the same in every inertial frame, but space and time are absolute. Einstein replaced this with a different invariance principle (next lesson) that ties space and time together into <strong>spacetime</strong>.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Inertial frames are related by uniform motion.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Newton's first law holds:", "options": ["always", "only in inertial frames", "only in rotating frames", "never"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Einstein tied space and time into ___.", "answer": "spacetime"},
         {"type": "true-false", "question": "Classical mechanics treats space and time as absolute.", "correctAnswer": True},
         {"type": "true-false", "question": "Relativity treats time as universal.", "correctAnswer": False}]},
    {"title": "Galilean vs Lorentz Transformations",
     "body_html": r"""
<p><strong>Galilean transformation</strong> (classical, low speed):</p>
<div class="math-block">$$x' = x - vt, \quad t' = t$$</div>
<p><strong>Lorentz transformation</strong> (relativistic):</p>
<div class="math-block">$$x' = \gamma(x - vt), \quad t' = \gamma\left(t - \frac{vx}{c^2}\right), \quad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$$</div>
<p>For \(v \ll c\), \(\gamma \approx 1\) and Lorentz reduces to Galilean. For \(v\) close to \(c\), \(\gamma\) diverges and time/space mix dramatically.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\gamma = 1/\sqrt{1 - v^2/c^?}\). Fill: ___.", "answer": "2"},
         {"type": "multiple-choice", "question": r"For \(v \ll c\), Lorentz reduces to:", "options": ["Schrödinger", "Galilean", "Newtonian gravity", "no transformation"], "correctIndex": 1},
         {"type": "true-false", "question": "Lorentz transformations mix space and time.", "correctAnswer": True},
         {"type": "true-false", "question": "Galilean transformations conserve time.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"For \(v=0\), \(\gamma =\) ___.", "answer": "1"}]},
    {"title": "The Spacetime Continuum",
     "body_html": r"""
<p>An <strong>event</strong> is a point in 4D spacetime, labeled \((ct, x, y, z)\). Spacetime is the natural arena for relativity: events are absolute, but their decomposition into "space" and "time" depends on the observer.</p>
<p>The factor of \(c\) on time gives all four coordinates the same units (length). It's a notational convenience; some treatments use \(c=1\) (natural units).</p>""",
     "exercises": [
         {"type": "true-false", "question": "An event is a point in spacetime.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Coordinates of spacetime:", "options": [r"\((t, x, y, z)\)", r"\((ct, x, y, z)\)", r"\((x, y, z, t)\)", "all of these (conventions vary)"], "correctIndex": 3},
         {"type": "fill-blank", "question": "The c-factor gives time the same units as ___.", "answer": "length"},
         {"type": "true-false", "question": "Decomposition of an event into space and time is observer-independent.", "correctAnswer": False},
         {"type": "true-false", "question": "Natural units often set c = 1.", "correctAnswer": True}]},
    {"title": "4-Position",
     "body_html": r"""
<p>The <strong>4-position</strong> of an event:</p>
<div class="math-block">$$x^\mu = (ct, x, y, z) = (ct, \vec{r})$$</div>
<p>Greek index \(\mu\) runs from \(0\) to \(3\): \(\mu = 0\) is the time component, \(\mu = 1, 2, 3\) are the spatial components. (Some conventions use \(\mu = 1, 2, 3, 4\) instead.)</p>
<p>Lorentz transformations are linear transformations of \(x^\mu\) that preserve a special bilinear form (next lesson).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"4-position: \(x^\mu = (ct, x, y,\) ___\()\).", "answer": "z"},
         {"type": "multiple-choice", "question": "Greek index μ runs:", "options": ["0 to 3", "1 to 3", "1 to 4", "any range"], "correctIndex": 0},
         {"type": "true-false", "question": "Lorentz transformations are linear in 4-position.", "correctAnswer": True},
         {"type": "true-false", "question": r"\(x^0 = ct\) is the time component (typical convention).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(x^\mu\) has ___ components.", "answer": "4"}]},
    {"title": "4-Velocity",
     "body_html": r"""
<p>The <strong>4-velocity</strong>: derivative of 4-position with respect to <strong>proper time</strong> \(\tau\) (time as measured by the moving particle's own clock):</p>
<div class="math-block">$$u^\mu = \frac{dx^\mu}{d\tau} = \gamma(c, \vec{v})$$</div>
<p>Has constant magnitude squared: \(u^\mu u_\mu = c^2\) for any massive particle, in any frame. This is one of the cleanest geometric facts in relativity.</p>
<p>For \(v=0\): \(u^\mu = (c, 0, 0, 0)\). The particle is "moving through time at speed \(c\)."</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"4-velocity: \(u^\mu = dx^\mu / d\) ___.", "answer": "tau"},
         {"type": "multiple-choice", "question": r"\(u^\mu u_\mu\) for a massive particle:", "options": [r"\(c^2\)", "0", r"\(v^2\)", "depends on frame"], "correctIndex": 0},
         {"type": "true-false", "question": "Proper time is measured by the moving particle's own clock.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(u^\mu = \gamma(c, \vec{v}\) ___\()\). Fill the missing tail (none): _v_.", "answer": "v"},
         {"type": "true-false", "question": "An object at rest is still moving through time at c.", "correctAnswer": True}]},
    {"title": "The Minkowski Metric",
     "body_html": r"""
<p>The <strong>Minkowski metric</strong>:</p>
<div class="math-block">$$\eta_{\mu\nu} = \text{diag}(+1, -1, -1, -1)$$</div>
<p>(or \((-,+,+,+)\) — conventions split). It defines the inner product of 4-vectors:</p>
<div class="math-block">$$A^\mu B_\mu = \eta_{\mu\nu} A^\mu B^\nu = A^0 B^0 - \vec{A}\cdot\vec{B}$$</div>
<p>The norm \(x^\mu x_\mu = (ct)^2 - x^2 - y^2 - z^2\) is the <strong>spacetime interval</strong> — invariant under Lorentz transformations. This is what relativity preserves; ordinary length isn't preserved.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Minkowski metric has signature (+,-,-,-) or (-,+,+,+).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Spacetime interval: \((ct)^2 - x^2 - y^2 - z^?\). Fill: ___.", "answer": "2"},
         {"type": "multiple-choice", "question": "Lorentz transformations preserve:", "options": ["length", "time", "spacetime interval", "speed"], "correctIndex": 2},
         {"type": "true-false", "question": "Ordinary 3D length is invariant under Lorentz boosts.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"\(\eta_{00} =\) ___ (in the +,-,-,- convention).", "answer": "1"}]},
    {"title": "Lorentz Boosts as Hyperbolic Rotations",
     "body_html": r"""
<p>A Lorentz boost in the \(x\)-direction can be written as a hyperbolic rotation:</p>
<div class="math-block">$$\begin{pmatrix} ct' \\ x' \end{pmatrix} = \begin{pmatrix} \cosh\eta & -\sinh\eta \\ -\sinh\eta & \cosh\eta \end{pmatrix} \begin{pmatrix} ct \\ x \end{pmatrix}$$</div>
<p>where \(\eta\) (rapidity) satisfies \(\tanh\eta = v/c\). Compare to Euclidean rotations with \(\cos, \sin\) — Lorentz boosts use the hyperbolic versions, reflecting Minkowski's mixed-sign metric.</p>
<p>Rapidities <strong>add</strong> when boosts compose. This is why velocities don't simply add: the rapidity does.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Lorentz boosts are hyperbolic rotations.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\tanh\eta = v/\) ___.", "answer": "c"},
         {"type": "multiple-choice", "question": "Rapidities:", "options": ["multiply", "add", "divide", "subtract"], "correctIndex": 1},
         {"type": "true-false", "question": "Velocity addition is simple in special relativity.", "correctAnswer": False},
         {"type": "true-false", "question": "Hyperbolic rotations preserve the Minkowski interval.", "correctAnswer": True}]},
    {"title": "Time Dilation",
     "body_html": r"""
<p>A clock moving at speed \(v\) ticks slower (according to a stationary observer) by a factor of \(\gamma\):</p>
<div class="math-block">$$\Delta t = \gamma \Delta\tau$$</div>
<p>\(\Delta\tau\) is proper time (clock's own time); \(\Delta t\) is observed time.</p>
<p>This is geometric: the moving clock's worldline is "tilted" in spacetime, and the spacetime interval along it is shorter (in proper-time units) than the coordinate-time difference suggests.</p>
<p>Confirmed experimentally: muons in cosmic rays, GPS satellites, atomic clocks on airplanes.</p>""",
     "exercises": [
         {"type": "true-false", "question": "A moving clock ticks slower than a stationary one (per outside observer).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\Delta t = \gamma\) ___.", "answer": "tau"},
         {"type": "multiple-choice", "question": r"For \(v = 0.6c\), \(\gamma =\)", "options": ["0.6", "0.8", "1.25", "5"], "correctIndex": 2},
         {"type": "true-false", "question": "GPS uses time dilation corrections.", "correctAnswer": True},
         {"type": "true-false", "question": "Cosmic-ray muons reach the ground because of time dilation.", "correctAnswer": True}]},
    {"title": "Length Contraction",
     "body_html": r"""
<p>An object of rest-length \(L_0\) moving at speed \(v\) along its length appears (to a stationary observer) shortened to</p>
<div class="math-block">$$L = L_0/\gamma$$</div>
<p>Only along the direction of motion — perpendicular dimensions are unchanged.</p>
<p>The combined effect of length contraction and time dilation is what makes the spacetime interval invariant. Both are coordinate effects, not "real" changes in the object — but they're observer-dependent in a real, measurable way.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(L = L_0/\) ___.", "answer": "gamma"},
         {"type": "true-false", "question": "Length contraction occurs only along the direction of motion.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"At \(v = 0.6c\), a meter stick along motion measures:", "options": ["1.25 m", "0.8 m", "0.6 m", "1.6 m"], "correctIndex": 1},
         {"type": "true-false", "question": "Length contraction in perpendicular directions is also observed.", "correctAnswer": False},
         {"type": "true-false", "question": "Both time dilation and length contraction together preserve the spacetime interval.", "correctAnswer": True}]},
    {"title": "4-Momentum & E = mc²",
     "body_html": r"""
<p>The <strong>4-momentum</strong>:</p>
<div class="math-block">$$p^\mu = m u^\mu = (E/c, \vec{p})$$</div>
<p>where \(E = \gamma m c^2\) (relativistic energy) and \(\vec{p} = \gamma m\vec{v}\) (relativistic momentum).</p>
<p>The invariant: \(p^\mu p_\mu = (E/c)^2 - |\vec{p}|^2 = (mc)^2\), giving the famous</p>
<div class="math-block">$$E^2 = (\vec{p}c)^2 + (mc^2)^2$$</div>
<p>For a particle at rest (\(\vec{p}=0\)): \(E = mc^2\). Energy and mass are the same thing.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(E^2 = (pc)^2 + (mc^2)^2\) is the energy-momentum relation.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"At rest: \(E = m c^?\). Fill: ___.", "answer": "2"},
         {"type": "multiple-choice", "question": r"\(p^\mu p_\mu =\)", "options": ["0", r"\((mc)^2\)", r"\(\gamma^2\)", r"\(E\)"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(p^\mu = (E/c, \vec{p})\) is the 4-momentum.", "correctAnswer": True},
         {"type": "true-false", "question": "Energy and mass are equivalent.", "correctAnswer": True}]},
    {"title": "Causality & Light Cones",
     "body_html": r"""
<p>The Minkowski interval \(s^2 = (ct)^2 - r^2\) classifies pairs of events:</p>
<ul>
<li>\(s^2 > 0\) — <strong>timelike</strong>: cause-and-effect possible; a slower-than-light signal can connect them.</li>
<li>\(s^2 = 0\) — <strong>lightlike</strong> (null): only light can connect them.</li>
<li>\(s^2 < 0\) — <strong>spacelike</strong>: no causal influence possible; signals would need to exceed \(c\).</li>
</ul>
<p>The set of events lightlike-connected to an event \(P\) forms its <strong>light cone</strong>. Events inside the future cone are P's future; outside the cone, they're causally disconnected.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Spacelike separated events can't influence each other.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(s^2 = 0\) means:", "options": ["timelike", "spacelike", "lightlike", "infinite"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Light-cone interior is the ___ of an event.", "answer": "future"},
         {"type": "true-false", "question": "Causality requires staying within light cones.", "correctAnswer": True},
         {"type": "true-false", "question": "Faster-than-light signals are allowed in special relativity.", "correctAnswer": False}]},
    {"title": "The Stress-Energy Tensor (Preview)",
     "body_html": r"""
<p>The <strong>stress-energy tensor</strong> \(T^{\mu\nu}\) packages energy density, momentum density, energy flux, and stress into one geometric object. \(T^{00}\) is energy density, \(T^{0i}\) is momentum density / energy flux, \(T^{ij}\) is stress.</p>
<p>In general relativity, \(T^{\mu\nu}\) appears on the right side of Einstein's field equations: \(G^{\mu\nu} = 8\pi G T^{\mu\nu}/c^4\). Mass-energy curves spacetime.</p>
<p>For a perfect fluid: \(T^{\mu\nu} = (\rho + p/c^2)u^\mu u^\nu + p g^{\mu\nu}\). For an electromagnetic field there's a similar nice expression.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(T^{00}\) is energy density.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Stress-energy appears in:", "options": ["Maxwell's", "Einstein's field eqns", "Newton's law", "thermodynamics"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"GR: \(G^{\mu\nu} = 8\pi G T^{\mu\nu}/c^?\). Fill: ___.", "answer": "4"},
         {"type": "true-false", "question": "Mass-energy curves spacetime in GR.", "correctAnswer": True},
         {"type": "true-false", "question": r"\(T^{\mu\nu}\) is a 4×4 tensor.", "correctAnswer": True}]},
    {"title": "Tensor Notation Sneak Peek",
     "body_html": r"""
<p>Summation convention: a repeated index, one upstairs and one downstairs, is summed:</p>
<div class="math-block">$$A^\mu B_\mu = \sum_\mu A^\mu B_\mu$$</div>
<p>Upstairs (contravariant) and downstairs (covariant) indices are related by the metric:</p>
<div class="math-block">$$A_\mu = \eta_{\mu\nu} A^\nu$$</div>
<p>This streamlines the heavy machinery of relativity. Tensors of any rank \((p,q)\) generalize: \(T^{\mu_1\ldots\mu_p}{}_{\nu_1\ldots\nu_q}\). Tensor calculus is the natural language of GR (next unit on tensors).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Repeated upper-lower indices imply summation (Einstein convention).", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Lowering an index uses:", "options": ["the metric", "the determinant", "the trace", "the inverse"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"\(A_\mu = \eta_{\mu\nu}\) ___.", "answer": "A^nu"},
         {"type": "true-false", "question": "Tensor notation is heavily used in GR.", "correctAnswer": True},
         {"type": "true-false", "question": "Indices upstairs are contravariant; downstairs are covariant.", "correctAnswer": True}]},
    {"title": "Practice: 4-Vectors",
     "body_html": r"""
<p>Quick problems:</p>
<ol>
<li>4-velocity squared for a massive particle: \(c^2\), no matter the speed.</li>
<li>Time dilation factor at \(v = 0.8c\): \(\gamma = 1/\sqrt{1 - 0.64} = 5/3 \approx 1.67\).</li>
<li>Length contraction at \(v=0.8c\): \(L = 0.6 L_0\).</li>
<li>Energy of a 1 kg mass at rest: \(E = mc^2 \approx 9 \times 10^{16}\) J.</li>
<li>If two events have \(s^2 > 0\), one can causally affect the other.</li>
</ol>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\gamma\) at \(v = 0.8c\) (approx): ___ (one decimal).", "answer": "1.7"},
         {"type": "multiple-choice", "question": r"Length contraction at \(v=0.8c\):", "options": [r"\(0.6 L_0\)", r"\(L_0\)", r"\(0.8 L_0\)", r"\(0.4 L_0\)"], "correctIndex": 0},
         {"type": "true-false", "question": "4-velocity squared is c² for massive particles.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(E\) of 1 kg at rest: \(\sim 9 \times 10^{?}\) J. Fill: ___.", "answer": "16"},
         {"type": "true-false", "question": "Spacelike separation forbids causal influence.", "correctAnswer": True}]},
    {"title": "Special Relativity Checkpoint",
     "body_html": r"""
<p>Recap of Unit 35:</p>
<ul>
<li>Spacetime is the natural arena for relativity — events get 4-position \((ct, \vec{r})\).</li>
<li>Lorentz transformations preserve the Minkowski interval \((ct)^2 - r^2\).</li>
<li>4-velocity \(u^\mu = \gamma(c, \vec{v})\), 4-momentum \(p^\mu = (E/c, \vec{p})\).</li>
<li>Time dilation, length contraction, \(E = mc^2\) — all geometric consequences.</li>
<li>Light cones partition events into causally connected (timelike), causally disconnected (spacelike), and lightlike.</li>
<li>Tensor notation packages 4-vectors and beyond into a unified language.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Lorentz transformations preserve the Minkowski interval.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(E^2 =\)", "options": [r"\((pc)^2 + (mc^2)^2\)", r"\(mc^2\)", r"\(p^2 + m^2\)", r"\(\gamma^2\)"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"\(\gamma = 1/\sqrt{1 - v^2/c^?}\). Fill: ___.", "answer": "2"},
         {"type": "true-false", "question": "Spacelike-separated events can interact causally.", "correctAnswer": False},
         {"type": "true-false", "question": "GPS works correctly only with relativistic corrections.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"At rest, \(E = m\) ___.", "answer": "c^2"},
         {"type": "true-false", "question": "Special relativity unifies space and time.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(35, "4-Vectors & Special Relativity", 511, LESSONS)
