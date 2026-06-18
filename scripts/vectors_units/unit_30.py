#!/usr/bin/env python3
"""Unit 30 — Curvilinear Coordinates In Depth (lessons 436-450)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Why Curvilinear Coordinates?",
     "body_html": r"""
<p>Cartesian coordinates are great for boxes — but most physical problems have curved symmetry. A planet has spherical symmetry. A pipe has cylindrical symmetry. A donut has toroidal symmetry. Forcing Cartesian coordinates onto these problems makes the math harder than it needs to be.</p>
<p><strong>Curvilinear coordinates</strong> let us match the coordinate system to the geometry of the problem. The result: simpler equations, fewer terms, and physical insight that's lost in Cartesian.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Curvilinear coordinates can simplify problems with curved symmetry.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Spherical symmetry suggests:", "options": ["Cartesian", "spherical coordinates", "cylindrical", "polar"], "correctIndex": 1},
         {"type": "fill-blank", "question": "A pipe naturally fits ___ coordinates.", "answer": "cylindrical"},
         {"type": "true-false", "question": "Cartesian coordinates are always the simplest.", "correctAnswer": False},
         {"type": "true-false", "question": "Coordinate choice can reveal symmetry.", "correctAnswer": True}]},
    {"title": "Coordinate Surfaces",
     "body_html": r"""
<p>In any 3D coordinate system \((u_1, u_2, u_3)\), holding two coordinates fixed and varying the third sweeps out a curve — a <strong>coordinate curve</strong>. Holding one fixed and varying the other two sweeps out a <strong>coordinate surface</strong>.</p>
<p><strong>Examples.</strong> In spherical:</p>
<ul>
<li>\(\rho = \text{const}\): sphere of radius \(\rho\).</li>
<li>\(\theta = \text{const}\): cone (or half-plane through the z-axis).</li>
<li>\(\phi = \text{const}\): half-plane making angle \(\phi\) with the x-axis.</li>
</ul>
<p>The intersection of any two coordinate surfaces is a coordinate curve.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": r"In spherical, \(\rho = \text{const}\) is:", "options": ["a plane", "a sphere", "a cone", "a line"], "correctIndex": 1},
         {"type": "true-false", "question": "Holding two coordinates fixed gives a curve.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"In cylindrical, \(z = \text{const}\) is a ___.", "answer": "plane"},
         {"type": "true-false", "question": "Coordinate surfaces are always flat.", "correctAnswer": False},
         {"type": "true-false", "question": "Intersections of coordinate surfaces give coordinate curves.", "correctAnswer": True}]},
    {"title": "Tangent Vectors at a Point",
     "body_html": r"""
<p>At each point \(\vec{r}(u_1,u_2,u_3)\), the tangent vector to the \(i\)-th coordinate curve is</p>
<div class="math-block">$$\vec{e}_i = \frac{\partial \vec{r}}{\partial u_i}$$</div>
<p>These tangent vectors define a local basis. For example, in spherical \((\rho, \theta, \phi)\):</p>
<ul>
<li>\(\vec{e}_\rho\): radial outward.</li>
<li>\(\vec{e}_\theta\): tangent to the circle of constant \(\rho, \phi\).</li>
<li>\(\vec{e}_\phi\): tangent to the longitude circle.</li>
</ul>
<p>These vary from point to point — that's the price of using a non-Cartesian system.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Tangent basis vectors generally vary from point to point.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\vec{e}_i = \partial \vec{r} / \partial\) ___.", "answer": "u_i"},
         {"type": "multiple-choice", "question": r"In spherical, \(\vec{e}_\rho\) points:", "options": ["along z", "radially outward", "tangentially", "azimuthally"], "correctIndex": 1},
         {"type": "true-false", "question": "In Cartesian, the basis vectors are constant.", "correctAnswer": True},
         {"type": "true-false", "question": "Tangent vectors are usually unit length.", "correctAnswer": False}]},
    {"title": "Scale Factors (Lamé Coefficients)",
     "body_html": r"""
<p>The <strong>scale factor</strong> for the \(i\)-th coordinate is</p>
<div class="math-block">$$h_i = \left|\frac{\partial \vec{r}}{\partial u_i}\right|$$</div>
<p>Dividing the tangent vector by its scale factor gives a unit basis vector \(\hat{e}_i\). Scale factors translate "change in coordinate" to "change in arc length."</p>
<p><strong>Spherical.</strong> \(h_\rho = 1\), \(h_\theta = \rho\), \(h_\phi = \rho\sin\theta\). Moving \(d\theta\) at radius \(\rho\) covers arc length \(\rho\,d\theta\) — exactly the scale factor.</p>
<p><strong>Cylindrical.</strong> \(h_r = 1\), \(h_\theta = r\), \(h_z = 1\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"In spherical, \(h_\theta =\) ___.", "answer": "rho"},
         {"type": "multiple-choice", "question": r"In cylindrical, \(h_\theta =\)", "options": ["1", r"\(r\)", r"\(z\)", "0"], "correctIndex": 1},
         {"type": "true-false", "question": "Scale factors translate coordinate change to arc length.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"In spherical, \(h_\phi =\) ___ \(\sin\theta\).", "answer": "rho"},
         {"type": "true-false", "question": "Scale factors are always 1 in any system.", "correctAnswer": False}]},
    {"title": "Orthogonal Curvilinear Coordinates",
     "body_html": r"""
<p>A curvilinear system is <strong>orthogonal</strong> if at every point, the tangent basis vectors \(\vec{e}_i\) are mutually perpendicular. Most useful systems (Cartesian, cylindrical, spherical, parabolic) are orthogonal.</p>
<p>In an orthogonal system, the line element simplifies dramatically:</p>
<div class="math-block">$$ds^2 = h_1^2 du_1^2 + h_2^2 du_2^2 + h_3^2 du_3^2$$</div>
<p>And the volume element is just the product of the scale factors:</p>
<div class="math-block">$$dV = h_1 h_2 h_3 \, du_1\, du_2\, du_3$$</div>""",
     "exercises": [
         {"type": "true-false", "question": "Orthogonal coordinate systems have perpendicular tangent bases.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"In orthogonal coords, \(dV = h_1 h_2 h_3\,du_1 du_2\) ___.", "answer": "du_3"},
         {"type": "multiple-choice", "question": "Cylindrical, spherical, Cartesian — all are:", "options": ["non-orthogonal", "orthogonal", "polar only", "1D"], "correctIndex": 1},
         {"type": "true-false", "question": r"In an orthogonal system, \(ds^2\) is a sum of squares.", "correctAnswer": True},
         {"type": "true-false", "question": "Most physically-motivated coordinate systems are orthogonal.", "correctAnswer": True}]},
    {"title": "The Jacobian Determinant",
     "body_html": r"""
<p>For a coordinate change \((x,y,z) = \vec{r}(u_1, u_2, u_3)\), the <strong>Jacobian determinant</strong> is</p>
<div class="math-block">$$J = \det \frac{\partial(x,y,z)}{\partial(u_1, u_2, u_3)}$$</div>
<p>For orthogonal coords, \(|J| = h_1 h_2 h_3\).</p>
<p>The Jacobian appears whenever you change variables in an integral:</p>
<div class="math-block">$$\iiint f\,dx\,dy\,dz = \iiint f\,|J|\,du_1\,du_2\,du_3$$</div>
<p><strong>Spherical.</strong> \(|J| = \rho^2 \sin\theta\). <strong>Cylindrical.</strong> \(|J| = r\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"For orthogonal coords, \(|J| = h_1 h_2\) ___.", "answer": "h_3"},
         {"type": "multiple-choice", "question": r"In spherical, \(|J| =\)", "options": [r"\(\rho\)", r"\(\rho^2\)", r"\(\rho^2 \sin\theta\)", r"\(\sin\theta\)"], "correctIndex": 2},
         {"type": "true-false", "question": "Jacobian appears in changes of variable in integrals.", "correctAnswer": True},
         {"type": "fill-blank", "question": "In cylindrical coords, |J| = ___.", "answer": "r"},
         {"type": "true-false", "question": "The Jacobian is always 1 for any coordinate transformation.", "correctAnswer": False}]},
    {"title": "Cylindrical Coordinates Revisited",
     "body_html": r"""
<p>Coordinates: \((r, \theta, z)\) with \(x = r\cos\theta\), \(y = r\sin\theta\), \(z = z\).</p>
<p>Scale factors: \(h_r = 1\), \(h_\theta = r\), \(h_z = 1\). Volume element: \(dV = r\,dr\,d\theta\,dz\).</p>
<p>Useful for: pipes, cables, anything with axial symmetry. The Laplacian becomes</p>
<div class="math-block">$$\nabla^2 f = \frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial f}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 f}{\partial \theta^2} + \frac{\partial^2 f}{\partial z^2}$$</div>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(dV = r\,dr\,d\theta\,d\) ___.", "answer": "z"},
         {"type": "multiple-choice", "question": r"In cylindrical, \(h_\theta =\)", "options": ["1", r"\(r\)", r"\(\theta\)", r"\(z\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Cylindrical coords help with axial symmetry.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(x = r \cos\) ___.", "answer": "theta"},
         {"type": "true-false", "question": "The Laplacian is the same in all coordinate systems.", "correctAnswer": False}]},
    {"title": "Spherical Coordinates Revisited",
     "body_html": r"""
<p>Coordinates: \((\rho, \theta, \phi)\) with \(\theta\) the polar angle from the \(z\)-axis, and \(\phi\) the azimuthal angle in the \(xy\)-plane.</p>
<p>\(x = \rho\sin\theta\cos\phi\), \(y = \rho\sin\theta\sin\phi\), \(z = \rho\cos\theta\).</p>
<p>Scale factors: \(h_\rho = 1\), \(h_\theta = \rho\), \(h_\phi = \rho\sin\theta\). Volume element: \(dV = \rho^2 \sin\theta\,d\rho\,d\theta\,d\phi\).</p>
<p>Useful for: planets, atoms, gravitational/Coulomb fields. Conventions vary — physicists and mathematicians swap \(\theta\) and \(\phi\)!</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(dV = \rho^2 \sin\theta\,d\rho\,d\theta\,d\) ___.", "answer": "phi"},
         {"type": "multiple-choice", "question": r"In spherical, \(z =\)", "options": [r"\(\rho \sin\theta\)", r"\(\rho \cos\theta\)", r"\(\rho \cos\phi\)", r"\(\rho\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Physicists and mathematicians use the same naming for spherical angles.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"\(h_\phi = \rho \sin\) ___.", "answer": "theta"},
         {"type": "true-false", "question": "Spherical coordinates suit problems with central symmetry.", "correctAnswer": True}]},
    {"title": "Other Orthogonal Systems",
     "body_html": r"""
<p>Beyond cylindrical and spherical, many other orthogonal systems exist, each tuned to specific geometries:</p>
<ul>
<li><strong>Parabolic:</strong> \(x = \tfrac{1}{2}(u^2-v^2)\), \(y = uv\). Useful for paraboloid problems.</li>
<li><strong>Elliptic cylindrical:</strong> for elliptical waveguides.</li>
<li><strong>Toroidal:</strong> for donuts (literally — fusion reactors, tokamaks).</li>
<li><strong>Bispherical:</strong> for two-body problems.</li>
<li><strong>Prolate/oblate spheroidal:</strong> for Earth's shape, ellipsoidal molecules.</li>
</ul>
<p>The Helmholtz/Laplace equation separates in eleven different orthogonal coordinate systems — the "11 separable systems" of mathematical physics.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Toroidal coordinates suit donut-shaped problems.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Prolate spheroidal coordinates suit:", "options": ["Earth's shape", "spheres exactly", "cubes", "cylinders only"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"There are eleven coordinate systems in which the ___ equation separates.", "answer": "Helmholtz"},
         {"type": "true-false", "question": "Most physical problems can be tackled in just two systems.", "correctAnswer": False},
         {"type": "true-false", "question": "Tokamaks use toroidal coordinates.", "correctAnswer": True}]},
    {"title": "Volume & Surface Elements",
     "body_html": r"""
<p>In any orthogonal curvilinear system:</p>
<div class="math-block">$$dV = h_1 h_2 h_3\,du_1\,du_2\,du_3$$</div>
<p>For a surface with one coordinate held fixed (e.g., \(u_1 = \text{const}\)), the surface area element is:</p>
<div class="math-block">$$dS = h_2 h_3\,du_2\,du_3$$</div>
<p><strong>Spherical.</strong> Surface area on a sphere of radius \(\rho\): \(dS = \rho^2 \sin\theta\,d\theta\,d\phi\). Total area: \(\int_0^\pi \int_0^{2\pi} \rho^2\sin\theta\,d\phi\,d\theta = 4\pi\rho^2\). ✓</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"On a sphere of radius \(\rho\), \(dS = \rho^2 \sin\theta\,d\theta\,d\) ___.", "answer": "phi"},
         {"type": "multiple-choice", "question": r"Total surface area of a sphere of radius \(R\):", "options": [r"\(4\pi R^2\)", r"\(2\pi R\)", r"\(\pi R^3\)", r"\(\frac{4}{3}\pi R^3\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Volume element factorizes into scale factors and coordinate differentials.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(dV\) in spherical \(= \rho^2 \sin\theta\,d\rho\,d\theta\,d\) ___.", "answer": "phi"},
         {"type": "true-false", "question": "Surface element is always flat (h_i = 1) on coordinate surfaces.", "correctAnswer": False}]},
    {"title": "Gradient in Curvilinear",
     "body_html": r"""
<p>In an orthogonal curvilinear system, the gradient of a scalar function \(f\) is</p>
<div class="math-block">$$\nabla f = \sum_i \frac{1}{h_i} \frac{\partial f}{\partial u_i} \hat{e}_i$$</div>
<p>The scale factors \(1/h_i\) account for the fact that "moving \(du_i\) in coordinate space" doesn't equal "moving \(du_i\) in real space."</p>
<p><strong>Spherical.</strong></p>
<div class="math-block">$$\nabla f = \frac{\partial f}{\partial \rho}\hat{e}_\rho + \frac{1}{\rho}\frac{\partial f}{\partial \theta}\hat{e}_\theta + \frac{1}{\rho \sin\theta}\frac{\partial f}{\partial \phi}\hat{e}_\phi$$</div>""",
     "exercises": [
         {"type": "fill-blank", "question": r"In curvilinear coords, \(\nabla f\) has \(1/h_i\) factors because of ___ factors.", "answer": "scale"},
         {"type": "multiple-choice", "question": r"In spherical, the radial component of \(\nabla f\) is:", "options": [r"\(\partial f / \partial \rho\)", r"\(\rho \partial f / \partial \rho\)", r"\(1/\rho \partial f / \partial \rho\)", r"\(\partial f / \partial \theta\)"], "correctIndex": 0},
         {"type": "true-false", "question": "The gradient takes the same form in all coordinate systems.", "correctAnswer": False},
         {"type": "true-false", "question": "Scale factors appear in the denominator of curvilinear gradient.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"In cylindrical, the \(\theta\) component of \(\nabla f\) has factor \(1/\) ___.", "answer": "r"}]},
    {"title": "Divergence in Curvilinear",
     "body_html": r"""
<p>For a vector field \(\vec{F} = F_1 \hat{e}_1 + F_2 \hat{e}_2 + F_3 \hat{e}_3\) in orthogonal coords:</p>
<div class="math-block">$$\nabla \cdot \vec{F} = \frac{1}{h_1 h_2 h_3} \left[ \frac{\partial}{\partial u_1}(h_2 h_3 F_1) + \frac{\partial}{\partial u_2}(h_1 h_3 F_2) + \frac{\partial}{\partial u_3}(h_1 h_2 F_3) \right]$$</div>
<p><strong>Spherical.</strong></p>
<div class="math-block">$$\nabla \cdot \vec{F} = \frac{1}{\rho^2}\frac{\partial(\rho^2 F_\rho)}{\partial\rho} + \frac{1}{\rho \sin\theta} \frac{\partial(\sin\theta\, F_\theta)}{\partial \theta} + \frac{1}{\rho\sin\theta} \frac{\partial F_\phi}{\partial \phi}$$</div>""",
     "exercises": [
         {"type": "true-false", "question": "Divergence in curvilinear coords includes scale factor weights.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(\nabla \cdot \vec{F}\) in spherical involves \(1/\rho^2\) for:", "options": ["the φ component", "the radial term", "the θ component", "all components equally"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"In curvilinear, prefactor is \(1/(h_1 h_2\) ___\()\).", "answer": "h_3"},
         {"type": "true-false", "question": "Cartesian divergence has no h-factors.", "correctAnswer": True},
         {"type": "true-false", "question": "Divergence formulae differ by coordinate system.", "correctAnswer": True}]},
    {"title": "Curl & Laplacian in Curvilinear",
     "body_html": r"""
<p><strong>Curl</strong> in orthogonal coordinates:</p>
<div class="math-block">$$(\nabla \times \vec{F})_i = \frac{1}{h_j h_k}\left[\frac{\partial(h_k F_k)}{\partial u_j} - \frac{\partial(h_j F_j)}{\partial u_k}\right]$$</div>
<p><strong>Laplacian</strong>:</p>
<div class="math-block">$$\nabla^2 f = \frac{1}{h_1 h_2 h_3} \sum_i \frac{\partial}{\partial u_i}\left(\frac{h_1 h_2 h_3}{h_i^2} \frac{\partial f}{\partial u_i}\right)$$</div>
<p>Spherical Laplacian (the famous one):</p>
<div class="math-block">$$\nabla^2 f = \frac{1}{\rho^2}\frac{\partial}{\partial \rho}\left(\rho^2 \frac{\partial f}{\partial \rho}\right) + \frac{1}{\rho^2 \sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta \frac{\partial f}{\partial \theta}\right) + \frac{1}{\rho^2 \sin^2 \theta}\frac{\partial^2 f}{\partial \phi^2}$$</div>""",
     "exercises": [
         {"type": "true-false", "question": "Curl and Laplacian formulae depend on the coordinate system.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(\nabla^2 f\) in spherical includes a factor of \(1/(\rho^2 \sin\theta)\) for:", "options": [r"\(\rho\) term", r"\(\theta\) term", r"\(\phi\) term", "none"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Laplacian outer prefactor: \(1/(h_1 h_2\) ___\()\).", "answer": "h_3"},
         {"type": "true-false", "question": "Spherical Laplacian appears in atomic orbital problems.", "correctAnswer": True},
         {"type": "true-false", "question": "Curl in curvilinear has no h factors.", "correctAnswer": False}]},
    {"title": "Practice: Coordinate System Choice",
     "body_html": r"""
<p>Pick the right coordinates:</p>
<ol>
<li><strong>Heat conduction in a sphere.</strong> → spherical coordinates.</li>
<li><strong>Flow through a circular pipe.</strong> → cylindrical coordinates.</li>
<li><strong>Fields outside two charges.</strong> → bispherical coordinates (advanced).</li>
<li><strong>Tokamak plasma.</strong> → toroidal coordinates.</li>
<li><strong>A disc galaxy.</strong> → cylindrical coordinates (with z = polar axis).</li>
<li><strong>Earth's gravity field as a function of latitude/longitude/height.</strong> → spherical (or oblate spheroidal for higher accuracy).</li>
</ol>""",
     "exercises": [
         {"type": "multiple-choice", "question": "Heat in a sphere → use:", "options": ["Cartesian", "cylindrical", "spherical", "toroidal"], "correctIndex": 2},
         {"type": "true-false", "question": "Flow in a pipe is naturally cylindrical.", "correctAnswer": True},
         {"type": "fill-blank", "question": "A donut/tokamak suggests ___ coordinates.", "answer": "toroidal"},
         {"type": "true-false", "question": "Earth's gravity is exactly spherical.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "Disc galaxies suit:", "options": ["Cartesian", "cylindrical", "elliptic", "rectangular"], "correctIndex": 1}]},
    {"title": "Curvilinear Checkpoint",
     "body_html": r"""
<p>Recap of Unit 30:</p>
<ul>
<li>Coordinate curves and surfaces define the local structure of any coordinate system.</li>
<li>Tangent vectors \(\vec{e}_i = \partial \vec{r}/\partial u_i\); scale factors \(h_i = |\vec{e}_i|\).</li>
<li>Orthogonal systems have perpendicular tangent vectors at every point.</li>
<li>Volume element: \(dV = h_1 h_2 h_3\,du_1\,du_2\,du_3\).</li>
<li>Cylindrical and spherical are the two most-used systems.</li>
<li>Gradient, divergence, curl, Laplacian all carry scale-factor decorations.</li>
<li>Choose coordinates matching the geometry of the problem.</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(h_\theta\) in spherical is ___.", "answer": "rho"},
         {"type": "multiple-choice", "question": "Volume in spherical:", "options": [r"\(\rho^2 d\rho\,d\theta\,d\phi\)", r"\(\rho^2\sin\theta\,d\rho\,d\theta\,d\phi\)", r"\(d\rho\,d\theta\,d\phi\)", r"\(r\,dr\,d\theta\,dz\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Cartesian, cylindrical, spherical are all orthogonal systems.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"In cylindrical, \(dV = r\,dr\,d\theta\,d\) ___.", "answer": "z"},
         {"type": "true-false", "question": "The Laplacian formula is the same in every coordinate system.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"Surface area of unit sphere is \(4\pi\) ___.", "answer": "1"},
         {"type": "true-false", "question": "Choosing curvilinear coords matched to symmetry simplifies many problems.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(30, "Curvilinear Coordinates In Depth", 436, LESSONS)
