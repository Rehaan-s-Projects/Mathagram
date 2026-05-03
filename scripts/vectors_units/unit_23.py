#!/usr/bin/env python3
"""Unit 23 — Eigenvalues & Eigenvectors (lessons 331-345)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

UNIT_NUM = 23
UNIT_NAME = "Eigenvalues & Eigenvectors"
START = 331

LESSONS = [
    {
        "title": "The Eigenvalue Equation",
        "body_html": r"""
<p>For a square matrix \(A\), an <strong>eigenvector</strong> is a nonzero vector \(\vec{v}\) such that \(A\vec{v}\) is a scalar multiple of \(\vec{v}\):</p>
<div class="math-block">$$A\vec{v} = \lambda \vec{v}$$</div>
<p>The scalar \(\lambda\) is called the <strong>eigenvalue</strong> associated with \(\vec{v}\). Geometrically: \(A\) doesn't rotate \(\vec{v}\); it only stretches or shrinks (or flips) it along its own line.</p>
<p>Eigenvectors and eigenvalues capture the "axes" along which a transformation acts diagonally. They show up everywhere: principal components, vibrational modes, quantum states, Google's PageRank.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(\vec{v} = \vec{0}\) is allowed as an eigenvector.", "correctAnswer": False},
            {"type": "fill-blank", "question": r"In \(A\vec{v} = \lambda\vec{v}\), \(\lambda\) is called the ___.", "answer": "eigenvalue"},
            {"type": "multiple-choice", "question": r"For \(A = 2I\), every nonzero vector is an eigenvector with eigenvalue:",
             "options": ["0", "1", "2", "depends"], "correctIndex": 2},
            {"type": "true-false", "question": "Eigenvectors are stretched/shrunk but not rotated by A.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Eigenvalues only exist for:",
             "options": ["all matrices", "square matrices", "symmetric matrices", "invertible matrices"], "correctIndex": 1}
        ]
    },
    {
        "title": "Geometric Meaning of an Eigenvector",
        "body_html": r"""
<p>Imagine \(A\) as a transformation of the plane. Most vectors get rotated as well as stretched. But along an <strong>eigendirection</strong>, vectors only stretch.</p>
<p>Concretely: an eigenline is a line through the origin that \(A\) maps to itself.</p>
<ul>
<li>If \(\lambda &gt; 1\): vectors on the eigenline stretch outward.</li>
<li>If \(0 &lt; \lambda &lt; 1\): they shrink toward the origin.</li>
<li>If \(\lambda &lt; 0\): they flip across the origin.</li>
<li>If \(\lambda = 0\): the eigenline is collapsed to the origin (\(\vec{v}\) is in the null space).</li>
</ul>
<p>The set of all vectors with eigenvalue \(\lambda\) (including \(\vec{0}\)) forms the <strong>eigenspace</strong> \(E_\lambda\) — a subspace.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"If \(\lambda = -1\), what does the matrix do to its eigenvectors?",
             "options": ["scales by 1", "rotates 90°", "flips them across origin", "sends them to zero"], "correctIndex": 2},
            {"type": "true-false", "question": "An eigenline is a line through the origin that A maps to itself.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"If \(\lambda = 0\), the eigenvectors lie in the ___ space.", "answer": "null"},
            {"type": "multiple-choice", "question": "An eigenspace is:",
             "options": ["just a vector", "a single line", "a subspace", "always 2-dimensional"], "correctIndex": 2},
            {"type": "true-false", "question": "Two eigenvectors for the same eigenvalue can be added to give another eigenvector.", "correctAnswer": True}
        ]
    },
    {
        "title": "The Characteristic Polynomial",
        "body_html": r"""
<p>To find eigenvalues, rearrange \(A\vec{v} = \lambda\vec{v}\) as \((A - \lambda I)\vec{v} = \vec{0}\). For a nonzero \(\vec{v}\) to satisfy this, \(A - \lambda I\) must be singular:</p>
<div class="math-block">$$\det(A - \lambda I) = 0$$</div>
<p>This equation is a polynomial in \(\lambda\) called the <strong>characteristic polynomial</strong>. Its roots are the eigenvalues.</p>
<p><strong>Example.</strong> For \(A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}\):</p>
<div class="math-block">$$\det(A - \lambda I) = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10$$</div>
<p>Factoring: \((\lambda-5)(\lambda-2) = 0\). Eigenvalues: \(\lambda = 5, 2\).</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"Eigenvalues are the roots of \(\det(A - \lambda I) =\) ___.", "answer": "0"},
            {"type": "multiple-choice", "question": r"For \(A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}\), the eigenvalues are:",
             "options": ["1, 6", "2, 5", "3, 4", "0, 7"], "correctIndex": 1},
            {"type": "true-false", "question": r"For an \(n \times n\) matrix, the characteristic polynomial has degree \(n\).", "correctAnswer": True},
            {"type": "fill-blank", "question": r"For \(A = I_2\), the characteristic polynomial is \((1-\lambda)^?\). Fill: ___.", "answer": "2"},
            {"type": "true-false", "question": "The characteristic polynomial doesn't always factor over the reals.", "correctAnswer": True}
        ]
    },
    {
        "title": "Finding Eigenvalues of a 2×2",
        "body_html": r"""
<p>For \(A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}\), the characteristic polynomial expands to:</p>
<div class="math-block">$$\lambda^2 - (a+d)\lambda + (ad - bc) = 0$$</div>
<p>Notice: the coefficient of \(\lambda\) is the <strong>trace</strong> (sum of diagonal entries) with a sign flip, and the constant is the <strong>determinant</strong>.</p>
<div class="math-block">$$\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$$</div>
<p>Apply the quadratic formula. <strong>Example.</strong> \(A = \begin{bmatrix} 5 & 4 \\ 1 & 2 \end{bmatrix}\). \(\text{tr} = 7\), \(\det = 6\). Solve \(\lambda^2 - 7\lambda + 6 = 0\): \(\lambda = 1, 6\).</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"For \(\begin{bmatrix} 5 & 4 \\ 1 & 2 \end{bmatrix}\), eigenvalues:",
             "options": ["1, 6", "3, 4", "2, 5", "-1, -6"], "correctIndex": 0},
            {"type": "fill-blank", "question": r"For \(\begin{bmatrix} 3 & 0 \\ 0 & 7 \end{bmatrix}\), the larger eigenvalue is ___.", "answer": "7"},
            {"type": "true-false", "question": r"\(\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0\) gives the eigenvalues of a 2×2.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\) has eigenvalues:",
             "options": ["1, -1", "0, 0", "i, -i", "real but unequal"], "correctIndex": 2},
            {"type": "fill-blank", "question": r"The trace of \(\begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}\) is ___.", "answer": "7"}
        ]
    },
    {
        "title": "Finding Eigenvectors",
        "body_html": r"""
<p>Once you have an eigenvalue \(\lambda\), find an eigenvector by solving \((A - \lambda I)\vec{v} = \vec{0}\) — that is, find the null space of \(A - \lambda I\).</p>
<p><strong>Example.</strong> Take \(A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}\) with \(\lambda = 5\):</p>
<div class="math-block">$$A - 5I = \begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix}$$</div>
<p>Reading off: \(-v_1 + v_2 = 0\) means \(v_2 = v_1\). So eigenvectors are scalar multiples of \(\begin{bmatrix} 1 \\ 1 \end{bmatrix}\).</p>
<p>For \(\lambda = 2\): \(A - 2I = \begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix}\), giving \(2v_1 + v_2 = 0\), so eigenvector \(\begin{bmatrix} 1 \\ -2 \end{bmatrix}\).</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"To find eigenvectors, solve \((A - \lambda I)\vec{v} =\) ___.", "answer": "0"},
            {"type": "multiple-choice", "question": r"For \(A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}\), an eigenvector for \(\lambda = 3\) is:",
             "options": [r"\((1,0)\)", r"\((0,1)\)", r"\((1,1)\)", r"\((1,-1)\)"], "correctIndex": 1},
            {"type": "true-false", "question": "Any nonzero scalar multiple of an eigenvector is also an eigenvector with the same eigenvalue.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"Eigenvectors are found in the ___ of \(A - \lambda I\).",
             "options": ["image", "null space", "row space", "diagonal"], "correctIndex": 1},
            {"type": "true-false", "question": "An eigenvalue may have more than one independent eigenvector.", "correctAnswer": True}
        ]
    },
    {
        "title": "Eigenvalues of Triangular Matrices",
        "body_html": r"""
<p>For an upper-triangular (or lower-triangular) matrix, the eigenvalues are simply the <strong>diagonal entries</strong>:</p>
<div class="math-block">$$A = \begin{bmatrix} 3 & 1 & 5 \\ 0 & 2 & 7 \\ 0 & 0 & 4 \end{bmatrix} \implies \lambda = 3, 2, 4$$</div>
<p>Why? \(\det(A - \lambda I)\) is the product of the diagonal entries of the triangular matrix \(A - \lambda I\):</p>
<div class="math-block">$$\det(A - \lambda I) = (a_{11}-\lambda)(a_{22}-\lambda)\cdots(a_{nn}-\lambda)$$</div>
<p>Setting this to zero forces \(\lambda = a_{ii}\) for some \(i\). No factoring required.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"Eigenvalues of \(\begin{bmatrix} 5 & 7 \\ 0 & 2 \end{bmatrix}\):",
             "options": ["5, 7", "5, 2", "7, 2", "0, 5"], "correctIndex": 1},
            {"type": "true-false", "question": "For triangular matrices, eigenvalues are the diagonal entries.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"Eigenvalues of \(\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{bmatrix}\): the smallest is ___.", "answer": "1"},
            {"type": "true-false", "question": "Diagonal matrices are a special case of triangular.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "The off-diagonal entries of a triangular matrix:",
             "options": ["are all zero", "all equal the eigenvalues", "don't affect the eigenvalues", "double the eigenvalues"], "correctIndex": 2}
        ]
    },
    {
        "title": "Eigenvalues of Diagonal Matrices",
        "body_html": r"""
<p>Diagonal matrices are the simplest possible case. For \(D = \text{diag}(d_1, d_2, \ldots, d_n)\), the eigenvalues are the diagonal entries themselves, and the standard basis vectors are eigenvectors:</p>
<div class="math-block">$$D \vec{e}_i = d_i \vec{e}_i$$</div>
<p>That's the whole point of diagonalization (next unit): if we can find a basis in which \(A\) becomes diagonal, then computing powers \(A^k\), exponentials \(e^A\), and solving systems become trivial.</p>
<p><strong>Example.</strong> If \(D = \text{diag}(2, 3)\), then \(D^{10} = \text{diag}(2^{10}, 3^{10}) = \text{diag}(1024, 59049)\).</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"Eigenvalues of \(\text{diag}(7, 4, -1)\): the negative one is ___.", "answer": "-1"},
            {"type": "multiple-choice", "question": r"\(\text{diag}(2,3)^{10}\) equals:",
             "options": [r"\(\text{diag}(20, 30)\)", r"\(\text{diag}(2^{10}, 3^{10})\)", r"\(\text{diag}(2,3)\)", r"\(\text{diag}(10\cdot 2, 10 \cdot 3)\)"], "correctIndex": 1},
            {"type": "true-false", "question": "Standard basis vectors are eigenvectors of any diagonal matrix.", "correctAnswer": True},
            {"type": "true-false", "question": "Multiplying diagonal matrices is just multiplying entries.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"If \(D = \text{diag}(0, 2)\), \(\det(D) =\) ___.", "answer": "0"}
        ]
    },
    {
        "title": "Trace = Sum of Eigenvalues",
        "body_html": r"""
<p>The <strong>trace</strong> of a square matrix is the sum of its diagonal entries: \(\text{tr}(A) = \sum_i a_{ii}\).</p>
<p>A beautiful identity: <strong>the trace equals the sum of the eigenvalues</strong> (counted with algebraic multiplicity, even complex ones).</p>
<div class="math-block">$$\text{tr}(A) = \sum_{i=1}^n \lambda_i$$</div>
<p>This gives a fast sanity check on eigenvalue computations: just add them up and compare to the trace.</p>
<p><strong>Example.</strong> For \(A\) with eigenvalues \(2\) and \(5\): trace must be \(7\). For \(A = \begin{bmatrix} 5 & 4 \\ 1 & 2 \end{bmatrix}\), trace is \(7\). ✓</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\text{tr} \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix} =\) ___.", "answer": "7"},
            {"type": "true-false", "question": "Trace equals sum of eigenvalues.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"If a 3×3 matrix has eigenvalues 1, 2, 3, its trace is:",
             "options": ["6", "5", "0", "12"], "correctIndex": 0},
            {"type": "true-false", "question": r"\(\text{tr}(A) = \text{tr}(A^T)\).", "correctAnswer": True},
            {"type": "fill-blank", "question": r"If a 2×2 has eigenvalues 4 and \(-1\), its trace is ___.", "answer": "3"}
        ]
    },
    {
        "title": "Determinant = Product of Eigenvalues",
        "body_html": r"""
<p>Another beautiful identity:</p>
<div class="math-block">$$\det(A) = \prod_{i=1}^n \lambda_i$$</div>
<p>The determinant equals the <strong>product</strong> of the eigenvalues (with multiplicity, complex eigenvalues included).</p>
<p>This explains why <strong>\(\det(A) = 0\) iff \(A\) has a zero eigenvalue</strong> — equivalently, \(A\) is singular iff its kernel is nontrivial. The two facts say the same thing.</p>
<p><strong>Example.</strong> Eigenvalues \(2\) and \(5\) → determinant \(10\). For \(A = \begin{bmatrix} 5 & 4 \\ 1 & 2 \end{bmatrix}\), \(\det = 10 - 4 = 6\). Wait — eigenvalues for that were 1 and 6. ✓ (\(1 \cdot 6 = 6\)).</p>
""",
        "exercises": [
            {"type": "true-false", "question": "Determinant equals product of eigenvalues.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"If eigenvalues are \(3\) and \(4\), \(\det = \) ___.", "answer": "12"},
            {"type": "multiple-choice", "question": r"\(A\) is singular iff:",
             "options": ["all eigenvalues equal 1", "trace is zero", "at least one eigenvalue is zero", "all eigenvalues are nonzero"], "correctIndex": 2},
            {"type": "true-false", "question": "An invertible matrix has all nonzero eigenvalues.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"For a 3×3 with eigenvalues 1, 2, 3: \(\det =\) ___.", "answer": "6"}
        ]
    },
    {
        "title": "Algebraic vs Geometric Multiplicity",
        "body_html": r"""
<p>An eigenvalue \(\lambda\) can have two different "multiplicities":</p>
<ul>
<li><strong>Algebraic multiplicity</strong> = its multiplicity as a root of the characteristic polynomial.</li>
<li><strong>Geometric multiplicity</strong> = \(\dim(E_\lambda)\), the number of independent eigenvectors for \(\lambda\).</li>
</ul>
<p><strong>Inequality:</strong> geometric multiplicity \(\le\) algebraic multiplicity. When they're equal for every eigenvalue, the matrix is <strong>diagonalizable</strong>.</p>
<p><strong>Example: defective matrix.</strong> \(A = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}\) has \(\lambda = 2\) with algebraic multiplicity \(2\), but only one independent eigenvector \((1, 0)\) — geometric multiplicity is \(1\). It cannot be diagonalized.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"For \(\begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}\), the eigenvalue 2 has:",
             "options": ["algebraic mult 1, geometric mult 1", "algebraic mult 2, geometric mult 1", "algebraic mult 2, geometric mult 2", "algebraic mult 1, geometric mult 2"], "correctIndex": 1},
            {"type": "true-false", "question": "Geometric multiplicity is always at most algebraic multiplicity.", "correctAnswer": True},
            {"type": "true-false", "question": "When all eigenvalues' multiplicities match, A is diagonalizable.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"For \(2I_3\), \(\lambda=2\) has geometric multiplicity ___.", "answer": "3"},
            {"type": "multiple-choice", "question": "A defective matrix is one that:",
             "options": ["has det = 0", "is not diagonalizable", "has complex eigenvalues", "is symmetric"], "correctIndex": 1}
        ]
    },
    {
        "title": "Complex Eigenvalues",
        "body_html": r"""
<p>Real matrices can have <strong>complex eigenvalues</strong>. The classic example is rotation:</p>
<div class="math-block">$$R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$</div>
<p>For \(\theta \neq 0, \pi\), \(R_\theta\) has no real eigenvalues — there's no real direction it preserves. The complex eigenvalues are \(\lambda = e^{\pm i\theta} = \cos\theta \pm i\sin\theta\).</p>
<p>For real matrices, complex eigenvalues come in <strong>conjugate pairs</strong>: if \(\lambda = a + bi\) is an eigenvalue, so is \(\bar\lambda = a - bi\). Their eigenvectors are likewise conjugates of each other.</p>
""",
        "exercises": [
            {"type": "true-false", "question": "Real rotation matrices can have complex eigenvalues.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(R_{90°} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\) has eigenvalues:",
             "options": ["1, 1", "1, -1", "i, -i", "0, 0"], "correctIndex": 2},
            {"type": "fill-blank", "question": r"If \(2 + 3i\) is an eigenvalue of a real matrix, so is ___.", "answer": "2-3i"},
            {"type": "true-false", "question": "Complex eigenvalues of real matrices come in conjugate pairs.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(|\lambda|\) for \(\lambda = e^{i\theta}\) equals:",
             "options": ["0", "1", r"\(\theta\)", r"\(\sin\theta\)"], "correctIndex": 1}
        ]
    },
    {
        "title": "Eigenvalues of Symmetric Matrices",
        "body_html": r"""
<p>Symmetric matrices (\(A = A^T\)) have <strong>spectacular</strong> properties:</p>
<ul>
<li>All eigenvalues are <strong>real</strong> (no complex ones).</li>
<li>Eigenvectors for distinct eigenvalues are <strong>orthogonal</strong>.</li>
<li>The matrix is always <strong>diagonalizable</strong> by an orthonormal basis of eigenvectors.</li>
</ul>
<p>This is the <strong>Spectral Theorem</strong> (next unit). It explains why symmetric matrices are so important: they always admit a clean geometric decomposition.</p>
<p>Concretely: any symmetric \(A\) can be written \(A = Q\Lambda Q^T\) where \(Q\) is orthogonal and \(\Lambda\) is diagonal.</p>
""",
        "exercises": [
            {"type": "true-false", "question": "All eigenvalues of a real symmetric matrix are real.", "correctAnswer": True},
            {"type": "true-false", "question": "Eigenvectors of a symmetric matrix for distinct eigenvalues are always orthogonal.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "The spectral theorem says symmetric matrices are:",
             "options": ["singular", "always have eigenvalue 0", "diagonalizable by orthogonal Q", "anti-symmetric"], "correctIndex": 2},
            {"type": "fill-blank", "question": r"If \(A = A^T\), eigenvectors are real and ___.", "answer": "orthogonal"},
            {"type": "true-false", "question": "Skew-symmetric real matrices have purely imaginary eigenvalues.", "correctAnswer": True}
        ]
    },
    {
        "title": "Power Iteration",
        "body_html": r"""
<p>Many real-world matrices are too big to compute eigenvalues exactly. <strong>Power iteration</strong> is a simple iterative algorithm to find the dominant eigenpair (largest \(|\lambda|\)).</p>
<p><strong>Algorithm.</strong> Start with a random unit vector \(\vec{v}_0\). Repeat:</p>
<ol>
<li>\(\vec{v}_{k+1} = A\vec{v}_k\)</li>
<li>Normalize: \(\vec{v}_{k+1} \leftarrow \vec{v}_{k+1}/\|\vec{v}_{k+1}\|\)</li>
</ol>
<p>The sequence converges to the dominant eigenvector. Approximate eigenvalue: \(\lambda \approx \vec{v}_k^T A \vec{v}_k\) (the <strong>Rayleigh quotient</strong>).</p>
<p>Used in PageRank: it computes the dominant eigenvector of the web hyperlink matrix.</p>
""",
        "exercises": [
            {"type": "true-false", "question": "Power iteration finds the eigenvector with the largest absolute eigenvalue.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "The Rayleigh quotient is:",
             "options": [r"\(A\vec{v}\)", r"\(\vec{v}^T A\vec{v}\)", r"\(\det A\)", r"\(\|\vec{v}\|\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"After multiplying by \(A\), we ___ the resulting vector.", "answer": "normalize"},
            {"type": "true-false", "question": "PageRank uses power iteration on the web hyperlink matrix.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Power iteration converges fastest when:",
             "options": ["all eigenvalues are equal", "the dominant eigenvalue is much larger than the others", "A is symmetric", "A = I"], "correctIndex": 1}
        ]
    },
    {
        "title": "Practice: Eigen Computations",
        "body_html": r"""
<p>Try these in your head — they're standard 2×2 cases.</p>
<ol>
<li>\(A = \begin{bmatrix} 3 & 0 \\ 0 & 7 \end{bmatrix}\): eigenvalues \(3, 7\); eigenvectors \(\vec{e}_1, \vec{e}_2\).</li>
<li>\(A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\): trace \(4\), det \(3\) → \(\lambda^2 - 4\lambda + 3 = 0\) → \(\lambda = 1, 3\).</li>
<li>\(A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\): trace \(0\), det \(-1\) → \(\lambda^2 - 1 = 0\) → \(\lambda = \pm 1\).</li>
<li>\(A = \begin{bmatrix} 5 & 0 \\ 4 & 5 \end{bmatrix}\): triangular, both \(\lambda = 5\) (algebraic mult 2, geometric mult 1).</li>
</ol>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"Eigenvalues of \(\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\):",
             "options": ["1, 3", "0, 4", "2, 2", "i, -i"], "correctIndex": 0},
            {"type": "fill-blank", "question": r"Eigenvalues of \(\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\): the larger is ___.", "answer": "1"},
            {"type": "true-false", "question": r"\(\begin{bmatrix} 5 & 0 \\ 4 & 5 \end{bmatrix}\) is diagonalizable.", "correctAnswer": False},
            {"type": "multiple-choice", "question": r"For \(\begin{bmatrix} 3 & 0 \\ 0 & 7 \end{bmatrix}\) with \(\lambda = 7\), an eigenvector is:",
             "options": [r"\((1,0)\)", r"\((0,1)\)", r"\((1,1)\)", r"\((7,0)\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"\(\det \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} =\) ___.", "answer": "3"}
        ]
    },
    {
        "title": "Eigenvalues Checkpoint",
        "body_html": r"""
<p>Quick recap of Unit 23:</p>
<ul>
<li>Eigenvector: \(A\vec{v} = \lambda\vec{v}\), \(\vec{v} \neq \vec{0}\). Eigenline: a direction \(A\) preserves.</li>
<li>Find eigenvalues by solving \(\det(A - \lambda I) = 0\).</li>
<li>Find eigenvectors as \(\ker(A - \lambda I)\).</li>
<li>Triangular & diagonal matrices: eigenvalues sit on the diagonal.</li>
<li>Trace = sum of eigenvalues. Determinant = product of eigenvalues.</li>
<li>Algebraic mult ≥ geometric mult. Equal everywhere → diagonalizable.</li>
<li>Symmetric matrices: real eigenvalues, orthogonal eigenvectors, always diagonalizable.</li>
<li>Power iteration: numerical method for the dominant eigenpair.</li>
</ul>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"Eigenvalues of \(\begin{bmatrix} 4 & 0 \\ 0 & -3 \end{bmatrix}\):",
             "options": ["4, 0", "-3, 0", "4, -3", "0, 1"], "correctIndex": 2},
            {"type": "true-false", "question": "Symmetric real matrices always have real eigenvalues.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"If eigenvalues are 2 and 5, \(\text{tr} = \) ___.", "answer": "7"},
            {"type": "fill-blank", "question": r"If eigenvalues are 2 and 5, \(\det = \) ___.", "answer": "10"},
            {"type": "true-false", "question": "An invertible matrix can have a zero eigenvalue.", "correctAnswer": False},
            {"type": "multiple-choice", "question": "Power iteration converges to the:",
             "options": ["smallest eigenvalue", "dominant eigenvector", "trace", "determinant"], "correctIndex": 1},
            {"type": "true-false", "question": "Two eigenvectors with the same eigenvalue span an eigenspace.", "correctAnswer": True}
        ]
    },
]

if __name__ == "__main__":
    render_unit(UNIT_NUM, UNIT_NAME, START, LESSONS)
