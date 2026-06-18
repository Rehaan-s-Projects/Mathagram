#!/usr/bin/env python3
"""Unit 26 — Inner Product Spaces (lessons 376-390)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Generalizing the Dot Product",
     "body_html": r"""
<p>An <strong>inner product</strong> is a generalization of the dot product to abstract vector spaces. Wherever you have one, you get notions of <em>length</em>, <em>angle</em>, and <em>orthogonality</em>.</p>
<p>The dot product on \(\mathbb{R}^n\) was \(\vec{u} \cdot \vec{v} = \sum u_i v_i\). For function spaces we'll write \(\langle f, g \rangle = \int f g\). For complex spaces, we add a conjugate. The point is: any operation \(\langle\cdot,\cdot\rangle\) satisfying the right axioms gives the same geometric machinery.</p>""",
     "exercises": [
         {"type": "true-false", "question": "An inner product generalizes the dot product.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"On function spaces, \(\langle f, g \rangle\) is typically defined as the ___ of the product.", "answer": "integral"},
         {"type": "multiple-choice", "question": "Inner products give us:", "options": ["lengths only", "angles only", "lengths AND angles AND orthogonality", "none"], "correctIndex": 2},
         {"type": "true-false", "question": "Inner products are always positive.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"\(\langle\vec{u},\vec{v}\rangle\) on \(\mathbb{R}^n\) is just the ___ product.", "answer": "dot"}]},
    {"title": "Inner Product Axioms",
     "body_html": r"""
<p>An inner product on a real vector space \(V\) is a map \(\langle\cdot,\cdot\rangle: V \times V \to \mathbb{R}\) satisfying:</p>
<ol>
<li><strong>Linearity in first slot:</strong> \(\langle a\vec{u} + b\vec{v}, \vec{w}\rangle = a\langle\vec{u},\vec{w}\rangle + b\langle\vec{v},\vec{w}\rangle\).</li>
<li><strong>Symmetry:</strong> \(\langle\vec{u},\vec{v}\rangle = \langle\vec{v},\vec{u}\rangle\).</li>
<li><strong>Positive definite:</strong> \(\langle\vec{v},\vec{v}\rangle \ge 0\), with equality iff \(\vec{v} = \vec{0}\).</li>
</ol>
<p>For complex spaces, symmetry is replaced by <strong>conjugate symmetry</strong>: \(\langle\vec{u},\vec{v}\rangle = \overline{\langle\vec{v},\vec{u}\rangle}\). This makes the inner product linear in the first slot and conjugate-linear in the second (physicists usually flip the convention).</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\langle\vec{v},\vec{v}\rangle \ge 0\) for any \(\vec{v}\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"For complex inner products, \(\langle\vec{u},\vec{v}\rangle =\)", "options": [r"\(\langle\vec{v},\vec{u}\rangle\)", r"\(\overline{\langle\vec{v},\vec{u}\rangle}\)", r"\(-\langle\vec{v},\vec{u}\rangle\)", r"\(\langle\vec{v},\vec{u}\rangle^2\)"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(\langle\vec{0},\vec{0}\rangle = 0\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Inner products are linear in the ___ slot (real case).", "answer": "first"},
         {"type": "true-false", "question": r"\(\langle\vec{v},\vec{v}\rangle = 0 \implies \vec{v} = \vec{0}\).", "correctAnswer": True}]},
    {"title": "Standard Inner Products",
     "body_html": r"""
<p>The standard inner products on common spaces:</p>
<ul>
<li>\(\mathbb{R}^n\): \(\langle\vec{u},\vec{v}\rangle = \vec{u}^T\vec{v} = \sum u_i v_i\).</li>
<li>\(\mathbb{C}^n\): \(\langle\vec{u},\vec{v}\rangle = \vec{u}^* \vec{v} = \sum \overline{u_i} v_i\) (conjugate the first vector).</li>
<li>\(M_{m \times n}(\mathbb{R})\): the <strong>Frobenius inner product</strong> \(\langle A, B\rangle = \text{tr}(A^T B) = \sum A_{ij} B_{ij}\).</li>
<li>Weighted: \(\langle\vec{u},\vec{v}\rangle_W = \vec{u}^T W \vec{v}\) for any positive-definite \(W\).</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Frobenius inner product of A, B is \(\text{tr}(A^T \cdot \) ___).", "answer": "B"},
         {"type": "multiple-choice", "question": r"\(\langle (1,2), (3,4) \rangle\) (standard) =", "options": ["7", "10", "11", "14"], "correctIndex": 2},
         {"type": "true-false", "question": "Weighted inner products work iff the weight matrix is positive definite.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"On \(\mathbb{C}^n\), the inner product conjugates the ___ vector.", "answer": "first"},
         {"type": "true-false", "question": "The Frobenius product turns matrix space into an inner product space.", "correctAnswer": True}]},
    {"title": "Inner Products on Function Spaces",
     "body_html": r"""
<p>On the space of continuous functions \(C[a,b]\), the standard inner product is the integral of the product:</p>
<div class="math-block">$$\langle f, g \rangle = \int_a^b f(x)g(x)\,dx$$</div>
<p>This satisfies all the axioms (linearity follows from integral linearity; symmetry is obvious; positive-definiteness uses continuity).</p>
<p><strong>Example.</strong> On \(C[0,1]\): \(\langle 1, x\rangle = \int_0^1 x\,dx = \tfrac{1}{2}\). \(\langle x, x\rangle = \int_0^1 x^2 dx = \tfrac{1}{3}\). So the "length" of \(f(x)=x\) on \([0,1]\) is \(\sqrt{1/3}\).</p>
<p>Function spaces with inner products are the foundation of <strong>Fourier analysis</strong>, <strong>Hilbert spaces</strong>, and <strong>quantum mechanics</strong>.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\langle f, g\rangle = \int_a^b f(x)\) ___ \(\,dx\).", "answer": "g(x)"},
         {"type": "multiple-choice", "question": r"On \(C[0,1]\), \(\langle 1, x\rangle =\)", "options": ["0", "1/2", "1", "1/3"], "correctIndex": 1},
         {"type": "true-false", "question": "Function inner products satisfy positive-definiteness.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"On \(C[0,1]\), \(\|x\|^2 = \int_0^1 x^2 dx =\) ___.", "answer": "1/3"},
         {"type": "true-false", "question": "Fourier analysis uses inner products on function spaces.", "correctAnswer": True}]},
    {"title": "Norm From an Inner Product",
     "body_html": r"""
<p>Every inner product induces a norm:</p>
<div class="math-block">$$\|\vec{v}\| = \sqrt{\langle\vec{v},\vec{v}\rangle}$$</div>
<p>This generalizes vector length. It satisfies all the norm axioms automatically (positivity, scaling, triangle inequality — the last follows from Cauchy-Schwarz).</p>
<p>Not every norm comes from an inner product, though. The L¹ and L∞ norms on \(\mathbb{R}^n\) don't. The test: a norm comes from an inner product iff it satisfies the <strong>parallelogram law</strong>:</p>
<div class="math-block">$$\|\vec{u}+\vec{v}\|^2 + \|\vec{u}-\vec{v}\|^2 = 2\|\vec{u}\|^2 + 2\|\vec{v}\|^2$$</div>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\|\vec{v}\| =\) ___ \(\langle \vec{v}, \vec{v}\rangle\).", "answer": "sqrt"},
         {"type": "true-false", "question": "Every inner product induces a norm.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Which norm does NOT come from an inner product?", "options": ["L²", "Euclidean", "L∞", "Frobenius"], "correctIndex": 2},
         {"type": "true-false", "question": "The parallelogram law characterizes inner-product norms.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\|c\vec{v}\| = |c| \cdot\) ___.", "answer": "||v||"}]},
    {"title": "Cauchy-Schwarz Inequality (Abstract)",
     "body_html": r"""
<p>For any inner product space:</p>
<div class="math-block">$$|\langle\vec{u},\vec{v}\rangle| \le \|\vec{u}\| \cdot \|\vec{v}\|$$</div>
<p>Equality holds iff \(\vec{u}\) and \(\vec{v}\) are linearly dependent.</p>
<p>This is one of the most important inequalities in mathematics. It implies the triangle inequality, and shows that the angle between vectors is well-defined: \(\cos\theta = \langle\vec{u},\vec{v}\rangle/(\|\vec{u}\|\|\vec{v}\|)\) is always between \(-1\) and \(1\).</p>
<p><strong>Function example.</strong> \(\left(\int fg\right)^2 \le \int f^2 \cdot \int g^2\). This is the integral form of Cauchy-Schwarz.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Cauchy-Schwarz holds in any inner product space.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Equality in Cauchy-Schwarz holds iff:", "options": ["one vector is zero", "the vectors are orthogonal", "the vectors are linearly dependent", "always"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"\(|\langle\vec{u},\vec{v}\rangle| \le \|\vec{u}\| \cdot\) ___.", "answer": "||v||"},
         {"type": "true-false", "question": "Cauchy-Schwarz implies the triangle inequality.", "correctAnswer": True},
         {"type": "true-false", "question": "Cauchy-Schwarz extends to integrals.", "correctAnswer": True}]},
    {"title": "Triangle Inequality (Abstract)",
     "body_html": r"""
<p>For any inner product norm:</p>
<div class="math-block">$$\|\vec{u} + \vec{v}\| \le \|\vec{u}\| + \|\vec{v}\|$$</div>
<p><strong>Proof sketch.</strong> Square both sides: \(\|\vec{u}+\vec{v}\|^2 = \|\vec{u}\|^2 + 2\langle\vec{u},\vec{v}\rangle + \|\vec{v}\|^2 \le \|\vec{u}\|^2 + 2\|\vec{u}\|\|\vec{v}\| + \|\vec{v}\|^2\) by Cauchy-Schwarz, which equals \((\|\vec{u}\|+\|\vec{v}\|)^2\).</p>
<p>Geometrically: the side of a triangle is no longer than the sum of the other two. With equality iff the vectors are parallel and pointing the same way.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\|\vec{u}+\vec{v}\| \le \|\vec{u}\| +\) ___.", "answer": "||v||"},
         {"type": "true-false", "question": "Triangle inequality follows from Cauchy-Schwarz.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Equality in triangle inequality holds when vectors are:", "options": ["orthogonal", "parallel same direction", "antiparallel", "perpendicular"], "correctIndex": 1},
         {"type": "true-false", "question": "Triangle inequality is required by all norm axioms.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\|\vec{u}-\vec{v}\| \ge | \|\vec{u}\| - \|\vec{v}\| |\) is called the ___ triangle inequality.", "answer": "reverse"}]},
    {"title": "Angle Between Abstract Vectors",
     "body_html": r"""
<p>Cauchy-Schwarz lets us define the <strong>angle</strong> \(\theta\) between any two nonzero vectors via</p>
<div class="math-block">$$\cos\theta = \frac{\langle\vec{u},\vec{v}\rangle}{\|\vec{u}\|\,\|\vec{v}\|} \in [-1, 1]$$</div>
<p>Two vectors are <strong>orthogonal</strong> if \(\langle\vec{u},\vec{v}\rangle = 0\). This works in any inner product space — including function spaces and matrix spaces.</p>
<p><strong>Example.</strong> On \(C[-1,1]\) with \(\langle f,g\rangle = \int_{-1}^1 fg\): the functions \(1\) and \(x\) are orthogonal because \(\int_{-1}^1 x\,dx = 0\). This is the basis of orthogonal polynomial families like Legendre polynomials.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Two vectors are orthogonal iff \(\langle\vec{u},\vec{v}\rangle =\) ___.", "answer": "0"},
         {"type": "multiple-choice", "question": r"On \(C[-1,1]\), are \(1\) and \(x\) orthogonal?", "options": ["yes", "no", "depends on basis", "only for x ≥ 0"], "correctIndex": 0},
         {"type": "true-false", "question": "Cosine of an angle in any inner product space is always in [-1, 1].", "correctAnswer": True},
         {"type": "true-false", "question": "Legendre polynomials are an orthogonal family on [-1, 1].", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\cos\theta = \langle\vec{u},\vec{v}\rangle / (\|\vec{u}\| \cdot\) ___).", "answer": "||v||"}]},
    {"title": "Orthogonality (Abstract)",
     "body_html": r"""
<p>A set of vectors is <strong>orthogonal</strong> if any two distinct vectors in the set have inner product zero. It's <strong>orthonormal</strong> if additionally each vector has norm 1.</p>
<p>An orthonormal set \(\{\vec{q}_1, \ldots, \vec{q}_k\}\) is automatically <strong>linearly independent</strong>: if \(\sum c_i \vec{q}_i = \vec{0}\), take inner product with \(\vec{q}_j\) → \(c_j = 0\).</p>
<p>Orthogonal sets are the cleanest possible bases. In an orthonormal basis, expressing any vector becomes trivial: \(\vec{v} = \sum_i \langle\vec{v},\vec{q}_i\rangle \vec{q}_i\).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Orthonormal sets are automatically linearly independent.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Orthonormal means:", "options": ["orthogonal only", "unit vectors only", "both", "neither"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"In an orthonormal basis \(\{\vec{q}_i\}\): \(\vec{v} = \sum_i\) ___ \(\vec{q}_i\).", "answer": "<v,q_i>"},
         {"type": "true-false", "question": "If \\(\\vec{q}_1, \\vec{q}_2\\) are orthonormal, then \\(\\langle\\vec{q}_1, \\vec{q}_2\\rangle = 1\\).", "correctAnswer": False},
         {"type": "true-false", "question": "An orthogonal set may include the zero vector.", "correctAnswer": False}]},
    {"title": "Pythagorean Theorem (Abstract)",
     "body_html": r"""
<p>If \(\vec{u}\) and \(\vec{v}\) are orthogonal in any inner product space:</p>
<div class="math-block">$$\|\vec{u} + \vec{v}\|^2 = \|\vec{u}\|^2 + \|\vec{v}\|^2$$</div>
<p>This is the abstract Pythagorean theorem. The proof is one line: expand \(\|\vec{u}+\vec{v}\|^2 = \|\vec{u}\|^2 + 2\langle\vec{u},\vec{v}\rangle + \|\vec{v}\|^2\), and the cross term vanishes by orthogonality.</p>
<p>It generalizes: for an orthogonal set \(\{\vec{u}_1, \ldots, \vec{u}_k\}\):</p>
<div class="math-block">$$\left\| \sum \vec{u}_i \right\|^2 = \sum \|\vec{u}_i\|^2$$</div>""",
     "exercises": [
         {"type": "fill-blank", "question": r"If \(\vec{u} \perp \vec{v}\), \(\|\vec{u}+\vec{v}\|^2 = \|\vec{u}\|^2 +\) ___.", "answer": "||v||^2"},
         {"type": "true-false", "question": "Pythagorean theorem holds in any inner product space.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The proof uses:", "options": ["determinants", "expansion of inner product", "induction", "trigonometry"], "correctIndex": 1},
         {"type": "true-false", "question": "It generalizes to any orthogonal set, not just pairs.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"For orthogonal vectors, \(\|\vec{u}-\vec{v}\|^2 = \|\vec{u}\|^2 +\) ___.", "answer": "||v||^2"}]},
    {"title": "Orthogonal Sets Are Independent",
     "body_html": r"""
<p><strong>Theorem.</strong> A set of nonzero, mutually orthogonal vectors is linearly independent.</p>
<p><strong>Proof.</strong> Suppose \(\sum c_i \vec{u}_i = \vec{0}\). Take inner product with \(\vec{u}_j\):</p>
<div class="math-block">$$\langle\vec{u}_j, \sum c_i \vec{u}_i\rangle = c_j \langle\vec{u}_j,\vec{u}_j\rangle = c_j \|\vec{u}_j\|^2 = 0$$</div>
<p>Since \(\vec{u}_j \neq \vec{0}\), \(c_j = 0\). True for every \(j\), so all coefficients vanish.</p>
<p>This is why orthonormal bases are so useful — orthogonality automatically gives you independence (and good numerics, when computing in finite precision).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Nonzero mutually orthogonal vectors are linearly independent.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The proof relies on:", "options": ["computing determinants", "taking inner products with each basis vector", "induction on dimension", "using a contradiction"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"If \(\vec{u}_j \neq \vec{0}\) and \(c_j \|\vec{u}_j\|^2 = 0\), then \(c_j =\) ___.", "answer": "0"},
         {"type": "true-false", "question": "An orthogonal set may include the zero vector and still be considered \"orthogonal.\"", "correctAnswer": True},
         {"type": "true-false", "question": "Orthonormal bases give numerically stable computations.", "correctAnswer": True}]},
    {"title": "Orthonormal Bases",
     "body_html": r"""
<p>An <strong>orthonormal basis</strong> is the gold standard: it's linearly independent, spans the space, AND has unit-length, mutually orthogonal vectors.</p>
<p>In an orthonormal basis \(\{\vec{q}_1, \ldots, \vec{q}_n\}\), coordinates are computed by inner products:</p>
<div class="math-block">$$\vec{v} = \sum_{i=1}^n \langle\vec{v},\vec{q}_i\rangle\, \vec{q}_i$$</div>
<p>The coefficient \(\langle\vec{v},\vec{q}_i\rangle\) is called a <strong>Fourier coefficient</strong> — yes, the same idea as Fourier series, just for general bases.</p>
<p>The Pythagorean theorem also gives <strong>Parseval's identity</strong>: \(\|\vec{v}\|^2 = \sum_i |\langle\vec{v},\vec{q}_i\rangle|^2\).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Coordinates in an orthonormal basis are inner products with basis vectors.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\|\vec{v}\|^2 = \sum_i |\langle\vec{v},\vec{q}_i\rangle|^2\) is called ___'s identity.", "answer": "Parseval"},
         {"type": "multiple-choice", "question": "Coefficients \\(\\langle\\vec{v}, \\vec{q}_i\\rangle\\) are called:", "options": ["scalars", "Fourier coefficients", "diagonal entries", "ranks"], "correctIndex": 1},
         {"type": "true-false", "question": r"Standard basis of \(\mathbb{R}^n\) is orthonormal.", "correctAnswer": True},
         {"type": "true-false", "question": "Every basis is orthonormal.", "correctAnswer": False}]},
    {"title": "Fourier Coefficients & Series",
     "body_html": r"""
<p>The most famous orthonormal basis is the trigonometric one on \(L^2[-\pi, \pi]\): the functions \(\frac{1}{\sqrt{2\pi}}, \frac{1}{\sqrt{\pi}}\cos(nx), \frac{1}{\sqrt{\pi}}\sin(nx)\) for \(n = 1, 2, \ldots\) are mutually orthogonal in the integral inner product.</p>
<p>Expanding a function in this basis gives the <strong>Fourier series</strong>:</p>
<div class="math-block">$$f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty (a_n \cos nx + b_n \sin nx)$$</div>
<p>where \(a_n, b_n\) are inner products of \(f\) with the corresponding basis function. Same machinery as \(\mathbb{R}^n\), just with infinitely many dimensions.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Trig functions form an orthogonal family on [-π, π].", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Fourier coefficients are computed via:", "options": ["determinants", "inner products with basis functions", "differentiation", "interpolation"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Fourier series expand functions in a basis of ___ and cosines.", "answer": "sines"},
         {"type": "true-false", "question": "Fourier analysis is just orthonormal-basis expansion in function space.", "correctAnswer": True},
         {"type": "true-false", "question": "Parseval's identity relates a function's L² norm to the sum of squared Fourier coefficients.", "correctAnswer": True}]},
    {"title": "Practice: Inner Product Computations",
     "body_html": r"""
<p>Quick practice problems:</p>
<ol>
<li>On \(\mathbb{R}^3\), \(\langle (1,2,3), (4,-1,0)\rangle = 4 - 2 + 0 = 2\).</li>
<li>On \(\mathbb{R}^2\), \(\|(3,4)\| = \sqrt{9+16} = 5\).</li>
<li>On \(C[0,1]\), \(\langle 1, x\rangle = \int_0^1 x\,dx = \tfrac{1}{2}\).</li>
<li>Are \((1,1,0)\) and \((1,-1,0)\) orthogonal? Yes (\(1-1+0=0\)).</li>
<li>Angle between \((1,0)\) and \((1,1)\): \(\cos\theta = 1/\sqrt{2}\), so \(\theta = 45°\).</li>
</ol>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\langle (1,2,3), (4,-1,0)\rangle =\) ___.", "answer": "2"},
         {"type": "multiple-choice", "question": r"\(\|(3,4)\| =\)", "options": ["7", "5", "6", "12"], "correctIndex": 1},
         {"type": "true-false", "question": r"\((1,1,0)\) and \((1,-1,0)\) are orthogonal.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Angle between \((1,0)\) and \((1,1)\): ___ degrees.", "answer": "45"},
         {"type": "fill-blank", "question": r"On \(C[0,1]\), \(\langle 1, x\rangle =\) ___.", "answer": "1/2"}]},
    {"title": "Inner Product Checkpoint",
     "body_html": r"""
<p>Recap of Unit 26:</p>
<ul>
<li>Inner products generalize the dot product to any vector space (real or complex).</li>
<li>They satisfy: linearity, symmetry (or conjugate symmetry), positive definiteness.</li>
<li>Functions, matrices, sequences all admit inner products.</li>
<li>Norm \(\|\vec{v}\| = \sqrt{\langle\vec{v},\vec{v}\rangle}\) gives length and distance.</li>
<li>Cauchy-Schwarz, triangle inequality, Pythagorean theorem hold in any IP space.</li>
<li>Orthogonal sets are independent; orthonormal bases give clean coordinate formulas.</li>
<li>Fourier expansion is just an orthonormal-basis expansion on function spaces.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": r"Cauchy-Schwarz: \(|\langle\vec{u},\vec{v}\rangle| \le \|\vec{u}\|\|\vec{v}\|\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": "An orthonormal basis lets you compute coordinates by:", "options": ["inverting matrices", "taking inner products", "differentiating", "factoring"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\|\vec{v}\| =\) ___ \(\langle\vec{v},\vec{v}\rangle\).", "answer": "sqrt"},
         {"type": "true-false", "question": "Function spaces have inner products.", "correctAnswer": True},
         {"type": "true-false", "question": "Pythagorean theorem requires orthogonality.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Parseval: \(\|\vec{v}\|^2 = \sum_i |\langle\vec{v},\vec{q}_i\rangle|^?\). Fill: ___.", "answer": "2"},
         {"type": "true-false", "question": "Triangle inequality: \\(\\|\\vec{u}+\\vec{v}\\| \\le \\|\\vec{u}\\| + \\|\\vec{v}\\|\\).", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(26, "Inner Product Spaces", 376, LESSONS)
