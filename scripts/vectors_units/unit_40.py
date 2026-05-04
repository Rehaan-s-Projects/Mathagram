#!/usr/bin/env python3
"""Unit 40 — Numerical Methods for Vectors (lessons 586-600)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Why Numerical Methods?",
     "body_html": r"""
<p>Real-world matrix problems can have millions of rows and columns: image data, neural network weights, simulation grids, social-graph connectivity. You can't solve these by hand.</p>
<p>Numerical linear algebra studies algorithms that:</p>
<ul>
<li>Run efficiently in time and memory.</li>
<li>Tolerate floating-point roundoff.</li>
<li>Exploit special structure (sparsity, symmetry, positive definiteness).</li>
</ul>
<p>The choice of algorithm matters as much as the math behind it.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Real linear algebra problems can have millions of unknowns.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Numerical methods care about:", "options": ["just correctness", "efficiency, stability, structure", "only memory", "only time"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Numerical methods must tolerate floating-point ___.", "answer": "roundoff"},
         {"type": "true-false", "question": "Sparsity often leads to dramatically faster algorithms.", "correctAnswer": True},
         {"type": "true-false", "question": "Algorithm choice doesn't matter — math is math.", "correctAnswer": False}]},
    {"title": "Floating-Point Arithmetic",
     "body_html": r"""
<p>Computers represent real numbers as IEEE 754 floating-point: a sign bit, exponent, and mantissa. Double precision has 52 mantissa bits — about 15–16 decimal digits.</p>
<p><strong>Roundoff:</strong> nearly every operation incurs an error of \(\sim 10^{-16}\). Errors compound — and a problem with high condition number can amplify them dramatically.</p>
<p><strong>Special values:</strong> Inf, -Inf, NaN. Catastrophic cancellation: subtracting nearly-equal numbers loses many significant digits.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Double-precision floats have about 15-16 decimal digits.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Catastrophic cancellation:", "options": ["adding small numbers", "subtracting near-equal numbers", "multiplying", "dividing"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Roundoff is on the order of \(10^{-?}\) for double precision.", "answer": "16"},
         {"type": "true-false", "question": "NaN means \"not a number.\"", "correctAnswer": True},
         {"type": "true-false", "question": "Roundoff errors always cancel out.", "correctAnswer": False}]},
    {"title": "Conditioning of Linear Systems",
     "body_html": r"""
<p>The <strong>condition number</strong> \(\kappa(A) = \sigma_1/\sigma_n\) (also \(\|A\|\|A^{-1}\|\)) tells you how much input errors get amplified in solving \(A\vec{x} = \vec{b}\).</p>
<p>Rule of thumb: lose \(\log_{10}\kappa\) digits of precision. \(\kappa = 10^8\) means about half your double-precision digits are gone. Above \(10^{16}\), the answer is meaningless on a standard machine.</p>
<p>Some problems are inherently ill-conditioned (Hilbert matrices, polynomial interpolation at unevenly-spaced points). Others can be reformulated to improve conditioning.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\kappa(A) = \sigma_1 /\) ___.", "answer": "sigma_n"},
         {"type": "multiple-choice", "question": "Condition number 10⁸ on doubles loses about:", "options": ["1 digit", "8 digits", "no digits", "all digits"], "correctIndex": 1},
         {"type": "true-false", "question": "Hilbert matrices are notoriously ill-conditioned.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Condition number of an orthogonal matrix is ___.", "answer": "1"},
         {"type": "true-false", "question": "Reformulating a problem can sometimes improve conditioning.", "correctAnswer": True}]},
    {"title": "Gaussian Elimination",
     "body_html": r"""
<p>Classical Gaussian elimination reduces \(A\) to upper triangular form via row operations, then back-substitutes. Cost: \(O(n^3)\) for an \(n \times n\) matrix.</p>
<p><strong>Pivoting</strong> swaps rows to put the largest entry on the diagonal. Without it, small pivots can amplify errors catastrophically. <em>Partial pivoting</em> swaps within a column; <em>full pivoting</em> swaps anywhere — more accurate but slower.</p>
<p>Stable in practice with partial pivoting on most matrices. The standard go-to for general dense systems.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Gaussian elimination cost: \(O(n^?)\). Fill: ___.", "answer": "3"},
         {"type": "multiple-choice", "question": "Partial pivoting swaps:", "options": ["entire matrix", "rows in a column", "columns", "nothing"], "correctIndex": 1},
         {"type": "true-false", "question": "Gaussian elimination without pivoting is reliable.", "correctAnswer": False},
         {"type": "true-false", "question": "Back-substitution solves the upper-triangular system.", "correctAnswer": True},
         {"type": "true-false", "question": "Full pivoting is always the best choice.", "correctAnswer": False}]},
    {"title": "LU Decomposition",
     "body_html": r"""
<p>LU decomposition writes \(A = LU\) (or \(PA = LU\) with row permutations) where \(L\) is lower triangular and \(U\) is upper triangular. Computed as a byproduct of Gaussian elimination.</p>
<p>Big advantage: once you have \(L, U\), solving \(A\vec{x} = \vec{b}\) for any new \(\vec{b}\) costs only \(O(n^2)\). Reuse the factorization across many right-hand sides.</p>
<p>This is what you should do when you'll solve repeatedly with the same matrix — much faster than starting over each time.</p>""",
     "exercises": [
         {"type": "true-false", "question": "LU is a byproduct of Gaussian elimination.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"After LU, solving \(A\vec{x}=\vec{b}\) for a new b costs:", "options": [r"\(O(n^3)\)", r"\(O(n^2)\)", r"\(O(n)\)", r"\(O(1)\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": "L is ___ triangular.", "answer": "lower"},
         {"type": "true-false", "question": "Pivoting requires the form PA = LU.", "correctAnswer": True},
         {"type": "true-false", "question": "LU is useful only for one solve.", "correctAnswer": False}]},
    {"title": "Cholesky Decomposition",
     "body_html": r"""
<p>For symmetric positive-definite matrices, <strong>Cholesky</strong> writes \(A = LL^T\) — half the work of LU, and numerically very stable.</p>
<p>Cost is \(O(n^3/3)\). Used heavily in optimization, statistics (multivariate normals, Kalman filtering), and finite-element solvers.</p>
<p>If Cholesky fails — i.e., a square root of a non-positive value — the matrix isn't positive definite. So Cholesky doubles as a positive-definiteness test.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Cholesky requires symmetric positive definiteness.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Cholesky writes A = ?", "options": [r"\(LL^T\)", r"\(LU\)", r"\(QR\)", r"\(U\Sigma V^T\)"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Cholesky is roughly twice as ___ as general LU.", "answer": "fast"},
         {"type": "true-false", "question": "Failure of Cholesky indicates the matrix isn't positive definite.", "correctAnswer": True},
         {"type": "true-false", "question": "Cholesky is unstable.", "correctAnswer": False}]},
    {"title": "Iterative Method: Jacobi",
     "body_html": r"""
<p>For very large sparse systems, direct methods like LU don't fit in memory. <strong>Iterative methods</strong> only need matrix-vector products.</p>
<p><strong>Jacobi iteration:</strong> split \(A = D + R\) (diagonal + remainder). Iterate</p>
<div class="math-block">$$\vec{x}^{(k+1)} = D^{-1}(\vec{b} - R\vec{x}^{(k)})$$</div>
<p>Converges if \(A\) is diagonally dominant (each diagonal entry exceeds the sum of off-diagonals in its row in absolute value). Slow but trivial to parallelize.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Jacobi requires only matrix-vector products.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Jacobi converges if A is:", "options": ["singular", "symmetric", "diagonally dominant", "any"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Jacobi splits A as D + ___.", "answer": "R"},
         {"type": "true-false", "question": "Jacobi is easy to parallelize.", "correctAnswer": True},
         {"type": "true-false", "question": "Jacobi is fast for non-diagonally-dominant matrices.", "correctAnswer": False}]},
    {"title": "Gauss-Seidel",
     "body_html": r"""
<p><strong>Gauss-Seidel</strong> is like Jacobi but uses updated values immediately:</p>
<div class="math-block">$$x^{(k+1)}_i = \frac{1}{A_{ii}}\left(b_i - \sum_{j<i} A_{ij}x^{(k+1)}_j - \sum_{j>i} A_{ij}x^{(k)}_j\right)$$</div>
<p>Faster than Jacobi (typically \(2 \times\)), but less parallelizable since each component depends on the previous in the same iteration.</p>
<p>Converges when \(A\) is symmetric positive definite or strictly diagonally dominant. <strong>SOR</strong> (successive over-relaxation) accelerates convergence further with a tunable parameter \(\omega\).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Gauss-Seidel is typically faster than Jacobi.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Gauss-Seidel parallelizes:", "options": ["trivially", "harder than Jacobi", "perfectly", "not at all"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Acceleration of Gauss-Seidel: ___ (3 letters).", "answer": "SOR"},
         {"type": "true-false", "question": "Gauss-Seidel uses already-updated values within an iteration.", "correctAnswer": True},
         {"type": "true-false", "question": "Gauss-Seidel always converges for any matrix.", "correctAnswer": False}]},
    {"title": "Conjugate Gradient",
     "body_html": r"""
<p><strong>Conjugate Gradient (CG)</strong> is the workhorse iterative method for symmetric positive-definite systems. Uses only matrix-vector products and converges in at most \(n\) steps in exact arithmetic; in practice, way fewer.</p>
<p>Each iteration is \(O(\text{nnz}(A))\) where nnz is the number of nonzeros in \(A\). For sparse problems, total cost can be much less than \(n^3\).</p>
<p>Convergence rate depends on the condition number; <strong>preconditioning</strong> (a clever variable change) can dramatically speed it up.</p>""",
     "exercises": [
         {"type": "true-false", "question": "CG works for symmetric positive-definite systems.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "CG cost per iteration:", "options": [r"\(O(n^3)\)", r"\(O(n^2)\)", r"\(O(\text{nnz})\)", r"\(O(n)\)"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Acceleration of CG via a clever change of variable: ___.", "answer": "preconditioning"},
         {"type": "true-false", "question": "CG converges in at most n steps in exact arithmetic.", "correctAnswer": True},
         {"type": "true-false", "question": "CG benefits from low condition number.", "correctAnswer": True}]},
    {"title": "Krylov Subspace Methods",
     "body_html": r"""
<p>CG belongs to a family of <strong>Krylov subspace methods</strong>: they work in subspaces spanned by \(\{\vec{b}, A\vec{b}, A^2\vec{b}, \ldots\}\).</p>
<p>Other Krylov methods:</p>
<ul>
<li><strong>GMRES:</strong> general non-symmetric systems.</li>
<li><strong>BiCGSTAB:</strong> non-symmetric, robust.</li>
<li><strong>MINRES:</strong> symmetric indefinite.</li>
<li><strong>Lanczos:</strong> finds extreme eigenvalues without forming \(A\) explicitly.</li>
</ul>
<p>This is the foundation of large-scale numerical linear algebra in physics, engineering, and ML.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Krylov methods build subspaces from powers of A applied to b.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "GMRES is for:", "options": ["symmetric only", "non-symmetric systems", "complex only", "diagonal only"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Lanczos finds ___ eigenvalues of large matrices.", "answer": "extreme"},
         {"type": "true-false", "question": "BiCGSTAB is a Krylov method.", "correctAnswer": True},
         {"type": "true-false", "question": "Krylov methods are useless for sparse problems.", "correctAnswer": False}]},
    {"title": "Numerical SVD",
     "body_html": r"""
<p>Production SVD uses two phases:</p>
<ol>
<li><strong>Bidiagonalization:</strong> Householder reflections reduce \(A\) to a bidiagonal matrix \(B\) with the same singular values.</li>
<li><strong>Diagonalization of \(B\):</strong> a QR-iteration variant that produces the singular values rapidly.</li>
</ol>
<p>This is the Golub-Kahan-Reinsch algorithm — the standard. Variants for huge matrices include <strong>randomized SVD</strong>: project onto a random low-dim subspace, do SVD there, recover an approximate SVD of the original. Fast and accurate when only the top singular triples are needed.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Numerical SVD has bidiagonalization and diagonalization phases.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Standard SVD algorithm:", "options": ["Gauss-Jordan", "Golub-Kahan-Reinsch", "Cramer's rule", "Jacobi"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Randomized SVD projects onto a random ___ subspace.", "answer": "low-dim"},
         {"type": "true-false", "question": "Randomized SVD is useful for low-rank approximation.", "correctAnswer": True},
         {"type": "true-false", "question": "Bidiagonalization changes the singular values.", "correctAnswer": False}]},
    {"title": "Numerical Eigenvalue Methods",
     "body_html": r"""
<p>For large matrices:</p>
<ul>
<li><strong>QR iteration:</strong> the standard for dense matrices. Converges to upper triangular (Schur form).</li>
<li><strong>Power iteration:</strong> finds the largest \(|\lambda|\) eigenpair.</li>
<li><strong>Inverse iteration:</strong> shifted to find any specific eigenvalue.</li>
<li><strong>Lanczos / Arnoldi:</strong> Krylov-based, for sparse or large symmetric/non-symmetric matrices.</li>
</ul>
<p>Computing all eigenvalues of a million-dim sparse matrix is impossible. Computing the few you need (extreme, or close to a target) is feasible with these tools.</p>""",
     "exercises": [
         {"type": "true-false", "question": "QR iteration is standard for dense eigenvalue problems.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Lanczos handles which kind of large matrices?", "options": ["dense only", "diagonal only", "sparse symmetric/large", "any size"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Inverse iteration is used to find a ___ eigenvalue.", "answer": "specific"},
         {"type": "true-false", "question": "Computing all eigenvalues of a billion-dim sparse matrix is feasible.", "correctAnswer": False},
         {"type": "true-false", "question": "Power iteration finds the dominant eigenpair.", "correctAnswer": True}]},
    {"title": "Sparse vs Dense",
     "body_html": r"""
<p>A <strong>sparse</strong> matrix is mostly zeros. Storing only the nonzeros (CSR or CSC format) saves enormous memory and lets matrix-vector multiplication run in \(O(\text{nnz})\) time.</p>
<p>Sparse direct methods (sparse LU, sparse Cholesky) try to keep the factor matrices sparse — but <strong>fill-in</strong> (zeros becoming nonzeros) is unavoidable. Reordering rows/columns (e.g., approximate minimum degree) reduces it.</p>
<p>For super-large sparse problems, iterative methods (CG, GMRES, BiCGSTAB) are usually preferred over sparse direct methods.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Sparse matrices store only nonzeros for memory efficiency.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Sparse storage formats:", "options": ["CSR, CSC", "JPEG, PNG", "JSON", "TXT"], "correctIndex": 0},
         {"type": "fill-blank", "question": "When zeros become nonzeros in factorization, that's called ___.", "answer": "fill-in"},
         {"type": "true-false", "question": "Iterative methods are preferred for very large sparse problems.", "correctAnswer": True},
         {"type": "true-false", "question": "Sparse matvec is O(nnz).", "correctAnswer": True}]},
    {"title": "Practice: Pick the Right Method",
     "body_html": r"""
<p>Match problem to method:</p>
<ol>
<li><strong>Dense system, one solve:</strong> Gaussian elimination (LU with partial pivoting).</li>
<li><strong>Dense system, many solves with same A:</strong> LU once; reuse the factors.</li>
<li><strong>Symmetric positive-definite system:</strong> Cholesky.</li>
<li><strong>Huge sparse SPD system (PDE discretization):</strong> Conjugate gradient, with preconditioning.</li>
<li><strong>Top-k singular triples of a huge matrix:</strong> randomized SVD.</li>
<li><strong>Few extreme eigenvalues of a sparse symmetric matrix:</strong> Lanczos.</li>
</ol>""",
     "exercises": [
         {"type": "multiple-choice", "question": "SPD dense system: best?", "options": ["Cholesky", "QR", "SVD", "Jacobi"], "correctIndex": 0},
         {"type": "multiple-choice", "question": "Sparse SPD huge system?", "options": ["Cholesky", "Conjugate gradient", "Cramer", "Inverse iteration"], "correctIndex": 1},
         {"type": "fill-blank", "question": "For top-k SVD of a huge matrix: ___ SVD.", "answer": "randomized"},
         {"type": "true-false", "question": "LU is best when you'll solve repeatedly with the same matrix.", "correctAnswer": True},
         {"type": "true-false", "question": "Lanczos is for dense matrices only.", "correctAnswer": False}]},
    {"title": "Numerical Methods Checkpoint",
     "body_html": r"""
<p>Recap of Unit 40:</p>
<ul>
<li>Floating-point limits and condition number determine achievable accuracy.</li>
<li>Direct methods: Gaussian elimination → LU; symmetric PSD → Cholesky.</li>
<li>Iterative methods: Jacobi, Gauss-Seidel (basic); CG (workhorse for SPD); GMRES (general).</li>
<li>Krylov subspace methods underpin large-scale linear algebra.</li>
<li>Numerical SVD via Golub-Kahan-Reinsch; randomized SVD for low-rank.</li>
<li>Sparse formats and fill-in awareness are crucial for large problems.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Cholesky requires symmetric positive definiteness.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "CG requires:", "options": ["non-symmetric", "SPD", "diagonal", "any"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Roundoff per operation is ~10^___ for double precision.", "answer": "-16"},
         {"type": "true-false", "question": "Krylov methods only need matrix-vector products.", "correctAnswer": True},
         {"type": "true-false", "question": "Gaussian elimination is O(n²).", "correctAnswer": False},
         {"type": "fill-blank", "question": "Loss of digits ≈ log10 of condition ___.", "answer": "number"},
         {"type": "true-false", "question": "Sparse problems usually call for iterative methods.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(40, "Numerical Methods for Vectors", 586, LESSONS)
