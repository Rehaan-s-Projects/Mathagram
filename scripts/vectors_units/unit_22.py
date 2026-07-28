#!/usr/bin/env python3
"""Unit 22 — Linear Transformations (lessons 316-330)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

UNIT_NUM = 22
UNIT_NAME = "Linear Transformations"
START = 316

LESSONS = [
    {
        "title": "What Is a Linear Transformation?",
        "body_html": r"""
<p>A <strong>linear transformation</strong> is a function \(T: V \to W\) between vector spaces that respects vector addition and scalar multiplication. It's the most well-behaved kind of function — and matrix multiplication is exactly how we compute one.</p>
<p>Concretely, \(T\) is linear if it satisfies the two <strong>linearity axioms</strong>:</p>
<div class="math-block">$$T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v}), \qquad T(c\vec{v}) = cT(\vec{v})$$</div>
<p>Geometrically, linear transformations send the origin to the origin, send straight lines to straight lines, and send parallel lines to parallel lines. They include rotations, scalings, reflections, projections, and shears — but NOT translations.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(T(\vec{0}) = \vec{0}\) for every linear transformation \(T\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Which is NOT a linear transformation?",
             "options": ["Rotation", "Scaling", "Translation", "Reflection"], "correctIndex": 2},
            {"type": "true-false", "question": "Linear transformations send straight lines to straight lines.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"For a linear \(T\), \(T(3\vec{v}) = 3 \cdot\) ___.", "answer": "T(v)"},
            {"type": "multiple-choice", "question": r"\(T(\vec{u}+\vec{v}) =\)",
             "options": [r"\(T(\vec{u}) - T(\vec{v})\)", r"\(T(\vec{u}) + T(\vec{v})\)", r"\(T(\vec{u}) \cdot T(\vec{v})\)", r"\(\vec{u} + \vec{v}\)"], "correctIndex": 1}
        ]
    },
    {
        "title": "The Two Linearity Axioms",
        "body_html": r"""
<p>To prove a function \(T\) is linear, you check the two axioms:</p>
<ul>
<li><strong>Additivity:</strong> \(T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})\) for all \(\vec{u}, \vec{v}\).</li>
<li><strong>Homogeneity:</strong> \(T(c\vec{v}) = c\,T(\vec{v})\) for all scalars \(c\) and vectors \(\vec{v}\).</li>
</ul>
<p>These can be combined into a single condition: \(T(c\vec{u} + d\vec{v}) = cT(\vec{u}) + dT(\vec{v})\) — \(T\) <strong>respects linear combinations</strong>.</p>
<p><strong>Why \(T(0)=0\)?</strong> Plug \(c=0\) into homogeneity: \(T(0\vec{v}) = 0 \cdot T(\vec{v}) = \vec{0}\). So a fast disqualifier: if \(T(\vec{0}) \neq \vec{0}\), \(T\) is NOT linear.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(T(\vec{x}) = \vec{x} + \vec{c}\) (\(\vec{c}\) constant nonzero) is linear.", "correctAnswer": False},
            {"type": "multiple-choice", "question": r"Which condition combines both axioms?",
             "options": [r"\(T(\vec{u}) = \vec{u}\)", r"\(T(c\vec{u} + d\vec{v}) = cT(\vec{u})+dT(\vec{v})\)", r"\(T(\vec{0}) = \vec{0}\)", r"\(T(\vec{u}+\vec{v})=T(\vec{u})\)"], "correctIndex": 1},
            {"type": "true-false", "question": r"If \(T(\vec{0}) \neq \vec{0}\), \(T\) cannot be linear.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"Is \(T(x,y) = (x^2, y)\) linear? (yes/no)", "answer": "no"},
            {"type": "true-false", "question": r"\(T(x,y) = (2x, 3y)\) is linear.", "correctAnswer": True}
        ]
    },
    {
        "title": "Stretches, Rotations & Reflections",
        "body_html": r"""
<p>Three families of linear transformations to know cold:</p>
<ul>
<li><strong>Scaling:</strong> \(\begin{bmatrix} k & 0 \\ 0 & k \end{bmatrix}\) stretches/shrinks by factor \(k\).</li>
<li><strong>Rotation by \(\theta\):</strong> \(R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}\).</li>
<li><strong>Reflection across the x-axis:</strong> \(\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\). Across \(y\)-axis: \(\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}\).</li>
</ul>
<p><strong>Shear:</strong> \(\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}\) slides points horizontally proportional to height. <strong>Projection</strong> onto the x-axis: \(\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\).</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"\(R_{90°} =\)",
             "options": [r"\(\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\)", r"\(\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\)", r"\(\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}\)", r"\(\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\)"], "correctIndex": 0},
            {"type": "true-false", "question": r"\(\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\) reflects across the x-axis.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"A scaling by factor \(3\) in 2D has matrix \(3I\); its determinant is ___.", "answer": "9"},
            {"type": "multiple-choice", "question": r"What does \(\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}\) do?",
             "options": ["scaling", "shear", "projection", "rotation"], "correctIndex": 1},
            {"type": "true-false", "question": "Projections are linear but not invertible.", "correctAnswer": True}
        ]
    },
    {
        "title": "Matrix of a Linear Transformation",
        "body_html": r"""
<p>Every linear transformation \(T: \mathbb{R}^n \to \mathbb{R}^m\) corresponds to a unique \(m \times n\) matrix \(A\). To find \(A\): apply \(T\) to each standard basis vector. The resulting vectors become the columns of \(A\).</p>
<div class="math-block">$$A = \begin{bmatrix} | & | & & | \\ T(\vec{e}_1) & T(\vec{e}_2) & \cdots & T(\vec{e}_n) \\ | & | & & | \end{bmatrix}$$</div>
<p><strong>Example.</strong> \(T(x,y) = (x+2y, 3x-y)\). Then \(T(\vec{e}_1) = T(1,0) = (1,3)\), \(T(\vec{e}_2) = T(0,1) = (2,-1)\). So \(A = \begin{bmatrix} 1 & 2 \\ 3 & -1 \end{bmatrix}\).</p>
<p>This is the bridge between abstract linear maps and concrete matrices: <strong>they're the same thing seen two ways</strong>.</p>
""",
        "exercises": [
            {"type": "multiple-choice", "question": r"For \(T(x,y) = (2x, 3y)\), the matrix is:",
             "options": [r"\(\begin{bmatrix} 2 & 3 \\ 0 & 0 \end{bmatrix}\)", r"\(\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}\)", r"\(\begin{bmatrix} 0 & 2 \\ 3 & 0 \end{bmatrix}\)", r"\(\begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}\)"], "correctIndex": 1},
            {"type": "true-false", "question": r"The columns of the matrix of \(T\) are \(T(\vec{e}_i)\).", "correctAnswer": True},
            {"type": "fill-blank", "question": r"For \(T(x,y) = (x+y, x-y)\), the top-left entry of its matrix is ___.", "answer": "1"},
            {"type": "multiple-choice", "question": r"\(T: \mathbb{R}^4 \to \mathbb{R}^2\) has a matrix of shape:",
             "options": [r"\(4 \times 2\)", r"\(2 \times 4\)", r"\(4 \times 4\)", r"\(2 \times 2\)"], "correctIndex": 1},
            {"type": "true-false", "question": "Different linear transformations can share the same matrix.", "correctAnswer": False}
        ]
    },
    {
        "title": "Composition of Linear Transformations",
        "body_html": r"""
<p>If \(S\) and \(T\) are linear transformations and the composition \(S \circ T\) is defined, then \(S \circ T\) is also linear, and its matrix is the <strong>product</strong> of the individual matrices:</p>
<div class="math-block">$$\text{matrix}(S \circ T) = \text{matrix}(S) \cdot \text{matrix}(T)$$</div>
<p>This is the geometric reason matrix multiplication is defined the way it is — it's just function composition.</p>
<p><strong>Order matters!</strong> \((S \circ T)(\vec{v}) = S(T(\vec{v}))\) — \(T\) first, then \(S\). That's why the matrix product reads "right-to-left." This is also why matrix multiplication isn't commutative: rotating-then-shearing isn't the same as shearing-then-rotating.</p>
""",
        "exercises": [
            {"type": "true-false", "question": "The composition of two linear maps is linear.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"If \(T\) has matrix \(A\) and \(S\) has matrix \(B\), then \(S\circ T\) has matrix:",
             "options": [r"\(A B\)", r"\(B A\)", r"\(A + B\)", r"\(A^T B\)"], "correctIndex": 1},
            {"type": "true-false", "question": r"In general, \(S \circ T = T \circ S\).", "correctAnswer": False},
            {"type": "fill-blank", "question": r"The composition \(R_{30°} \circ R_{60°}\) is a rotation by ___ degrees.", "answer": "90"},
            {"type": "multiple-choice", "question": r"Apply \(T\) then \(S\): which evaluates first?",
             "options": [r"\(S\) first", r"\(T\) first", "they evaluate together", "depends on dimension"], "correctIndex": 1}
        ]
    },
    {
        "title": "The Kernel (Null Space)",
        "body_html": r"""
<p>The <strong>kernel</strong> of a linear transformation \(T\), written \(\ker(T)\) or \(\text{null}(A)\), is the set of vectors that \(T\) sends to zero:</p>
<div class="math-block">$$\ker(T) = \{\vec{v} : T(\vec{v}) = \vec{0}\}$$</div>
<p>The kernel is always a <strong>subspace</strong> of the domain (it contains \(\vec{0}\) and is closed under addition and scaling).</p>
<p><strong>Example.</strong> Projection onto the \(x\)-axis: \(T(x,y) = (x,0)\). The kernel is \(\{(0,y) : y \in \mathbb{R}\}\) — the entire \(y\)-axis collapses to zero.</p>
<p>To find the kernel of a matrix \(A\), solve \(A\vec{v} = \vec{0}\) — a homogeneous linear system.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(\vec{0}\) is always in \(\ker(T)\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(\ker(T)\) is always a:",
             "options": ["line", "plane", "subspace", "vector"], "correctIndex": 2},
            {"type": "fill-blank", "question": r"For \(T(x,y) = (x, 0)\), \(\ker(T)\) is the ___-axis.", "answer": "y"},
            {"type": "true-false", "question": r"If \(\ker(T) = \{\vec{0}\}\), then \(T\) sends only the zero vector to zero.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"Find \(\ker\) of \(\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\):",
             "options": [r"\(\{0\}\)", r"the line \(y=-x\)", r"the line \(y=x\)", r"\(\mathbb{R}^2\)"], "correctIndex": 1}
        ]
    },
    {
        "title": "The Image (Range)",
        "body_html": r"""
<p>The <strong>image</strong> (or <strong>range</strong>) of \(T: V \to W\), written \(\text{im}(T)\) or \(\text{range}(T)\), is the set of all output vectors:</p>
<div class="math-block">$$\text{im}(T) = \{T(\vec{v}) : \vec{v} \in V\}$$</div>
<p>For a matrix \(A\), the image is the <strong>column space</strong> — the span of the columns of \(A\). It's always a subspace of the codomain.</p>
<p><strong>Example.</strong> \(A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}\). Both columns are multiples of \((1,2)\), so \(\text{im}(A)\) is the line through the origin in direction \((1,2)\) — a 1-dimensional subspace of \(\mathbb{R}^2\).</p>
""",
        "exercises": [
            {"type": "true-false", "question": "The image of a matrix is the span of its columns.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"For \(\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\), the image is:",
             "options": [r"all of \(\mathbb{R}^2\)", "the x-axis", "the y-axis", r"\(\{0\}\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"For an \(n \times n\) identity matrix, \(\text{im}\) is all of \(\mathbb{R}^?\). Fill: ___.", "answer": "n"},
            {"type": "true-false", "question": r"\(\text{im}(T)\) is always a subspace of the codomain.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"For \(\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}\), \(\text{im}\) is:",
             "options": ["the origin only", "a line", "all of R²", "two lines"], "correctIndex": 1}
        ]
    },
    {
        "title": "Rank of a Linear Transformation",
        "body_html": r"""
<p>The <strong>rank</strong> of \(T\) (or matrix \(A\)) is the dimension of its image:</p>
<div class="math-block">$$\text{rank}(A) = \dim(\text{im}(A)) = \dim(\text{column space of } A)$$</div>
<p>It tells you how many linearly independent columns \(A\) has — that is, how "big" the output space is.</p>
<p><strong>Examples.</strong></p>
<ul>
<li>\(\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\) has rank \(2\) (full rank).</li>
<li>\(\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}\) has rank \(1\) (one redundant column).</li>
<li>\(\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}\) has rank \(0\).</li>
</ul>
<p>For an \(m \times n\) matrix, \(\text{rank}(A) \le \min(m,n)\). Equal rank to \(\min(m,n)\) means "full rank."</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"\(\text{rank}(I_3) =\) ___.", "answer": "3"},
            {"type": "multiple-choice", "question": r"\(\text{rank} \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} =\)",
             "options": ["0", "1", "2", "4"], "correctIndex": 1},
            {"type": "true-false", "question": r"For an \(m \times n\) matrix, \(\text{rank} \le \min(m,n)\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Rank measures the:",
             "options": ["height", "width", "number of independent columns", "trace"], "correctIndex": 2},
            {"type": "true-false", "question": "A zero matrix has rank 0.", "correctAnswer": True}
        ]
    },
    {
        "title": "Nullity & The Rank-Nullity Theorem",
        "body_html": r"""
<p>The <strong>nullity</strong> of \(T\) is the dimension of its kernel:</p>
<div class="math-block">$$\text{nullity}(A) = \dim(\ker(A))$$</div>
<p>The <strong>Rank-Nullity Theorem</strong> connects rank and nullity to the input dimension. For \(T: \mathbb{R}^n \to \mathbb{R}^m\):</p>
<div class="math-block">$$\text{rank}(T) + \text{nullity}(T) = n$$</div>
<p>This says: every direction in the domain is either preserved (contributes to rank) or collapsed (contributes to nullity). Nothing is lost or duplicated.</p>
<p><strong>Example.</strong> Projection \(\mathbb{R}^3 \to \mathbb{R}^3\) onto the \(xy\)-plane has rank \(2\) (image is the plane) and nullity \(1\) (kernel is the \(z\)-axis). \(2 + 1 = 3\). ✓</p>
""",
        "exercises": [
            {"type": "fill-blank", "question": r"For \(T: \mathbb{R}^5 \to \mathbb{R}^7\) with rank \(3\), nullity \(=\) ___.", "answer": "2"},
            {"type": "multiple-choice", "question": r"For projection in \(\mathbb{R}^3\) onto the \(xy\)-plane, nullity \(=\):",
             "options": ["0", "1", "2", "3"], "correctIndex": 1},
            {"type": "true-false", "question": r"\(\text{rank}(T) + \text{nullity}(T)\) equals the dimension of the domain.", "correctAnswer": True},
            {"type": "fill-blank", "question": r"For an injective \(T\), \(\text{nullity}(T) =\) ___.", "answer": "0"},
            {"type": "multiple-choice", "question": r"For \(I_n\), nullity equals:",
             "options": ["0", "1", "n", r"\(n-1\)"], "correctIndex": 0}
        ]
    },
    {
        "title": "Injective (One-to-One) Transformations",
        "body_html": r"""
<p>\(T\) is <strong>injective</strong> (one-to-one) if different inputs always produce different outputs:</p>
<div class="math-block">$$T(\vec{u}) = T(\vec{v}) \implies \vec{u} = \vec{v}$$</div>
<p>For a linear transformation, this is equivalent to a much simpler condition:</p>
<div class="math-block">$$T \text{ is injective} \iff \ker(T) = \{\vec{0}\}$$</div>
<p>That is: only the zero vector maps to zero. Equivalently: nullity is \(0\), or rank equals the domain dimension.</p>
<p>Why? If \(T(\vec{u}) = T(\vec{v})\), linearity gives \(T(\vec{u}-\vec{v}) = \vec{0}\), so \(\vec{u}-\vec{v}\) lies in the kernel.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"A linear \(T\) is injective iff \(\ker(T) = \{\vec{0}\}\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Injective linear transformations have nullity:",
             "options": ["1", "0", "n", "depends"], "correctIndex": 1},
            {"type": "true-false", "question": "Projection in 3D onto a plane is injective.", "correctAnswer": False},
            {"type": "multiple-choice", "question": r"\(T(x) = 2x\) on \(\mathbb{R}\) is:",
             "options": ["injective", "not injective", "constant", "undefined"], "correctIndex": 0},
            {"type": "fill-blank", "question": r"For an injective \(T: \mathbb{R}^n \to \mathbb{R}^m\), the rank equals ___.", "answer": "n"}
        ]
    },
    {
        "title": "Surjective (Onto) Transformations",
        "body_html": r"""
<p>\(T: V \to W\) is <strong>surjective</strong> (onto) if every vector in \(W\) is hit by some input:</p>
<div class="math-block">$$\forall \vec{w} \in W,\ \exists \vec{v} \in V \text{ with } T(\vec{v}) = \vec{w}$$</div>
<p>Equivalently: \(\text{im}(T) = W\), or \(\text{rank}(T) = \dim(W)\).</p>
<p>Combining with rank-nullity: a linear \(T: \mathbb{R}^n \to \mathbb{R}^m\) is surjective iff \(\text{rank}(T) = m\). This requires \(n \ge m\) — you can't surject from a lower-dimensional space onto a higher one.</p>
<p><strong>Example.</strong> \(T: \mathbb{R}^3 \to \mathbb{R}^2\) given by dropping the \(z\)-coordinate is surjective: every \((x,y) \in \mathbb{R}^2\) is hit.</p>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(T\) is surjective iff its image equals the codomain.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\(T: \mathbb{R}^2 \to \mathbb{R}^3\) can be:",
             "options": ["surjective", "not surjective", "always injective", "always rank 3"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"A surjective \(T: \mathbb{R}^n \to \mathbb{R}^m\) needs rank \(=\) ___.", "answer": "m"},
            {"type": "true-false", "question": r"You can have a surjective linear map \(\mathbb{R}^2 \to \mathbb{R}^3\).", "correctAnswer": False},
            {"type": "multiple-choice", "question": "Surjective + injective is called:",
             "options": ["partial", "bijective", "subjective", "monomorphic"], "correctIndex": 1}
        ]
    },
    {
        "title": "Invertible Transformations",
        "body_html": r"""
<p>A linear \(T: V \to W\) is <strong>invertible</strong> if there exists \(T^{-1}\) such that \(T^{-1} \circ T = \text{id}_V\) and \(T \circ T^{-1} = \text{id}_W\).</p>
<p>For a linear map: <strong>invertible \(\iff\) bijective \(\iff\) injective AND surjective</strong>.</p>
<p>Between equal-dimensional spaces, this collapses to a single test: \(T\) is invertible iff its matrix has nonzero determinant. Equivalently, full rank, or trivial kernel — pick your favorite.</p>
<div class="math-block">$$T \text{ invertible} \iff \det A \neq 0 \iff \text{rank}(A) = n \iff \ker(A) = \{\vec{0}\}$$</div>
""",
        "exercises": [
            {"type": "true-false", "question": "A linear map is invertible iff bijective.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"A square matrix \(A\) is invertible iff:",
             "options": [r"\(\det A = 0\)", r"\(\det A \neq 0\)", r"\(A = A^T\)", r"\(A = I\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"For invertible \(T\), \(\ker(T) =\) ___.", "answer": "{0}"},
            {"type": "true-false", "question": r"If \(\det A = 0\), the system \(A\vec{x} = \vec{b}\) always has a unique solution.", "correctAnswer": False},
            {"type": "multiple-choice", "question": "Non-square matrices are:",
             "options": ["always invertible", "never invertible", "invertible if det = 1", "invertible if symmetric"], "correctIndex": 1}
        ]
    },
    {
        "title": "Change of Basis Matrix",
        "body_html": r"""
<p>A vector \(\vec{v}\) doesn't change, but its <strong>coordinates</strong> change depending on the basis you use. To switch coordinates between two bases, you multiply by a <strong>change of basis matrix</strong>.</p>
<p>If \(\mathcal{B} = \{\vec{b}_1, \ldots, \vec{b}_n\}\) is a basis, the change-of-basis matrix \(P_\mathcal{B}\) has the basis vectors as columns:</p>
<div class="math-block">$$P_\mathcal{B} = \begin{bmatrix} | & & | \\ \vec{b}_1 & \cdots & \vec{b}_n \\ | & & | \end{bmatrix}$$</div>
<p>Then \([\vec{v}]_{\text{std}} = P_\mathcal{B} \cdot [\vec{v}]_\mathcal{B}\) (basis coords → standard coords). To go the other way: \([\vec{v}]_\mathcal{B} = P_\mathcal{B}^{-1} \cdot [\vec{v}]_{\text{std}}\).</p>
<p>To express a transformation \(T\) in the new basis: \([T]_\mathcal{B} = P^{-1} A P\). This is called <strong>conjugation</strong> by \(P\).</p>
""",
        "exercises": [
            {"type": "true-false", "question": "A vector's coordinates depend on the chosen basis.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"To express \(T\) in a new basis, we form:",
             "options": [r"\(P + A\)", r"\(P^{-1} A P\)", r"\(A^T\)", r"\(PA\)"], "correctIndex": 1},
            {"type": "fill-blank", "question": r"The change-of-basis matrix has the new basis vectors as its ___.", "answer": "columns"},
            {"type": "true-false", "question": "Change-of-basis matrices are always invertible.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"\([\vec{v}]_\mathcal{B} =\)",
             "options": [r"\(P [\vec{v}]_{\text{std}}\)", r"\(P^{-1} [\vec{v}]_{\text{std}}\)", r"\(P^T [\vec{v}]_{\text{std}}\)", r"\([\vec{v}]_{\text{std}}\)"], "correctIndex": 1}
        ]
    },
    {
        "title": "Practice: Identify Linear Transformations",
        "body_html": r"""
<p>A linear transformation must satisfy <strong>two checks</strong>:</p>
<ol>
<li>\(T(\vec{0}) = \vec{0}\) — fastest disqualifier.</li>
<li>\(T(c\vec{u} + d\vec{v}) = cT(\vec{u}) + dT(\vec{v})\) — the linearity condition.</li>
</ol>
<p>Run through these examples and decide.</p>
<ul>
<li>\(T(x,y) = (3x-y, x+2y)\) — linear (each output is a linear combination of inputs).</li>
<li>\(T(x,y) = (x^2, y)\) — NOT linear (\(x^2\) breaks homogeneity).</li>
<li>\(T(x,y) = (x+1, y)\) — NOT linear (\(T(\vec{0}) = (1,0) \neq \vec{0}\)).</li>
<li>\(T(x,y) = (\sin x, y)\) — NOT linear.</li>
<li>\(T(x,y,z) = (x+y, y+z)\) — linear.</li>
</ul>
""",
        "exercises": [
            {"type": "true-false", "question": r"\(T(x,y) = (x^2, y)\) is linear.", "correctAnswer": False},
            {"type": "true-false", "question": r"\(T(x,y) = (3x-y, x+2y)\) is linear.", "correctAnswer": True},
            {"type": "multiple-choice", "question": r"Which of these is linear?",
             "options": [r"\(T(x) = x+5\)", r"\(T(x) = 7x\)", r"\(T(x) = x^2\)", r"\(T(x) = \sin(x)\)"], "correctIndex": 1},
            {"type": "true-false", "question": r"\(T(x,y) = (x+1, y)\) is linear.", "correctAnswer": False},
            {"type": "multiple-choice", "question": r"Which fails first for \(T(x,y) = (x+1, y)\)?",
             "options": [r"homogeneity", r"\(T(\vec{0}) = \vec{0}\)", "additivity", "all of the above"], "correctIndex": 1}
        ]
    },
    {
        "title": "Linear Transformations Checkpoint",
        "body_html": r"""
<p>Quick recap of Unit 22:</p>
<ul>
<li>Linear transformations preserve addition and scalar multiplication; they correspond exactly to matrix multiplication.</li>
<li>The matrix of \(T\) has the columns \(T(\vec{e}_i)\).</li>
<li>Composition of linear maps = matrix product.</li>
<li>Kernel = inputs sent to zero (a subspace of the domain).</li>
<li>Image = outputs achievable (a subspace of the codomain, equals column space).</li>
<li>Rank = dim of image; nullity = dim of kernel; <strong>rank + nullity = dim(domain)</strong>.</li>
<li>Injective ⇔ kernel \(\{0\}\). Surjective ⇔ image = codomain. Invertible ⇔ both ⇔ \(\det \neq 0\).</li>
</ul>
""",
        "exercises": [
            {"type": "true-false", "question": "Translations are linear transformations.", "correctAnswer": False},
            {"type": "fill-blank", "question": r"For \(T: \mathbb{R}^4 \to \mathbb{R}^4\) with rank 3, nullity = ___.", "answer": "1"},
            {"type": "multiple-choice", "question": r"\(T\) is invertible iff:",
             "options": [r"\(\det A = 0\)", r"\(\ker(T) = \{0\}\) and \(T\) is square", "rank = 1", r"\(T = I\)"], "correctIndex": 1},
            {"type": "true-false", "question": r"\(T(\vec{u}+\vec{v}) = T(\vec{u}) + T(\vec{v})\) for any linear \(T\).", "correctAnswer": True},
            {"type": "multiple-choice", "question": "Image of a matrix equals its:",
             "options": ["null space", "column space", "row space", "kernel"], "correctIndex": 1},
            {"type": "true-false", "question": "Composition of linear maps corresponds to matrix product (in reverse order).", "correctAnswer": True},
            {"type": "fill-blank", "question": r"Geometrically, the matrix \(\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\) is rotation by ___ degrees.", "answer": "90"}
        ]
    },
]

if __name__ == "__main__":
    render_unit(UNIT_NUM, UNIT_NAME, START, LESSONS)
