#!/usr/bin/env python3
"""Unit 21 — Matrices & Vector Operations (lessons 301-315)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

UNIT_NUM = 21
UNIT_NAME = "Matrices & Vector Operations"
START = 301

LESSONS = [
    {
        "title": "Matrix as a Grid of Numbers",
        "body_html": r"""
<p>A <strong>matrix</strong> is a rectangular grid of numbers arranged in rows and columns. We use matrices to package collections of vectors, encode linear transformations, and solve systems of equations.</p>
<div class="math-block">$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$$</div>
<p>This matrix has \(2\) rows and \(3\) columns. We say its <strong>shape</strong> (or <strong>size</strong>) is \(2 \times 3\) — always rows first, then columns.</p>
<p>A vector is just a special case of a matrix: a column vector in \(\mathbb{R}^n\) is an \(n \times 1\) matrix, and a row vector is \(1 \times n\).</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"What is the shape of \(\begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 2 & 3 \end{bmatrix}\)?",
             "options": [r"\(2 \times 3\)", r"\(3 \times 2\)", r"\(2 \times 2\)", r"\(3 \times 3\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"A column vector in \(\mathbb{R}^4\) is a matrix of shape \(4 \times\) ___.", "answer": "1"},
            {"type": "true-false", "question": "Matrix shape is always written as rows × columns.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"How many entries does a \(3 \times 4\) matrix have?",
             "options": ["7", "10", "12", "16"], "correctIndex": 2},
            {"type": "fill-blank", "question": r"A \(1 \times 5\) matrix is also called a ___ vector.", "answer": "row"}
        ]
    },
    {
        "title": "Matrix Notation & Indexing",
        "body_html": r"""
<p>Matrix entries are referenced by <strong>row, then column</strong>. The entry in row \(i\), column \(j\) of matrix \(A\) is written \(A_{ij}\) or \(a_{ij}\).</p>
<div class="math-block">$$A = \begin{bmatrix} 7 & -1 & 4 \\ 2 & 0 & 5 \end{bmatrix}, \qquad A_{12} = -1, \quad A_{23} = 5$$</div>
<p>Indices usually start at \(1\) in math notation; in code (Python, JavaScript) they start at \(0\). Be careful which world you're in.</p>
<p>We sometimes write \(A = [a_{ij}]\) to define a matrix entry-by-entry — for example, the matrix with \(a_{ij} = i + j\) has \(\begin{bmatrix} 2 & 3 \\ 3 & 4 \end{bmatrix}\) for a \(2 \times 2\).</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"In \(A = \begin{bmatrix} 7 & -1 & 4 \\ 2 & 0 & 5 \end{bmatrix}\), \(A_{21} =\) ___.", "answer": "2"},
            {"type": "multiple-choice", "question": r"In \(A = \begin{bmatrix} 7 & -1 & 4 \\ 2 & 0 & 5 \end{bmatrix}\), \(A_{13} =\)",
             "options": ["7", "-1", "4", "5"], "correctIndex": 2},
            {"type": "true-false", "question": r"\(A_{ij}\) means the entry in row \(j\), column \(i\).", "correctAnswer": False},
            {"type": "fill-blank", "question": r"If \(a_{ij} = i \cdot j\), then for a \(2 \times 2\) matrix \(a_{22} =\) ___.", "answer": "4"},
            {"type": "multiple-choice", "question": r"In a \(4 \times 5\) matrix, the entry \(A_{34}\) lies in row __ and column __.",
             "options": ["row 4, col 3", "row 3, col 4", "row 5, col 4", "row 3, col 5"], "correctIndex": 1}
        ]
    },
    {
        "title": "Square, Row, and Column Matrices",
        "body_html": r"""
<p>Matrices come in shapes that show up so often they have names:</p>
<ul>
<li><strong>Square matrix</strong>: same number of rows and columns (\(n \times n\)). These are special — only square matrices can be inverted, have eigenvalues, etc.</li>
<li><strong>Row matrix / row vector</strong>: \(1 \times n\). One row, many columns.</li>
<li><strong>Column matrix / column vector</strong>: \(m \times 1\). Many rows, one column.</li>
</ul>
<div class="math-block">$$\underbrace{\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}}_{\text{square}} \quad \underbrace{\begin{bmatrix} 1 & 2 & 3 \end{bmatrix}}_{\text{row}} \quad \underbrace{\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}}_{\text{column}}$$</div>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"\(\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}\) is a:",
             "options": ["row matrix", "column matrix", "square matrix", "none of the above"], "correctIndex": 2},
            {"type": "true-false", "question": "A column vector in 3D is a 3×1 matrix.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"A square matrix of order \(n\) has shape \(n \times\) ___.", "answer": "n"},
            {"type": "multiple-choice", "question": r"\(\begin{bmatrix} 4 & 5 & 6 \end{bmatrix}\) is a:",
             "options": ["row vector", "column vector", "square matrix", "scalar"], "correctIndex": 0},
            {"type": "true-false", "question": "Only square matrices can have an inverse.", "correctAnswer": True}
        ]
    },
    {
        "title": "Matrix Addition & Scalar Multiplication",
        "body_html": r"""
<p>To add two matrices, add corresponding entries. The two matrices must have the <strong>same shape</strong>:</p>
<div class="math-block">$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}$$</div>
<p><strong>Scalar multiplication</strong> multiplies every entry by the scalar:</p>
<div class="math-block">$$3 \cdot \begin{bmatrix} 1 & -2 \\ 0 & 4 \end{bmatrix} = \begin{bmatrix} 3 & -6 \\ 0 & 12 \end{bmatrix}$$</div>
<p>Matrix addition is commutative (\(A + B = B + A\)) and associative — just like vector addition, because matrices ARE just bundles of vectors stacked side-by-side.</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \begin{bmatrix} 2 & 3 \\ 4 & 5 \end{bmatrix}\) has top-right entry ___.", "answer": "3"},
            {"type": "multiple-choice", "question": r"\(2 \cdot \begin{bmatrix} 3 & -1 \\ 0 & 5 \end{bmatrix} =\)",
             "options": [r"\(\begin{bmatrix} 6 & -1 \\ 0 & 5 \end{bmatrix}\)", r"\(\begin{bmatrix} 6 & -2 \\ 0 & 10 \end{bmatrix}\)", r"\(\begin{bmatrix} 5 & 1 \\ 2 & 7 \end{bmatrix}\)", r"\(\begin{bmatrix} 3 & -1 \\ 0 & 5 \end{bmatrix}\)"],
             "correctIndex": 1},
            {"type": "true-false", "question": "You can add a 2×3 matrix and a 3×2 matrix.", "correctAnswer": False},
            {"type": "true-false", "question": r"Matrix addition is commutative: \(A+B = B+A\).", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(-1 \cdot \begin{bmatrix} 2 & 4 \end{bmatrix}\) has first entry ___.", "answer": "-2"}
        ]
    },
    {
        "title": "Matrix Times a Vector",
        "body_html": r"""
<p>Multiplying a matrix \(A\) by a column vector \(\vec{v}\) produces another vector. The rule: the entry in row \(i\) of \(A\vec{v}\) is the dot product of row \(i\) of \(A\) with \(\vec{v}\).</p>
<div class="math-block">$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 \\ 6 \end{bmatrix} = \begin{bmatrix} 1\cdot 5 + 2\cdot 6 \\ 3\cdot 5 + 4\cdot 6 \end{bmatrix} = \begin{bmatrix} 17 \\ 39 \end{bmatrix}$$</div>
<p><strong>Shape rule:</strong> an \(m \times n\) matrix times an \(n \times 1\) vector produces an \(m \times 1\) vector. The "inner" dimensions must match.</p>
<p>Another way to see it: \(A\vec{v}\) is a <strong>linear combination of the columns of \(A\)</strong>, with weights from \(\vec{v}\).</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"\(\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 7 \\ -3 \end{bmatrix} =\)",
             "options": [r"\(\begin{bmatrix} 0 \\ 0 \end{bmatrix}\)", r"\(\begin{bmatrix} 7 \\ -3 \end{bmatrix}\)", r"\(\begin{bmatrix} -3 \\ 7 \end{bmatrix}\)", r"\(\begin{bmatrix} 4 \\ 4 \end{bmatrix}\)"],
             "correctIndex": 1},
            {"type": "fill-blank", "question": r"\(\begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix}\) has top entry ___.", "answer": "4"},
            {"type": "true-false", "question": r"You can multiply a \(3 \times 2\) matrix by a \(2 \times 1\) vector.", "correctAnswer": True},
            {"type": "true-false", "question": r"You can multiply a \(2 \times 3\) matrix by a \(2 \times 1\) vector.", "correctAnswer": False},
            {"type": "multiple-choice", "question": r"The product \(A\vec{v}\) is a linear combination of the ___ of \(A\).",
             "options": ["rows", "columns", "diagonals", "transposes"], "correctIndex": 1}
        ]
    },
    {
        "title": "Geometric Meaning of \\(A\\vec{v}\\)",
        "body_html": r"""
<p>A matrix \(A\) acts as a <strong>function</strong> on vectors: feed in \(\vec{v}\), get out \(A\vec{v}\). Geometrically, \(A\) stretches, rotates, reflects, or shears \(\vec{v}\).</p>
<p>The columns of \(A\) tell you exactly where the standard basis vectors go:</p>
<div class="math-block">$$A = \begin{bmatrix} | & | \\ A\vec{e}_1 & A\vec{e}_2 \\ | & | \end{bmatrix}$$</div>
<p><strong>Example.</strong> The matrix \(R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\) sends \(\vec{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}\) to \(\begin{bmatrix} 0 \\ 1 \end{bmatrix}\) and \(\vec{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}\) to \(\begin{bmatrix} -1 \\ 0 \end{bmatrix}\). That's a \(90°\) counter-clockwise rotation.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"The first column of \(A\) tells you where ___ goes.",
             "options": [r"\(\vec{e}_1\)", r"\(\vec{e}_2\)", "the origin", "any vector"], "correctIndex": 0},
            {"type": "true-false", "question": r"\(\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\) rotates by 90° counter-clockwise.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(\begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \vec{v}\) scales \(\vec{v}\) by a factor of ___.", "answer": "2"},
            {"type": "multiple-choice", "question": r"What does \(\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\) do?",
             "options": ["Rotates 180°", "Reflects across the x-axis", "Reflects across the y-axis", "Identity"], "correctIndex": 1},
            {"type": "true-false", "question": r"Multiplying by \(\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\) leaves vectors unchanged.", "correctAnswer": True}
        ]
    },
    {
        "title": "Matrix Times a Matrix",
        "body_html": r"""
<p>The product \(AB\) is defined when the number of columns of \(A\) equals the number of rows of \(B\). The entry in row \(i\), column \(j\) of \(AB\) is the dot product of row \(i\) of \(A\) with column \(j\) of \(B\):</p>
<div class="math-block">$$(AB)_{ij} = \sum_k A_{ik} B_{kj}$$</div>
<p><strong>Example.</strong> \(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}\)</p>
<p><strong>Shape rule:</strong> \((m \times n)(n \times p) = (m \times p)\). Inner dims must match; the outer dims give the result.</p>
<p>Matrix multiplication is <strong>not commutative</strong>: in general \(AB \neq BA\).</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"What shape is the product of a \(3 \times 4\) and a \(4 \times 2\) matrix?",
             "options": [r"\(3 \times 2\)", r"\(4 \times 4\)", r"\(2 \times 3\)", "undefined"], "correctIndex": 0},
            {"type": "true-false", "question": r"In general, \(AB = BA\).", "correctAnswer": False},
            {"type": "fill-blank", "question": r"\(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\) has top-left entry ___.", "answer": "2"},
            {"type": "multiple-choice", "question": r"You can multiply a \(2 \times 3\) by a:",
             "options": [r"\(2 \times 3\)", r"\(3 \times \text{anything}\)", r"\(2 \times \text{anything}\)", "any matrix"], "correctIndex": 1},
            {"type": "true-false", "question": r"Matrix multiplication is associative: \((AB)C = A(BC)\).", "correctAnswer": True}
        ]
    },
    {
        "title": "The Identity Matrix",
        "body_html": r"""
<p>The <strong>identity matrix</strong> \(I_n\) is the \(n \times n\) matrix with \(1\)s on the diagonal and \(0\)s everywhere else:</p>
<div class="math-block">$$I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \qquad I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$</div>
<p>It plays the role of \(1\) in matrix multiplication: for any \(n \times n\) matrix \(A\),</p>
<div class="math-block">$$AI = IA = A$$</div>
<p>Its columns are the standard basis vectors \(\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n\). Geometrically, \(I\) is the "do nothing" transformation.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"Which is \(I_3\)?",
             "options": [r"\(\begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}\)", r"\(\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}\)", r"\(\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}\)", r"\(\begin{bmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{bmatrix}\)"],
             "correctIndex": 1},
            {"type": "true-false", "question": r"\(I A = A\) for any matrix \(A\) of compatible shape.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"\(I_5\) has ___ ones on its diagonal.", "answer": "5"},
            {"type": "multiple-choice", "question": "Geometrically, the identity matrix represents:",
             "options": ["a 90° rotation", "the do-nothing transform", "a reflection", "a projection"], "correctIndex": 1},
            {"type": "true-false", "question": r"The columns of \(I_n\) are the standard basis vectors.", "correctAnswer": True}
        ]
    },
    {
        "title": "Zero Matrix & Algebraic Properties",
        "body_html": r"""
<p>The <strong>zero matrix</strong> \(0\) (of any shape) has every entry equal to \(0\). It plays the role of \(0\) in matrix algebra:</p>
<ul>
<li>\(A + 0 = A\)</li>
<li>\(A + (-A) = 0\)</li>
<li>\(0 \cdot A = 0\)</li>
</ul>
<p>Combined with the identity, matrices satisfy most familiar algebraic laws — distributivity, associativity — except for one big difference: <strong>multiplication is not commutative</strong>.</p>
<div class="math-block">$$A(B+C) = AB + AC, \quad (A+B)C = AC + BC$$</div>
<p>Also: \(AB = 0\) does <em>not</em> imply \(A=0\) or \(B=0\). Two non-zero matrices can multiply to zero.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(A + 0 = A\) for any matrix \(A\).", "correctAnswer": True},
            {"type": "true-false", "question": r"If \(AB = 0\), at least one of \(A\) or \(B\) must be zero.", "correctAnswer": False},
            {"type": "multiple-choice", "question": "Matrix multiplication is:",
             "options": ["commutative", "anti-commutative", "associative but not commutative", "neither"], "correctIndex": 2},
            {"type": "fill-blank", "question": r"\(A(B+C) = AB +\) ___.", "answer": "AC"},
            {"type": "true-false", "question": r"\(0 \cdot A = 0\).", "correctAnswer": True}
        ]
    },
    {
        "title": "Matrix Transpose",
        "body_html": r"""
<p>The <strong>transpose</strong> \(A^T\) of a matrix \(A\) flips it across its main diagonal — rows become columns, columns become rows.</p>
<div class="math-block">$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}, \quad A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$</div>
<p>If \(A\) is \(m \times n\), then \(A^T\) is \(n \times m\). Entries: \((A^T)_{ij} = A_{ji}\).</p>
<p>Useful identities:</p>
<ul>
<li>\((A^T)^T = A\)</li>
<li>\((A + B)^T = A^T + B^T\)</li>
<li>\((AB)^T = B^T A^T\) — order reverses!</li>
</ul>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"If \(A\) is \(3 \times 5\), then \(A^T\) is:",
             "options": [r"\(3 \times 5\)", r"\(5 \times 3\)", r"\(5 \times 5\)", r"\(3 \times 3\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"\((A^T)^T =\) ___.", "answer": "A"},
            {"type": "true-false", "question": r"\((AB)^T = A^T B^T\).", "correctAnswer": False},
            {"type": "multiple-choice", "question": r"\((AB)^T =\)",
             "options": [r"\(A^T B^T\)", r"\(B^T A^T\)", r"\(A^T B\)", r"\(AB\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"If \(A_{12} = 7\), then \((A^T)_{21} =\) ___.", "answer": "7"}
        ]
    },
    {
        "title": "Symmetric Matrices",
        "body_html": r"""
<p>A square matrix \(A\) is <strong>symmetric</strong> if \(A^T = A\) — that is, it equals its own transpose. Equivalently, \(A_{ij} = A_{ji}\) for every \(i, j\).</p>
<div class="math-block">$$\begin{bmatrix} 2 & 5 & 1 \\ 5 & 3 & 7 \\ 1 & 7 & 4 \end{bmatrix} \quad \text{is symmetric.}$$</div>
<p>Symmetric matrices appear everywhere: covariance matrices in statistics, the Hessian in optimization, the metric tensor in geometry. They have remarkable properties (which we'll explore in later units): all real eigenvalues, orthogonal eigenvectors, and they're always diagonalizable.</p>
<p>An <strong>antisymmetric</strong> (or skew-symmetric) matrix satisfies \(A^T = -A\); its diagonal must be all zeros.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": "Which matrix is symmetric?",
             "options": [r"\(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\)", r"\(\begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix}\)", r"\(\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}\)", r"\(\begin{bmatrix} 2 & 3 \\ 4 & 2 \end{bmatrix}\)"],
             "correctIndex": 1},
            {"type": "true-false", "question": r"A symmetric matrix satisfies \(A_{ij} = A_{ji}\).", "correctAnswer": True},
            {"type": "true-false", "question": "Every square matrix is symmetric.", "correctAnswer": False},
            {"type": "fill-blank", "question": r"For a skew-symmetric matrix, the diagonal entries must all equal ___.", "answer": "0"},
            {"type": "multiple-choice", "question": "Which is NOT typically symmetric?",
             "options": ["covariance matrix", "metric tensor", "rotation matrix", "Hessian"], "correctIndex": 2}
        ]
    },
    {
        "title": "Inverse of a 2×2 Matrix",
        "body_html": r"""
<p>For a \(2 \times 2\) matrix \(A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}\), the inverse \(A^{-1}\) (when it exists) is given by</p>
<div class="math-block">$$A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$</div>
<p>The number \(ad-bc\) is the <strong>determinant</strong>. If it's zero, the matrix has no inverse — we call it <strong>singular</strong>.</p>
<p>The inverse satisfies \(A A^{-1} = A^{-1} A = I\). Geometrically, \(A^{-1}\) is the transformation that undoes \(A\).</p>
<p><strong>Example.</strong> \(A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}\), \(\det = 2-1=1\), so \(A^{-1} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}\).</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"\(\begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}^{-1} =\)",
             "options": [r"\(\begin{bmatrix} 1 & 0 \\ 0 & 0.5 \end{bmatrix}\)", r"\(\begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}\)", r"\(\begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}\)", r"\(\begin{bmatrix} -1 & 0 \\ 0 & -2 \end{bmatrix}\)"], "correctIndex": 0},
            {"type": "fill-blank", "question": r"For \(A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}\), \(\det A =\) ___.", "answer": "3"},
            {"type": "true-false", "question": "A matrix with determinant 0 has no inverse.", "correctAnswer": True},
            {"type": "true-false", "question": r"\(A A^{-1} = I\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"For \(A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}\), the inverse:",
             "options": ["is the identity", "doesn't exist (singular)", "equals \\(A^T\\)", "equals \\(2A\\)"], "correctIndex": 1}
        ]
    },
    {
        "title": "Determinant of a 2×2 Matrix",
        "body_html": r"""
<p>For \(A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}\), the <strong>determinant</strong> is</p>
<div class="math-block">$$\det A = ad - bc$$</div>
<p>Geometrically, \(|\det A|\) is the area of the parallelogram spanned by the columns of \(A\). The sign tells you whether the transformation preserves or flips orientation:</p>
<ul>
<li>\(\det A &gt; 0\): orientation-preserving</li>
<li>\(\det A &lt; 0\): orientation-flipping (reflection)</li>
<li>\(\det A = 0\): collapses 2D into a line or point — non-invertible</li>
</ul>
<p><strong>Example.</strong> \(\det \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix} = 3 \cdot 4 - 2 \cdot 1 = 10\).</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\det \begin{bmatrix} 5 & 2 \\ 3 & 1 \end{bmatrix} =\) ___.", "answer": "-1"},
            {"type": "multiple-choice", "question": r"\(\det \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} =\)",
             "options": ["10", "-2", "2", "-10"], "correctIndex": 1},
            {"type": "true-false", "question": "If the determinant is zero, the matrix is invertible.", "correctAnswer": False},
            {"type": "fill-blank", "question": r"\(\det I_2 =\) ___.", "answer": "1"},
            {"type": "multiple-choice", "question": r"Geometrically, \(|\det A|\) for a \(2 \times 2\) is the:",
             "options": ["length of column 1", "area of the parallelogram of columns", "trace", "sum of entries"], "correctIndex": 1}
        ]
    },
    {
        "title": "Determinant of a 3×3 Matrix",
        "body_html": r"""
<p>For a \(3 \times 3\) matrix, expand along the first row using <strong>cofactors</strong>:</p>
<div class="math-block">$$\det \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = a(ei-fh) - b(di-fg) + c(dh-eg)$$</div>
<p>Watch the alternating signs: \(+, -, +\). Each cofactor is the determinant of the \(2 \times 2\) you get by crossing out the row and column of the leading entry.</p>
<p>Geometrically, \(|\det A|\) for a \(3 \times 3\) is the <strong>volume of the parallelepiped</strong> spanned by the columns. Sign indicates orientation (right-handed vs left-handed).</p>
<p><strong>Example.</strong> \(\det \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix} = 1 \cdot 2 \cdot 3 = 6\). For diagonal matrices, just multiply the diagonal.</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\det \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{bmatrix} =\) ___.", "answer": "30"},
            {"type": "multiple-choice", "question": r"\(\det I_3 =\)",
             "options": ["0", "1", "3", "depends"], "correctIndex": 1},
            {"type": "true-false", "question": r"For a \(3 \times 3\), \(|\det A|\) equals the volume of the parallelepiped spanned by the columns.", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Cofactor expansion along the first row uses signs:",
             "options": [r"\(+, +, +\)", r"\(+, -, +\)", r"\(-, +, -\)", r"\(+, -, -\)"], "correctIndex": 1},
            {"type": "true-false", "question": "The determinant of a triangular matrix is the product of its diagonal entries.", "correctAnswer": True}
        ]
    },
    {
        "title": "Matrix Operations Checkpoint",
        "body_html": r"""
<p>Quick recap of Unit 21:</p>
<ul>
<li>A matrix is a grid of numbers, indexed as \(A_{ij}\) (row, column).</li>
<li>Add matrices entry-by-entry; multiply by scalars entry-by-entry.</li>
<li>\(A\vec{v}\): row \(i\) dotted with \(\vec{v}\). \(AB\): row \(i\) of \(A\) dotted with column \(j\) of \(B\).</li>
<li>Matrix multiplication is associative but <strong>not commutative</strong>.</li>
<li>The identity \(I\) does nothing; the inverse \(A^{-1}\) undoes \(A\) (if it exists).</li>
<li>Transpose flips rows and columns; \((AB)^T = B^T A^T\).</li>
<li>Determinant: \(2 \times 2\) → area; \(3 \times 3\) → volume; zero → singular.</li>
</ul>
<p>Time to test your skills before moving on to linear transformations.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"What shape is \(A^T\) if \(A\) is \(2 \times 7\)?",
             "options": [r"\(2 \times 7\)", r"\(7 \times 2\)", r"\(7 \times 7\)", r"\(2 \times 2\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"\(\det \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix} =\) ___.", "answer": "10"},
            {"type": "true-false", "question": r"\(AB\) and \(BA\) are always equal.", "correctAnswer": False},
            {"type": "true-false", "question": "A singular matrix is one with no inverse.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} =\)",
             "options": [r"\(\begin{bmatrix} 3 \\ 7 \end{bmatrix}\)", r"\(\begin{bmatrix} 1 \\ 1 \end{bmatrix}\)", r"\(\begin{bmatrix} 4 \\ 6 \end{bmatrix}\)", r"\(\begin{bmatrix} 2 \\ 5 \end{bmatrix}\)"], "correctIndex": 0},
            {"type": "fill-blank", "question": r"The identity matrix \(I_n\) has ___ ones on its diagonal.", "answer": "n"},
            {"type": "true-false", "question": "Symmetric matrices satisfy \\(A^T = A\\).", "correctAnswer": True}
        ]
    },
]

if __name__ == "__main__":
    render_unit(UNIT_NUM, UNIT_NAME, START, LESSONS)
