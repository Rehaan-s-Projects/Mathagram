#!/usr/bin/env python3
"""Unit 37 — Tensors: An Introduction (lessons 541-555)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "From Vectors to Tensors",
     "body_html": r"""
<p>A <strong>tensor</strong> is a generalization of vectors and matrices: an object that takes \(p\) vectors and \(q\) covectors as inputs and produces a scalar in a multilinear way. Vectors (rank 1) and matrices (rank 2) are special cases.</p>
<p>Tensors of different ranks include:</p>
<ul>
<li>Rank 0: scalar (e.g., temperature).</li>
<li>Rank 1: vector or covector (e.g., velocity, gradient).</li>
<li>Rank 2: linear operator or bilinear form (e.g., metric, stress).</li>
<li>Rank 3+: e.g., curvature, elasticity tensors.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Vectors and matrices are special cases of tensors.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "A scalar is a tensor of rank:", "options": ["0", "1", "2", "any"], "correctIndex": 0},
         {"type": "fill-blank", "question": "A linear operator (matrix) is a rank-___ tensor.", "answer": "2"},
         {"type": "true-false", "question": "The stress tensor is rank 2.", "correctAnswer": True},
         {"type": "true-false", "question": "Rank-3 tensors don't exist in physics.", "correctAnswer": False}]},
    {"title": "Tensors as Multilinear Maps",
     "body_html": r"""
<p>A type-(\(p, q\)) tensor takes \(p\) covectors and \(q\) vectors and outputs a scalar, with the output linear in each input slot.</p>
<p>For example, a (1,1) tensor takes a covector and a vector and gives a scalar — exactly the action of a linear operator. The action is computed entirely from the components and the inputs by summing over indices.</p>
<p>Multilinearity means: <strong>linear in each argument separately</strong>. This is what makes tensors well-behaved under transformations.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Multilinear means linear in each argument separately.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "A type-(0,1) tensor takes a vector to:", "options": ["a vector", "a scalar", "a tensor", "a matrix"], "correctIndex": 1},
         {"type": "fill-blank", "question": "A type-(1,1) tensor matches a linear ___.", "answer": "operator"},
         {"type": "true-false", "question": "Tensors are linear in all their arguments.", "correctAnswer": True},
         {"type": "true-false", "question": "Quadratic functions are bilinear.", "correctAnswer": False}]},
    {"title": "Rank of a Tensor",
     "body_html": r"""
<p>The <strong>rank</strong> (or order) of a tensor is the total number of indices it has, ignoring whether they're up or down. Sometimes "type" \((p, q)\) is used to indicate \(p\) upper and \(q\) lower indices.</p>
<p>Rank 0 = scalar. Rank 1 = vector or covector. Rank 2 = matrix-like. Rank 3 = "stack of matrices" (Levi-Civita symbol \(\epsilon_{ijk}\), Riemann curvature \(R^\mu{}_{\nu\rho\sigma}\) which is rank 4).</p>
<p>In Cartesian coordinates the up/down distinction collapses. In curved or non-Cartesian settings it matters.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Rank counts the number of indices.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Levi-Civita symbol εᵢⱼₖ has rank:", "options": ["1", "2", "3", "0"], "correctIndex": 2},
         {"type": "fill-blank", "question": "Riemann curvature tensor has rank ___.", "answer": "4"},
         {"type": "true-false", "question": "In Cartesian, up vs down indices coincide.", "correctAnswer": True},
         {"type": "true-false", "question": "Type (p,q) tensors have p+q total indices.", "correctAnswer": True}]},
    {"title": "Tensor Components",
     "body_html": r"""
<p>Once a basis is chosen, a tensor is fully described by its <strong>components</strong> in that basis. A type-(2,0) tensor in 3D has \(3 \times 3 = 9\) components \(T^{ij}\).</p>
<p><strong>Transformation rule.</strong> Components transform under a change of basis by a specific multilinear rule, with \(p\) factors of the change-of-basis matrix and \(q\) factors of its inverse. This is what makes them tensors — not just arrays of numbers.</p>
<p>"Tensor as multilinear map" is basis-free; "tensor as components with a transformation rule" is basis-dependent. Both views are equivalent.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Tensor components depend on the chosen basis.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"A type-(2,0) tensor in 3D has \(9 = 3 \times\) ___ components.", "answer": "3"},
         {"type": "multiple-choice", "question": "Tensors transform under basis change by:", "options": ["arbitrary functions", "multilinear rules with change matrices", "no rule", "matrix multiplication only"], "correctIndex": 1},
         {"type": "true-false", "question": "A general array of numbers is a tensor.", "correctAnswer": False},
         {"type": "true-false", "question": "Tensors as multilinear maps are basis-free.", "correctAnswer": True}]},
    {"title": "Index Notation Basics",
     "body_html": r"""
<p>Greek indices \(\mu, \nu, \rho\) for spacetime (0–3). Latin indices \(i, j, k\) often for spatial (1–3). Repeated indices, one up and one down, are summed (Einstein convention):</p>
<div class="math-block">$$A^\mu B_\mu = \sum_\mu A^\mu B_\mu$$</div>
<p>Free indices (not summed) appear once on each side of an equation. <strong>Both sides must have the same free indices in the same positions.</strong></p>
<p>Slot order matters: \(T^{\mu\nu}\) and \(T^{\nu\mu}\) are generally different tensors (unless \(T\) is symmetric).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Repeated indices (one up, one down) are summed in Einstein convention.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(A^\mu B_\mu\) is a:", "options": ["vector", "scalar", "matrix", "rank-2 tensor"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Greek indices μ usually run from 0 to ___.", "answer": "3"},
         {"type": "true-false", "question": "Both sides of an equation must have the same free indices.", "correctAnswer": True},
         {"type": "true-false", "question": r"\(T^{\mu\nu}\) and \(T^{\nu\mu}\) are always equal.", "correctAnswer": False}]},
    {"title": "Covariant vs Contravariant",
     "body_html": r"""
<p>Two flavors of vectors:</p>
<ul>
<li><strong>Contravariant</strong> (upper index, e.g., \(V^\mu\)): vectors. Transform "the opposite way" of basis vectors.</li>
<li><strong>Covariant</strong> (lower index, e.g., \(V_\mu\)): covectors / dual vectors. Transform the same way as basis vectors.</li>
</ul>
<p>The names come from how components transform under coordinate changes. The metric \(g_{\mu\nu}\) lets you convert between them by raising/lowering indices.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Upper index = contravariant.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "The metric is used to:", "options": ["count dimensions", "raise/lower indices", "rotate vectors", "compute determinants"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Lower index = ___ vector.", "answer": "covariant"},
         {"type": "true-false", "question": "Covariant and contravariant transform the same way.", "correctAnswer": False},
         {"type": "true-false", "question": "In Euclidean space, upper and lower indices match.", "correctAnswer": True}]},
    {"title": "The Metric Tensor",
     "body_html": r"""
<p>The <strong>metric tensor</strong> \(g_{\mu\nu}\) defines the inner product and lets you raise/lower indices:</p>
<div class="math-block">$$V_\mu = g_{\mu\nu} V^\nu, \quad V^\mu = g^{\mu\nu} V_\nu$$</div>
<p>where \(g^{\mu\nu}\) is the matrix inverse of \(g_{\mu\nu}\) (i.e., \(g^{\mu\rho}g_{\rho\nu} = \delta^\mu{}_\nu\)).</p>
<p><strong>Examples.</strong> In Euclidean 3D Cartesian: \(g_{ij} = \delta_{ij}\). In Minkowski: \(g_{\mu\nu} = \text{diag}(1, -1, -1, -1)\). In curved space, \(g_{\mu\nu}\) varies from point to point — that's what curvature is.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Metric: \\(V_\\mu = g_{\\mu\\nu} V^\\) ___.", "answer": "nu"},
         {"type": "multiple-choice", "question": "Minkowski metric:", "options": ["diag(1,1,1,1)", "diag(1,-1,-1,-1)", "all zeros", "I"], "correctIndex": 1},
         {"type": "true-false", "question": r"\(g^{\mu\nu}\) is the matrix inverse of \(g_{\mu\nu}\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"In Cartesian Euclidean: \(g_{ij} = \delta_{ij}\), no distinction between up and ___.", "answer": "down"},
         {"type": "true-false", "question": "Curvature is encoded in how the metric varies.", "correctAnswer": True}]},
    {"title": "Tensor Product",
     "body_html": r"""
<p>The <strong>tensor product</strong> \(\otimes\) combines a tensor of type \((p_1, q_1)\) with one of type \((p_2, q_2)\) to produce a tensor of type \((p_1+p_2, q_1+q_2)\):</p>
<div class="math-block">$$(T \otimes S)^{\mu_1\ldots\mu_{p_1+p_2}}{}_{\nu_1\ldots\nu_{q_1+q_2}} = T^{\mu\ldots}{}_{\nu\ldots} S^{\mu\ldots}{}_{\nu\ldots}$$</div>
<p>For two vectors: \((V \otimes W)^{\mu\nu} = V^\mu W^\nu\) — a rank-2 tensor formed by all products of components.</p>
<p>The space of tensors of given type forms a vector space, and tensor products generalize the matrix outer product.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"For two vectors: \((V \otimes W)^{\mu\nu} = V^\mu W^?\). Fill: ___.", "answer": "nu"},
         {"type": "multiple-choice", "question": r"Tensor product of two rank-1's gives:", "options": ["a scalar", "rank 2", "rank 3", "rank 0"], "correctIndex": 1},
         {"type": "true-false", "question": "Tensor product is commutative.", "correctAnswer": False},
         {"type": "true-false", "question": "Tensor product generalizes the outer product.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"A type-(p₁,q₁) ⊗ type-(p₂,q₂) is type-(?, q₁+q₂). Fill: ___.", "answer": "p_1+p_2"}]},
    {"title": "Contraction (Trace)",
     "body_html": r"""
<p><strong>Contraction</strong> sums one upper index with one lower index, reducing the rank by 2:</p>
<div class="math-block">$$T^\mu{}_\mu = \sum_\mu T^\mu{}_\mu$$</div>
<p>For a (1,1) tensor (matrix), this is the <strong>trace</strong>. For higher-rank tensors, you can contract any pair of one-up-one-down indices.</p>
<p>Contractions are coordinate-invariant — that's why traces of matrices give scalars that are invariant under changes of basis.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Contraction reduces rank by 2.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Trace = contraction of:", "options": ["two upper indices", "one upper one lower of a (1,1)", "two lower", "rank 0"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Contraction sums one upper and one ___ index.", "answer": "lower"},
         {"type": "true-false", "question": "Trace is coordinate-invariant.", "correctAnswer": True},
         {"type": "true-false", "question": "Contraction works only for (1,1) tensors.", "correctAnswer": False}]},
    {"title": "Symmetric & Antisymmetric Tensors",
     "body_html": r"""
<p>A rank-2 tensor is <strong>symmetric</strong> if \(T^{\mu\nu} = T^{\nu\mu}\), <strong>antisymmetric</strong> if \(T^{\mu\nu} = -T^{\nu\mu}\).</p>
<p>Any rank-2 tensor decomposes uniquely as symmetric + antisymmetric: \(T = \tfrac{1}{2}(T + T^T) + \tfrac{1}{2}(T - T^T)\).</p>
<p>The metric is symmetric. The electromagnetic field strength tensor \(F^{\mu\nu}\) is antisymmetric. Higher ranks have richer symmetry classes.</p>""",
     "exercises": [
         {"type": "true-false", "question": r"\(T^{\mu\nu} = T^{\nu\mu}\) is symmetric.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Electromagnetic field tensor F^{μν}:", "options": ["symmetric", "antisymmetric", "neither", "diagonal"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Any rank-2 tensor splits into symmetric + ___.", "answer": "antisymmetric"},
         {"type": "true-false", "question": "Antisymmetric tensors have zero diagonal entries.", "correctAnswer": True},
         {"type": "true-false", "question": "The metric tensor is symmetric.", "correctAnswer": True}]},
    {"title": "The Kronecker Delta",
     "body_html": r"""
<p>The <strong>Kronecker delta</strong>:</p>
<div class="math-block">$$\delta^\mu{}_\nu = \begin{cases} 1 & \mu = \nu \\ 0 & \text{otherwise} \end{cases}$$</div>
<p>It's the components of the identity matrix viewed as a (1,1) tensor — and is the only invariant tensor of its type. Used everywhere as an "index renamer":</p>
<div class="math-block">$$\delta^\mu{}_\nu T^\nu = T^\mu$$</div>""",
     "exercises": [
         {"type": "fill-blank", "question": "δ^μ_ν is 1 when μ = ν, else ___.", "answer": "0"},
         {"type": "multiple-choice", "question": "Kronecker delta represents:", "options": ["zero", "identity", "metric", "Levi-Civita"], "correctIndex": 1},
         {"type": "true-false", "question": "δ^μ_ν T^ν = T^μ.", "correctAnswer": True},
         {"type": "fill-blank", "question": "δ acts as an index ___.", "answer": "renamer"},
         {"type": "true-false", "question": "Kronecker delta has the same components in every basis.", "correctAnswer": True}]},
    {"title": "The Levi-Civita Symbol",
     "body_html": r"""
<p>The <strong>Levi-Civita symbol</strong> \(\epsilon_{ijk}\) (rank 3, totally antisymmetric):</p>
<ul>
<li>\(\epsilon_{123} = \epsilon_{231} = \epsilon_{312} = +1\)</li>
<li>\(\epsilon_{132} = \epsilon_{213} = \epsilon_{321} = -1\)</li>
<li>Else (any repeat): \(0\).</li>
</ul>
<p>Encodes the cross product: \((\vec a \times \vec b)_i = \epsilon_{ijk} a_j b_k\), and the determinant: \(\det A = \epsilon_{ijk} A_{1i} A_{2j} A_{3k}\). It's a tensor only with appropriate density-weight conventions; in practice it's incredibly useful.</p>""",
     "exercises": [
         {"type": "true-false", "question": "ε is totally antisymmetric.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\epsilon_{123} =\) ___.", "answer": "1"},
         {"type": "multiple-choice", "question": r"\(\epsilon_{ijk} a_j b_k\) gives:", "options": ["dot product", "cross product i-th component", "trace", "determinant"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\epsilon_{122} =\) ___.", "answer": "0"},
         {"type": "true-false", "question": "Levi-Civita can compute determinants by index summation.", "correctAnswer": True}]},
    {"title": "Practice: Tensor Manipulation",
     "body_html": r"""
<p>Try these.</p>
<ol>
<li>\(\delta^\mu{}_\nu T^\nu{}_\rho = T^\mu{}_\rho\). Index renaming.</li>
<li>\(g_{\mu\nu} g^{\nu\rho} = \delta_\mu{}^\rho\). Matrix inversion.</li>
<li>\(\text{tr}(A) = \delta^i{}_j A^j{}_i\) — but note \(\delta^i{}_j A^j{}_i = A^i{}_i\) directly.</li>
<li>Cross product: \((\vec a \times \vec b)_i = \epsilon_{ijk} a_j b_k\). Each component is a sum of \(2\) terms (others vanish).</li>
<li>\(\epsilon_{ijk}\epsilon^{ijl} = 2 \delta_k{}^l\) (a useful identity).</li>
</ol>""",
     "exercises": [
         {"type": "true-false", "question": r"\(\delta^\mu{}_\nu T^\nu = T^\mu\).", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(g_{\mu\nu} g^{\nu\rho} =\)", "options": [r"\(\eta_{\mu\rho}\)", r"\(\delta_\mu{}^\rho\)", "0", r"\(g\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\text{tr}(A) =\) ___ \(A^i{}_i\).", "answer": "δ^i_j (or just A^i_i)"},
         {"type": "true-false", "question": r"\((\vec a \times \vec b)_i = \epsilon_{ijk} a_j b_k\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"\(\epsilon_{ijk}\epsilon^{ijl} = ?\delta_k{}^l\). Fill: ___.", "answer": "2"}]},
    {"title": "Tensors in Physics: A Quick Tour",
     "body_html": r"""
<p>Where tensors show up across physics:</p>
<ul>
<li><strong>Stress tensor</strong> \(\sigma_{ij}\): force per area on internal surfaces in a material. Symmetric rank 2.</li>
<li><strong>Inertia tensor</strong> \(I_{ij}\): rotational analogue of mass. Symmetric rank 2.</li>
<li><strong>Electromagnetic field tensor</strong> \(F^{\mu\nu}\): unifies \(\vec{E}\) and \(\vec{B}\) into one antisymmetric rank-2 tensor.</li>
<li><strong>Stress-energy tensor</strong> \(T^{\mu\nu}\): source of gravity in general relativity.</li>
<li><strong>Riemann curvature</strong> \(R^\mu{}_{\nu\rho\sigma}\): rank-4 tensor encoding curvature of spacetime.</li>
<li><strong>Strain</strong>, <strong>elasticity</strong>, <strong>conductivity</strong>: all tensors in materials science.</li>
</ul>
<p>Tensors aren't a niche tool; they're the natural language for describing how physical quantities respond linearly along multiple directions at once.</p>""",
     "exercises": [
         {"type": "multiple-choice", "question": "Stress tensor has rank:", "options": ["1", "2", "3", "4"], "correctIndex": 1},
         {"type": "true-false", "question": "Electromagnetic field tensor is antisymmetric.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Riemann curvature tensor has rank ___.", "answer": "4"},
         {"type": "true-false", "question": "Stress-energy tensor sources gravity in GR.", "correctAnswer": True},
         {"type": "true-false", "question": "Inertia tensor is symmetric.", "correctAnswer": True}]},
    {"title": "Tensors Checkpoint",
     "body_html": r"""
<p>Recap of Unit 37:</p>
<ul>
<li>Tensors generalize vectors and matrices to multilinear maps of any rank.</li>
<li>Type \((p, q)\): \(p\) upper indices, \(q\) lower. Rank \(= p + q\).</li>
<li>Einstein summation: repeated up/down indices are summed.</li>
<li>Metric \(g_{\mu\nu}\) raises/lowers indices, defines inner products.</li>
<li>Tensor product builds higher-rank tensors; contraction reduces rank by 2.</li>
<li>Symmetric/antisymmetric decompositions arise frequently.</li>
<li>Kronecker delta and Levi-Civita symbol are the workhorse invariants.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Repeated up/down indices are summed.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Contraction reduces rank by:", "options": ["1", "2", "0", "any amount"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Metric raises and lowers ___.", "answer": "indices"},
         {"type": "true-false", "question": "Levi-Civita symbol is symmetric.", "correctAnswer": False},
         {"type": "true-false", "question": "Kronecker delta acts as the identity in tensor algebra.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Total rank of a type-(p,q) tensor is p + ___.", "answer": "q"},
         {"type": "true-false", "question": "Symmetric and antisymmetric pieces decompose any rank-2 tensor uniquely.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(37, "Tensors: An Introduction", 541, LESSONS)
