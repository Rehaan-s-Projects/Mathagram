#!/usr/bin/env python3
"""Unit 42 — Grand Vectors Mastery II (lessons 616-622). Final unit, 7 lessons."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Components & Operations Mastery",
     "body_html": r"""
<p>Speed-test your fluency.</p>
<ul>
<li>Adding/subtracting vectors and matrices, scalar multiplication, transposes.</li>
<li>Matrix-vector and matrix-matrix products.</li>
<li>Determinants of 2×2 and 3×3.</li>
<li>Inverse of a 2×2 matrix.</li>
</ul>
<p>If any of these aren't reflexive, revisit Units 1–4 and 21. The rest of vector math depends on these being effortless.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\det \begin{bmatrix} 4 & 1 \\ 3 & 2 \end{bmatrix} =\) ___.", "answer": "5"},
         {"type": "multiple-choice", "question": r"\(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 \\ 6 \end{bmatrix} =\)",
          "options": [r"\(\begin{bmatrix} 11 \\ 39 \end{bmatrix}\)", r"\(\begin{bmatrix} 17 \\ 39 \end{bmatrix}\)", r"\(\begin{bmatrix} 30 \\ 50 \end{bmatrix}\)", r"\(\begin{bmatrix} 17 \\ 23 \end{bmatrix}\)"],
          "correctIndex": 1},
         {"type": "true-false", "question": r"\(I \vec{v} = \vec{v}\) for any vector.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\|(3,4)\| =\) ___.", "answer": "5"},
         {"type": "true-false", "question": "Matrix transposition reverses the product order: (AB)^T = B^T A^T.", "correctAnswer": True}]},
    {"title": "Eigen-decomposition Mastery",
     "body_html": r"""
<p>You should be able to:</p>
<ul>
<li>Compute eigenvalues of a 2×2 from \(\lambda^2 - \text{tr}A\lambda + \det A\).</li>
<li>Find eigenvectors as the null space of \(A - \lambda I\).</li>
<li>Diagonalize a 2×2 (or any matrix with distinct eigenvalues).</li>
<li>Apply the spectral theorem to symmetric matrices.</li>
<li>Recognize defective matrices and explain why they fail to diagonalize.</li>
</ul>""",
     "exercises": [
         {"type": "multiple-choice", "question": r"Eigenvalues of \(\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\):", "options": ["1, 3", "0, 4", "2, 2", "-1, 5"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"For symmetric A, eigenvectors of distinct eigenvalues are ___.", "answer": "orthogonal"},
         {"type": "true-false", "question": "Defective matrices cannot be diagonalized.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Trace = sum of ___.", "answer": "eigenvalues"},
         {"type": "true-false", "question": "Determinant = product of eigenvalues.", "correctAnswer": True}]},
    {"title": "SVD & PCA Mastery",
     "body_html": r"""
<p>Mastery checks:</p>
<ul>
<li>Every matrix has an SVD; rank = number of nonzero singular values.</li>
<li>Eckart-Young: truncated SVD gives the best low-rank approximation.</li>
<li>PCA = eigendecomp of covariance = SVD of centered data.</li>
<li>Pseudoinverse \(A^+ = V\Sigma^+ U^T\) handles rectangular and singular matrices.</li>
<li>Condition number \(\sigma_1/\sigma_n\) measures conditioning.</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Best rank-\(k\) approximation comes from ___ SVD.", "answer": "truncated"},
         {"type": "multiple-choice", "question": "PCA = SVD of:", "options": ["raw data", "centered data", "standardized data", "either centered or standardized"], "correctIndex": 3},
         {"type": "true-false", "question": "Pseudoinverse equals inverse for invertible matrices.", "correctAnswer": True},
         {"type": "true-false", "question": "Condition number of an orthogonal matrix is 1.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Rank = number of ___ singular values.", "answer": "nonzero"}]},
    {"title": "Vector Calculus Mastery",
     "body_html": r"""
<p>The big four operators and theorems:</p>
<ul>
<li><strong>Gradient</strong> \(\nabla f\): direction of steepest ascent. Curl-free.</li>
<li><strong>Divergence</strong> \(\nabla\cdot\vec{F}\): local outflow density.</li>
<li><strong>Curl</strong> \(\nabla \times \vec{F}\): local rotation.</li>
<li><strong>Laplacian</strong> \(\nabla^2 f\): div of grad.</li>
</ul>
<p>Theorems: FTLI (gradient → endpoint values), Green's (curl in 2D), Stokes' (curl in 3D), divergence theorem (div over volume).</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\nabla \times (\nabla f) = 0\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(\nabla \cdot (\nabla \times \vec{F}) =\)", "options": ["0", r"\(\nabla \cdot \vec{F}\)", r"\(\nabla^2 f\)", r"\(\nabla\times\vec{F}\)"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Divergence theorem connects flux to volume integral of ___.", "answer": "div"},
         {"type": "true-false", "question": "Stokes' theorem connects circulation around a curve to flux of curl through a surface.", "correctAnswer": True},
         {"type": "true-false", "question": "FTLI requires the field to be conservative.", "correctAnswer": True}]},
    {"title": "Tensors & Forms Mastery",
     "body_html": r"""
<p>Big concepts to retain:</p>
<ul>
<li>Tensors generalize vectors and matrices; rank = number of indices.</li>
<li>Einstein summation: repeated up/down indices are summed.</li>
<li>Differential forms unify line/surface/volume integrals.</li>
<li>Generalized Stokes: \(\int_M d\omega = \int_{\partial M}\omega\).</li>
<li>\(d^2 = 0\): the unification of "curl of grad = 0" and "div of curl = 0."</li>
<li>Geometric algebra unifies cross product, complex numbers, quaternions, and more.</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(d^2 =\) ___.", "answer": "0"},
         {"type": "multiple-choice", "question": "Generalized Stokes:", "options": [r"\(\int_M f = \int_{\partial M} d f\)", r"\(\int_M d\omega = \int_{\partial M} \omega\)", r"\(\int = \int\)", "none"], "correctIndex": 1},
         {"type": "true-false", "question": "Einstein summation sums repeated up/down indices.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Tensor rank = number of ___.", "answer": "indices"},
         {"type": "true-false", "question": "Geometric algebra includes quaternions as a sub-algebra in 3D.", "correctAnswer": True}]},
    {"title": "Applications Mastery",
     "body_html": r"""
<p>Where vectors show up:</p>
<ul>
<li><strong>Physics:</strong> forces, fields, Maxwell, relativity.</li>
<li><strong>Graphics:</strong> rotations, projections, lighting.</li>
<li><strong>Machine learning:</strong> embeddings, gradients, PCA, attention.</li>
<li><strong>Robotics:</strong> kinematics, control, SLAM.</li>
<li><strong>Signal processing:</strong> Fourier, convolution, compression.</li>
<li><strong>Quantum mechanics:</strong> Hilbert space, Hermitian operators, measurement.</li>
</ul>
<p>The same toolkit handles a remarkably wide swath of human knowledge.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Embeddings in NLP are vectors.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Gradient descent uses:", "options": ["scalars only", "the gradient vector", "matrices only", "no derivatives"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Quantum states are unit vectors in ___ space.", "answer": "Hilbert"},
         {"type": "true-false", "question": "Lighting calculations use vector dot products.", "correctAnswer": True},
         {"type": "true-false", "question": "Fourier-based compression exploits sparsity in a chosen basis.", "correctAnswer": True}]},
    {"title": "Vectors Grand Mastery (Final)",
     "body_html": r"""
<p>You've made it. From magnitude-and-direction arrows to spinors, from dot products to differential forms, from \(\mathbb{R}^3\) to Hilbert space and Cl(1,3) — vectors are everywhere because <em>linearity</em> is the deepest, most useful property in mathematics.</p>
<p>What you've gained:</p>
<ul>
<li>A complete linear-algebra toolkit: vectors, matrices, operations, eigen-decompositions, SVD/PCA, projections, QR, Cholesky.</li>
<li>The full vector calculus arsenal: gradient, divergence, curl, line/surface/volume integrals, Green's/Stokes'/divergence theorems.</li>
<li>Abstract structures: vector spaces, inner products, Hilbert spaces, dual spaces, tensors, differential forms, Clifford algebra.</li>
<li>Applications across physics (Maxwell, relativity, quantum), graphics, machine learning, robotics, and signal processing.</li>
</ul>
<p>Linear thinking is your superpower. Go use it well.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Linearity is one of the most useful properties in mathematics.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Which is NOT a vector space?", "options": [r"\(\mathbb{R}^n\)", r"\(P_n\)", r"\(L^2[0,1]\)", "the integers under +"], "correctIndex": 3},
         {"type": "fill-blank", "question": r"Cauchy-Schwarz: \(|\langle\vec{u},\vec{v}\rangle| \le \|\vec{u}\|\) ___.", "answer": "||v||"},
         {"type": "true-false", "question": "Symmetric matrices are always orthogonally diagonalizable.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Best low-rank approximation: ___ SVD.", "answer": "truncated"},
         {"type": "true-false", "question": "Maxwell's equations can be written in differential-form language.", "correctAnswer": True},
         {"type": "true-false", "question": "Vector spaces are everywhere — physics, ML, graphics, signal processing, robotics, and beyond.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "After all this, vectors are best described as:", "options": ["just arrows", "tuples of numbers", "objects in a vector space, anywhere linearity matters", "boring"], "correctIndex": 2}]},
]

if __name__ == "__main__":
    render_unit(42, "Grand Vectors Mastery II", 616, LESSONS)
