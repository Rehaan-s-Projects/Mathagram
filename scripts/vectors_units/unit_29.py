#!/usr/bin/env python3
"""Unit 29 — Principal Component Analysis (lessons 421-435)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "The Goal of PCA",
     "body_html": r"""
<p><strong>Principal Component Analysis</strong> finds new orthogonal axes for your data along which the variance is largest. Project onto the top \(k\) of these axes, and you get the best \(k\)-dimensional summary in a least-squares sense.</p>
<p>Why? Real data sits near a low-dimensional surface inside a high-dimensional space. PCA finds that surface. It's the workhorse of dimensionality reduction, visualization, denoising, and feature engineering.</p>
<p>It is the most-used unsupervised technique in machine learning.</p>""",
     "exercises": [
         {"type": "true-false", "question": "PCA finds axes of maximum variance.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "PCA is:", "options": ["supervised", "unsupervised", "reinforcement learning", "online"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"PCA gives the best ___ approximation in a least-squares sense.", "answer": "low-dimensional"},
         {"type": "true-false", "question": "PCA assumes data is high-dimensional but truly low-dimensional in structure.", "correctAnswer": True},
         {"type": "true-false", "question": "PCA requires labels.", "correctAnswer": False}]},
    {"title": "Centering the Data",
     "body_html": r"""
<p>PCA assumes the data is <strong>centered</strong>: the mean of each feature is subtracted off. Otherwise the dominant direction is just the mean, not the true variance structure.</p>
<p>For a data matrix \(X\) (rows = observations, columns = features), set</p>
<div class="math-block">$$X_c = X - \bar{X}$$</div>
<p>where \(\bar{X}\) is the column mean of \(X\) broadcast across all rows. After centering, every column has mean zero.</p>
<p>Centering is non-negotiable. Forgetting it makes PCA give wrong answers.</p>""",
     "exercises": [
         {"type": "true-false", "question": "PCA requires centering the data first.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"After centering, each column has mean ___.", "answer": "0"},
         {"type": "multiple-choice", "question": "Without centering, PCA's first PC may align with the:", "options": ["zero vector", "mean", "median", "max"], "correctIndex": 1},
         {"type": "true-false", "question": "Centering is optional for PCA.", "correctAnswer": False},
         {"type": "true-false", "question": "Centering changes the variance structure.", "correctAnswer": False}]},
    {"title": "Covariance Matrix",
     "body_html": r"""
<p>For centered data \(X_c\) with \(n\) observations, the <strong>sample covariance matrix</strong> is</p>
<div class="math-block">$$C = \frac{1}{n-1} X_c^T X_c$$</div>
<p>It's symmetric, positive semi-definite, and \(p \times p\) (where \(p\) is the number of features).</p>
<p>Diagonal entries are variances of individual features; off-diagonal entries are covariances. Large positive off-diagonal: features rise together. Large negative: one rises as the other falls. Zero: linearly uncorrelated.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(C = \frac{1}{n-1} X_c^T\) ___.", "answer": "X_c"},
         {"type": "true-false", "question": "The covariance matrix is symmetric and positive semi-definite.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Diagonal entries of C are:", "options": ["covariances", "variances", "means", "ranks"], "correctIndex": 1},
         {"type": "true-false", "question": "Zero off-diagonal entries mean the features are uncorrelated.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(C\) has shape \(p \times\) ___.", "answer": "p"}]},
    {"title": "Variance Along a Direction",
     "body_html": r"""
<p>For a unit vector \(\hat{w}\), the variance of the data projected onto \(\hat{w}\) is</p>
<div class="math-block">$$\text{Var}(X_c \hat{w}) = \hat{w}^T C \hat{w}$$</div>
<p>This is a quadratic form in \(\hat{w}\), governed by the symmetric covariance matrix \(C\). Maximizing over unit vectors:</p>
<div class="math-block">$$\max_{\|\hat{w}\|=1} \hat{w}^T C \hat{w} = \lambda_1 \text{ (largest eigenvalue of } C\text{)}$$</div>
<p>achieved when \(\hat{w}\) is the corresponding eigenvector. <strong>So the direction of maximum variance is the top eigenvector of \(C\)</strong>.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Variance along \(\hat{w}\) is \(\hat{w}^T\) ___ \(\hat{w}\).", "answer": "C"},
         {"type": "true-false", "question": "Direction of max variance = top eigenvector of C.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Maximum of \(\hat{w}^T C \hat{w}\) over unit \(\hat{w}\) equals:", "options": ["trace of C", "largest eigenvalue of C", "smallest eigenvalue", "determinant"], "correctIndex": 1},
         {"type": "true-false", "question": "Variance is always nonnegative.", "correctAnswer": True},
         {"type": "true-false", "question": "Off-diagonal entries of C measure variance of features.", "correctAnswer": False}]},
    {"title": "Eigendecomposition of the Covariance",
     "body_html": r"""
<p>Since \(C\) is symmetric, the spectral theorem applies:</p>
<div class="math-block">$$C = Q \Lambda Q^T$$</div>
<p>The columns of \(Q\) are the <strong>principal directions</strong>; the diagonal of \(\Lambda\) (in descending order) gives the variances along each.</p>
<p>The first PC is the eigenvector for the largest eigenvalue, the second PC for the second-largest, and so on. PCs are mutually orthogonal — no redundancy.</p>""",
     "exercises": [
         {"type": "true-false", "question": "PCs are eigenvectors of the covariance matrix.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(C = Q\Lambda\) ___.", "answer": "Q^T"},
         {"type": "multiple-choice", "question": "The k-th PC corresponds to the:", "options": ["smallest eigenvalue", "k-th largest eigenvalue", "k-th column of X", "k-th row of X"], "correctIndex": 1},
         {"type": "true-false", "question": "Different PCs are mutually orthogonal.", "correctAnswer": True},
         {"type": "true-false", "question": "Eigenvalues of C give the variance along each PC.", "correctAnswer": True}]},
    {"title": "Principal Components Defined",
     "body_html": r"""
<p>The \(i\)-th <strong>principal component</strong> is the eigenvector \(\vec{v}_i\) of \(C\) corresponding to the \(i\)-th largest eigenvalue \(\lambda_i\). It captures the direction of \(i\)-th largest variance.</p>
<p>The data, projected onto \(\vec{v}_i\), gives the <strong>i-th PC scores</strong>:</p>
<div class="math-block">$$\text{score}_i = X_c \vec{v}_i$$</div>
<p>This is a single column of "coordinates along PC \(i\)" for each observation. Stacking the first \(k\) PC scores gives the reduced \(k\)-dimensional representation.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"The \(i\)-th PC corresponds to the \(i\)-th largest ___.", "answer": "eigenvalue"},
         {"type": "multiple-choice", "question": r"PC scores are computed by:", "options": [r"\(X_c\)", r"\(X_c \vec{v}_i\)", r"\(C \vec{v}_i\)", r"\(\vec{v}_i^T \vec{v}_i\)"], "correctIndex": 1},
         {"type": "true-false", "question": "The first PC captures the most variance.", "correctAnswer": True},
         {"type": "true-false", "question": "Different PC score columns are uncorrelated.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Reducing to \(k\) dims means stacking the first ___ PC scores.", "answer": "k"}]},
    {"title": "Explained Variance",
     "body_html": r"""
<p>The total variance in the data is \(\text{tr}(C) = \sum_i \lambda_i\). The fraction of variance "explained" by the first \(k\) PCs is</p>
<div class="math-block">$$\frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^p \lambda_i}$$</div>
<p>Plotting cumulative explained variance vs. number of PCs gives a "scree plot." Look for an elbow — the point of diminishing returns.</p>
<p>For data with strong low-rank structure, a few PCs explain almost everything. For noisy or high-dim data, you may need many.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Total variance equals \(\text{tr}(C) = \sum_i\) ___.", "answer": "lambda_i"},
         {"type": "true-false", "question": "Explained variance ratio is between 0 and 1.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "A scree plot is:", "options": ["a histogram of features", "cumulative explained variance vs PC count", "a covariance matrix", "data scatter"], "correctIndex": 1},
         {"type": "true-false", "question": "Strong low-rank data: few PCs explain most variance.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Look for an ___ in the scree plot to choose \(k\).", "answer": "elbow"}]},
    {"title": "Choosing How Many Components",
     "body_html": r"""
<p>Common rules for choosing \(k\):</p>
<ul>
<li><strong>Variance threshold:</strong> keep enough PCs to explain, e.g., 95% of variance.</li>
<li><strong>Scree plot elbow:</strong> visually find the kink.</li>
<li><strong>Cross-validation:</strong> tune \(k\) using a downstream metric.</li>
<li><strong>Kaiser criterion:</strong> keep PCs with eigenvalue \(&gt; 1\) (when working with the correlation matrix).</li>
</ul>
<p>None of these is canonical. The right \(k\) depends on what you'll use the reduced representation for: visualization (\(k=2\) or \(3\)), denoising (\(k\) where the noise floor begins), or downstream modeling (tune via CV).</p>""",
     "exercises": [
         {"type": "true-false", "question": "There's a single canonical rule for choosing k in PCA.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "For visualization, k is typically:", "options": [r"\(p\)", "0", "2 or 3", "10"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"Threshold approach: keep enough PCs to explain ___% (e.g.) of variance.", "answer": "95"},
         {"type": "true-false", "question": "Cross-validation can choose k for a downstream task.", "correctAnswer": True},
         {"type": "true-false", "question": "The Kaiser criterion uses eigenvalue > 1.", "correctAnswer": True}]},
    {"title": "PCA via SVD",
     "body_html": r"""
<p>You don't have to form \(C = X_c^T X_c / (n-1)\) explicitly. SVD of \(X_c\) gives PCA directly:</p>
<div class="math-block">$$X_c = U\Sigma V^T$$</div>
<ul>
<li>Columns of \(V\) are the principal directions.</li>
<li>Singular values give variance: \(\lambda_i = \sigma_i^2/(n-1)\).</li>
<li>PC scores are \(U\Sigma\) (each column is a score for one PC).</li>
</ul>
<p>SVD is more numerically stable than forming \(X_c^T X_c\) explicitly, especially for high-dim or near-rank-deficient data. Production PCA (in scikit-learn etc.) does it this way.</p>""",
     "exercises": [
         {"type": "true-false", "question": "PCA can be computed via SVD of the centered data.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Eigenvalues of \(C\) are \(\sigma_i^2 / (n - \) ___\()\).", "answer": "1"},
         {"type": "multiple-choice", "question": "The columns of V are the:", "options": ["scores", "principal directions", "means", "variances"], "correctIndex": 1},
         {"type": "true-false", "question": "Forming X^TX explicitly can hurt numerical stability.", "correctAnswer": True},
         {"type": "true-false", "question": "Production PCA uses SVD.", "correctAnswer": True}]},
    {"title": "Whitening (Decorrelation)",
     "body_html": r"""
<p><strong>Whitening</strong> transforms the data so its covariance becomes the identity. After whitening, all features are uncorrelated and have unit variance.</p>
<div class="math-block">$$\tilde X = X_c V \Lambda^{-1/2}$$</div>
<p>Geometrically: it un-stretches and un-rotates the data. The "ellipsoid of variance" becomes a sphere.</p>
<p>Whitening is useful as a preprocessing step before applying methods sensitive to feature scaling (e.g., k-NN). It's also a step in some neural network normalization schemes.</p>""",
     "exercises": [
         {"type": "true-false", "question": "After whitening, the covariance matrix is the identity.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Geometrically, whitening:", "options": ["stretches the data", "turns ellipsoid into a sphere", "shifts the data", "rotates by 45°"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\tilde X = X_c V \Lambda^{?}\). Fill: ___.", "answer": "-1/2"},
         {"type": "true-false", "question": "Whitening is useful before k-NN.", "correctAnswer": True},
         {"type": "true-false", "question": "After whitening, all features have unit variance.", "correctAnswer": True}]},
    {"title": "PCA for Visualization",
     "body_html": r"""
<p>The classic 2D scatter plot of PC1 vs PC2 reveals structure that's invisible in raw high-dim space: clusters, gradients, outliers.</p>
<p>It's a near-default first step in exploratory data analysis. Worth doing every time you encounter a new dataset, before more elaborate methods.</p>
<p><strong>Caveats.</strong> If the data lives on a curved manifold, PCA misses it (linear-only). For nonlinear structure, try t-SNE or UMAP after PCA-preprocessing.</p>""",
     "exercises": [
         {"type": "true-false", "question": "PC1 vs PC2 scatter is a standard exploratory tool.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "For nonlinear structure, prefer:", "options": ["PCA", "t-SNE or UMAP", "linear regression", "covariance"], "correctIndex": 1},
         {"type": "fill-blank", "question": "PCA is a ___ method (not nonlinear).", "answer": "linear"},
         {"type": "true-false", "question": "PCA-then-t-SNE is a common workflow for visualization.", "correctAnswer": True},
         {"type": "true-false", "question": "Outliers tend to dominate PC directions.", "correctAnswer": True}]},
    {"title": "Limitations of PCA",
     "body_html": r"""
<p>PCA has real limits to be aware of:</p>
<ul>
<li><strong>Linear only.</strong> It can't find curved manifolds. For that, use kernel PCA, autoencoders, or t-SNE/UMAP.</li>
<li><strong>Variance ≠ importance.</strong> If your task depends on a low-variance direction, PCA may discard the signal.</li>
<li><strong>Sensitive to scale.</strong> Always standardize features (z-score) when they live on different scales.</li>
<li><strong>Outlier-sensitive.</strong> A single outlier can dominate PCs. Robust PCA exists but isn't the default.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "PCA finds nonlinear structure.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "PCA is sensitive to:", "options": ["row order", "feature scale", "label distribution", "the date"], "correctIndex": 1},
         {"type": "fill-blank", "question": "When features are on different scales, you should ___ before PCA.", "answer": "standardize"},
         {"type": "true-false", "question": "Variance and predictive importance are the same thing.", "correctAnswer": False},
         {"type": "true-false", "question": "Outliers can hijack PC directions.", "correctAnswer": True}]},
    {"title": "PCA vs Other Methods",
     "body_html": r"""
<p>How PCA compares to its peers:</p>
<ul>
<li><strong>LDA (Linear Discriminant Analysis):</strong> supervised — uses labels to find class-discriminating directions.</li>
<li><strong>ICA (Independent Component Analysis):</strong> finds statistically independent components, not just uncorrelated. Useful for source separation.</li>
<li><strong>Kernel PCA:</strong> nonlinear PCA via the kernel trick.</li>
<li><strong>t-SNE / UMAP:</strong> nonlinear, non-linear-projection methods, typically used post-PCA for 2D viz.</li>
<li><strong>Autoencoders:</strong> neural-network PCA generalization; can capture nonlinear manifolds.</li>
</ul>""",
     "exercises": [
         {"type": "multiple-choice", "question": "Which is supervised?", "options": ["PCA", "LDA", "ICA", "t-SNE"], "correctIndex": 1},
         {"type": "true-false", "question": "ICA produces statistically independent components.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Autoencoders can capture ___ manifolds.", "answer": "nonlinear"},
         {"type": "true-false", "question": "Kernel PCA handles nonlinear structure.", "correctAnswer": True},
         {"type": "true-false", "question": "PCA is supervised.", "correctAnswer": False}]},
    {"title": "Practice: Run a PCA",
     "body_html": r"""
<p>The pipeline:</p>
<ol>
<li>Standardize features (z-score).</li>
<li>Compute SVD: \(X_c = U\Sigma V^T\).</li>
<li>Components = columns of \(V\). Scores = \(U\Sigma\).</li>
<li>Inspect explained variance ratio: \(\lambda_i / \sum_j \lambda_j\).</li>
<li>Choose \(k\) (variance threshold or elbow).</li>
<li>Project: \(X_{\text{reduced}} = X_c V_{[:, :k]}\).</li>
</ol>
<p>In Python: <code>sklearn.decomposition.PCA(n_components=k).fit_transform(X)</code> does all this in one line. But knowing what's under the hood matters when something goes wrong.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "PCA pipeline starts with ___ features.", "answer": "standardize"},
         {"type": "multiple-choice", "question": "Reduced data is computed by:", "options": [r"\(C V\)", r"\(X_c V_{[:, :k]}\)", r"\(\Sigma V\)", r"\(V \Lambda\)"], "correctIndex": 1},
         {"type": "true-false", "question": "scikit-learn's PCA encapsulates this whole pipeline.", "correctAnswer": True},
         {"type": "true-false", "question": "You should center but not scale before PCA.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"Explained variance ratio for PC \(i\): \(\lambda_i / \sum_j\) ___.", "answer": "lambda_j"}]},
    {"title": "PCA Checkpoint",
     "body_html": r"""
<p>Recap of Unit 29:</p>
<ul>
<li>PCA finds orthogonal axes of maximum variance.</li>
<li>Center the data first; covariance matrix is symmetric, PSD.</li>
<li>PCs = eigenvectors of \(C\), eigenvalues = variance explained per PC.</li>
<li>SVD of \(X_c\) yields PCA directly: \(V\) gives PCs, \(\Sigma\) gives variances.</li>
<li>Choose number of PCs by variance threshold or scree-plot elbow.</li>
<li>Whitening makes the covariance the identity.</li>
<li>Limits: linear only, scale-sensitive, outlier-sensitive.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "PCA always requires labeled data.", "correctAnswer": False},
         {"type": "multiple-choice", "question": "PCs come from:", "options": ["randomization", "eigenvectors of the covariance", "k-means", "linear regression"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Total variance in centered data equals trace of ___.", "answer": "C"},
         {"type": "true-false", "question": "PCA is unsupervised.", "correctAnswer": True},
         {"type": "true-false", "question": "PCA can find nonlinear manifolds.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"Eigenvalues of \(C\) measure ___ along each PC.", "answer": "variance"},
         {"type": "true-false", "question": "Whitening produces unit-variance, decorrelated features.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(29, "Principal Component Analysis", 421, LESSONS)
