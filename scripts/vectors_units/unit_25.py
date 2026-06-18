#!/usr/bin/env python3
"""Unit 25 — Abstract Vector Spaces (lessons 361-375)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

UNIT_NUM = 25
UNIT_NAME = "Abstract Vector Spaces"
START = 361

LESSONS = [
    {
        "title": "Beyond \\(\\mathbb{R}^n\\): Generalizing Vectors",
        "body_html": r"""
<p>So far "vector" meant a tuple of real numbers. But the algebraic rules of vectors apply to many other objects: <strong>functions</strong>, <strong>polynomials</strong>, <strong>matrices</strong>, even <strong>sequences</strong>.</p>
<p>The abstract definition: a <strong>vector space</strong> is a set \(V\) with an addition operation and a scalar multiplication operation that satisfy 8 axioms (next lesson). Anything fitting these axioms is a vector space.</p>
<p>Why bother? Because once you prove a theorem in the abstract setting, it applies to all instances at once. Linear algebra of polynomials, ODE solution spaces, and quantum states all flow from the same theorems.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"Polynomials can form a vector space.", "correctAnswer": True},
            {"type": "true-false", "question": "Only tuples of real numbers can be vectors.", "correctAnswer": False},
            {"type": "multiple-choice", "question": "An abstract vector space requires:",
             "options": ["a fixed dimension", "addition and scalar multiplication satisfying axioms", "always be infinite", "always be over real numbers"], "correctIndex": 1},
            {"type": "fill-blank", "question": "The number of vector space axioms is ___.", "answer": "8"},
            {"type": "true-false", "question": "Vector space theorems apply to all instances simultaneously.", "correctAnswer": True}
        ]
    },
    {
        "title": "The 8 Vector Space Axioms",
        "body_html": r"""
<p>A set \(V\) (with addition \(+\) and scalar multiplication \(\cdot\) over a field \(\mathbb{F}\)) is a <strong>vector space</strong> if for all \(\vec{u}, \vec{v}, \vec{w} \in V\) and \(a, b \in \mathbb{F}\):</p>
<ol>
<li>\(\vec{u} + \vec{v} \in V\) (closed under addition)</li>
<li>\(\vec{u} + \vec{v} = \vec{v} + \vec{u}\) (commutative)</li>
<li>\((\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})\) (associative)</li>
<li>\(\exists\, \vec{0} \in V\) with \(\vec{v} + \vec{0} = \vec{v}\)</li>
<li>\(\forall \vec{v}\), \(\exists\, -\vec{v}\) with \(\vec{v} + (-\vec{v}) = \vec{0}\)</li>
<li>\(a\vec{v} \in V\) (closed under scalar multiplication)</li>
<li>\(a(\vec{u} + \vec{v}) = a\vec{u} + a\vec{v}\); \((a+b)\vec{v} = a\vec{v} + b\vec{v}\) (distributivity)</li>
<li>\(a(b\vec{v}) = (ab)\vec{v}\); \(1 \cdot \vec{v} = \vec{v}\)</li>
</ol>
""",
        "exercises": [
            {"type": "true-false", "question": "Every vector space contains a zero vector.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(1 \cdot \vec{v} =\) ___ in any vector space.", "answer": "v"},
            {"type": "true-false", "question": r"\(\vec{u} + \vec{v} = \vec{v} + \vec{u}\) is one of the axioms.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "The field of scalars is typically:",
             "options": [r"\(\mathbb{N}\)", r"\(\mathbb{Z}\)", r"\(\mathbb{R}\) or \(\mathbb{C}\)", "always finite"], "correctIndex": 2},
            {"type": "true-false", "question": "Closure under addition is one of the axioms.", "correctAnswer": True}
        ]
    },
    {
        "title": "Subspaces",
        "body_html": r"""
<p>A <strong>subspace</strong> \(W\) of a vector space \(V\) is a subset that is itself a vector space under the same operations. To check, you only need three things:</p>
<ol>
<li>\(\vec{0} \in W\)</li>
<li>\(W\) is closed under addition: if \(\vec{u}, \vec{v} \in W\), then \(\vec{u} + \vec{v} \in W\).</li>
<li>\(W\) is closed under scalar multiplication: if \(\vec{v} \in W\) and \(c\) is a scalar, then \(c\vec{v} \in W\).</li>
</ol>
<p><strong>Examples in \(\mathbb{R}^3\).</strong> Lines and planes through the origin are subspaces. \(\{\vec{0}\}\) and \(\mathbb{R}^3\) itself are subspaces (the trivial ones). A line NOT through the origin is NOT a subspace.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"Which is a subspace of \(\mathbb{R}^3\)?",
             "options": [r"the plane \(z = 0\)", r"the plane \(z = 1\)", r"the line \(y = 2x + 1\)", "all of these"], "correctIndex": 0},
            {"type": "true-false", "question": "Every subspace contains the zero vector.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"To check subspace, verify zero vector is in \(W\), and \(W\) is closed under addition and scalar ___.", "answer": "multiplication"},
            {"type": "true-false", "question": r"\(\{\vec{0}\}\) is a subspace.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"A line through origin in \(\mathbb{R}^3\) has dimension:",
             "options": ["0", "1", "2", "3"], "correctIndex": 1}
        ]
    },
    {
        "title": "Examples of Vector Spaces",
        "body_html": r"""
<p>Familiar and unfamiliar vector spaces:</p>
<ul>
<li>\(\mathbb{R}^n\): the prototypical example.</li>
<li>\(\mathbb{C}^n\): \(n\)-tuples of complex numbers.</li>
<li>\(M_{m \times n}(\mathbb{R})\): all \(m \times n\) real matrices, with entry-wise addition and scaling.</li>
<li>\(P_n\): polynomials of degree \(\le n\) in one variable.</li>
<li>\(C[a,b]\): continuous functions on \([a,b]\), with \((f+g)(x) = f(x)+g(x)\) and \((cf)(x) = cf(x)\).</li>
<li>Solution spaces of homogeneous linear ODEs (e.g., solutions of \(y'' + y = 0\)).</li>
<li>Sequence spaces \(\ell^p\): infinite sequences with \(\sum |a_n|^p &lt; \infty\).</li>
</ul>
<p>The vector-space framework unifies them all.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(M_{2 \times 3}(\mathbb{R})\) is a vector space.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"Which is NOT a vector space?",
             "options": [r"\(\mathbb{R}^3\)", r"\(P_5\)", r"\(C[0,1]\)", "the integers"], "correctIndex": 3},
            {"type": "fill-blank", "question": r"Solutions of \(y'' + y = 0\) form a vector space of dimension ___.", "answer": "2"},
            {"type": "true-false", "question": "Continuous functions form a vector space under pointwise addition.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"Why aren't integers a vector space (over \(\mathbb{R}\))?",
             "options": ["no zero", "not closed under scalar multiplication by reals", "not associative", "no addition"], "correctIndex": 1}
        ]
    },
    {
        "title": "Function Spaces",
        "body_html": r"""
<p>The set of all functions \(f: X \to \mathbb{R}\) on some domain \(X\) is a vector space under pointwise operations:</p>
<div class="math-block">$$(f + g)(x) = f(x) + g(x), \qquad (cf)(x) = c \cdot f(x)$$</div>
<p>Important subspaces include continuous functions \(C(X)\), differentiable functions, smooth functions \(C^\infty(X)\), \(L^p\) integrable functions, and solution spaces of linear ODEs/PDEs.</p>
<p>Function spaces are typically <strong>infinite-dimensional</strong>. They appear everywhere: Fourier analysis, quantum mechanics, signal processing.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": "Function spaces are typically:",
             "options": ["finite-dimensional", "infinite-dimensional", "always 1D", "always 2D"], "correctIndex": 1},
            {"type": "true-false", "question": "Continuous functions form a subspace of all functions.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"The pointwise sum of \(f\) and \(g\) at point \(x\) is \(f(x) +\) ___.", "answer": "g(x)"},
            {"type": "true-false", "question": "Smooth functions form a vector space.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Which is NOT a function space?",
             "options": ["smooth functions", "L^2 functions", "continuous functions", "non-zero functions"], "correctIndex": 3}
        ]
    },
    {
        "title": "Polynomial Spaces \\(P_n\\)",
        "body_html": r"""
<p>The space \(P_n\) consists of all polynomials of degree at most \(n\) in one variable:</p>
<div class="math-block">$$p(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n$$</div>
<p>Addition and scalar multiplication are pointwise. \(P_n\) has dimension \(n+1\), with the standard basis \(\{1, x, x^2, \ldots, x^n\}\).</p>
<p>The space \(P\) of all polynomials (any degree) is infinite-dimensional with basis \(\{1, x, x^2, x^3, \ldots\}\).</p>
<p><strong>Example.</strong> \(P_2\) (quadratics or lower) has dimension \(3\). A polynomial like \(2 + 3x - x^2\) has coordinates \((2, 3, -1)\) in this basis.</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"Dimension of \(P_4\) is ___.", "answer": "5"},
            {"type": "multiple-choice", "question": r"A standard basis for \(P_2\):",
             "options": [r"\(\{1, x, x^2\}\)", r"\(\{x, x^2\}\)", r"\(\{x^0\}\)", r"\(\{x^2\}\)"], "correctIndex": 0},
            {"type": "true-false", "question": "All polynomials (any degree) form an infinite-dimensional space.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"In the basis \(\{1, x, x^2\}\), \(p(x) = 5 - 3x\) has coordinates \((5, -3,\) ___).", "answer": "0"},
            {"type": "multiple-choice", "question": r"\(P_n\) has dimension:",
             "options": [r"\(n\)", r"\(n+1\)", r"\(n^2\)", r"\(2n\)"], "correctIndex": 1}
        ]
    },
    {
        "title": "Matrix Spaces \\(M_{m \\times n}\\)",
        "body_html": r"""
<p>The space \(M_{m \times n}(\mathbb{R})\) of all \(m \times n\) real matrices is itself a vector space — addition is entry-wise, and scaling is entry-wise.</p>
<p>Its dimension is \(m \cdot n\). The standard basis is \(\{E_{ij}\}\), where \(E_{ij}\) is the matrix with a \(1\) in position \((i,j)\) and \(0\)s elsewhere.</p>
<p><strong>Subspaces.</strong> Symmetric \(n \times n\) matrices form a subspace of dimension \(n(n+1)/2\). Skew-symmetric \(n \times n\) matrices form a subspace of dimension \(n(n-1)/2\). Every \(n \times n\) matrix decomposes uniquely as symmetric + skew-symmetric.</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"Dimension of \(M_{3 \times 4}(\mathbb{R})\) is ___.", "answer": "12"},
            {"type": "multiple-choice", "question": "Dim of symmetric 3×3 matrices:",
             "options": ["3", "6", "9", "8"], "correctIndex": 1},
            {"type": "true-false", "question": "Skew-symmetric matrices form a subspace.", "correctAnswer": True},
            {"type": "true-false", "question": "Every n×n matrix decomposes uniquely as symmetric + skew-symmetric.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"Dim of skew-symmetric 3×3 matrices: ___.", "answer": "3"}
        ]
    },
    {
        "title": "Linear Independence (Abstract)",
        "body_html": r"""
<p>The same definition as in \(\mathbb{R}^n\): vectors \(\vec{v}_1, \ldots, \vec{v}_k\) in any vector space \(V\) are <strong>linearly independent</strong> if</p>
<div class="math-block">$$c_1 \vec{v}_1 + \cdots + c_k \vec{v}_k = \vec{0} \implies c_1 = \cdots = c_k = 0$$</div>
<p>Equivalently: no vector in the set is a linear combination of the others.</p>
<p><strong>Example in \(P_2\).</strong> Are \(\{1, x, x^2\}\) independent? Suppose \(c_0 + c_1 x + c_2 x^2 = 0\) for all \(x\). The zero polynomial has all zero coefficients, so \(c_0 = c_1 = c_2 = 0\). Yes, independent.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(\{1, x, x^2\}\) is linearly independent in \(P_2\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"Which set is linearly dependent?",
             "options": [r"\(\{1, x\}\)", r"\(\{x, 2x\}\)", r"\(\{x, x^2\}\)", r"\(\{1, x^2\}\)"], "correctIndex": 1},
            {"type": "true-false", "question": "Independent in vector spaces means no nontrivial zero combination.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"The zero vector by itself is ___ independent. (yes/no)", "answer": "no"},
            {"type": "multiple-choice", "question": r"In \(P_2\), is \(\{1, 1+x, 1+x+x^2\}\) independent?",
             "options": ["Yes", "No", "Depends on the field", "Cannot tell"], "correctIndex": 0}
        ]
    },
    {
        "title": "Basis (Abstract)",
        "body_html": r"""
<p>A <strong>basis</strong> of a vector space \(V\) is a linearly independent set that <strong>spans</strong> \(V\). Every vector in \(V\) is a unique linear combination of basis vectors.</p>
<p>Standard bases:</p>
<ul>
<li>\(\mathbb{R}^n\): standard basis \(\{\vec{e}_1, \ldots, \vec{e}_n\}\).</li>
<li>\(P_n\): \(\{1, x, x^2, \ldots, x^n\}\).</li>
<li>\(M_{m \times n}\): the matrix units \(E_{ij}\).</li>
</ul>
<p>The basis isn't unique — \(\{1, x, 1-x\}\) doesn't work for \(P_1\) (it's dependent), but \(\{1+x, 1-x\}\) is a perfectly good basis. Choosing a basis is choosing a coordinate system.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(\{1, x, x^2\}\) is a basis for \(P_2\).", "correctAnswer": True},
            {"type": "true-false", "question": "A basis must be both linearly independent AND span the space.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(\{1, 1+x\}\) in \(P_1\):",
             "options": ["is not a basis", "is a basis", "spans but isn't independent", "is independent but doesn't span"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"Choosing a basis is choosing a ___ system.", "answer": "coordinate"},
            {"type": "true-false", "question": "Every vector space has multiple bases (if it has any).", "correctAnswer": True}
        ]
    },
    {
        "title": "Dimension (Abstract)",
        "body_html": r"""
<p>The <strong>dimension</strong> of a vector space \(V\) is the number of vectors in any basis of \(V\). The fact that all bases have the same size is a fundamental theorem.</p>
<ul>
<li>\(\dim \mathbb{R}^n = n\)</li>
<li>\(\dim P_n = n + 1\)</li>
<li>\(\dim M_{m \times n} = mn\)</li>
<li>\(\dim C[a,b] = \infty\)</li>
</ul>
<p>For finite-dim spaces, dimension is the most important invariant: <strong>two finite-dim vector spaces are isomorphic iff they have the same dimension</strong>. So \(\mathbb{R}^4\), \(P_3\), \(M_{2 \times 2}\) are all "the same" as vector spaces — just dressed differently.</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\dim P_3 =\) ___.", "answer": "4"},
            {"type": "multiple-choice", "question": r"Which has dimension 4?",
             "options": [r"\(\mathbb{R}^3\)", r"\(P_3\)", r"\(M_{2 \times 3}\)", r"\(C[0,1]\)"], "correctIndex": 1},
            {"type": "true-false", "question": "All bases of the same vector space have the same number of vectors.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(\dim M_{2 \times 2} =\) ___.", "answer": "4"},
            {"type": "true-false", "question": r"\(\mathbb{R}^4\), \(P_3\), \(M_{2 \times 2}\) are isomorphic as vector spaces.", "correctAnswer": True}
        ]
    },
    {
        "title": "Direct Sums of Subspaces",
        "body_html": r"""
<p>If \(U\) and \(W\) are subspaces of \(V\), their <strong>sum</strong> is \(U + W = \{\vec{u} + \vec{w} : \vec{u} \in U, \vec{w} \in W\}\). It's the smallest subspace containing both.</p>
<p>If additionally \(U \cap W = \{\vec{0}\}\), the sum is called a <strong>direct sum</strong>, written \(U \oplus W\). Every vector in \(U \oplus W\) has a <em>unique</em> decomposition \(\vec{v} = \vec{u} + \vec{w}\).</p>
<div class="math-block">$$\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$$</div>
<p><strong>Example.</strong> In \(\mathbb{R}^2\), the \(x\)-axis \(\oplus\) \(y\)-axis \(= \mathbb{R}^2\). They span everything and intersect only at the origin.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"In a direct sum, every vector has a unique decomposition.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"x-axis \(\oplus\) y-axis \(=\) \(\mathbb{R}^?\). Fill: ___.", "answer": "2"},
            {"type": "multiple-choice", "question": r"Direct sum requires \(U \cap W =\):",
             "options": [r"\(U\)", r"\(W\)", r"\(\{\vec{0}\}\)", r"\(V\)"], "correctIndex": 2},
            {"type": "true-false", "question": r"\(\dim(U+W) = \dim U + \dim W\) only if their intersection is trivial.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"Two lines through the origin in \(\mathbb{R}^3\) sum to a:",
             "options": ["plane (if distinct)", "line (always)", r"\(\mathbb{R}^3\)", "point"], "correctIndex": 0}
        ]
    },
    {
        "title": "Quotient Spaces (Preview)",
        "body_html": r"""
<p>Given a subspace \(W \subseteq V\), the <strong>quotient</strong> \(V/W\) is the set of "cosets" \(\vec{v} + W = \{\vec{v} + \vec{w} : \vec{w} \in W\}\). Two vectors \(\vec{v}_1, \vec{v}_2\) are identified if their difference is in \(W\).</p>
<p>Geometric picture: in \(\mathbb{R}^3\), if \(W\) is the \(z\)-axis, then \(V/W\) is the plane of "shadows": each point gets identified with everything directly above or below it.</p>
<p>Quotient spaces show up in linear algebra (cokernel), abstract algebra (group/ring quotients), and topology. The dimension formula:</p>
<div class="math-block">$$\dim(V/W) = \dim V - \dim W$$</div>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\dim(V/W) = \dim V - \dim\) ___.", "answer": "W"},
            {"type": "true-false", "question": r"In the quotient, \(\vec{v}_1\) and \(\vec{v}_2\) are identified iff \(\vec{v}_1 - \vec{v}_2 \in W\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(\mathbb{R}^3\) modded out by the \(z\)-axis is:",
             "options": [r"\(\mathbb{R}\)", r"\(\mathbb{R}^2\)", "the z-axis", "trivial"], "correctIndex": 1},
            {"type": "true-false", "question": "Quotient spaces are themselves vector spaces.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"In \(V/W\), the zero element is the coset of ___.", "answer": "0"}
        ]
    },
    {
        "title": "Isomorphism of Vector Spaces",
        "body_html": r"""
<p>Two vector spaces \(V\) and \(W\) are <strong>isomorphic</strong> (written \(V \cong W\)) if there is an invertible linear map \(T: V \to W\). They have the "same shape" as vector spaces.</p>
<p><strong>Theorem.</strong> Finite-dimensional vector spaces (over the same field) are isomorphic iff they have the same dimension.</p>
<p>So \(\mathbb{R}^4 \cong P_3 \cong M_{2 \times 2}\). Each is described by 4 numbers; you can move freely between them via a chosen basis.</p>
<p>This is why you can do "coordinate" computations: pick a basis, work with column vectors in \(\mathbb{R}^n\), then translate back. The choice of basis is the isomorphism \(V \to \mathbb{R}^n\).</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(\mathbb{R}^4 \cong P_3\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Finite-dim vector spaces over the same field are isomorphic iff:",
             "options": ["they're equal", "they have the same dimension", "they're both finite", "they're both real"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"An isomorphism is an ___ linear map.", "answer": "invertible"},
            {"type": "true-false", "question": r"\(\mathbb{R}^3 \cong \mathbb{R}^4\).", "correctAnswer": False},
            {"type": "true-false", "question": "Choosing a basis amounts to choosing an isomorphism with R^n.", "correctAnswer": True}
        ]
    },
    {
        "title": "Dual Spaces (Preview)",
        "body_html": r"""
<p>The <strong>dual space</strong> \(V^*\) is the vector space of all linear functionals \(\varphi: V \to \mathbb{F}\). For finite-dim \(V\), \(\dim V^* = \dim V\), so \(V \cong V^*\) — but the isomorphism isn't canonical.</p>
<p>For \(V = \mathbb{R}^n\) (column vectors), \(V^*\) is naturally identified with row vectors. The functional "dot with \(\vec{a}\)" sends \(\vec{v} \mapsto \vec{a}^T \vec{v}\).</p>
<p>Dual spaces matter for: gradients (a gradient is a covector, an element of \(V^*\)), differential forms, Dirac bra-ket notation, and many more advanced topics.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"For finite-dim \(V\), \(\dim V^* = \dim V\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"For \(\mathbb{R}^n\) (column vectors), the dual is naturally:",
             "options": [r"\(\mathbb{R}^{2n}\)", "row vectors", "matrices", "polynomials"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"Elements of \(V^*\) are called linear ___.", "answer": "functionals"},
            {"type": "true-false", "question": "Gradients can be viewed as elements of the dual space.", "correctAnswer": True},
            {"type": "true-false", "question": r"\(V \cong V^*\) for finite-dim V (but not canonically).", "correctAnswer": True}
        ]
    },
    {
        "title": "Abstract Spaces Checkpoint",
        "body_html": r"""
<p>Quick recap of Unit 25:</p>
<ul>
<li>A vector space is any set with addition and scalar multiplication satisfying the 8 axioms.</li>
<li>Polynomials, matrices, functions, sequences are all vector spaces.</li>
<li>Subspaces: closed under +, scalar mult, and contain \(\vec{0}\).</li>
<li>Independence/basis/dimension generalize from \(\mathbb{R}^n\) to any space.</li>
<li>Direct sum: every vector decomposes uniquely.</li>
<li>Two finite-dim spaces are isomorphic iff dimensions match.</li>
<li>Dual space \(V^*\): linear functionals from \(V\) to scalars.</li>
</ul>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\dim P_5 =\) ___.", "answer": "6"},
            {"type": "multiple-choice", "question": r"Which is NOT a vector space?",
             "options": [r"\(P_3\)", r"\(C[0,1]\)", r"\(M_{2 \times 2}\)", "the integers under +"], "correctIndex": 3},
            {"type": "true-false", "question": "Every basis of the same finite-dim space has the same number of vectors.", "correctAnswer": True},
            {"type": "true-false", "question": "A line not through the origin is a subspace.", "correctAnswer": False},
            {"type": "fill-blank", "question": r"\(\dim(U \oplus W) =\) ___ \(+ \dim W\).", "answer": "dim U"},
            {"type": "multiple-choice", "question": r"Which is canonically isomorphic to \(\mathbb{R}^4\)?",
             "options": [r"\(P_3\)", r"\(M_{2 \times 2}\)", "both", "neither (only via choice of basis)"], "correctIndex": 3},
            {"type": "true-false", "question": "Closure under addition + scalar multiplication is necessary for a subspace.", "correctAnswer": True}
        ]
    },
]

if __name__ == "__main__":
    render_unit(UNIT_NUM, UNIT_NAME, START, LESSONS)
