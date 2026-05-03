#!/usr/bin/env python3
"""Unit 24 — Diagonalization & Spectral Theorem (lessons 346-360)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

UNIT_NUM = 24
UNIT_NAME = "Diagonalization & Spectral Theorem"
START = 346

LESSONS = [
    {
        "title": "What Is Diagonalization?",
        "body_html": r"""
<p>A square matrix \(A\) is <strong>diagonalizable</strong> if there exists an invertible \(P\) and a diagonal \(D\) such that</p>
<div class="math-block">$$A = P D P^{-1}$$</div>
<p>The columns of \(P\) are eigenvectors of \(A\), and the diagonal entries of \(D\) are the corresponding eigenvalues. Diagonalizing \(A\) means finding "the right basis" — the eigenbasis — in which \(A\) acts as a simple stretch along each axis.</p>
<p>Diagonalization simplifies almost every matrix computation: powers, exponentials, solving linear ODEs, computing functions of matrices.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"In \(A = PDP^{-1}\), the columns of \(P\) are eigenvectors of \(A\).", "correctAnswer": True},
            {"type": "fill-blank", "question": r"Diagonal entries of \(D\) are the ___ of \(A\).", "answer": "eigenvalues"},
            {"type": "true-false", "question": "Every square matrix is diagonalizable.", "correctAnswer": False},
            {"type": "multiple-choice", "question": "Diagonalization corresponds to:",
             "options": ["finding determinant", "finding the eigenbasis", "computing inverse", "transposing"], "correctIndex": 1},
            {"type": "true-false", "question": "Diagonalization simplifies computing matrix powers.", "correctAnswer": True}
        ]
    },
    {
        "title": "The Diagonalization Recipe",
        "body_html": r"""
<p><strong>Step 1.</strong> Find all eigenvalues of \(A\) by solving \(\det(A - \lambda I) = 0\).</p>
<p><strong>Step 2.</strong> For each eigenvalue, find a basis of its eigenspace (eigenvectors).</p>
<p><strong>Step 3.</strong> If the total number of independent eigenvectors equals \(n\), \(A\) is diagonalizable. Form \(P\) by stacking eigenvectors as columns; \(D\) by putting matching eigenvalues on the diagonal.</p>
<p><strong>Example.</strong> \(A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}\) has eigenvalues \(5, 2\) with eigenvectors \(\begin{bmatrix} 1 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ -2 \end{bmatrix}\). Then \(P = \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix}\), \(D = \begin{bmatrix} 5 & 0 \\ 0 & 2 \end{bmatrix}\).</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"To diagonalize, you need __ independent eigenvectors for an \(n \times n\) matrix.",
             "options": [r"\(n-1\)", r"\(n\)", r"\(2n\)", "any number"], "correctIndex": 1},
            {"type": "true-false", "question": "The order of eigenvectors as columns of P must match the order of eigenvalues on the diagonal of D.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"In the example, \(D = \text{diag}(5, ?\)). Fill: ___.", "answer": "2"},
            {"type": "true-false", "question": "Step 1 is always to compute the determinant of A.", "correctAnswer": False},
            {"type": "multiple-choice", "question": "Diagonalization fails when:",
             "options": ["A has complex eigenvalues only", "A is singular", "A has too few independent eigenvectors", "A is symmetric"], "correctIndex": 2}
        ]
    },
    {
        "title": "Why P D P⁻¹ Works",
        "body_html": r"""
<p>The identity \(A = PDP^{-1}\) is just a change of basis statement. Read it right-to-left:</p>
<ol>
<li>\(P^{-1}\) converts standard coordinates into eigenbasis coordinates.</li>
<li>\(D\) scales each axis (each by its eigenvalue).</li>
<li>\(P\) converts back to standard coordinates.</li>
</ol>
<p>So \(A\) acts as a scaling — but in the right basis. The eigenbasis is the "natural coordinate system" for \(A\).</p>
<p>Equivalent statement: \(P^{-1} A P = D\). Same equation, different emphasis.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"\(P^{-1} A P =\)",
             "options": [r"\(A\)", r"\(D\)", r"\(I\)", r"\(A^T\)"], "correctIndex": 1},
            {"type": "true-false", "question": r"\(A = PDP^{-1}\) means \(A\) is similar to \(D\).", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(P\) maps eigenbasis coords to ___ coords.", "answer": "standard"},
            {"type": "true-false", "question": "Similar matrices have the same eigenvalues.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"Reading \(A = PDP^{-1}\) right to left, the order of operations is:",
             "options": [r"\(P\), then \(D\), then \(P^{-1}\)", r"\(P^{-1}\), then \(D\), then \(P\)", r"\(D\), then \(P\), then \(P^{-1}\)", "all simultaneous"], "correctIndex": 1}
        ]
    },
    {
        "title": "Why Diagonal Is Easy: Powers",
        "body_html": r"""
<p>Computing \(D^k\) for a diagonal matrix is trivial: just raise each diagonal entry to the \(k\)th power.</p>
<div class="math-block">$$D = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix} \implies D^k = \begin{bmatrix} \lambda_1^k & 0 \\ 0 & \lambda_2^k \end{bmatrix}$$</div>
<p>If you want \(A^k\) for general \(A\), diagonalize:</p>
<div class="math-block">$$A^k = (PDP^{-1})^k = PD^kP^{-1}$$</div>
<p>The interior \(P^{-1}P\) factors all collapse, leaving just \(D^k\) sandwiched between \(P\) and \(P^{-1}\). Computing \(A^{1000}\) becomes as easy as computing \(D^{1000}\).</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\text{diag}(2,3)^{5}\) has top-left entry ___.", "answer": "32"},
            {"type": "multiple-choice", "question": r"\(A^k =\)",
             "options": [r"\(P^k D P^{-k}\)", r"\(PD^kP^{-1}\)", r"\(P^k D^k P^k\)", r"\(D P^k\)"], "correctIndex": 1},
            {"type": "true-false", "question": "Computing diagonal matrix powers is trivial.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(\text{diag}(1, -1)^{100}\) equals \(\text{diag}(?, ?)\). Fill the second: ___.", "answer": "1"},
            {"type": "true-false", "question": "Diagonalization helps even for non-symmetric matrices when they're diagonalizable.", "correctAnswer": True}
        ]
    },
    {
        "title": "Computing Aⁿ Quickly",
        "body_html": r"""
<p><strong>Example.</strong> Find \(A^{10}\) where \(A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}\).</p>
<p>From earlier: \(A = PDP^{-1}\) with \(P = \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix}\), \(D = \begin{bmatrix} 5 & 0 \\ 0 & 2 \end{bmatrix}\). Then</p>
<div class="math-block">$$A^{10} = P \begin{bmatrix} 5^{10} & 0 \\ 0 & 2^{10} \end{bmatrix} P^{-1}$$</div>
<p>This avoids actually multiplying matrices ten times. The dominant eigenvalue \(\lambda = 5\) controls long-term behavior: as \(k \to \infty\), \(A^k\) is approximately a rank-1 matrix in the direction of the dominant eigenvector.</p>
<p>This is exactly how Fibonacci numbers grow: their recurrence matrix has eigenvalues \(\varphi\) (golden ratio) and \(1-\varphi\); the dominant one wins.</p>
""",
        "exercises": [
            {"type": "true-false", "question": "The dominant eigenvalue controls long-term behavior of A^k.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "For Fibonacci, the dominant eigenvalue is:",
             "options": ["1", r"\(\sqrt 2\)", r"\(\varphi\) (golden ratio)", "2"], "correctIndex": 2},
            {"type": "fill-blank", "question": r"For \(A = \text{diag}(2,3)\), \(A^{10}\) bottom-right entry is \(3^{?}\). Fill: ___.", "answer": "10"},
            {"type": "true-false", "question": "Computing A^k via diagonalization is generally faster than direct multiplication.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"As \(k \to \infty\), \(A^k\) (with distinct eigenvalues) is dominated by:",
             "options": ["the smallest eigenvalue", "the largest |λ| eigenvalue", "the trace", "the determinant"], "correctIndex": 1}
        ]
    },
    {
        "title": "The Matrix Exponential",
        "body_html": r"""
<p>The matrix exponential, defined by the series</p>
<div class="math-block">$$e^A = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots$$</div>
<p>is fundamental in solving linear ODEs: the solution to \(\frac{d\vec{x}}{dt} = A\vec{x}\) with \(\vec{x}(0) = \vec{x}_0\) is \(\vec{x}(t) = e^{At}\vec{x}_0\).</p>
<p>For diagonalizable \(A = PDP^{-1}\):</p>
<div class="math-block">$$e^A = P\,e^D\,P^{-1}, \quad e^D = \text{diag}(e^{\lambda_1}, \ldots, e^{\lambda_n})$$</div>
<p>So computing \(e^A\) reduces to exponentiating real numbers along the diagonal.</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(e^{\text{diag}(0,1)}\) equals \(\text{diag}(?, e)\). Fill: ___.", "answer": "1"},
            {"type": "multiple-choice", "question": r"\(\frac{d\vec{x}}{dt} = A\vec{x}\), \(\vec{x}(0) = \vec{x}_0\). Solution:",
             "options": [r"\(A\vec{x}_0\)", r"\(e^{At}\vec{x}_0\)", r"\(t \vec{x}_0\)", r"\(A^t\vec{x}_0\)"], "correctIndex": 1},
            {"type": "true-false", "question": r"For diagonal \(D\), \(e^D\) just exponentiates the diagonal entries.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(e^0 = ?\) (the matrix). Fill: ___.", "answer": "I"},
            {"type": "true-false", "question": "Matrix exponentials are useful for solving linear ODE systems.", "correctAnswer": True}
        ]
    },
    {
        "title": "When Is a Matrix Diagonalizable?",
        "body_html": r"""
<p>An \(n \times n\) matrix \(A\) is diagonalizable iff it has \(n\) linearly independent eigenvectors. This is equivalent to:</p>
<ul>
<li>The geometric multiplicity equals the algebraic multiplicity for every eigenvalue, OR</li>
<li>\(A\) has \(n\) distinct eigenvalues (sufficient but not necessary), OR</li>
<li>\(A\) is symmetric (with real entries), OR more generally, \(A\) is normal: \(A^* A = A A^*\).</li>
</ul>
<p>Most matrices "in the wild" are diagonalizable. The non-diagonalizable cases (called <strong>defective</strong>) are a measure-zero subset, but they do come up — particularly in differential equations with repeated eigenvalues.</p>
""",
        "exercises": [
            {"type": "true-false", "question": "Distinct eigenvalues imply diagonalizable.", "correctAnswer": True},
            {"type": "true-false", "question": "Repeated eigenvalues imply NOT diagonalizable.", "correctAnswer": False},
            {"type": "multiple-choice", "question": "Symmetric matrices are:",
             "options": ["never diagonalizable", "always diagonalizable", "diagonalizable iff invertible", "diagonalizable only over complex numbers"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"A matrix that's not diagonalizable is called ___.", "answer": "defective"},
            {"type": "multiple-choice", "question": "Normal matrices satisfy:",
             "options": [r"\(A^2 = I\)", r"\(A^*A = AA^*\)", r"\(\det A = 1\)", r"\(A = A^T\)"], "correctIndex": 1}
        ]
    },
    {
        "title": "Defective Matrices & Jordan Blocks",
        "body_html": r"""
<p>A <strong>defective</strong> matrix has fewer independent eigenvectors than its size. Classic example:</p>
<div class="math-block">$$J = \begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}$$</div>
<p>This has \(\lambda\) as a double eigenvalue but only one eigenvector \((1, 0)\). It cannot be diagonalized.</p>
<p>Defective matrices can still be brought to a near-diagonal <strong>Jordan canonical form</strong>: blocks of the above shape, each containing one eigenvalue. The Jordan form is the closest thing to diagonal you can get when diagonalization fails.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(\begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}\) is defective.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"The Jordan form is the closest thing to ___ when diagonalization fails.", "answer": "diagonal"},
            {"type": "true-false", "question": "Jordan blocks have eigenvalues on their diagonal.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Defective matrices are characterized by:",
             "options": ["complex eigenvalues", "geometric mult < algebraic mult", "trace zero", "always invertible"], "correctIndex": 1},
            {"type": "true-false", "question": "Most matrices encountered in practice are diagonalizable.", "correctAnswer": True}
        ]
    },
    {
        "title": "The Spectral Theorem",
        "body_html": r"""
<p>The <strong>Spectral Theorem</strong> for real symmetric matrices: if \(A = A^T\), then there exists an orthogonal matrix \(Q\) (with \(Q^T Q = I\)) and a diagonal matrix \(\Lambda\) such that</p>
<div class="math-block">$$A = Q \Lambda Q^T$$</div>
<p>This is the gold-standard decomposition. The columns of \(Q\) are an <strong>orthonormal basis</strong> of eigenvectors. The eigenvalues on the diagonal of \(\Lambda\) are real.</p>
<p>Why this matters: any quadratic form \(\vec{x}^T A \vec{x}\) can be diagonalized into \(\vec{y}^T \Lambda \vec{y} = \sum \lambda_i y_i^2\) just by rotating into the eigenbasis.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"For symmetric \(A\), \(A = Q\Lambda Q^T\) with orthogonal \(Q\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"In the spectral decomposition, \(Q^{-1} =\)",
             "options": [r"\(Q^T\)", r"\(Q^2\)", r"\(\Lambda\)", r"\(-Q\)"], "correctIndex": 0},
            {"type": "fill-blank", "question": r"The columns of \(Q\) form an orthonormal basis of ___.", "answer": "eigenvectors"},
            {"type": "true-false", "question": "Eigenvalues from the spectral theorem can be complex.", "correctAnswer": False},
            {"type": "true-false", "question": "Quadratic forms can always be diagonalized in an eigenbasis.", "correctAnswer": True}
        ]
    },
    {
        "title": "Orthogonal Diagonalization",
        "body_html": r"""
<p>"Orthogonally diagonalizable" means diagonalizable with an orthogonal \(P\) (so \(P^{-1} = P^T\)). The Spectral Theorem says:</p>
<div class="math-block">$$A \text{ is orthogonally diagonalizable} \iff A \text{ is symmetric}$$</div>
<p><strong>Recipe.</strong> Compute eigenvalues; find eigenvectors; if eigenvalues are distinct, the eigenvectors are automatically orthogonal — just normalize. If you have a repeated eigenvalue, apply Gram-Schmidt to the eigenspace to produce an orthonormal basis there.</p>
<p><strong>Example.</strong> \(A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\). Eigenvalues \(\lambda = 1, 3\). Eigenvectors: \((1,-1)/\sqrt{2}\), \((1,1)/\sqrt{2}\) — already orthonormal.</p>
""",
        "exercises": [
            {"type": "true-false", "question": "Orthogonal diagonalizability is exactly symmetry (for real matrices).", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"For symmetric \(A\), eigenvectors of distinct eigenvalues are:",
             "options": ["parallel", "orthogonal", "always equal", "complex"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"For an orthogonal \(P\), \(P^{-1} =\) ___.", "answer": "P^T"},
            {"type": "true-false", "question": "Repeated eigenvalues of a symmetric matrix may need Gram-Schmidt.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"If \(A = Q\Lambda Q^T\) and \(Q\) is orthogonal, the columns of \(Q\) are:",
             "options": ["any basis", "an orthonormal basis of eigenvectors", "the rows of A", "the columns of A"], "correctIndex": 1}
        ]
    },
    {
        "title": "Quadratic Forms",
        "body_html": r"""
<p>A <strong>quadratic form</strong> is a homogeneous polynomial of degree 2 in several variables, written compactly as \(Q(\vec{x}) = \vec{x}^T A \vec{x}\) for a symmetric matrix \(A\).</p>
<div class="math-block">$$Q(x,y) = ax^2 + 2bxy + cy^2 = \begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} a & b \\ b & c \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$</div>
<p>By the spectral theorem, you can rotate coordinates so that \(Q\) becomes a sum of squares with eigenvalue weights:</p>
<div class="math-block">$$Q(\vec{y}) = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots$$</div>
<p>The signs of the eigenvalues classify the shape: positive eigenvalues → bowl, negative → upside-down bowl, mixed → saddle.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"\(x^2 + 2xy + y^2 = (x+y)^2\) corresponds to \(A=\):",
             "options": [r"\(\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\)", r"\(\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\)", r"\(\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\)", r"\(\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}\)"], "correctIndex": 1},
            {"type": "true-false", "question": "Quadratic forms always correspond to symmetric matrices.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(Q(\vec{x}) = \vec{x}^T A \vec{x}\): in the eigenbasis, \(Q = \sum_i \lambda_i\) ___.", "answer": "y_i^2"},
            {"type": "multiple-choice", "question": "If all eigenvalues are positive, the quadratic form is:",
             "options": ["a saddle", "a bowl (positive definite)", "negative definite", "indefinite"], "correctIndex": 1},
            {"type": "true-false", "question": "Mixed-sign eigenvalues create a saddle.", "correctAnswer": True}
        ]
    },
    {
        "title": "Definite & Semidefinite Matrices",
        "body_html": r"""
<p>A symmetric matrix \(A\) is classified by the signs of its eigenvalues:</p>
<ul>
<li><strong>Positive definite:</strong> all \(\lambda_i &gt; 0\). \(\vec{x}^T A \vec{x} &gt; 0\) for all nonzero \(\vec{x}\).</li>
<li><strong>Positive semidefinite:</strong> all \(\lambda_i \ge 0\). \(\vec{x}^T A \vec{x} \ge 0\).</li>
<li><strong>Negative definite / semidefinite:</strong> mirror image (all \(\lambda &lt; 0\) or \(\le 0\)).</li>
<li><strong>Indefinite:</strong> at least one positive and one negative eigenvalue.</li>
</ul>
<p>These classifications drive optimization: the Hessian of a function tells you whether a critical point is a min, max, or saddle.</p>
""",
        "exercises": [
            {"type": "true-false", "question": "A positive definite matrix has all positive eigenvalues.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "If a Hessian is indefinite at a critical point, the point is a:",
             "options": ["minimum", "maximum", "saddle", "inflection"], "correctIndex": 2},
            {"type": "fill-blank", "question": r"For PSD \(A\), \(\vec{x}^T A \vec{x} \ge\) ___.", "answer": "0"},
            {"type": "true-false", "question": "The identity matrix is positive definite.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\) is:",
             "options": ["positive definite", "negative definite", "indefinite", "PSD"], "correctIndex": 2}
        ]
    },
    {
        "title": "Spectral Decomposition Form",
        "body_html": r"""
<p>The spectral theorem can be rewritten as a <strong>sum of rank-1 outer products</strong>:</p>
<div class="math-block">$$A = \sum_{i=1}^n \lambda_i \vec{q}_i \vec{q}_i^T$$</div>
<p>where the \(\vec{q}_i\) are orthonormal eigenvectors. Each term \(\lambda_i \vec{q}_i \vec{q}_i^T\) is a rank-1 projection scaled by \(\lambda_i\).</p>
<p>This view is powerful: applying \(A\) to \(\vec{x}\) decomposes as</p>
<div class="math-block">$$A\vec{x} = \sum_i \lambda_i (\vec{q}_i^T \vec{x}) \vec{q}_i$$</div>
<p>"Project onto each eigenaxis, scale by its eigenvalue, sum." Truncating this sum to the largest eigenvalues gives a low-rank approximation — the foundation of PCA.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": "Spectral decomposition writes A as a sum of:",
             "options": ["determinants", "rank-1 outer products", "row vectors", "scalars"], "correctIndex": 1},
            {"type": "true-false", "question": r"\(\vec{q}_i \vec{q}_i^T\) is a projection onto the line spanned by \(\vec{q}_i\).", "correctAnswer": True},
            {"type": "fill-blank", "question": r"Truncating spectral decomposition gives a ___ approximation.", "answer": "low-rank"},
            {"type": "true-false", "question": "PCA is built on spectral decomposition of the covariance matrix.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"In the spectral form \(A = \sum \lambda_i \vec{q}_i \vec{q}_i^T\), the \(\vec{q}_i\) are:",
             "options": ["arbitrary", "orthonormal eigenvectors", "rows of A", "columns of A"], "correctIndex": 1}
        ]
    },
    {
        "title": "Practice: Diagonalize",
        "body_html": r"""
<p>Diagonalize \(A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\).</p>
<p><strong>Step 1.</strong> Trace \(= 4\), det \(= 3\). \(\lambda^2 - 4\lambda + 3 = 0\). Eigenvalues: \(\lambda = 1, 3\).</p>
<p><strong>Step 2.</strong> For \(\lambda = 1\): \((A - I) = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\). Eigenvector: \((1, -1)\). For \(\lambda = 3\): \((A - 3I) = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}\). Eigenvector: \((1, 1)\).</p>
<p><strong>Step 3.</strong> \(P = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}\), \(D = \begin{bmatrix} 1 & 0 \\ 0 & 3 \end{bmatrix}\), and \(A = PDP^{-1}\).</p>
<p><strong>Bonus.</strong> Notice the eigenvectors are orthogonal (since \(A\) is symmetric). Normalize them to get the orthogonal version.</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"Eigenvalues of \(\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\): the smaller is ___.", "answer": "1"},
            {"type": "multiple-choice", "question": r"An eigenvector for \(\lambda = 3\) of the matrix above:",
             "options": [r"\((1,1)\)", r"\((1,-1)\)", r"\((2,1)\)", r"\((0,1)\)"], "correctIndex": 0},
            {"type": "true-false", "question": "Eigenvectors of a symmetric matrix for distinct eigenvalues are orthogonal.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(\det \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} =\) ___.", "answer": "3"},
            {"type": "multiple-choice", "question": "When you swap eigenvalue order in D, you must also:",
             "options": ["transpose A", "swap the corresponding eigenvector columns in P", "negate D", "do nothing"], "correctIndex": 1}
        ]
    },
    {
        "title": "Diagonalization Checkpoint",
        "body_html": r"""
<p>Quick recap of Unit 24:</p>
<ul>
<li>\(A = PDP^{-1}\): \(P\) holds eigenvectors, \(D\) holds eigenvalues.</li>
<li>Diagonalizable iff \(n\) independent eigenvectors. Distinct eigenvalues guarantee this.</li>
<li>Powers, exponentials, ODEs all simplify in the eigenbasis.</li>
<li>Symmetric \(\implies\) orthogonally diagonalizable: \(A = Q\Lambda Q^T\) (Spectral Theorem).</li>
<li>Spectral decomposition: \(A = \sum_i \lambda_i \vec{q}_i \vec{q}_i^T\).</li>
<li>Quadratic forms classified by eigenvalue signs: positive/negative definite, semidefinite, or indefinite.</li>
</ul>
""",
        "exercises": [
            {"type": "true-false", "question": "Symmetric matrices are always diagonalizable.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(A^k\) (diagonalizable) equals:",
             "options": [r"\(P^k D^k\)", r"\(PD^kP^{-1}\)", r"\(D^k\)", r"\(A^kI\)"], "correctIndex": 1},
            {"type": "true-false", "question": "Defective matrices can still be Jordan-decomposed.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"For positive definite \(A\), all eigenvalues are ___.", "answer": "positive"},
            {"type": "multiple-choice", "question": "Spectral decomposition expresses A as:",
             "options": ["sum of rank-1 outer products", "product of triangular matrices", "an integral", "a Taylor series"], "correctIndex": 0},
            {"type": "true-false", "question": "Indefinite matrices have eigenvalues of mixed signs.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"For an orthogonal \(Q\), \(Q^TQ =\) ___.", "answer": "I"}
        ]
    },
]

if __name__ == "__main__":
    render_unit(UNIT_NUM, UNIT_NAME, START, LESSONS)
