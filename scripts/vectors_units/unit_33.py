#!/usr/bin/env python3
"""Unit 33 — Green's, Stokes' & Divergence Theorems (lessons 481-495)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Green's Theorem (Full)",
     "body_html": r"""
<p>For a region \(R\) in the plane with positively-oriented boundary \(C\), and \(\vec{F} = (P, Q)\):</p>
<div class="math-block">$$\oint_C P\,dx + Q\,dy = \iint_R \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\,dA$$</div>
<p>"Positively oriented" means counter-clockwise — the region is on your left as you walk the boundary.</p>
<p>The integrand on the right is the 2D curl of \(\vec{F}\). Green's theorem says: <strong>circulation around the boundary = total curl inside</strong>. It's the 2D version of Stokes' theorem.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"Green's theorem requires \(C\) to be a closed curve.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Green's: \(\oint P\,dx + Q\,dy = \iint (\partial Q/\partial x - \partial P /\partial y)\,d\) ___.", "answer": "A"},
         {"type": "multiple-choice", "question": "Positive orientation of a 2D boundary is:", "options": ["clockwise", "counter-clockwise", "either", "doesn't matter"], "correctIndex": 1},
         {"type": "true-false", "question": "Green's is the 2D version of Stokes' theorem.", "correctAnswer": True},
         {"type": "true-false", "question": "The integrand on the right is the 2D curl of (P, Q).", "correctAnswer": True}]},
    {"title": "Green's: Area Application",
     "body_html": r"""
<p>Setting \(P = -y/2\), \(Q = x/2\) in Green's theorem gives</p>
<div class="math-block">$$\text{Area}(R) = \frac{1}{2}\oint_C (x\,dy - y\,dx)$$</div>
<p>Other choices: \(P=0, Q=x\) gives \(\oint x\,dy\); \(P = -y, Q = 0\) gives \(-\oint y\,dx\). All compute the same area.</p>
<p>This formula is the math behind <strong>planimeters</strong> — historical drafting instruments that measure area by tracing a boundary.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Area = \(\tfrac{1}{2}\oint(x\,dy - y\,d\) ___\()\).", "answer": "x"},
         {"type": "multiple-choice", "question": r"\(\oint x\,dy =\)", "options": ["circumference", "area", "perimeter", "volume"], "correctIndex": 1},
         {"type": "true-false", "question": "Planimeters use Green's theorem.", "correctAnswer": True},
         {"type": "true-false", "question": "The area formula requires the curve to be closed.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Area of unit disk \(\pi \cdot\) ___.", "answer": "1"}]},
    {"title": "The 3D Divergence Theorem",
     "body_html": r"""
<p>For a solid region \(V\) with closed surface \(S = \partial V\) (outward-oriented), and a vector field \(\vec{F}\):</p>
<div class="math-block">$$\oiint_S \vec{F} \cdot d\vec{S} = \iiint_V \nabla \cdot \vec{F}\,dV$$</div>
<p>The total flux out of the volume equals the integral of divergence inside.</p>
<p>This is the central theorem connecting <em>local</em> behavior (divergence at every point) to <em>global</em> behavior (net flux through the boundary). Most physical conservation laws (mass, charge, energy) come from the divergence theorem applied to a flux/current vector.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Divergence theorem: \(\oiint \vec{F}\cdot d\vec{S} = \iiint \nabla \cdot \vec{F}\,d\) ___.", "answer": "V"},
         {"type": "multiple-choice", "question": "Surface S in the divergence theorem must be:", "options": ["open", "closed", "flat", "any"], "correctIndex": 1},
         {"type": "true-false", "question": "The normal in the divergence theorem points outward.", "correctAnswer": True},
         {"type": "true-false", "question": "Most conservation laws come from this theorem.", "correctAnswer": True},
         {"type": "true-false", "question": "Divergence theorem is also called Gauss's theorem.", "correctAnswer": True}]},
    {"title": "Divergence Theorem: Examples",
     "body_html": r"""
<p><strong>Example 1.</strong> \(\vec{F} = (x, y, z)\), unit sphere. \(\nabla \cdot \vec{F} = 3\). Volume of unit ball \(= \tfrac{4}{3}\pi\). Flux \(= 3 \cdot \tfrac{4}{3}\pi = 4\pi\). Matches direct surface computation.</p>
<p><strong>Example 2.</strong> \(\vec{F} = (x^2, y^2, z^2)\) through unit cube \([0,1]^3\). Divergence \(= 2x + 2y + 2z\). Volume integral: \(\iiint_V (2x+2y+2z)\,dV = 3\). Flux through cube boundary equals \(3\) — much easier than integrating over six faces directly.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\nabla \cdot (x, y, z) =\) ___.", "answer": "3"},
         {"type": "multiple-choice", "question": r"Flux of \((x,y,z)\) through unit sphere:", "options": ["0", r"\(\pi\)", r"\(2\pi\)", r"\(4\pi\)"], "correctIndex": 3},
         {"type": "true-false", "question": "Divergence theorem can simplify flux through cube boundaries.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\nabla \cdot (x^2, y^2, z^2) = 2x + 2y + 2\) ___.", "answer": "z"},
         {"type": "true-false", "question": "Volume of unit ball is 4π/3.", "correctAnswer": True}]},
    {"title": "Gauss's Law",
     "body_html": r"""
<p>Maxwell's first equation: \(\nabla \cdot \vec{E} = \rho/\epsilon_0\) (charge density divided by vacuum permittivity).</p>
<p>Integrate over a region using the divergence theorem:</p>
<div class="math-block">$$\oiint_S \vec{E} \cdot d\vec{S} = \frac{Q_{\text{enc}}}{\epsilon_0}$$</div>
<p>Total electric flux through any closed surface equals the enclosed charge over \(\epsilon_0\). This is <strong>Gauss's Law</strong>: charge is the source of electric field flux. Massively useful for computing fields under symmetry — point charge, line charge, infinite plane.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Gauss's law: total electric flux \(= Q_{\text{enc}} / \) ___.", "answer": "epsilon_0"},
         {"type": "multiple-choice", "question": r"Maxwell's first equation: \(\nabla \cdot \vec{E} =\)", "options": [r"\(\rho/\epsilon_0\)", "0", r"\(\vec{B}\)", r"\(\rho c\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Gauss's law is the integral form of Maxwell's first equation.", "correctAnswer": True},
         {"type": "true-false", "question": "Symmetric charge distributions admit easy field calculations via Gauss.", "correctAnswer": True},
         {"type": "true-false", "question": "Charge is the source of electric field flux.", "correctAnswer": True}]},
    {"title": "Heat Flow & Continuity",
     "body_html": r"""
<p><strong>Heat equation.</strong> Heat flux is \(\vec{q} = -k\nabla T\) (Fourier's law). Conservation of energy plus the divergence theorem gives:</p>
<div class="math-block">$$\rho c \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T)$$</div>
<p>The continuity equation \(\partial_t \rho + \nabla \cdot (\rho\vec{v}) = 0\) (mass conservation) is similarly the local form of "what flows out of any region must come from inside."</p>
<p>Lesson: every conservation law has the structure (rate of change inside) = -(net flux out). The divergence theorem is what makes this local-to-global picture work.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Continuity equation expresses conservation of mass.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Fourier's law states heat flux is:", "options": [r"\(k\nabla T\)", r"\(-k \nabla T\)", r"\(k T\)", "0"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Heat equation: \(\rho c \partial_t T = \nabla \cdot (k \nabla\) ___\()\).", "answer": "T"},
         {"type": "true-false", "question": "Conservation laws have a (rate change) + (net flux out) = 0 structure.", "correctAnswer": True},
         {"type": "true-false", "question": "The divergence theorem is the key to local conservation laws.", "correctAnswer": True}]},
    {"title": "Stokes' Theorem",
     "body_html": r"""
<p>For an oriented surface \(S\) with boundary curve \(C\) (oriented compatibly):</p>
<div class="math-block">$$\oint_C \vec{F} \cdot d\vec{r} = \iint_S (\nabla \times \vec{F}) \cdot d\vec{S}$$</div>
<p>Circulation around the boundary = flux of curl through the surface. The 3D analogue of Green's theorem.</p>
<p>Compatibility rule: walk around \(C\) with your head along the surface normal. Then \(S\) is on your left. (Right-hand rule.)</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Stokes': \(\oint \vec{F}\cdot d\vec{r} = \iint (\nabla \times \vec{F}) \cdot d\) ___.", "answer": "S"},
         {"type": "multiple-choice", "question": r"Stokes' equates circulation around the boundary to:", "options": ["divergence integrated over volume", "flux of curl through surface", "average value of F", "trace of A"], "correctIndex": 1},
         {"type": "true-false", "question": "Stokes' is the 3D version of Green's theorem.", "correctAnswer": True},
         {"type": "true-false", "question": "The boundary curve and surface orientation must be compatibly oriented.", "correctAnswer": True},
         {"type": "true-false", "question": "Green's is a special case of Stokes'.", "correctAnswer": True}]},
    {"title": "Stokes': Curl Through a Surface",
     "body_html": r"""
<p>The flux of curl through any surface depends only on the boundary curve. This means: if two surfaces \(S_1, S_2\) share the same boundary \(C\), then</p>
<div class="math-block">$$\iint_{S_1} (\nabla \times \vec{F})\cdot d\vec{S} = \iint_{S_2} (\nabla \times \vec{F})\cdot d\vec{S}$$</div>
<p>This freedom to deform the surface is incredibly powerful. Often you can replace a complicated surface with a simple disk having the same boundary, then compute the flux easily.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Surfaces with the same boundary give the same curl flux.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "This freedom is useful because:", "options": ["it eliminates curl", "you can pick the simplest surface with that boundary", "it forces F = 0", "no reason"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Curl flux depends on the ___ curve only.", "answer": "boundary"},
         {"type": "true-false", "question": "If a boundary is empty (closed surface), curl flux is zero.", "correctAnswer": True},
         {"type": "true-false", "question": r"\(\nabla \cdot (\nabla \times \vec{F}) = 0\) confirms curl flux through closed surfaces is zero.", "correctAnswer": True}]},
    {"title": "Stokes' = Generalized Green's",
     "body_html": r"""
<p>If \(S\) is flat in the \(xy\)-plane, Stokes' reduces to Green's. The "curl" \(\nabla \times \vec{F}\) has only a \(z\)-component there, namely \(\partial Q/\partial x - \partial P/\partial y\), which is the Green's-theorem integrand.</p>
<p>So Green's, Stokes', and the divergence theorem are all special cases of a single statement: integrating an exterior derivative over a region equals integrating the original form over its boundary. That's <strong>Stokes' theorem in differential-form language</strong>:</p>
<div class="math-block">$$\int_M d\omega = \int_{\partial M} \omega$$</div>""",
     "exercises": [
         {"type": "true-false", "question": "Green's is the planar special case of Stokes'.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"In 2D, \(\nabla \times (P, Q, 0)\) has nonzero component:", "options": ["x", "y", "z", "all"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"General Stokes': \(\int_M d\omega = \int\) ___ \(\omega\).", "answer": "_dM"},
         {"type": "true-false", "question": "Divergence theorem is also a special case of general Stokes' theorem.", "correctAnswer": True},
         {"type": "true-false", "question": "Differential forms unify the big theorems.", "correctAnswer": True}]},
    {"title": "Faraday's Law",
     "body_html": r"""
<p>Maxwell's third equation: \(\nabla \times \vec{E} = -\partial \vec{B}/\partial t\). Apply Stokes':</p>
<div class="math-block">$$\oint_C \vec{E} \cdot d\vec{r} = -\frac{d}{dt}\iint_S \vec{B} \cdot d\vec{S}$$</div>
<p>The EMF around a loop equals the negative time-rate-of-change of magnetic flux through the loop. This is <strong>Faraday's Law of Induction</strong> — the basis of generators, transformers, and everything that converts magnetic motion into electric current.</p>
<p>Maxwell's equations express two of the big theorems (divergence and curl) directly.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Faraday: \(\oint \vec{E}\cdot d\vec{r} = -d/dt \iint \vec{B}\cdot d\) ___.", "answer": "S"},
         {"type": "multiple-choice", "question": r"Maxwell's third: \(\nabla \times \vec{E} =\)", "options": ["0", r"\(-\partial \vec{B}/\partial t\)", r"\(\rho/\epsilon_0\)", r"\(\mu_0 \vec{J}\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Faraday's law underlies electric generators.", "correctAnswer": True},
         {"type": "true-false", "question": "Faraday's law is the integral form of Maxwell's third equation.", "correctAnswer": True},
         {"type": "true-false", "question": "Changing magnetic flux induces an EMF.", "correctAnswer": True}]},
    {"title": "The Big Picture: Boundary Integrals",
     "body_html": r"""
<p>Three fundamental theorems of vector calculus, all unified:</p>
<ul>
<li><strong>FTLI:</strong> \(\int_a^b \nabla f \cdot d\vec{r} = f(\vec{b}) - f(\vec{a})\) — boundary is two points.</li>
<li><strong>Green's / Stokes':</strong> \(\int (\text{curl}) = \oint(\text{boundary})\) — boundary is a curve.</li>
<li><strong>Divergence:</strong> \(\int (\text{div}) = \oiint (\text{boundary})\) — boundary is a surface.</li>
</ul>
<p>Each says: <strong>the integral of a derivative over a region equals the original function evaluated on the boundary</strong>. The dimensions move down by one each time. This is what differential forms generalize.</p>""",
     "exercises": [
         {"type": "true-false", "question": "FTLI, Stokes', and divergence theorem are unified statements.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"FTLI's \"boundary\" is:", "options": ["a curve", "a surface", "two endpoints", "empty"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"\"Integral of derivative over region = original on ___.\"", "answer": "boundary"},
         {"type": "true-false", "question": "Each theorem reduces dimension by one.", "correctAnswer": True},
         {"type": "true-false", "question": "Differential forms generalize all three theorems.", "correctAnswer": True}]},
    {"title": "Topological Conditions",
     "body_html": r"""
<p>Some equivalences require topological assumptions:</p>
<ul>
<li><strong>Curl = 0 ⇒ conservative:</strong> requires the domain to be <strong>simply connected</strong> (every loop can be contracted to a point).</li>
<li><strong>Div = 0 ⇒ \(\vec{F} = \nabla \times \vec{A}\):</strong> requires the domain to have trivial topology (e.g., be star-shaped).</li>
</ul>
<p>Counterexample: \(\vec{F} = (-y, x)/(x^2+y^2)\) on the punctured plane. Curl = 0 everywhere, but circulation around the origin is \(2\pi\), not 0. The domain isn't simply connected.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Curl = 0 implies conservative only in simply connected domains.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Punctured plane is:", "options": ["simply connected", "not simply connected", "convex", "compact"], "correctIndex": 1},
         {"type": "fill-blank", "question": "A simply connected region: every loop can be contracted to a ___.", "answer": "point"},
         {"type": "true-false", "question": "Topology matters in vector calculus.", "correctAnswer": True},
         {"type": "true-false", "question": "Star-shaped domains have trivial topology.", "correctAnswer": True}]},
    {"title": "Vector Calculus Identities",
     "body_html": r"""
<p>Useful identities you'll see again and again:</p>
<ul>
<li>\(\nabla \times (\nabla f) = \vec{0}\) — gradient is curl-free.</li>
<li>\(\nabla \cdot (\nabla \times \vec{F}) = 0\) — curl is divergence-free.</li>
<li>\(\nabla \times (\nabla \times \vec{F}) = \nabla(\nabla \cdot \vec{F}) - \nabla^2 \vec{F}\) — useful in deriving wave equations from Maxwell.</li>
<li>\(\nabla(fg) = f\nabla g + g\nabla f\) — product rule for gradient.</li>
<li>\(\nabla \cdot (f\vec{F}) = (\nabla f) \cdot \vec{F} + f \nabla \cdot \vec{F}\) — product rule for divergence.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\nabla \times (\nabla f) = 0\).", "correctAnswer": True},
         {"type": "true-false", "question": r"\(\nabla \cdot (\nabla \times \vec{F}) = 0\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(\nabla \times (\nabla \times \vec{F}) =\)", "options": [r"\(\nabla(\nabla\cdot\vec{F}) - \nabla^2 \vec{F}\)", r"\(\nabla^2 \vec{F}\)", r"\(\vec{F}\)", "0"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"\(\nabla(fg) = f \nabla g + g \nabla\) ___.", "answer": "f"},
         {"type": "true-false", "question": "These identities are used in deriving the wave equation from Maxwell.", "correctAnswer": True}]},
    {"title": "Practice: The Big Theorems",
     "body_html": r"""
<p>Quick practice:</p>
<ol>
<li>Use Green's to compute area of an ellipse \(x^2/a^2 + y^2/b^2 = 1\): \(\pi a b\).</li>
<li>Flux of \(\vec{F} = (x,y,z)\) through unit sphere by divergence theorem: \(\nabla \cdot \vec{F} = 3\), volume \(\tfrac{4}{3}\pi\), flux \(4\pi\).</li>
<li>Stokes' for \(\vec{F} = (-y, x, 0)\), \(C\) = unit circle in xy-plane: curl \(= (0,0,2)\), flux through unit disk \(= 2\pi\). Equals direct line integral.</li>
<li>\(\oint xy^2\,dx + (x^2 y + 2x)\,dy\) around unit circle: by Green's \(= \iint_R 2 \,dA = 2\pi\).</li>
</ol>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Area of ellipse \(x^2/a^2 + y^2/b^2 = 1\) is \(\pi a\) ___.", "answer": "b"},
         {"type": "multiple-choice", "question": r"\(\nabla \times (-y, x, 0) =\)", "options": [r"\((0,0,2)\)", r"\((0,0,1)\)", r"\((1,0,0)\)", r"\((0,0,0)\)"], "correctIndex": 0},
         {"type": "true-false", "question": r"Flux of curl of \((-y,x,0)\) through unit disk is \(2\pi\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Volume of unit ball: \(\tfrac{4}{3}\) ___.", "answer": "pi"},
         {"type": "true-false", "question": "Divergence theorem turns flux problems into volume integrals.", "correctAnswer": True}]},
    {"title": "Big Theorems Checkpoint",
     "body_html": r"""
<p>Recap of Unit 33:</p>
<ul>
<li>Green's theorem: 2D boundary integral = double integral of 2D curl.</li>
<li>Divergence theorem: surface flux out = volume integral of divergence.</li>
<li>Stokes' theorem: boundary circulation = surface flux of curl.</li>
<li>All three are special cases of generalized Stokes': \(\int_M d\omega = \int_{\partial M}\omega\).</li>
<li>Topological hypotheses (simply connected) matter.</li>
<li>Curl-free + simply-connected ⇒ conservative; div-free + star-shaped ⇒ has a vector potential.</li>
<li>Vector calculus identities provide endless algebraic tricks.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\nabla \cdot (\nabla \times \vec{F}) = 0\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Stokes' theorem is for:", "options": ["closed curves bounded by surfaces", "scalar functions", "only 2D", "matrices"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"Divergence theorem: net flux out = integral of ___ over volume.", "answer": "div"},
         {"type": "true-false", "question": "Maxwell's equations contain divergence and curl theorems directly.", "correctAnswer": True},
         {"type": "true-false", "question": "Green's theorem is a special case of Stokes' theorem.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"All three theorems unify under \(\int_M\) ___ \(= \int_{\partial M} \omega\).", "answer": "dω"},
         {"type": "true-false", "question": "Topological conditions can change the validity of these theorems.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(33, "Green's, Stokes' & Divergence Theorems", 481, LESSONS)
