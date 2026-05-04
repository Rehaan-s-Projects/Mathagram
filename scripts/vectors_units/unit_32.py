#!/usr/bin/env python3
"""Unit 32 — Surface Integrals (lessons 466-480)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Parametrizing a Surface",
     "body_html": r"""
<p>Just as a curve is parametrized by one parameter, a 2D surface in 3D is parametrized by two:</p>
<div class="math-block">$$\vec{r}(u, v) \in \mathbb{R}^3, \quad (u, v) \in D$$</div>
<p><strong>Examples.</strong></p>
<ul>
<li>Plane patch: \(\vec{r}(u,v) = \vec{p} + u\vec{a} + v\vec{b}\).</li>
<li>Sphere of radius \(R\): \(\vec{r}(\theta,\phi) = (R\sin\theta\cos\phi, R\sin\theta\sin\phi, R\cos\theta)\).</li>
<li>Cylinder of radius \(R\): \(\vec{r}(\theta, z) = (R\cos\theta, R\sin\theta, z)\).</li>
</ul>
<p>The partial derivatives \(\vec{r}_u\) and \(\vec{r}_v\) span the tangent plane at each point.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Surfaces in 3D need two parameters.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Sphere of radius R: \((R\sin\theta\cos\phi,\) ...?", "options": [r"\(R\sin\theta\sin\phi, R\cos\theta\)", r"\(R\cos\theta, 0\)", r"\(R\sin\phi, 0\)", r"\(R, R\)"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"Tangent plane is spanned by \(\vec{r}_u\) and \(\vec{r}_?\). Fill: ___.", "answer": "v"},
         {"type": "true-false", "question": "Surface parametrizations are unique.", "correctAnswer": False},
         {"type": "true-false", "question": "A plane patch can be parametrized by two parameters.", "correctAnswer": True}]},
    {"title": "The Surface Element",
     "body_html": r"""
<p>For a parametrized surface, the area element is</p>
<div class="math-block">$$dS = |\vec{r}_u \times \vec{r}_v|\,du\,dv$$</div>
<p>The cross product gives a vector normal to the surface; its magnitude is the area of the parallelogram spanned by \(\vec{r}_u, \vec{r}_v\).</p>
<p>The <strong>oriented surface element</strong> for vector integrals:</p>
<div class="math-block">$$d\vec{S} = (\vec{r}_u \times \vec{r}_v)\,du\,dv$$</div>
<p>This vector points along the normal and has magnitude \(dS\). The direction depends on parameter ordering.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(dS = |\vec{r}_u \times \vec{r}_v|\,du\,d\) ___.", "answer": "v"},
         {"type": "multiple-choice", "question": r"Direction of \(d\vec{S}\):", "options": ["tangent to surface", "normal to surface", "along x-axis", "depends on f"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(\vec{r}_u \times \vec{r}_v\) is perpendicular to the surface.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"For \(d\vec{S}\), the magnitude equals ___.", "answer": "dS"},
         {"type": "true-false", "question": "Swapping u and v reverses the orientation.", "correctAnswer": True}]},
    {"title": "Scalar Surface Integral",
     "body_html": r"""
<p>For a scalar function \(f\) and surface \(S\):</p>
<div class="math-block">$$\iint_S f\,dS = \iint_D f(\vec{r}(u,v))\,|\vec{r}_u \times \vec{r}_v|\,du\,dv$$</div>
<p>Geometric meaning: \(\iint_S 1\,dS = \text{area}(S)\). For \(f \neq 1\), it weights each piece of area by the value of \(f\) there.</p>
<p><strong>Application.</strong> Total mass of a surface with mass density \(\rho(x,y,z)\): \(M = \iint_S \rho\,dS\).</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\iint_S 1\,dS\) is the area of \(S\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Total mass with surface density \(\rho\):", "options": [r"\(\iint_S \rho\,dS\)", r"\(\iint_S \rho^2\,dS\)", r"\(\rho \cdot S\)", r"\(\int \rho\,d\vec{S}\)"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"Scalar surface integrals are ___ of orientation.", "answer": "independent"},
         {"type": "true-false", "question": "Reparametrizing changes the value of a scalar surface integral.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"\(dS = |\vec{r}_u \times\) ___\(|\,du\,dv\).", "answer": "r_v"}]},
    {"title": "Surface Area",
     "body_html": r"""
<p>Surface area examples.</p>
<p><strong>Sphere.</strong> Parametrize \(\vec{r}(\theta,\phi) = R(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)\), \(\theta \in [0,\pi]\), \(\phi \in [0,2\pi]\). \(|\vec{r}_\theta \times \vec{r}_\phi| = R^2 \sin\theta\). Total area:</p>
<div class="math-block">$$\int_0^{2\pi}\int_0^\pi R^2\sin\theta\,d\theta\,d\phi = 4\pi R^2$$</div>
<p><strong>Cylinder lateral surface.</strong> Radius \(R\), height \(h\): area \(2\pi R h\). Disk \(x^2+y^2 \le R^2\): area \(\pi R^2\). All recoverable from the surface integral formula.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Surface area of a sphere of radius \(R\): \(4\pi R^?\). Fill: ___.", "answer": "2"},
         {"type": "multiple-choice", "question": "Lateral area of a cylinder (radius R, height h):", "options": [r"\(\pi R^2 h\)", r"\(2\pi R h\)", r"\(2\pi R^2 h\)", r"\(\pi R h\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Surface area is computed via the scalar surface integral with f = 1.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"On a sphere, \(|\vec{r}_\theta \times \vec{r}_\phi| = R^2\) ___.", "answer": "sin theta"},
         {"type": "true-false", "question": "The disk x²+y²≤R² has area πR².", "correctAnswer": True}]},
    {"title": "Vector Surface Integral (Flux)",
     "body_html": r"""
<p>For a vector field \(\vec{F}\) and oriented surface \(S\):</p>
<div class="math-block">$$\iint_S \vec{F} \cdot d\vec{S} = \iint_D \vec{F}(\vec{r}(u,v)) \cdot (\vec{r}_u \times \vec{r}_v)\,du\,dv$$</div>
<p>This is the <strong>flux</strong> of \(\vec{F}\) through \(S\). Only the component of \(\vec{F}\) <em>normal</em> to the surface counts.</p>
<p>If \(\vec{F}\) is fluid velocity, the flux is the volumetric flow rate through the surface. If \(\vec{F}\) is electric field, it's the electric flux (Gauss's law).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Flux of \(\vec{F}\) through \(S\) is \(\iint_S \vec{F} \cdot d\) ___.", "answer": "S"},
         {"type": "multiple-choice", "question": "Flux captures the:", "options": ["tangential component", "normal component", "magnitude", "curl"], "correctIndex": 1},
         {"type": "true-false", "question": "Reversing orientation flips the sign of the flux.", "correctAnswer": True},
         {"type": "true-false", "question": "Flux of a fluid velocity = volumetric flow rate.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Gauss's law uses electric ___.", "answer": "flux"}]},
    {"title": "Orientation of a Surface",
     "body_html": r"""
<p>An <strong>orientation</strong> is a choice of "outward" normal direction at each point of \(S\) (consistent across the whole surface). For a sphere there's an inside and an outside; you have to pick which way the normals point.</p>
<p><strong>Möbius strip.</strong> Famously non-orientable — there's no consistent choice of normal. Surface integrals of vector fields aren't defined on it.</p>
<p>For a closed surface, the convention is the <strong>outward</strong> normal — pointing away from the interior. The flux through a closed surface measures net outflow.</p>""",
     "exercises": [
         {"type": "true-false", "question": "A Möbius strip is non-orientable.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "For closed surfaces, the convention is:", "options": ["inward normal", "outward normal", "tangent vectors", "any direction"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Net flux through a closed surface measures ___.", "answer": "outflow"},
         {"type": "true-false", "question": "Vector flux integrals require orientation.", "correctAnswer": True},
         {"type": "true-false", "question": "Scalar surface integrals require orientation.", "correctAnswer": False}]},
    {"title": "Outward Normals",
     "body_html": r"""
<p>For a surface defined as a level set \(g(x,y,z) = 0\), the gradient \(\nabla g\) is normal to the surface. Normalize and pick the right sign for outward.</p>
<p><strong>Sphere of radius \(R\).</strong> \(g = x^2+y^2+z^2 - R^2\). \(\nabla g = (2x, 2y, 2z)\). Outward unit normal: \(\hat{n} = (x, y, z)/R\). Just \(\vec{r}/R\) — the radial direction.</p>
<p><strong>Cylinder \(x^2+y^2 = R^2\).</strong> Normal: \((x, y, 0)/R\) — pointing radially outward (no z-component).</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\nabla g\) is normal to the level surface \(g = 0\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Outward normal of a sphere centered at origin: \(\hat n = \vec{r} /\) ___.", "answer": "R"},
         {"type": "multiple-choice", "question": r"Outward normal of cylinder \(x^2+y^2=R^2\):", "options": [r"\((x, y, z)/R\)", r"\((x, y, 0)/R\)", r"\((0,0,1)\)", r"\((1,0,0)\)"], "correctIndex": 1},
         {"type": "true-false", "question": "On a sphere, the outward normal is radial.", "correctAnswer": True},
         {"type": "true-false", "question": "Sign of the gradient must be picked carefully for outward orientation.", "correctAnswer": True}]},
    {"title": "Flux Through Common Surfaces",
     "body_html": r"""
<p><strong>Through a flat disk in the xy-plane.</strong> Outward normal \(\hat z\). Flux of \(\vec{F} = (F_1,F_2,F_3)\) is \(\iint_D F_3\,dA\). Just integrate the z-component over the disk.</p>
<p><strong>Through a sphere.</strong> If \(\vec{F} = \vec{r}/|\vec{r}|^2\) (Coulomb-like), flux through any closed surface containing the origin is \(4\pi\) (a Gauss's-law statement).</p>
<p><strong>Through a cylinder.</strong> Often easiest in cylindrical coordinates: lateral surface contributes \(F_r \cdot 2\pi R h\) (if \(F_r\) is constant on the cylinder).</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": r"Flux of \(\vec{F} = (0,0,1)\) through unit disk in xy-plane (oriented up):", "options": ["0", "1", "π", r"\(\pi\)"], "correctIndex": 2},
         {"type": "true-false", "question": r"Flux through a sphere of \(\vec{r}/|\vec{r}|^2\) (origin inside) is \(4\pi\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Lateral cylinder surface area: \(2\pi R\) ___.", "answer": "h"},
         {"type": "true-false", "question": "Flux through a flat horizontal disk depends only on Fz.", "correctAnswer": True},
         {"type": "true-false", "question": "Coulomb's flux is the basis for Gauss's law.", "correctAnswer": True}]},
    {"title": "Flux of a Conservative Field",
     "body_html": r"""
<p>A conservative field \(\vec{F} = \nabla\varphi\) does NOT necessarily have zero flux through arbitrary surfaces — that's a property of curl, not divergence.</p>
<p>However: a <strong>solenoidal</strong> (divergence-free) field has zero flux through any closed surface. So conservative + solenoidal ⇒ harmonic potential (\(\nabla^2 \varphi = 0\)).</p>
<p>Magnetic fields \(\vec{B}\) are solenoidal (\(\nabla \cdot \vec{B} = 0\)). Their flux through any closed surface is zero — there are no magnetic monopoles. This is one of Maxwell's equations.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Conservative fields automatically have zero flux through closed surfaces.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "Zero flux through closed surfaces ↔:", "options": ["zero curl", "zero divergence", "zero vector field", "incompressible flow"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\nabla \cdot \vec{B} = 0\) means there are no magnetic ___.", "answer": "monopoles"},
         {"type": "true-false", "question": "Solenoidal means divergence-free.", "correctAnswer": True},
         {"type": "true-false", "question": "Conservative + solenoidal implies harmonic potential.", "correctAnswer": True}]},
    {"title": "Divergence as Local Flux Density",
     "body_html": r"""
<p>Divergence has a beautiful interpretation: at a point, it measures the <strong>local outflow</strong> of the field per unit volume. Formally:</p>
<div class="math-block">$$\nabla \cdot \vec{F}(P) = \lim_{V \to 0} \frac{1}{|V|} \oiint_{\partial V} \vec{F} \cdot d\vec{S}$$</div>
<p>Positive divergence = "source" (field flowing out). Negative divergence = "sink" (field flowing in). Zero = no net flow.</p>
<p>This is the local form of the <strong>Divergence Theorem</strong>: the total flux out of a region equals the integral of divergence over the region's volume.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Divergence equals local flux density per unit volume.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Positive divergence at a point means:", "options": ["sink", "source", "saddle", "no flow"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Negative divergence at a point means a ___.", "answer": "sink"},
         {"type": "true-false", "question": "Divergence theorem connects volume integrals of div to flux.", "correctAnswer": True},
         {"type": "true-false", "question": "Zero divergence everywhere means the field is incompressible.", "correctAnswer": True}]},
    {"title": "Flux of Velocity in Fluids",
     "body_html": r"""
<p>For an incompressible fluid with velocity field \(\vec{v}\), the flux \(\iint_S \vec{v} \cdot d\vec{S}\) is the <strong>volumetric flow rate</strong> through \(S\) — how much fluid (in \(\text{m}^3/\text{s}\)) crosses the surface per unit time.</p>
<p>Mass flow rate: replace \(\vec{v}\) with \(\rho \vec{v}\). Then the flux is mass per second crossing.</p>
<p><strong>Continuity equation.</strong> For an incompressible fluid, \(\nabla \cdot \vec{v} = 0\) — flux through any closed surface is zero, fluid in equals fluid out.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Flux of fluid velocity = volumetric flow rate through the surface.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "For incompressible fluid:", "options": [r"\(\nabla \cdot \vec{v} = 0\)", r"\(\nabla \times \vec{v} = 0\)", r"\(\vec{v} = 0\)", r"\(\rho = 0\)"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"Mass flux uses \(\rho\) ___.", "answer": "v"},
         {"type": "true-false", "question": "Continuity equation expresses mass conservation.", "correctAnswer": True},
         {"type": "true-false", "question": "Incompressible fluids have nonzero divergence everywhere.", "correctAnswer": False}]},
    {"title": "Closed Surfaces",
     "body_html": r"""
<p>A <strong>closed surface</strong> bounds a region (no boundary curves). Examples: spheres, ellipsoids, cubes, the surface of a torus.</p>
<p>The flux through a closed surface is always taken with the <strong>outward</strong> normal. The result equals the integrated divergence of the field over the enclosed volume:</p>
<div class="math-block">$$\oiint_{\partial V} \vec{F} \cdot d\vec{S} = \iiint_V \nabla \cdot \vec{F}\,dV$$</div>
<p>This is the <strong>Divergence Theorem</strong> (Gauss's theorem). It's one of the central results of vector calculus.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Closed surfaces have no boundary curves.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Divergence theorem: \(\oiint \vec{F}\cdot d\vec{S} = \iiint\) ___ \(\,dV\).", "answer": "div F"},
         {"type": "multiple-choice", "question": "For a closed surface, normal direction is:", "options": ["arbitrary", "outward", "inward", "tangential"], "correctIndex": 1},
         {"type": "true-false", "question": "The divergence theorem is also called Gauss's theorem.", "correctAnswer": True},
         {"type": "true-false", "question": "Cubes are closed surfaces.", "correctAnswer": True}]},
    {"title": "Surface Integrals on Spheres",
     "body_html": r"""
<p>On a sphere of radius \(R\) centered at origin, with parametrization \((R\sin\theta\cos\phi, R\sin\theta\sin\phi, R\cos\theta)\):</p>
<ul>
<li>\(dS = R^2 \sin\theta\,d\theta\,d\phi\).</li>
<li>Outward normal \(\hat n = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)\) (the unit radial vector).</li>
<li>\(d\vec{S} = R^2 \sin\theta\,\hat n\,d\theta\,d\phi\).</li>
</ul>
<p><strong>Standard problem: flux of \(\vec{F} = \vec{r}\) through sphere.</strong> \(\vec{F} \cdot \hat n = R\). Total flux: \(\iint R \cdot R^2 \sin\theta\,d\theta\,d\phi = R^3 \cdot 4\pi\). Matches divergence theorem since \(\nabla \cdot \vec{r} = 3\) and volume \(= \tfrac{4}{3}\pi R^3\). ✓</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"On sphere of radius \(R\), \(dS = R^2 \sin\theta\,d\theta\,d\) ___.", "answer": "phi"},
         {"type": "multiple-choice", "question": r"Outward normal on a sphere centered at origin:", "options": [r"\(\hat z\)", r"\(\vec{r}/|\vec{r}|\)", "tangent vector", "anywhere"], "correctIndex": 1},
         {"type": "true-false", "question": r"Flux of \(\vec{F} = \vec{r}\) through sphere of radius \(R\) is \(4\pi R^3\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\nabla \cdot \vec{r} =\) ___.", "answer": "3"},
         {"type": "true-false", "question": "Divergence theorem matches flux and volume integrals.", "correctAnswer": True}]},
    {"title": "Practice: Surface Integrals",
     "body_html": r"""
<p>Quick practice:</p>
<ol>
<li>Area of unit sphere: \(4\pi\). Area of sphere radius 2: \(16\pi\).</li>
<li>Flux of \(\vec{F} = (1,0,0)\) through unit disk in yz-plane (normal \(\hat x\)): \(\pi\).</li>
<li>Flux of \(\vec{F} = (x,y,z)\) through unit sphere (outward): \(4\pi\). (Use \(\vec{F}\cdot\hat n = 1\) on the unit sphere.)</li>
<li>Mass of unit sphere with density \(\rho = 1\): area \(\cdot\) density \(= 4\pi\).</li>
</ol>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Area of unit sphere: \(4\pi\) ___.", "answer": "1"},
         {"type": "multiple-choice", "question": r"Flux of \((1,0,0)\) through yz unit disk:", "options": ["0", r"\(\pi\)", r"\(2\pi\)", "1"], "correctIndex": 1},
         {"type": "true-false", "question": r"Flux of \((x,y,z)\) through unit sphere is \(4\pi\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Surface area of sphere radius 2: \(16\) ___.", "answer": "pi"},
         {"type": "true-false", "question": "Mass with constant density is area times density.", "correctAnswer": True}]},
    {"title": "Surface Integrals Checkpoint",
     "body_html": r"""
<p>Recap of Unit 32:</p>
<ul>
<li>Surfaces are parametrized by two variables; tangent plane spanned by \(\vec{r}_u, \vec{r}_v\).</li>
<li>Surface element \(dS = |\vec{r}_u \times \vec{r}_v|\,du\,dv\).</li>
<li>Scalar surface integrals: \(\iint_S f\,dS\). Area when \(f=1\).</li>
<li>Vector surface integrals (flux): \(\iint_S \vec{F} \cdot d\vec{S}\).</li>
<li>Orientation matters for flux; pick outward normal on closed surfaces.</li>
<li>Divergence is local flux density.</li>
<li>Closed surfaces and the divergence theorem will return us in Unit 33.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Flux requires an oriented surface.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Surface area of a sphere of radius R:", "options": [r"\(2\pi R\)", r"\(4\pi R^2\)", r"\(\pi R^2\)", r"\(4\pi R\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(d\vec{S} = (\vec{r}_u \times \vec{r}_v)\,du\,d\) ___.", "answer": "v"},
         {"type": "true-false", "question": "Möbius strips support vector flux integrals.", "correctAnswer": False},
         {"type": "true-false", "question": "Divergence measures local flux density.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Volumetric flow rate is the flux of velocity ___.", "answer": "v"},
         {"type": "true-false", "question": "Surface integrals can be reduced to double integrals over the parameter domain.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(32, "Surface Integrals", 466, LESSONS)
