#!/usr/bin/env python3
"""Unit 31 — Line Integrals (lessons 451-465)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "What Is a Line Integral?",
     "body_html": r"""
<p>A <strong>line integral</strong> integrates a function along a curve, rather than over an interval. Two flavors:</p>
<ul>
<li><strong>Scalar line integral:</strong> \(\int_C f\,ds\) — integrate a scalar function \(f\) along curve \(C\) with respect to arc length.</li>
<li><strong>Vector line integral:</strong> \(\int_C \vec{F} \cdot d\vec{r}\) — integrate a vector field along the curve, picking up only the component tangent to the path.</li>
</ul>
<p>Both build the integral by chopping the curve into tiny pieces, evaluating the integrand on each piece, and summing.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Line integrals integrate along a curve, not an interval.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(\int_C f\,ds\) is a:", "options": ["scalar line integral", "vector line integral", "surface integral", "double integral"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"In a vector line integral, you take the dot product with \(d\) ___.", "answer": "r"},
         {"type": "true-false", "question": "Scalar line integrals don't depend on direction along the curve.", "correctAnswer": True},
         {"type": "true-false", "question": "Vector line integrals do depend on direction.", "correctAnswer": True}]},
    {"title": "Parametrizing a Curve",
     "body_html": r"""
<p>A curve \(C\) is described by a parametrization \(\vec{r}(t)\) for \(t \in [a, b]\). Common parametrizations:</p>
<ul>
<li>Line segment from \(\vec{p}\) to \(\vec{q}\): \(\vec{r}(t) = (1-t)\vec{p} + t\vec{q}\), \(t \in [0,1]\).</li>
<li>Circle of radius \(R\): \(\vec{r}(t) = (R\cos t, R\sin t)\), \(t \in [0, 2\pi]\).</li>
<li>Helix: \(\vec{r}(t) = (\cos t, \sin t, t)\).</li>
</ul>
<p>The velocity \(\vec{r}'(t)\) is tangent to the curve. Its magnitude \(|\vec{r}'(t)|\) is the speed; it determines arc length: \(ds = |\vec{r}'(t)|\,dt\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(ds = |\vec{r}'(t)|\) ___.", "answer": "dt"},
         {"type": "multiple-choice", "question": r"Parametrize a circle of radius 2:", "options": [r"\((2t, 2t)\)", r"\((2\cos t, 2\sin t)\)", r"\((t, t^2)\)", r"\((\cos 2t, \sin 2t)\)"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(\vec{r}'(t)\) is tangent to the curve.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Line from \(\vec{p}\) to \(\vec{q}\): \(\vec{r}(t) = (1-t)\vec{p} + t\) ___.", "answer": "q"},
         {"type": "true-false", "question": "Different parametrizations can describe the same curve.", "correctAnswer": True}]},
    {"title": "Scalar Line Integral",
     "body_html": r"""
<p>For a curve \(C\) parametrized by \(\vec{r}(t)\), \(t \in [a,b]\):</p>
<div class="math-block">$$\int_C f\,ds = \int_a^b f(\vec{r}(t)) \,|\vec{r}'(t)|\,dt$$</div>
<p>Geometrically: imagine a fence with height \(f(\vec{r}(t))\) standing along the curve. \(\int_C f\,ds\) is the area of the fence.</p>
<p>Special case: \(f \equiv 1\) gives the <strong>arc length</strong> of \(C\).</p>
<p><strong>Example.</strong> Line segment from origin to \((1,1)\), \(f(x,y) = x+y\). Parametrize \(\vec{r}(t)=(t,t)\), \(t \in [0,1]\). Then \(|\vec{r}'(t)| = \sqrt{2}\), \(f(\vec{r}(t)) = 2t\). Integral: \(\int_0^1 2t \sqrt 2\,dt = \sqrt{2}\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\int_C 1\,ds\) is the ___ of \(C\).", "answer": "arc length"},
         {"type": "multiple-choice", "question": r"For \(\vec{r}(t)=(t,t)\), \(|\vec{r}'(t)| =\)", "options": ["1", r"\(\sqrt{2}\)", "2", r"\(t\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Scalar line integrals depend on direction of traversal.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"\(\int_C f\,ds = \int_a^b f(\vec{r}(t))\) ___ \(\,dt\).", "answer": "|r'(t)|"},
         {"type": "true-false", "question": "If f ≡ 1, the line integral gives arc length.", "correctAnswer": True}]},
    {"title": "Arc Length via Line Integrals",
     "body_html": r"""
<p>The arc length of \(C\) parametrized by \(\vec{r}(t)\) on \([a,b]\) is</p>
<div class="math-block">$$L = \int_a^b |\vec{r}'(t)|\,dt = \int_C ds$$</div>
<p><strong>Examples.</strong></p>
<ul>
<li>Circle of radius \(R\): \(L = \int_0^{2\pi} R\,dt = 2\pi R\).</li>
<li>Line segment from origin to \((3,4)\): parametrize \(\vec{r}(t) = (3t,4t)\), \(t \in [0,1]\). Then \(L = \int_0^1 5\,dt = 5\).</li>
<li>Helix \(\vec{r}(t) = (\cos t, \sin t, t)\) for \(t \in [0, 2\pi]\): speed \(\sqrt 2\), so \(L = 2\pi \sqrt 2\).</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Circumference of a circle of radius \(R\) is \(2\pi\) ___.", "answer": "R"},
         {"type": "multiple-choice", "question": r"Length of helix \((\cos t, \sin t, t)\) over \([0, 2\pi]\):", "options": [r"\(2\pi\)", r"\(2\pi \sqrt 2\)", r"\(\sqrt 2\)", r"\(\pi^2\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Arc length is independent of parametrization.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"For \(\vec{r}(t)=(3t,4t)\), speed is ___.", "answer": "5"},
         {"type": "true-false", "question": r"\(L = \int_a^b |\vec{r}'(t)|\,dt\).", "correctAnswer": True}]},
    {"title": "Line Integral of a Vector Field",
     "body_html": r"""
<p>For a vector field \(\vec{F}\) and curve \(C\):</p>
<div class="math-block">$$\int_C \vec{F} \cdot d\vec{r} = \int_a^b \vec{F}(\vec{r}(t)) \cdot \vec{r}'(t)\,dt$$</div>
<p>This integrates the <strong>tangential component</strong> of \(\vec{F}\) along the curve. Components of \(\vec{F}\) perpendicular to the path don't contribute.</p>
<p><strong>Example.</strong> \(\vec{F} = (y, -x)\), \(C\) the unit circle counter-clockwise. Parametrize \(\vec{r}(t) = (\cos t, \sin t)\). \(\vec{r}'(t) = (-\sin t, \cos t)\). \(\vec{F}(\vec{r}(t)) = (\sin t, -\cos t)\). Dot product: \(-\sin^2 t - \cos^2 t = -1\). Integral: \(-2\pi\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\int_C \vec{F} \cdot d\vec{r} = \int_a^b \vec{F}(\vec{r}(t)) \cdot\) ___ \(\,dt\).", "answer": "r'(t)"},
         {"type": "multiple-choice", "question": "Vector line integrals capture which component of F?", "options": ["normal", "tangential", "vertical", "all components"], "correctIndex": 1},
         {"type": "true-false", "question": "Reversing direction of C flips the sign of the vector line integral.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"For \(\vec{F} = (y,-x)\) around the unit circle CCW: integral is \(-\) ___.", "answer": "2pi"},
         {"type": "true-false", "question": "Components of F perpendicular to the curve contribute to the line integral.", "correctAnswer": False}]},
    {"title": "Work as a Line Integral",
     "body_html": r"""
<p>The most common physical interpretation: if \(\vec{F}\) is a force field and a particle moves along \(C\), the <strong>work</strong> done by \(\vec{F}\) is</p>
<div class="math-block">$$W = \int_C \vec{F} \cdot d\vec{r}$$</div>
<p>Only the tangential component of force does work; perpendicular components don't.</p>
<p><strong>Example.</strong> Push a block with constant force \((F, 0)\) along the x-axis from \(0\) to \(d\). Work \(= F \cdot d\) — recovering high-school physics. The line-integral form generalizes to any path and any varying force.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Work equals the line integral of force along the path.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Work for constant force F over distance d (parallel):", "options": [r"\(F \cdot d\)", r"\(F + d\)", r"\(F/d\)", "0"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"Force perpendicular to motion does ___ work.", "answer": "no"},
         {"type": "true-false", "question": "A circular orbit under central gravity does net zero work.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Work units (SI) are ___.", "answer": "joules"}]},
    {"title": "Independence of Parametrization",
     "body_html": r"""
<p>Both the scalar and vector line integrals are <strong>independent of the parametrization</strong> — only the curve and (for vector integrals) the orientation matter.</p>
<p>Reparametrizing a curve doesn't change \(\int_C f\,ds\) at all. Reversing direction doesn't change a scalar line integral, but flips the sign of a vector line integral.</p>
<p>Why? In the change of variables, \(|\vec{r}'(t)|\,dt\) and \(\vec{r}'(t)\,dt\) transform exactly as \(ds\) and \(d\vec{r}\) should. The geometry, not the parametrization, controls the answer.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Reparametrizing a curve never changes the scalar line integral.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Reversing direction of C does what to the vector line integral?", "options": ["nothing", "flips the sign", "doubles it", "zeroes it"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(\int_C f\,ds\) depends on direction of traversal.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"What changes a vector line integral on reversing direction: the ___.", "answer": "sign"},
         {"type": "true-false", "question": "Geometry determines the line integral, not the parametrization.", "correctAnswer": True}]},
    {"title": "Path Dependence",
     "body_html": r"""
<p>Generally, \(\int_C \vec{F} \cdot d\vec{r}\) depends on the path \(C\), not just its endpoints. Try the same integral on two different curves between the same start and end — you typically get different answers.</p>
<p><strong>Example.</strong> \(\vec{F} = (y, 0)\) from origin to \((1,1)\). Path 1 (along x then up): integral is 0 (no \(y\) on the x-axis, then \(F_x = 1\) but \(dx = 0\)). Path 2 (diagonal): integral is \(\int_0^1 t\,dt = \tfrac{1}{2}\). Different paths, different answers.</p>
<p>When \(\int_C \vec{F}\cdot d\vec{r}\) is path-independent, the field \(\vec{F}\) is special — it's <strong>conservative</strong>.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Vector line integrals generally depend on the path, not just endpoints.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Path-independent fields are called ___.", "answer": "conservative"},
         {"type": "multiple-choice", "question": r"\(\vec{F} = (y, 0)\) line integral on diagonal from origin to (1,1) is:", "options": ["0", "1/2", "1", "2"], "correctIndex": 1},
         {"type": "true-false", "question": "All line integrals are path-independent.", "correctAnswer": False},
         {"type": "true-false", "question": "Different paths between the same endpoints can give the same integral if F is conservative.", "correctAnswer": True}]},
    {"title": "Conservative Vector Fields",
     "body_html": r"""
<p>A vector field \(\vec{F}\) is <strong>conservative</strong> if there exists a scalar function \(\varphi\) (a "potential") with \(\vec{F} = \nabla \varphi\).</p>
<p>Equivalent characterizations (in a simply connected region):</p>
<ul>
<li>Line integrals depend only on endpoints (path-independent).</li>
<li>The integral around any closed curve is zero.</li>
<li>The curl is zero: \(\nabla \times \vec{F} = \vec{0}\).</li>
</ul>
<p><strong>Examples.</strong> Gravity, electrostatic force, ideal-spring force — all conservative. Friction, magnetic force on a moving charge — not conservative.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Conservative \(\vec{F}\) means \(\vec{F} = \nabla\) ___.", "answer": "phi"},
         {"type": "multiple-choice", "question": "In a simply connected region, conservative is equivalent to:", "options": [r"\(\nabla \cdot \vec{F} = 0\)", r"\(\nabla \times \vec{F} = 0\)", r"\(\vec{F} = 0\)", "F is constant"], "correctIndex": 1},
         {"type": "true-false", "question": "Gravity is conservative.", "correctAnswer": True},
         {"type": "true-false", "question": "Friction is conservative.", "correctAnswer": False},
         {"type": "true-false", "question": "Around any closed curve, conservative line integrals equal zero.", "correctAnswer": True}]},
    {"title": "Potential Functions",
     "body_html": r"""
<p>A <strong>potential</strong> for a conservative field \(\vec{F} = \nabla \varphi\). Once you find one, line integrals collapse:</p>
<div class="math-block">$$\int_C \vec{F} \cdot d\vec{r} = \varphi(\text{end}) - \varphi(\text{start})$$</div>
<p><strong>Finding potentials.</strong> Given \(\vec{F} = (P, Q, R)\), require \(\partial \varphi/\partial x = P\), \(\partial \varphi/\partial y = Q\), \(\partial \varphi/\partial z = R\). Integrate one and check consistency with the others.</p>
<p><strong>Example.</strong> \(\vec{F} = (2x, 2y)\). \(\varphi = x^2 + y^2\) works: \(\partial \varphi/\partial x = 2x\), \(\partial \varphi/\partial y = 2y\). ✓</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"For conservative fields, \(\int_C \vec{F}\cdot d\vec{r} = \varphi(\text{end}) - \varphi(\) ___\()\).", "answer": "start"},
         {"type": "multiple-choice", "question": r"A potential for \((2x, 2y)\):", "options": [r"\(x + y\)", r"\(x^2 + y^2\)", r"\(xy\)", r"\(x^2 - y^2\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Potentials are unique up to a constant.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\partial \varphi / \partial x =\) ___ component of F.", "answer": "x"},
         {"type": "true-false", "question": "Potentials make line integrals trivial: just evaluate at endpoints.", "correctAnswer": True}]},
    {"title": "Fundamental Theorem of Line Integrals",
     "body_html": r"""
<p>If \(\vec{F} = \nabla \varphi\) and \(C\) is any (piecewise smooth) curve from \(\vec{a}\) to \(\vec{b}\):</p>
<div class="math-block">$$\int_C \nabla\varphi \cdot d\vec{r} = \varphi(\vec{b}) - \varphi(\vec{a})$$</div>
<p>This is the line-integral version of the fundamental theorem of calculus. Path doesn't matter — only endpoints. Closed loops give zero.</p>
<p><strong>Physical meaning.</strong> For a conservative force \(\vec{F} = -\nabla U\), work done equals \(-\Delta U\) — the drop in potential energy. This is why energy conservation works.</p>""",
     "exercises": [
         {"type": "true-false", "question": "FTLI: line integrals of gradients depend only on endpoints.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"For \(\vec{F} = \nabla\varphi\), the line integral around any closed curve is:", "options": [r"\(2\pi\)", "0", r"\(\varphi\)", "infinite"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"For conservative force \(\vec{F} = -\nabla U\), \(W = -\Delta\) ___.", "answer": "U"},
         {"type": "true-false", "question": "FTLI generalizes the FTC of single-variable calculus.", "correctAnswer": True},
         {"type": "true-false", "question": "FTLI requires F to be conservative.", "correctAnswer": True}]},
    {"title": "Closed Curves & Circulation",
     "body_html": r"""
<p>The line integral around a closed curve is called the <strong>circulation</strong>:</p>
<div class="math-block">$$\oint_C \vec{F} \cdot d\vec{r}$$</div>
<p>Conservative fields have zero circulation around every loop. Non-conservative fields can have nonzero circulation — they're "curling" somewhere inside.</p>
<p><strong>Example.</strong> \(\vec{F} = (-y, x)\) (rotation field). Circulation around the unit circle CCW: \(\oint = 2\pi\). This field circulates everywhere — not conservative.</p>
<p>Circulation is intimately tied to the curl, leading to <strong>Stokes' theorem</strong> in Unit 33.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Circulation of a conservative field around any loop is zero.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Closed line integrals are written with \(\oint\); they're called ___.", "answer": "circulation"},
         {"type": "multiple-choice", "question": r"Circulation of \((-y, x)\) around the unit circle CCW:", "options": ["0", r"\(\pi\)", r"\(2\pi\)", r"\(-2\pi\)"], "correctIndex": 2},
         {"type": "true-false", "question": "Nonzero circulation indicates a non-conservative field.", "correctAnswer": True},
         {"type": "true-false", "question": "Circulation connects to curl via Stokes' theorem.", "correctAnswer": True}]},
    {"title": "Green's Theorem (Sneak Peek)",
     "body_html": r"""
<p><strong>Green's Theorem</strong> connects a line integral around a closed plane curve to a double integral over the enclosed region:</p>
<div class="math-block">$$\oint_C P\,dx + Q\,dy = \iint_R \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\,dA$$</div>
<p>The integrand on the right is the 2D curl of \(\vec{F} = (P, Q)\). So circulation around the boundary equals the total curl inside.</p>
<p>Special case: \(P = 0\), \(Q = x\) gives \(\oint x\,dy = \iint dA = \text{area}(R)\). You can compute area via a line integral! Engineers use this for planimeters.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Green's theorem connects line and double integrals.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The integrand on the right of Green's theorem is the 2D:", "options": ["divergence", "curl", "gradient", "Laplacian"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\oint x\,dy = \) area of ___.", "answer": "R"},
         {"type": "true-false", "question": "Green's theorem can compute area from a boundary line integral.", "correctAnswer": True},
         {"type": "true-false", "question": "Green's theorem requires the curve to be closed.", "correctAnswer": True}]},
    {"title": "Practice: Line Integrals",
     "body_html": r"""
<p>Quick problems:</p>
<ol>
<li>Length of straight segment from \((0,0)\) to \((3,4)\): \(5\).</li>
<li>\(\int_C (x+y)\,ds\) on segment from origin to \((1,1)\): the integrand at parameter \(t\) is \(2t\), \(ds = \sqrt 2\,dt\). \(\int_0^1 2\sqrt 2\,t\,dt = \sqrt 2\).</li>
<li>\(\oint_C (-y, x)\,d\vec{r}\) around the unit circle CCW: \(2\pi\).</li>
<li>\(\vec{F} = (2x, 2y)\) is conservative with potential \(\varphi = x^2+y^2\). Integral from \((1,0)\) to \((0,1)\) on any path: \(\varphi(0,1) - \varphi(1,0) = 1 - 1 = 0\).</li>
</ol>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Length from origin to \((3,4)\): ___.", "answer": "5"},
         {"type": "multiple-choice", "question": r"\(\oint (-y,x)\,d\vec{r}\) around unit circle CCW:", "options": [r"\(\pi\)", r"\(2\pi\)", "0", r"\(4\pi\)"], "correctIndex": 1},
         {"type": "true-false", "question": "A conservative-field integral between fixed endpoints is path-independent.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Potential for \((2x, 2y)\): \(x^2 + y^?\). Fill: ___.", "answer": "2"},
         {"type": "true-false", "question": "Integral of a conservative field from origin to itself is zero.", "correctAnswer": True}]},
    {"title": "Line Integrals Checkpoint",
     "body_html": r"""
<p>Recap of Unit 31:</p>
<ul>
<li>Scalar line integrals: \(\int_C f\,ds\) — fence area; arc length when \(f = 1\).</li>
<li>Vector line integrals: \(\int_C \vec{F}\cdot d\vec{r}\) — work; tangential component only.</li>
<li>Both are independent of parametrization (orientation-sensitive for vectors).</li>
<li>Conservative \(\iff\) \(\vec{F} = \nabla\varphi\) \(\iff\) closed loops give 0 \(\iff\) curl = 0 (in simply connected regions).</li>
<li>FTLI: \(\int_C \nabla\varphi \cdot d\vec{r} = \varphi(\text{end}) - \varphi(\text{start})\).</li>
<li>Circulation \(\oint\) measures the "twisting" of the field.</li>
<li>Green's theorem connects circulation to curl over the enclosed region.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Vector line integrals depend on direction of traversal.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(\int_C 1\,ds\) gives:", "options": ["work", "arc length", "area", "circulation"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"For conservative \(\vec{F} = \nabla\varphi\): \(\oint \vec{F}\cdot d\vec{r} =\) ___.", "answer": "0"},
         {"type": "true-false", "question": "Path-independence is equivalent to conservativeness (in simply connected regions).", "correctAnswer": True},
         {"type": "true-false", "question": "Green's theorem applies to non-closed curves.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"Circulation is the line integral around a ___ curve.", "answer": "closed"},
         {"type": "true-false", "question": "Friction is a conservative force.", "correctAnswer": False}]},
]

if __name__ == "__main__":
    render_unit(31, "Line Integrals", 451, LESSONS)
