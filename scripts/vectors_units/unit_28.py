#!/usr/bin/env python3
"""Unit 28 — Singular Value Decomposition (lessons 406-420)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "From Eigendecomposition to SVD",
     "body_html": r"""
<p>Eigendecomposition only works for square (and ideally symmetric) matrices. The <strong>Singular Value Decomposition (SVD)</strong> is the universal generalization: every matrix \(A\) (any shape) factors as</p>
<div class="math-block">$$A = U\Sigma V^T$$</div>
<p>where \(U\) and \(V\) are orthogonal and \(\Sigma\) is a diagonal matrix of non-negative entries (the <strong>singular values</strong>).</p>
<p>SVD is sometimes called "the most important factorization in numerical linear algebra." It powers PCA, recommendations, image compression, the pseudoinverse, conditioning analysis, and far more.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Every matrix has an SVD.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(A = U\Sigma\) ___.", "answer": "V^T"},
         {"type": "multiple-choice", "question": "U and V in SVD are:", "options": ["arbitrary", "orthogonal", "triangular", "diagonal"], "correctIndex": 1},
         {"type": "true-false", "question": "Singular values can be negative.", "correctAnswer": False},
         {"type": "true-false", "question": "Eigendecomposition works for all matrices.", "correctAnswer": False}]},
    {"title": "The SVD Definition",
     "body_html": r"""
<p>For an \(m \times n\) matrix \(A\), the SVD is</p>
<div class="math-block">$$A = U\Sigma V^T$$</div>
<ul>
<li>\(U\) is \(m \times m\), orthogonal — its columns are <strong>left singular vectors</strong>.</li>
<li>\(\Sigma\) is \(m \times n\), with non-negative diagonal entries (<strong>singular values</strong>) in descending order: \(\sigma_1 \ge \sigma_2 \ge \cdots \ge 0\).</li>
<li>\(V\) is \(n \times n\), orthogonal — its columns are <strong>right singular vectors</strong>.</li>
</ul>
<p>The number of nonzero singular values equals the rank of \(A\). Beyond that, the diagonal of \(\Sigma\) is zero.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Singular values are listed in descending order.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "U is of size:", "options": [r"\(m \times n\)", r"\(m \times m\)", r"\(n \times n\)", r"\(n \times m\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Number of nonzero singular values equals \(\text{rank}(A) =\) ___.", "answer": "rank"},
         {"type": "true-false", "question": r"\(V\) is \(n \times n\) for an \(m \times n\) matrix \(A\).", "correctAnswer": True},
         {"type": "true-false", "question": "Singular values are always real and nonnegative.", "correctAnswer": True}]},
    {"title": "Geometric Picture",
     "body_html": r"""
<p>SVD has a beautiful geometric meaning. Any linear map \(A\) can be decomposed into three steps:</p>
<ol>
<li>\(V^T\): rotate the input so its principal directions align with axes.</li>
<li>\(\Sigma\): scale each axis by the corresponding singular value.</li>
<li>\(U\): rotate again into the output space.</li>
</ol>
<p>So every linear map looks like rotate → stretch axes → rotate. This is sometimes called "the rotation-stretch-rotation" structure. Even non-square \(A\) can be decomposed this way.</p>
<p>The image of the unit sphere under \(A\) is always an <strong>ellipsoid</strong>; its semi-axes are the singular values, oriented along the columns of \(U\).</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "SVD decomposes a linear map into:", "options": ["scale, scale, scale", "rotate, stretch, rotate", "shear, project, rotate", "translate, scale, rotate"], "correctIndex": 1},
         {"type": "true-false", "question": "The image of a unit sphere under any matrix is an ellipsoid.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"The semi-axes of the ellipsoid have lengths equal to the ___ values.", "answer": "singular"},
         {"type": "true-false", "question": "Even rectangular matrices have a rotate-stretch-rotate structure.", "correctAnswer": True},
         {"type": "true-false", "question": "U gives directions in the output space.", "correctAnswer": True}]},
    {"title": "Singular Values",
     "body_html": r"""
<p>The singular values \(\sigma_i\) measure how much \(A\) stretches the most-stretched directions. They satisfy:</p>
<ul>
<li>\(\sigma_1 = \max_{\|\vec{x}\|=1} \|A\vec{x}\|\) — the largest stretching factor (also the spectral norm \(\|A\|_2\)).</li>
<li>\(\sigma_i = \sqrt{\lambda_i(A^T A)}\) — square roots of eigenvalues of \(A^T A\).</li>
<li>\(\sigma_n = \min_{\|\vec{x}\|=1} \|A\vec{x}\|\) (for full-rank square \(A\)) — the smallest stretching factor.</li>
</ul>
<p>The ratio \(\sigma_1/\sigma_n\) is the <strong>condition number</strong>: large means \(A\) is "ill-conditioned" — small input changes can produce huge output changes.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\sigma_1\) equals the spectral norm \(\|A\|\) ___.", "answer": "_2"},
         {"type": "multiple-choice", "question": r"\(\sigma_i =\)", "options": [r"\(\sqrt{\lambda_i(A^TA)}\)", r"\(\lambda_i(A)\)", r"\(\det(A)\)", r"\(A_{ii}\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Condition number is the ratio of largest to smallest singular value.", "correctAnswer": True},
         {"type": "true-false", "question": "Singular values are always nonnegative.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"For an orthogonal matrix, all singular values equal ___.", "answer": "1"}]},
    {"title": "Left & Right Singular Vectors",
     "body_html": r"""
<p>The columns of \(V\) are <strong>right singular vectors</strong> (\(\vec{v}_i\)). The columns of \(U\) are <strong>left singular vectors</strong> (\(\vec{u}_i\)). They satisfy:</p>
<div class="math-block">$$A\vec{v}_i = \sigma_i \vec{u}_i, \qquad A^T\vec{u}_i = \sigma_i \vec{v}_i$$</div>
<p>These are eigenvectors:</p>
<ul>
<li>\(\vec{v}_i\) is an eigenvector of \(A^T A\) with eigenvalue \(\sigma_i^2\).</li>
<li>\(\vec{u}_i\) is an eigenvector of \(AA^T\) with eigenvalue \(\sigma_i^2\).</li>
</ul>
<p>So computing SVD reduces to computing eigenvectors of \(A^T A\) (and \(AA^T\), but they share eigenvalues).</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(A\vec{v}_i = \sigma_i \vec{u}_i\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Right singular vectors are eigenvectors of:", "options": [r"\(A\)", r"\(A^TA\)", r"\(AA^T\)", r"\(A + A^T\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Eigenvalues of \(A^TA\) are \(\sigma_i^?\). Fill: ___.", "answer": "2"},
         {"type": "true-false", "question": "Left singular vectors are eigenvectors of \\(AA^T\\).", "correctAnswer": True},
         {"type": "true-false", "question": "U and V have the same dimensions.", "correctAnswer": False}]},
    {"title": "Reduced (Thin) SVD",
     "body_html": r"""
<p>For a tall matrix \(A\) (\(m &gt; n\)), most of \(\Sigma\) is zero. The <strong>thin SVD</strong> drops the zero parts:</p>
<div class="math-block">$$A = \tilde U \tilde\Sigma V^T$$</div>
<ul>
<li>\(\tilde U\) is \(m \times n\) (only the first \(n\) left singular vectors).</li>
<li>\(\tilde\Sigma\) is \(n \times n\) diagonal.</li>
<li>\(V\) is unchanged at \(n \times n\).</li>
</ul>
<p>For data analysis, the thin SVD is what you actually compute — it has the same content but is much smaller.</p>
<p>Even more compact: <strong>truncated SVD</strong> keeps only the top \(k\) singular triples \(\sigma_i \vec{u}_i \vec{v}_i^T\).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Thin SVD drops zero parts of Σ.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"For tall \(A\), thin SVD has \(\tilde U\) of size:", "options": [r"\(m \times m\)", r"\(m \times n\)", r"\(n \times n\)", r"\(n \times m\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Truncated SVD keeps the top ___ triples.", "answer": "k"},
         {"type": "true-false", "question": "Thin SVD has the same information as full SVD for tall matrices.", "correctAnswer": True},
         {"type": "true-false", "question": "Truncated SVD gives the best low-rank approximation.", "correctAnswer": True}]},
    {"title": "Computing SVD via Eigendecomposition",
     "body_html": r"""
<p>Conceptually:</p>
<ol>
<li>Compute eigenvalues/eigenvectors of \(A^T A\). Eigenvalues are \(\sigma_i^2\); eigenvectors form \(V\).</li>
<li>Set \(\sigma_i = \sqrt{\lambda_i(A^TA)}\) (descending order).</li>
<li>Compute \(\vec{u}_i = A\vec{v}_i / \sigma_i\) for nonzero \(\sigma_i\); fill in remaining columns of \(U\) with vectors completing an orthonormal basis.</li>
</ol>
<p>In practice, the eigendecomposition route is unstable — production code uses <strong>bidiagonalization + QR iteration</strong> on the bidiagonal form (Golub-Kahan-Reinsch). But conceptually, SVD is just the eigendecomposition of \(A^T A\) with packaging.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"You can compute SVD by eigendecomposing \(A^T A\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\vec{u}_i = A\vec{v}_i /\) ___.", "answer": "sigma_i"},
         {"type": "multiple-choice", "question": "Production SVD uses:", "options": [r"\(A^TA\) eigendecomp directly", "Golub-Kahan-Reinsch", "Gauss-Jordan", "Cramer's rule"], "correctIndex": 1},
         {"type": "true-false", "question": r"The eigenvalues of \(A^TA\) are nonnegative.", "correctAnswer": True},
         {"type": "true-false", "question": r"For a nonzero eigenvalue, \(\sigma = \sqrt{\lambda}\).", "correctAnswer": True}]},
    {"title": "Rank from SVD",
     "body_html": r"""
<p>The <strong>rank</strong> of \(A\) equals the number of nonzero singular values.</p>
<p>This is the most numerically robust way to compute rank: in practice, "nonzero" is replaced by "above some tolerance \(\epsilon\)" — singular values smaller than \(\epsilon \sigma_1\) are treated as effectively zero. This is <strong>numerical rank</strong>.</p>
<p>Other rank notions (row rank, column rank, etc.) all collapse to the same number, but only SVD gives a numerically stable count.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Rank equals the number of nonzero singular values.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Numerical rank uses:", "options": ["exact zero", "a tolerance ε", "trace", "determinant"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"For a full-rank \(n \times n\) matrix, all \(n\) singular values are ___.", "answer": "nonzero"},
         {"type": "true-false", "question": "Row rank, column rank, and SVD rank are all equal.", "correctAnswer": True},
         {"type": "true-false", "question": "Counting Gaussian elimination pivots is more numerically stable than SVD for rank.", "correctAnswer": False}]},
    {"title": "Pseudoinverse from SVD",
     "body_html": r"""
<p>The <strong>Moore-Penrose pseudoinverse</strong> \(A^+\) generalizes the inverse to any matrix:</p>
<div class="math-block">$$A^+ = V\Sigma^+ U^T$$</div>
<p>where \(\Sigma^+\) is the transpose of \(\Sigma\) with nonzero diagonal entries replaced by their reciprocals.</p>
<p>For invertible \(A\): \(A^+ = A^{-1}\). For tall \(A\) with full column rank: \(A^+ = (A^TA)^{-1}A^T\) — and \(A^+\vec{b}\) is exactly the <strong>least-squares solution</strong>. For wide \(A\) with full row rank: \(A^+\) gives the <strong>minimum-norm solution</strong> to underdetermined systems.</p>""",
     "exercises": [
         {"type": "true-false", "question": "The pseudoinverse generalizes the inverse to any matrix.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(A^+ = V\Sigma^+ U^?\). Fill: ___.", "answer": "T"},
         {"type": "multiple-choice", "question": r"For tall full-column-rank \(A\), \(A^+ \vec{b}\) is the:", "options": ["minimum-norm", "least-squares", "trivial", "exact"], "correctIndex": 1},
         {"type": "true-false", "question": r"For invertible \(A\), \(A^+ = A^{-1}\).", "correctAnswer": True},
         {"type": "true-false", "question": "Σ⁺ flips reciprocals of nonzero diagonal entries.", "correctAnswer": True}]},
    {"title": "Low-Rank Approximation (Eckart-Young)",
     "body_html": r"""
<p>The <strong>Eckart-Young theorem</strong> says: the best rank-\(k\) approximation to \(A\) (in the Frobenius or spectral norm) is</p>
<div class="math-block">$$A_k = \sum_{i=1}^k \sigma_i \vec{u}_i \vec{v}_i^T$$</div>
<p>That is: keep only the top \(k\) singular triples and zero out the rest. The error is</p>
<div class="math-block">$$\|A - A_k\|_2 = \sigma_{k+1}, \quad \|A - A_k\|_F^2 = \sum_{i &gt; k} \sigma_i^2$$</div>
<p>SVD provides the optimal data compression. This is the foundation of PCA, dimensionality reduction, recommender systems, and many other applications.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Eckart-Young: the best rank-k approximation comes from truncated SVD.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Spectral-norm approximation error: \(\|A - A_k\|_2 =\) ___.", "answer": "sigma_(k+1)"},
         {"type": "multiple-choice", "question": "The best rank-k approximation keeps:", "options": ["top k singular triples", "first k rows", "first k columns", "any k entries"], "correctIndex": 0},
         {"type": "true-false", "question": "PCA uses Eckart-Young theorem.", "correctAnswer": True},
         {"type": "true-false", "question": "Frobenius and spectral norms give different optima.", "correctAnswer": False}]},
    {"title": "Image Compression via SVD",
     "body_html": r"""
<p>A grayscale image is just a matrix of pixel intensities. Compute its SVD; keep the top \(k\) singular triples; discard the rest. The result is a rank-\(k\) approximation of the image.</p>
<p>For an \(m \times n\) image with truncation rank \(k\), storage drops from \(mn\) to \(k(m+n+1)\) numbers. With \(k\) small (say \(50\) for a \(1000 \times 1000\) image), you get drastic compression with often-imperceptible loss.</p>
<p>This is a textbook example, not industry-grade compression (JPEG uses DCT, not SVD), but it's a beautiful demonstration of how the largest singular values capture the "shape" of an image.</p>""",
     "exercises": [
         {"type": "true-false", "question": "SVD-based image compression keeps the top k singular triples.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Storage for rank-\(k\) approximation of \(m \times n\) image:", "options": [r"\(mn\)", r"\(k(m+n+1)\)", r"\(mn-k\)", r"\(k^2\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"JPEG uses ___, not SVD.", "answer": "DCT"},
         {"type": "true-false", "question": "The largest singular values capture the dominant patterns in an image.", "correctAnswer": True},
         {"type": "true-false", "question": "Visually, dropping small singular values is often imperceptible.", "correctAnswer": True}]},
    {"title": "Condition Number",
     "body_html": r"""
<p>For an invertible matrix, the <strong>condition number</strong> is</p>
<div class="math-block">$$\kappa(A) = \sigma_1 / \sigma_n = \|A\| \cdot \|A^{-1}\|$$</div>
<p>It quantifies <strong>numerical sensitivity</strong>: solving \(A\vec{x} = \vec{b}\) can amplify input errors by up to a factor of \(\kappa(A)\).</p>
<p>Rule of thumb: a matrix with condition number \(10^k\) loses \(k\) digits of precision in computations. \(\kappa = 10^{16}\) on double-precision floats means useless results.</p>
<p>Symmetric positive-definite matrices have \(\kappa = \lambda_{max}/\lambda_{min}\). Orthogonal matrices have \(\kappa = 1\) — perfectly conditioned.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\kappa(A) = \sigma_1 /\) ___.", "answer": "sigma_n"},
         {"type": "multiple-choice", "question": "Orthogonal matrices have condition number:", "options": ["0", "1", r"\(\infty\)", r"\(\det Q\)"], "correctIndex": 1},
         {"type": "true-false", "question": "Large condition number means ill-conditioned.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"A condition number of \(10^k\) loses about ___ digits of precision.", "answer": "k"},
         {"type": "true-false", "question": "Singular matrices have infinite condition number.", "correctAnswer": True}]},
    {"title": "SVD vs Eigendecomposition",
     "body_html": r"""
<p>How they compare:</p>
<ul>
<li><strong>SVD</strong> works for any matrix; eigendecomposition needs square (and ideally diagonalizable).</li>
<li><strong>SVD's bases</strong> \(U, V\) are orthonormal; eigendecomp's basis is just linearly independent.</li>
<li><strong>Singular values</strong> are non-negative reals; eigenvalues can be complex.</li>
<li>For symmetric positive-definite \(A\): SVD = eigendecomp (same up to signs/order).</li>
<li>SVD is numerically stable; eigendecomposition can fail for defective matrices.</li>
</ul>
<p>Rule of thumb: when you have a choice, <strong>use SVD</strong>.</p>""",
     "exercises": [
         {"type": "true-false", "question": "SVD works for any matrix.", "correctAnswer": True},
         {"type": "true-false", "question": "Eigendecomposition is more general than SVD.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "For symmetric PSD A, SVD and eigendecomp:", "options": ["are unrelated", "agree (up to signs/order)", "give negative singular values", "differ in dimension"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Singular values are always real and ___.", "answer": "nonnegative"},
         {"type": "true-false", "question": "SVD is generally more numerically stable than eigendecomposition.", "correctAnswer": True}]},
    {"title": "Practice: Compute an SVD",
     "body_html": r"""
<p>Find the SVD of \(A = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}\).</p>
<p>It's already diagonal with positive entries, so trivially: \(U = I\), \(\Sigma = A\), \(V^T = I\). Singular values \(3\) and \(2\).</p>
<p>Now \(A = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}\). Compute \(A^TA = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\). Eigenvalues \(2, 0\). Eigenvectors \((1,1)/\sqrt{2}\) and \((1,-1)/\sqrt{2}\). Singular values \(\sqrt{2}, 0\). Then \(\vec{u}_1 = A\vec{v}_1/\sqrt{2} = (1, 0)\). Pick \(\vec{u}_2 = (0,1)\) to fill out \(U\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Singular values of \(\text{diag}(3,2)\): the larger is ___.", "answer": "3"},
         {"type": "multiple-choice", "question": r"For \(\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}\), nonzero singular value is:", "options": [r"\(\sqrt{2}\)", "1", "2", "0"], "correctIndex": 0},
         {"type": "true-false", "question": "A diagonal matrix with positive entries has its diagonal as singular values directly.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Rank of \(\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}\) is ___.", "answer": "1"},
         {"type": "true-false", "question": r"Singular values of \(I_n\) are all 1.", "correctAnswer": True}]},
    {"title": "SVD Checkpoint",
     "body_html": r"""
<p>Recap of Unit 28:</p>
<ul>
<li>SVD: every matrix \(A = U\Sigma V^T\). Universal.</li>
<li>Singular values are non-negative reals (\(\sigma_1 \ge \sigma_2 \ge \cdots \ge 0\)).</li>
<li>Geometric: rotate-stretch-rotate. Image of unit sphere is an ellipsoid.</li>
<li>Singular values are square roots of eigenvalues of \(A^TA\).</li>
<li>Rank = number of nonzero singular values.</li>
<li>Pseudoinverse \(A^+\) generalizes the inverse via SVD.</li>
<li>Eckart-Young: truncated SVD gives the best low-rank approximation.</li>
<li>Condition number \(\kappa(A) = \sigma_1/\sigma_n\) measures numerical sensitivity.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": r"\(A = U\Sigma V^T\) for any matrix.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Best rank-k approximation comes from:", "options": ["truncated SVD", "first k rows", "first k columns", "first k entries"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"\(\sigma_i^2\) are eigenvalues of \(A^?A\). Fill: ___.", "answer": "T"},
         {"type": "true-false", "question": "Condition number = 1 means perfectly conditioned.", "correctAnswer": True},
         {"type": "true-false", "question": "Pseudoinverse equals inverse for invertible matrices.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Number of nonzero singular values equals ___.", "answer": "rank"},
         {"type": "true-false", "question": "U and V are orthogonal in any SVD.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(28, "Singular Value Decomposition", 406, LESSONS)
