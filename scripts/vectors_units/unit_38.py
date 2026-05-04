#!/usr/bin/env python3
"""Unit 38 — Differential Forms Preview (lessons 556-570)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "What Are Differential Forms?",
     "body_html": r"""
<p><strong>Differential forms</strong> are antisymmetric multilinear gadgets that generalize line, surface, and volume integrands. They unify gradient, curl, and divergence into a single operation called the exterior derivative.</p>
<p>The big payoff: a single theorem (Stokes' theorem in form language) recovers FTLI, Green's, Stokes', and the divergence theorem. The notation also reveals which formulas generalize to higher dimensions and which don't.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Differential forms unify grad, curl, div.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Forms are:", "options": ["scalars only", "antisymmetric multilinear maps", "matrices", "vectors"], "correctIndex": 1},
         {"type": "fill-blank", "question": "A single Stokes' theorem in forms recovers FTLI, Green's, ___, and divergence.", "answer": "Stokes"},
         {"type": "true-false", "question": "Forms generalize naturally to higher dimensions.", "correctAnswer": True},
         {"type": "true-false", "question": "Forms are commutative under multiplication.", "correctAnswer": False}]},
    {"title": "0-forms, 1-forms, 2-forms",
     "body_html": r"""
<p>Forms are classified by degree:</p>
<ul>
<li><strong>0-form:</strong> a function \(f(x,y,z)\). Integrate over a 0-dim region (point) to get \(f\) at that point.</li>
<li><strong>1-form:</strong> looks like \(P\,dx + Q\,dy + R\,dz\). Integrate over a curve.</li>
<li><strong>2-form:</strong> like \(P\,dy\wedge dz + Q\,dz\wedge dx + R\,dx\wedge dy\). Integrate over a surface.</li>
<li><strong>3-form:</strong> like \(f\,dx\wedge dy\wedge dz\). Integrate over a volume.</li>
</ul>
<p>The "differential" symbols \(dx, dy, dz\) (and their wedges) are the building blocks.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "What's a 0-form?", "options": ["a function", "a vector field", "a surface", "an integral"], "correctIndex": 0},
         {"type": "fill-blank", "question": "1-forms are integrated over ___.", "answer": "curves"},
         {"type": "true-false", "question": "2-forms are integrated over surfaces.", "correctAnswer": True},
         {"type": "true-false", "question": r"\(f\,dx\,dy\,dz\) (without wedges) is the standard form notation.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"3-forms in 3D look like \(f\,dx\wedge dy\wedge\) ___.", "answer": "dz"}]},
    {"title": "Basis 1-forms",
     "body_html": r"""
<p>The 1-forms \(dx, dy, dz\) are the basis 1-forms in \(\mathbb{R}^3\). They're the natural duals of the basis vectors \(\partial_x, \partial_y, \partial_z\):</p>
<div class="math-block">$$dx(\partial_x) = 1, \quad dx(\partial_y) = 0, \quad \ldots$$</div>
<p>Every 1-form is a linear combination \(P\,dx + Q\,dy + R\,dz\) (with coefficient functions \(P, Q, R\)).</p>
<p>Vector fields and 1-forms are dual: a vector field \(\vec{F} = (P,Q,R)\) corresponds to the 1-form \(\omega = P\,dx + Q\,dy + R\,dz\) (in Euclidean space, with the standard metric).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Vector fields and 1-forms are dual.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(dx(\partial_x) =\)", "options": ["0", "1", r"\(\partial_x\)", r"\(dx\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"In 3D, basis 1-forms are \(dx, dy,\) ___.", "answer": "dz"},
         {"type": "true-false", "question": r"Every 1-form is a linear combination \(P\,dx + Q\,dy + R\,dz\).", "correctAnswer": True},
         {"type": "true-false", "question": r"\(dx(\partial_y) = 1\).", "correctAnswer": False}]},
    {"title": "The Wedge Product",
     "body_html": r"""
<p>The <strong>wedge product</strong> \(\wedge\) builds higher-degree forms from lower-degree ones:</p>
<ul>
<li>\(dx \wedge dy\) is a 2-form representing the oriented area element in the \(xy\)-plane.</li>
<li>\(dx \wedge dy \wedge dz\) is the oriented volume element.</li>
</ul>
<p>It's bilinear and <strong>antisymmetric</strong> on 1-forms: \(dx \wedge dy = -dy \wedge dx\) and \(dx \wedge dx = 0\). For higher-degree forms, swapping any two arguments multiplies by \((-1)^{kl}\) for forms of degrees \(k, l\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(dx \wedge dy = -dy \wedge\) ___.", "answer": "dx"},
         {"type": "multiple-choice", "question": r"\(dx \wedge dx =\)", "options": [r"\(dx\)", "0", r"\(dx^2\)", "undefined"], "correctIndex": 1},
         {"type": "true-false", "question": "Wedge product is associative.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(dx \wedge dy \wedge dz\) is the oriented ___ element.", "answer": "volume"},
         {"type": "true-false", "question": "Wedge of two 1-forms is symmetric.", "correctAnswer": False}]},
    {"title": "Antisymmetry of Wedge",
     "body_html": r"""
<p>For 1-forms \(\alpha, \beta\): \(\alpha \wedge \beta = -\beta \wedge \alpha\). For a 1-form and 2-form: \(\alpha \wedge \omega = (-1)^{1 \cdot 2}\omega \wedge \alpha = \omega \wedge \alpha\). For two 2-forms: same — they commute.</p>
<p>General rule: \(\alpha \wedge \beta = (-1)^{kl} \beta \wedge \alpha\), where \(k, l\) are the degrees.</p>
<p>This pattern explains why a 2-form on \(\mathbb{R}^2\) has only one independent component (\(dx \wedge dy\)) and a 3-form on \(\mathbb{R}^3\) has only one (\(dx \wedge dy \wedge dz\)). The dimension of the space of \(k\)-forms on \(\mathbb{R}^n\) is \(\binom{n}{k}\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"For 1-forms: \(\alpha \wedge \beta = -\beta \wedge\) ___.", "answer": "alpha"},
         {"type": "multiple-choice", "question": r"Dim of \(k\)-forms on \(\mathbb{R}^n\):", "options": [r"\(n\)", r"\(k\)", r"\(\binom{n}{k}\)", r"\(n^k\)"], "correctIndex": 2},
         {"type": "true-false", "question": "Two 2-forms commute under wedge.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Dim of 2-forms on \(\mathbb{R}^3\): ___.", "answer": "3"},
         {"type": "true-false", "question": r"\(dx \wedge dy \wedge dz \wedge dx = 0\).", "correctAnswer": True}]},
    {"title": "Volume Forms",
     "body_html": r"""
<p>A <strong>volume form</strong> on an \(n\)-dim oriented manifold is a top-degree form (degree \(n\)) that's nowhere zero. On Euclidean \(\mathbb{R}^n\), the standard volume form is \(dx_1 \wedge dx_2 \wedge \cdots \wedge dx_n\).</p>
<p>Integrating the volume form over a region gives that region's volume. For a generic top-form \(f \cdot dx \wedge dy \wedge dz\) on \(\mathbb{R}^3\), \(\int_V f\,dx\wedge dy\wedge dz = \iiint_V f\,dV\) — same as the usual triple integral.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Volume form is the top-degree form on a manifold.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Standard volume form on \(\mathbb{R}^3\):", "options": [r"\(dx + dy + dz\)", r"\(dx \wedge dy \wedge dz\)", r"\(dx \cdot dy \cdot dz\)", "0"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Top-degree form on n-manifold has degree ___.", "answer": "n"},
         {"type": "true-false", "question": "Volume form is nowhere zero on an oriented manifold.", "correctAnswer": True},
         {"type": "true-false", "question": "Integrating volume form gives volume.", "correctAnswer": True}]},
    {"title": "The Exterior Derivative",
     "body_html": r"""
<p>The <strong>exterior derivative</strong> \(d\) maps \(k\)-forms to \((k+1)\)-forms. It generalizes gradient, curl, and divergence:</p>
<ul>
<li>On 0-forms (functions): \(df = \partial_i f\,dx^i\) — the gradient as a 1-form.</li>
<li>On 1-forms in 3D: \(d(P\,dx + Q\,dy + R\,dz) = (\nabla \times \vec{F}) \cdot d\vec{S}\) — the curl wrapped as a 2-form.</li>
<li>On 2-forms in 3D: \(d\) gives the divergence as a 3-form.</li>
</ul>
<p>One operator, three classical operators in disguise.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Exterior derivative d generalizes grad, curl, div.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(d\) of a 1-form is a:", "options": ["0-form", "1-form", "2-form", "3-form"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"\(df = \partial_i f \,dx^?\). Fill: ___.", "answer": "i"},
         {"type": "true-false", "question": r"\(d\) raises the degree of a form by 1.", "correctAnswer": True},
         {"type": "true-false", "question": "On 0-forms, d gives the gradient as a 1-form.", "correctAnswer": True}]},
    {"title": "d² = 0",
     "body_html": r"""
<p>Applying \(d\) twice always gives zero:</p>
<div class="math-block">$$d(d\omega) = 0$$</div>
<p>This is the unified version of the classical identities</p>
<ul>
<li>\(\nabla \times (\nabla f) = \vec{0}\) (curl of grad is zero), and</li>
<li>\(\nabla \cdot (\nabla \times \vec{F}) = 0\) (div of curl is zero).</li>
</ul>
<p>So both classical identities are special cases of one beautiful fact: the exterior derivative squares to zero. This is the foundation of <em>de Rham cohomology</em>.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(d \circ d = 0\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Classical identity contained in \(d^2 = 0\):", "options": [r"\(\nabla \cdot \nabla = 0\)", r"\(\nabla \times \nabla f = 0\)", r"\(\nabla^2 = 0\)", "none"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\nabla \cdot (\nabla \times \vec{F}) =\) ___.", "answer": "0"},
         {"type": "true-false", "question": r"\(d^2 = 0\) is the foundation of de Rham cohomology.", "correctAnswer": True},
         {"type": "true-false", "question": r"\(d^2 = 0\) is independent of the dimension.", "correctAnswer": True}]},
    {"title": "Closed and Exact Forms",
     "body_html": r"""
<p>A form \(\omega\) is <strong>closed</strong> if \(d\omega = 0\). It's <strong>exact</strong> if \(\omega = d\eta\) for some \(\eta\) (one degree lower).</p>
<p>Since \(d^2 = 0\), every exact form is closed. The converse — "every closed form is exact" — depends on the topology of the underlying manifold (Poincaré lemma: locally yes; globally only if the manifold is "nice").</p>
<p>Closed-but-not-exact forms detect topological features: holes, handles, cycles. <strong>de Rham cohomology</strong> measures exactly this gap.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Exact \(\implies\) ___.", "answer": "closed"},
         {"type": "multiple-choice", "question": r"\(\omega\) closed means:", "options": [r"\(\omega = d\eta\)", r"\(d\omega = 0\)", r"\(\omega = 0\)", r"\(\int \omega = 0\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Every closed form is globally exact.", "correctAnswer": False},
         {"type": "true-false", "question": "Poincaré lemma: locally, closed = exact.", "correctAnswer": True},
         {"type": "fill-blank", "question": "The gap between closed and exact is measured by ___ cohomology.", "answer": "de Rham"}]},
    {"title": "Integration of Forms",
     "body_html": r"""
<p>You integrate a \(k\)-form over a (compatibly oriented) \(k\)-dim region:</p>
<ul>
<li>0-form integrated over a point = the function value.</li>
<li>1-form integrated over a curve = line integral.</li>
<li>2-form over a surface = surface integral.</li>
<li>3-form over a volume = triple integral.</li>
</ul>
<p>Forms naturally encode "what to integrate" — they include orientation and the change-of-variables Jacobian automatically. Pulling back a form via a parametrization is exactly how the Jacobian appears.</p>""",
     "exercises": [
         {"type": "true-false", "question": "k-forms are integrated over k-dim regions.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "A 2-form is integrated over:", "options": ["a curve", "a surface", "a volume", "a point"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Forms automatically encode orientation and the ___ for change of variables.", "answer": "Jacobian"},
         {"type": "true-false", "question": "0-forms integrated over a point yield the function value.", "correctAnswer": True},
         {"type": "true-false", "question": "Forms can be integrated over arbitrary-dim regions.", "correctAnswer": False}]},
    {"title": "Stokes' Theorem in Forms",
     "body_html": r"""
<p>The general Stokes' theorem:</p>
<div class="math-block">$$\int_M d\omega = \int_{\partial M} \omega$$</div>
<p>Read it: "the integral of \(d\omega\) over a region \(M\) equals the integral of \(\omega\) over the boundary \(\partial M\)."</p>
<p><strong>Special cases:</strong></p>
<ul>
<li>FTLI (forms degree 0 → 1, region a curve).</li>
<li>Green's & classical Stokes' (forms degree 1 → 2, region a surface).</li>
<li>Divergence theorem (forms degree 2 → 3, region a volume).</li>
</ul>
<p>One theorem, all the usual ones as corollaries.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\int_M d\omega = \int_{\) ___ \(} \omega\).", "answer": "_dM"},
         {"type": "multiple-choice", "question": "Forms version of FTLI is:", "options": [r"\(\int d f = f|_{\partial}\)", "Green's theorem", "the metric tensor", "Cauchy"], "correctIndex": 0},
         {"type": "true-false", "question": "Generalized Stokes contains the divergence theorem as a special case.", "correctAnswer": True},
         {"type": "true-false", "question": "Generalized Stokes works in any dimension.", "correctAnswer": True},
         {"type": "true-false", "question": "FTLI is a special case of generalized Stokes.", "correctAnswer": True}]},
    {"title": "Maxwell in Forms (F = dA)",
     "body_html": r"""
<p>Electromagnetism in 4D spacetime is gorgeous in form language. Define the 4-potential 1-form \(A = -\varphi\,dt + A_x\,dx + A_y\,dy + A_z\,dz\).</p>
<p>The electromagnetic field is the 2-form \(F = dA\). Maxwell's homogeneous equations (Faraday + no magnetic monopoles) become</p>
<div class="math-block">$$dF = 0$$</div>
<p>(automatic from \(d^2 = 0\)). The inhomogeneous equations (Gauss for \(E\) + Ampère-Maxwell) become \(d\,{\star F} = J\), where \(\star\) is the Hodge dual and \(J\) is the current 3-form.</p>
<p>Two equations replace four. This is the cleanest formulation of classical electromagnetism.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"In forms, \(F = d\) ___.", "answer": "A"},
         {"type": "multiple-choice", "question": "Maxwell's homogeneous equations are encoded as:", "options": [r"\(dF = 0\)", r"\(F = 0\)", r"\(dA = 0\)", r"\(\star F = 0\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Forms reduce 4 Maxwell equations to 2.", "correctAnswer": True},
         {"type": "fill-blank", "question": "The Hodge dual is denoted by ___.", "answer": "*"},
         {"type": "true-false", "question": r"\(dF = 0\) follows from \(d^2 = 0\) and \(F = dA\).", "correctAnswer": True}]},
    {"title": "de Rham Cohomology (Preview)",
     "body_html": r"""
<p>The \(k\)-th <strong>de Rham cohomology</strong> of a manifold is</p>
<div class="math-block">$$H^k_{\text{dR}}(M) = \frac{\text{closed } k\text{-forms}}{\text{exact } k\text{-forms}}$$</div>
<p>It measures topological features:</p>
<ul>
<li>\(H^0\): connected components.</li>
<li>\(H^1\): "holes" / loops.</li>
<li>\(H^2\): "voids" / closed surfaces enclosing nothing.</li>
</ul>
<p>For \(\mathbb{R}^n\): \(H^0 = \mathbb{R}\), all higher \(H^k = 0\) (no topological holes). For a 2-torus: \(H^0 = H^2 = \mathbb{R}\), \(H^1 = \mathbb{R}^2\) (two independent cycles). de Rham theorem: this matches singular cohomology — analysis recovers topology.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(H^k_{\text{dR}} =\) closed mod ___.", "answer": "exact"},
         {"type": "multiple-choice", "question": r"\(H^0_{\text{dR}}\) counts:", "options": ["holes", "connected components", "voids", "intersections"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(\mathbb{R}^n\) has trivial higher de Rham cohomology.", "correctAnswer": True},
         {"type": "true-false", "question": "de Rham theorem connects analysis and topology.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"For a 2-torus, \(\dim H^1 =\) ___.", "answer": "2"}]},
    {"title": "Practice: Forms Calculations",
     "body_html": r"""
<p>Quick practice:</p>
<ol>
<li>Compute \(d(x^2 y)\): \(2xy\,dx + x^2\,dy\).</li>
<li>\(d(P\,dx + Q\,dy)\): \((\partial_x Q - \partial_y P)\,dx \wedge dy\). The 2D curl as a 2-form.</li>
<li>Apply \(d\) to \(\omega = -y\,dx + x\,dy\): \(d\omega = 2\,dx \wedge dy\). Curl is \(2\); check.</li>
<li>\(d(\,d(x^2 y)\,) = d(2xy\,dx + x^2\,dy) = (2x - 2x)\,dx\wedge dy = 0\). Confirms \(d^2 = 0\).</li>
</ol>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(d(x^2 y) = 2xy\,dx + x^?\,dy\). Fill: ___.", "answer": "2"},
         {"type": "multiple-choice", "question": r"\(d(P\,dx + Q\,dy) =\)", "options": [r"\(P\,dx + Q\,dy\)", r"\((Q_x - P_y)\,dx \wedge dy\)", "0", r"\(dx \wedge dy\)"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(d(\,df) = 0\) for any function \(f\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(d(-y\,dx + x\,dy) = ?\,dx \wedge dy\). Fill: ___.", "answer": "2"},
         {"type": "true-false", "question": r"\(d(dy \wedge dx) = 0\) (top-form on R²).", "correctAnswer": True}]},
    {"title": "Forms Checkpoint",
     "body_html": r"""
<p>Recap of Unit 38:</p>
<ul>
<li>k-forms are antisymmetric multilinear gadgets; integrate over k-dim regions.</li>
<li>Wedge product builds higher-degree forms; antisymmetric for 1-forms.</li>
<li>Exterior derivative \(d\) raises degree by 1; satisfies \(d^2 = 0\).</li>
<li>Closed: \(d\omega = 0\). Exact: \(\omega = d\eta\). Exact ⇒ closed.</li>
<li>Generalized Stokes: \(\int_M d\omega = \int_{\partial M} \omega\) — unifies FTLI, Green's, classical Stokes', divergence.</li>
<li>de Rham cohomology: closed mod exact — measures topology.</li>
<li>Maxwell's equations in forms: \(F = dA\), \(dF = 0\), \(d{\star F} = J\).</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": r"\(d^2 = 0\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Forms generalize:", "options": ["only vectors", "vectors and matrices", "grad/curl/div, integrals, Stokes", "none of the above"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Wedge of two 1-forms is ___.", "answer": "antisymmetric"},
         {"type": "true-false", "question": "Closed forms are always globally exact.", "correctAnswer": False},
         {"type": "true-false", "question": "Generalized Stokes works in any dimension.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(F = d\) ___ in form-language electromagnetism.", "answer": "A"},
         {"type": "true-false", "question": r"\(d\) on a function gives the gradient as a 1-form.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(38, "Differential Forms Preview", 556, LESSONS)
