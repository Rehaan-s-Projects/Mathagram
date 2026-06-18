#!/usr/bin/env python3
"""Unit 27 — Orthogonality & QR Decomposition (lessons 391-405)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Orthogonal Complement",
     "body_html": r"""
<p>For a subspace \(W\) of an inner-product space \(V\), the <strong>orthogonal complement</strong> is</p>
<div class="math-block">$$W^\perp = \{\vec{v} \in V : \langle\vec{v},\vec{w}\rangle = 0 \text{ for all } \vec{w} \in W\}$$</div>
<p>It's also a subspace of \(V\), and \(V = W \oplus W^\perp\). Every vector decomposes uniquely as a piece in \(W\) plus a piece orthogonal to \(W\).</p>
<p><strong>Example.</strong> If \(W\) is a plane through the origin in \(\mathbb{R}^3\), \(W^\perp\) is the line through the origin perpendicular to \(W\) (the normal line).</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(W^\perp\) is itself a subspace.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(V = W \oplus W^?\). Fill: ___.", "answer": "perp"},
         {"type": "multiple-choice", "question": r"In \(\mathbb{R}^3\), the orthogonal complement of a plane is:", "options": ["a plane", "a line", "the origin", r"\(\mathbb{R}^3\)"], "correctIndex": 1},
         {"type": "true-false", "question": r"\((W^\perp)^\perp = W\) for finite-dim subspaces.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\dim W + \dim W^\perp =\) ___.", "answer": "dim V"}]},
    {"title": "Orthogonal Projection onto a Line",
     "body_html": r"""
<p>Given a unit vector \(\hat{u}\), the orthogonal projection of \(\vec{v}\) onto the line through \(\hat{u}\) is</p>
<div class="math-block">$$\text{proj}_{\hat{u}}(\vec{v}) = \langle\vec{v},\hat{u}\rangle\,\hat{u}$$</div>
<p>If \(\vec{u}\) is not unit-length, scale appropriately: \(\text{proj}_{\vec{u}}(\vec{v}) = \frac{\langle\vec{v},\vec{u}\rangle}{\langle\vec{u},\vec{u}\rangle}\vec{u}\).</p>
<p>The remainder \(\vec{v} - \text{proj}_{\vec{u}}(\vec{v})\) is automatically orthogonal to \(\vec{u}\). This decomposition into "along \(\vec{u}\)" + "perpendicular to \(\vec{u}\)" is the workhorse of Gram-Schmidt.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\(\text{proj}_{\hat{u}}(\vec{v}) = \langle\vec{v},\hat{u}\rangle\) ___.", "answer": "u"},
         {"type": "multiple-choice", "question": r"\(\vec{v} - \text{proj}_{\hat{u}}(\vec{v})\) is:", "options": [r"parallel to \(\hat{u}\)", r"orthogonal to \(\hat{u}\)", r"the zero vector", "always longer than v"], "correctIndex": 1},
         {"type": "true-false", "question": r"For a unit vector \(\hat{u}\), the projection has length \(|\langle\vec{v},\hat{u}\rangle|\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"The denominator in projection is \(\langle\vec{u},\) ___\(\rangle\).", "answer": "u"},
         {"type": "true-false", "question": "Projection onto a line is a linear transformation.", "correctAnswer": True}]},
    {"title": "Orthogonal Projection onto a Subspace",
     "body_html": r"""
<p>Given an orthonormal basis \(\{\vec{q}_1, \ldots, \vec{q}_k\}\) of a subspace \(W\), the projection of \(\vec{v}\) onto \(W\) is the sum of one-dimensional projections:</p>
<div class="math-block">$$\text{proj}_W(\vec{v}) = \sum_{i=1}^k \langle\vec{v},\vec{q}_i\rangle\,\vec{q}_i$$</div>
<p>If the basis isn't orthonormal, things are messier — you can use the matrix form: stacking basis vectors as columns of \(A\), the projection is \(A(A^T A)^{-1} A^T \vec{v}\).</p>
<p><strong>Key property:</strong> \(\vec{v} - \text{proj}_W(\vec{v}) \in W^\perp\). The projection is the closest point in \(W\) to \(\vec{v}\).</p>""",
     "exercises": [
         {"type": "true-false", "question": r"With an orthonormal basis, projection is a sum of inner products with basis vectors.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"For columns of \(A\) NOT orthonormal, the projection matrix is:", "options": [r"\(AA^T\)", r"\(A(A^TA)^{-1}A^T\)", r"\(A^T A\)", r"\(A^{-1}\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\vec{v} - \text{proj}_W(\vec{v})\) lies in ___.", "answer": "W^perp"},
         {"type": "true-false", "question": r"\(\text{proj}_W(\vec{v})\) is the closest point in \(W\) to \(\vec{v}\).", "correctAnswer": True},
         {"type": "true-false", "question": r"Projecting twice does nothing more than projecting once: \(P^2 = P\).", "correctAnswer": True}]},
    {"title": "The Projection Matrix",
     "body_html": r"""
<p>The matrix form of orthogonal projection: if \(A\) has linearly independent columns spanning \(W\),</p>
<div class="math-block">$$P = A(A^T A)^{-1} A^T$$</div>
<p>This \(P\) projects any \(\vec{v}\) onto \(W\): \(P\vec{v} = \text{proj}_W(\vec{v})\).</p>
<p>Properties of any projection matrix:</p>
<ul>
<li><strong>Idempotent:</strong> \(P^2 = P\).</li>
<li><strong>Symmetric:</strong> \(P^T = P\).</li>
<li><strong>Rank:</strong> \(\text{rank}(P) = \dim W\).</li>
<li><strong>Eigenvalues:</strong> \(0\) and \(1\) only.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": r"Projection matrices satisfy \(P^2 = P\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Eigenvalues of any projection matrix are:", "options": ["only 0", "only 1", "0 and 1", "anything"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"Orthogonal projection matrices satisfy \(P^T =\) ___.", "answer": "P"},
         {"type": "true-false", "question": r"\(\text{rank}(P) = \dim W\) where \(W\) is the projection target.", "correctAnswer": True},
         {"type": "true-false", "question": r"Projection matrices are invertible.", "correctAnswer": False}]},
    {"title": "Decomposing a Vector",
     "body_html": r"""
<p>For any subspace \(W\) and any vector \(\vec{v}\), we can write</p>
<div class="math-block">$$\vec{v} = \underbrace{\text{proj}_W(\vec{v})}_{\in W} + \underbrace{(\vec{v} - \text{proj}_W(\vec{v}))}_{\in W^\perp}$$</div>
<p>This decomposition is <strong>unique</strong>. The two pieces are mutually orthogonal, and Pythagoras gives</p>
<div class="math-block">$$\|\vec{v}\|^2 = \|\text{proj}_W(\vec{v})\|^2 + \|\vec{v} - \text{proj}_W(\vec{v})\|^2$$</div>
<p>This is the basis of <strong>least squares</strong>: the best approximation of \(\vec{v}\) inside \(W\) is the projection.</p>""",
     "exercises": [
         {"type": "true-false", "question": "The decomposition into W and W^perp parts is unique.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\|\vec{v}\|^2 = \|\text{proj}_W(\vec{v})\|^2 + \|\vec{v} - \text{proj}_W(\vec{v})\|^?\). Fill: ___.", "answer": "2"},
         {"type": "multiple-choice", "question": "Best approximation to v in W is:", "options": ["the closest point in W to v", "any point in W", "the centroid of W", "v itself"], "correctIndex": 0},
         {"type": "true-false", "question": "Least-squares minimizes the perpendicular distance.", "correctAnswer": True},
         {"type": "true-false", "question": "The two pieces of the decomposition are orthogonal.", "correctAnswer": True}]},
    {"title": "Best Approximation in a Subspace",
     "body_html": r"""
<p><strong>Theorem.</strong> Among all vectors in \(W\), the one closest to \(\vec{v}\) is \(\text{proj}_W(\vec{v})\). That is,</p>
<div class="math-block">$$\min_{\vec{w} \in W} \|\vec{v} - \vec{w}\| = \|\vec{v} - \text{proj}_W(\vec{v})\|$$</div>
<p>This is huge — it converts a hard optimization problem (minimize over a whole subspace) into a single matrix computation.</p>
<p>Applications: linear regression (best fit line in a function space), signal denoising (project onto a low-frequency subspace), data compression (best low-rank approximation), and many more.</p>""",
     "exercises": [
         {"type": "true-false", "question": "The projection is the best approximation in the subspace.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Linear regression is fundamentally a:", "options": ["differentiation", "projection problem", "matrix inversion", "eigenvalue computation"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\min_{\vec{w} \in W} \|\vec{v} - \vec{w}\|\) is achieved at \(\vec{w} = \) ___.", "answer": "proj_W(v)"},
         {"type": "true-false", "question": "Signal denoising can use orthogonal projection.", "correctAnswer": True},
         {"type": "true-false", "question": "Best approximation is unique in inner-product spaces.", "correctAnswer": True}]},
    {"title": "The Gram-Schmidt Process",
     "body_html": r"""
<p>Gram-Schmidt converts any basis \(\{\vec{v}_1, \ldots, \vec{v}_n\}\) into an orthonormal one \(\{\vec{q}_1, \ldots, \vec{q}_n\}\) for the same subspace.</p>
<p><strong>Algorithm.</strong></p>
<ol>
<li>\(\vec{u}_1 = \vec{v}_1\), then \(\vec{q}_1 = \vec{u}_1 / \|\vec{u}_1\|\).</li>
<li>\(\vec{u}_2 = \vec{v}_2 - \langle\vec{v}_2,\vec{q}_1\rangle\vec{q}_1\), then \(\vec{q}_2 = \vec{u}_2/\|\vec{u}_2\|\).</li>
<li>\(\vec{u}_k = \vec{v}_k - \sum_{i &lt; k} \langle\vec{v}_k, \vec{q}_i\rangle\vec{q}_i\), then \(\vec{q}_k = \vec{u}_k/\|\vec{u}_k\|\).</li>
</ol>
<p>At each step, subtract off the projections onto previously-built orthonormal vectors, then normalize.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Gram-Schmidt produces an orthonormal basis from any basis.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\vec{u}_1 = \vec{v}_1\), then \(\vec{q}_1 = \vec{u}_1 /\) ___.", "answer": "||u_1||"},
         {"type": "multiple-choice", "question": "At step k of Gram-Schmidt, you subtract:", "options": ["all v_i for i ≠ k", "the projection of v_k onto each previous q_i", "the average of v_i", "nothing"], "correctIndex": 1},
         {"type": "true-false", "question": "The orthonormal basis from Gram-Schmidt spans the same subspace.", "correctAnswer": True},
         {"type": "true-false", "question": "Gram-Schmidt requires the input vectors to already be orthogonal.", "correctAnswer": False}]},
    {"title": "Modified Gram-Schmidt",
     "body_html": r"""
<p>The classical Gram-Schmidt formula is mathematically correct but <strong>numerically unstable</strong> in finite-precision arithmetic — small roundoff errors accumulate.</p>
<p><strong>Modified Gram-Schmidt</strong> reorders the projections to avoid this. Instead of computing \(\vec{u}_k = \vec{v}_k - \sum \langle\vec{v}_k,\vec{q}_i\rangle\vec{q}_i\) all at once, project away one component at a time:</p>
<ol>
<li>Set \(\vec{u} \leftarrow \vec{v}_k\).</li>
<li>For each \(i = 1, \ldots, k-1\): \(\vec{u} \leftarrow \vec{u} - \langle\vec{u},\vec{q}_i\rangle \vec{q}_i\).</li>
<li>Then \(\vec{q}_k = \vec{u}/\|\vec{u}\|\).</li>
</ol>
<p>Same answer in exact arithmetic, much better numerics. This is what real software uses.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Modified Gram-Schmidt is numerically more stable than classical.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The two algorithms differ in:", "options": ["the answer", "ordering of operations", "the input", "the dimension"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"In modified GS, you project away ___ component(s) at a time.", "answer": "one"},
         {"type": "true-false", "question": "Production software typically uses classical Gram-Schmidt.", "correctAnswer": False},
         {"type": "true-false", "question": "Both algorithms produce the same result in exact arithmetic.", "correctAnswer": True}]},
    {"title": "QR Decomposition: Definition",
     "body_html": r"""
<p>The <strong>QR decomposition</strong> writes a matrix \(A\) (with linearly independent columns) as</p>
<div class="math-block">$$A = QR$$</div>
<p>where \(Q\) has orthonormal columns and \(R\) is upper triangular.</p>
<p>Geometrically: the columns of \(Q\) are an orthonormal basis for the column space of \(A\), and \(R\) records the linear combinations needed to recover \(A\)'s columns from \(Q\)'s.</p>
<p>QR exists for every full-column-rank matrix and is essentially unique (up to signs of diagonal entries of \(R\)).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"In \(A = QR\), \(Q\) has ___ columns.", "answer": "orthonormal"},
         {"type": "multiple-choice", "question": "R in QR is:", "options": ["lower triangular", "upper triangular", "diagonal", "symmetric"], "correctIndex": 1},
         {"type": "true-false", "question": "The columns of Q span the column space of A.", "correctAnswer": True},
         {"type": "true-false", "question": "QR exists for every matrix.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"For a square \(A\), \(Q\) is an ___ matrix.", "answer": "orthogonal"}]},
    {"title": "Computing QR via Gram-Schmidt",
     "body_html": r"""
<p>Apply Gram-Schmidt to the columns \(\vec{a}_1, \ldots, \vec{a}_n\) of \(A\). The orthonormal vectors become the columns of \(Q\).</p>
<p>The matrix \(R\) records the inner products needed: \(R_{ij} = \langle\vec{a}_j, \vec{q}_i\rangle\) for \(i \le j\), and \(0\) below the diagonal. Diagonal entries are the norms \(\|\vec{u}_k\|\).</p>
<p>This yields a clean factorization \(A = QR\). In practice the modified algorithm or a Householder-reflection variant (next lesson) is used for numerical stability.</p>
<p><strong>Use:</strong> QR turns "solve \(A\vec{x} = \vec{b}\)" into "solve \(R\vec{x} = Q^T\vec{b}\)" — a triangular system, easy to back-solve.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Gram-Schmidt on the columns of A produces Q.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(R_{ij}\) for \(i \le j\) equals:", "options": [r"\(\langle\vec{a}_j,\vec{q}_i\rangle\)", r"\(\det(A_{ij})\)", r"the trace", "always 0"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"The diagonal entries \(R_{kk}\) equal \(\|\) ___ \(\|\).", "answer": "u_k"},
         {"type": "true-false", "question": r"\(A\vec{x} = \vec{b}\) becomes \(R\vec{x} = Q^T\vec{b}\), which is triangular.", "correctAnswer": True},
         {"type": "true-false", "question": "Production solvers use classical Gram-Schmidt for QR.", "correctAnswer": False}]},
    {"title": "Householder Reflections (Preview)",
     "body_html": r"""
<p>An alternative way to compute QR uses <strong>Householder reflections</strong>. A Householder matrix has the form</p>
<div class="math-block">$$H = I - 2\hat{u}\hat{u}^T$$</div>
<p>for a unit vector \(\hat{u}\). It reflects across the hyperplane perpendicular to \(\hat{u}\). Applying a sequence of cleverly-chosen Householder reflections to \(A\) zeros out entries below the diagonal one column at a time, producing the upper-triangular \(R\).</p>
<p>Householder QR is more accurate than Gram-Schmidt and is what LAPACK uses internally. Each \(H\) is orthogonal, so the product is too — that becomes \(Q\).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Householder matrices are orthogonal.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(H = I - 2\hat{u}\hat{u}^T\) represents:", "options": ["a rotation", "a reflection", "a projection", "a shear"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Householder QR is what production library ___ uses.", "answer": "LAPACK"},
         {"type": "true-false", "question": "Householder QR is generally more numerically stable than Gram-Schmidt.", "correctAnswer": True},
         {"type": "true-false", "question": r"\(H^2 = I\) for any Householder reflection.", "correctAnswer": True}]},
    {"title": "Solving Least Squares with QR",
     "body_html": r"""
<p>Given an overdetermined system \(A\vec{x} = \vec{b}\) (more equations than unknowns), the <strong>least-squares solution</strong> minimizes \(\|A\vec{x} - \vec{b}\|\). It satisfies the <strong>normal equations</strong> \(A^T A \vec{x} = A^T \vec{b}\).</p>
<p>QR makes this clean: with \(A = QR\), the normal equations become</p>
<div class="math-block">$$R\vec{x} = Q^T \vec{b}$$</div>
<p>which is upper-triangular and trivial to solve by back-substitution. No matrix inversion, better numerical conditioning than going through \(A^TA\) directly.</p>
<p>This is the standard way to fit a linear model to data.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Normal equations: \(A^T A \vec{x} = A^T\) ___.", "answer": "b"},
         {"type": "multiple-choice", "question": "QR-based least squares solves:", "options": [r"\(R\vec{x} = Q^T\vec{b}\)", r"\(R\vec{x} = \vec{b}\)", r"\(Q\vec{x} = \vec{b}\)", r"\(A^T\vec{x} = R\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Least-squares minimizes the L² norm of the residual.", "correctAnswer": True},
         {"type": "true-false", "question": "QR avoids computing A^T A explicitly, improving conditioning.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Triangular systems are solved by ___-substitution.", "answer": "back"}]},
    {"title": "Orthogonal Matrices Recap",
     "body_html": r"""
<p>An <strong>orthogonal matrix</strong> \(Q\) satisfies \(Q^T Q = QQ^T = I\) — equivalently, its columns (and rows) form an orthonormal basis.</p>
<p>Properties:</p>
<ul>
<li>\(Q^{-1} = Q^T\) (cheap to invert!).</li>
<li>Preserves length: \(\|Q\vec{v}\| = \|\vec{v}\|\).</li>
<li>Preserves angles and inner products: \(\langle Q\vec{u}, Q\vec{v}\rangle = \langle\vec{u},\vec{v}\rangle\).</li>
<li>\(\det Q = \pm 1\). \(+1\) is a rotation, \(-1\) includes a reflection.</li>
<li>Eigenvalues are on the unit circle (\(|\lambda| = 1\)).</li>
</ul>
<p>Orthogonal matrices are the "rigid motions" — rotations and reflections — that preserve all geometric structure.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Orthogonal matrices preserve length.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"For orthogonal \(Q\), \(Q^{-1} =\)", "options": [r"\(Q\)", r"\(Q^T\)", r"\(-Q\)", r"\(I-Q\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\det Q = \pm\) ___.", "answer": "1"},
         {"type": "true-false", "question": "Orthogonal matrices preserve inner products.", "correctAnswer": True},
         {"type": "true-false", "question": "Eigenvalues of an orthogonal matrix lie on the unit circle.", "correctAnswer": True}]},
    {"title": "Practice: Project & Decompose",
     "body_html": r"""
<p>Try these by hand.</p>
<ol>
<li>Project \(\vec{v} = (3,4)\) onto \(\vec{u} = (1,0)\): result \((3, 0)\). Residual \((0,4)\) is orthogonal.</li>
<li>Gram-Schmidt on \(\{(1,1), (1,0)\}\): \(\vec{q}_1 = (1,1)/\sqrt{2}\). \(\vec{u}_2 = (1,0) - \langle(1,0),\vec{q}_1\rangle\vec{q}_1 = (1,0) - \tfrac{1}{\sqrt 2}\vec{q}_1 = (\tfrac{1}{2},-\tfrac{1}{2})\). Normalize: \(\vec{q}_2 = (1,-1)/\sqrt{2}\).</li>
<li>Project \(\vec{v} = (1,2,3)\) onto the \(xy\)-plane: \((1,2,0)\).</li>
</ol>""",
     "exercises": [
         {"type": "multiple-choice", "question": r"Project \((3,4)\) onto the x-axis:", "options": [r"\((3,0)\)", r"\((0,4)\)", r"\((4,0)\)", r"\((3,4)\)"], "correctIndex": 0},
         {"type": "fill-blank", "question": r"Project \((1,2,3)\) onto the xy-plane: 3rd coord is ___.", "answer": "0"},
         {"type": "true-false", "question": "Gram-Schmidt on (1,1), (1,0) yields the orthonormal basis (1,1)/√2, (1,-1)/√2.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\|(3,0)\| = \) ___.", "answer": "3"},
         {"type": "multiple-choice", "question": r"Residual after projecting \((3,4)\) onto x-axis:", "options": [r"\((0,4)\)", r"\((3,0)\)", r"\((0,0)\)", r"\((4,0)\)"], "correctIndex": 0}]},
    {"title": "Orthogonality Checkpoint",
     "body_html": r"""
<p>Recap of Unit 27:</p>
<ul>
<li>Orthogonal complement \(W^\perp\): \(V = W \oplus W^\perp\).</li>
<li>Projection onto a line uses one inner product; onto a subspace uses an orthonormal basis.</li>
<li>Projection matrices: \(P^2 = P\), \(P^T = P\), eigenvalues 0 and 1.</li>
<li>Best approximation theorem: projection minimizes distance.</li>
<li>Gram-Schmidt produces orthonormal bases; modified version is more stable.</li>
<li>QR decomposition: \(A = QR\) with \(Q\) orthonormal-columned and \(R\) upper triangular.</li>
<li>QR is the right tool for least-squares.</li>
<li>Orthogonal matrices preserve length, angles, and inner products.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Projection matrices are idempotent.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"In \(A = QR\), \(R\) is:", "options": ["lower triangular", "upper triangular", "diagonal", "orthogonal"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"For an orthogonal \(Q\), \(Q^TQ =\) ___.", "answer": "I"},
         {"type": "true-false", "question": r"\((W^\perp)^\perp = W\) for finite-dim \(W\).", "correctAnswer": True},
         {"type": "true-false", "question": "Least-squares minimizes the perpendicular distance from b to the column space of A.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Householder matrices have the form \(I - 2\hat{u}\hat{u}^?\). Fill: ___.", "answer": "T"},
         {"type": "true-false", "question": "Production QR algorithms typically use Householder reflections.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(27, "Orthogonality & QR Decomposition", 391, LESSONS)
