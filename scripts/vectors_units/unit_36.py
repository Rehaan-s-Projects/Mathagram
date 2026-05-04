#!/usr/bin/env python3
"""Unit 36 — Dirac Notation & Quantum Vectors (lessons 526-540)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Why Dirac Notation?",
     "body_html": r"""
<p>Quantum mechanics is linear algebra on infinite-dimensional complex vector spaces (Hilbert spaces). <strong>Dirac notation</strong> (bra-ket) makes this clean and explicit. Vectors become "kets" \(|\psi\rangle\); covectors become "bras" \(\langle\phi|\); inner products are \(\langle\phi|\psi\rangle\).</p>
<p>The notation makes the abstract structure clear and is easy to manipulate algebraically. It's standard worldwide for quantum mechanics, quantum information, and quantum chemistry.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Quantum mechanics uses complex Hilbert spaces.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Dirac notation includes:", "options": ["scalars only", "kets and bras", "matrices only", "tensors only"], "correctIndex": 1},
         {"type": "fill-blank", "question": "A ket \\(|\\psi\\rangle\\) is a vector in a ___ space.", "answer": "Hilbert"},
         {"type": "true-false", "question": "Bra-ket notation is universal in quantum mechanics.", "correctAnswer": True},
         {"type": "true-false", "question": "Hilbert spaces are always finite-dimensional.", "correctAnswer": False}]},
    {"title": "Kets as State Vectors",
     "body_html": r"""
<p>A quantum state is a unit vector in Hilbert space, written \(|\psi\rangle\). For a qubit:</p>
<div class="math-block">$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1$$</div>
<p>where \(|0\rangle, |1\rangle\) are basis kets and \(\alpha, \beta \in \mathbb{C}\). Two kets that differ by a global phase \(e^{i\theta}\) represent the same physical state.</p>
<p>Kets are added, scaled by complex numbers, and form a vector space — exactly what we've been studying.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Normalization: \\(|\\alpha|^2 + |\\beta|^2 =\\) ___.", "answer": "1"},
         {"type": "multiple-choice", "question": "Two kets differing by a global phase represent:", "options": ["different states", "the same physical state", "orthogonal states", "no state"], "correctIndex": 1},
         {"type": "true-false", "question": "Kets are added like vectors.", "correctAnswer": True},
         {"type": "fill-blank", "question": "A qubit has dimension ___.", "answer": "2"},
         {"type": "true-false", "question": "Quantum states are unit vectors.", "correctAnswer": True}]},
    {"title": "Bras as Dual Vectors",
     "body_html": r"""
<p>For each ket \(|\psi\rangle\), there's a corresponding <strong>bra</strong> \(\langle\psi|\) — the dual (covector) version. In matrix terms, if \(|\psi\rangle\) is a column vector, \(\langle\psi|\) is its conjugate transpose:</p>
<div class="math-block">$$|\psi\rangle = \begin{pmatrix}\alpha \\ \beta\end{pmatrix} \implies \langle\psi| = \begin{pmatrix}\bar\alpha & \bar\beta\end{pmatrix}$$</div>
<p>Bras live in the dual space \(H^*\), and pair with kets to give scalars. Crucially: complex conjugation is part of the dual map.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Bras are conjugate transposes of kets.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Bras live in the:", "options": ["same Hilbert space", "dual space", "tensor product", "trivial space"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Conjugating a complex number means flipping the sign of its ___ part.", "answer": "imaginary"},
         {"type": "true-false", "question": "The dual map is anti-linear (involves complex conjugation).", "correctAnswer": True},
         {"type": "true-false", "question": "Bras pair with kets to give vectors.", "correctAnswer": False}]},
    {"title": "Inner Products ⟨φ|ψ⟩",
     "body_html": r"""
<p>The pairing of a bra with a ket produces a complex number — the inner product:</p>
<div class="math-block">$$\langle\phi|\psi\rangle = \bar\phi_0 \psi_0 + \bar\phi_1 \psi_1 + \cdots$$</div>
<p>Properties:</p>
<ul>
<li>\(\langle\psi|\psi\rangle = 1\) for normalized states.</li>
<li>\(\langle\phi|\psi\rangle = \overline{\langle\psi|\phi\rangle}\).</li>
<li>Linear in the second slot (ket); conjugate-linear in the first (bra).</li>
</ul>""",
     "exercises": [
         {"type": "fill-blank", "question": "\\(\\langle\\phi|\\psi\\rangle = \\overline{\\langle\\) ___ \\(|\\phi\\rangle}\\).", "answer": "psi"},
         {"type": "multiple-choice", "question": r"For a normalized state, \(\langle\psi|\psi\rangle =\)", "options": ["0", "1", r"\(\psi\)", "depends"], "correctIndex": 1},
         {"type": "true-false", "question": "Inner product is linear in the ket.", "correctAnswer": True},
         {"type": "true-false", "question": "Inner product is linear in the bra.", "correctAnswer": False},
         {"type": "fill-blank", "question": r"For complex Hilbert space, \(\langle\phi|\psi\rangle\) is a ___ number.", "answer": "complex"}]},
    {"title": "Outer Products |ψ⟩⟨φ|",
     "body_html": r"""
<p>An <strong>outer product</strong> \(|\psi\rangle\langle\phi|\) is an operator: a ket on the left, a bra on the right. In matrix terms it's \(\vec{\psi}\vec{\phi}^*\) — a rank-1 matrix.</p>
<p>Outer products act on kets:</p>
<div class="math-block">$$\big(|\psi\rangle\langle\phi|\big) |\chi\rangle = \langle\phi|\chi\rangle\, |\psi\rangle$$</div>
<p><strong>Special case:</strong> \(|\psi\rangle\langle\psi|\) (with \(|\psi\rangle\) a unit vector) is the <strong>projection onto the \(|\psi\rangle\) line</strong>. The completeness relation \(\sum_k |k\rangle\langle k| = I\) (over a basis) is a key tool.</p>""",
     "exercises": [
         {"type": "true-false", "question": "An outer product is an operator.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"\(|\psi\rangle\langle\psi|\) (unit \(|\psi\rangle\)) is:", "options": ["a number", "a bra", "a projection operator", "an eigenvector"], "correctIndex": 2},
         {"type": "fill-blank", "question": r"Completeness: \(\sum_k |k\rangle\langle k| = \) ___.", "answer": "I"},
         {"type": "true-false", "question": "Outer products are typically rank 1.", "correctAnswer": True},
         {"type": "true-false", "question": "Inner and outer products are the same thing.", "correctAnswer": False}]},
    {"title": "Operators on Hilbert Space",
     "body_html": r"""
<p>Quantum mechanics uses linear operators \(\hat A\) acting on kets: \(|\psi\rangle \mapsto \hat A |\psi\rangle\). In a finite-dim basis they're matrices.</p>
<p>Special classes:</p>
<ul>
<li><strong>Hermitian:</strong> \(\hat A = \hat A^\dagger\). Real eigenvalues; correspond to <em>observables</em>.</li>
<li><strong>Unitary:</strong> \(\hat U^\dagger \hat U = I\). Preserve inner products; correspond to <em>time evolution</em> and <em>symmetries</em>.</li>
<li><strong>Projection:</strong> \(\hat P^2 = \hat P = \hat P^\dagger\).</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Hermitian operators have real eigenvalues.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Time evolution corresponds to a:", "options": ["projection", "unitary operator", "Hermitian eigenvector", "scalar"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"\(\hat A\) is Hermitian iff \(\hat A = \hat A^?\). Fill: ___.", "answer": "dagger"},
         {"type": "true-false", "question": "Unitary operators preserve inner products.", "correctAnswer": True},
         {"type": "true-false", "question": "Projections are both Hermitian and idempotent.", "correctAnswer": True}]},
    {"title": "Hermitian Operators (Observables)",
     "body_html": r"""
<p>Physical observables (energy, position, momentum, spin) are represented by <strong>Hermitian operators</strong>. Why? Their eigenvalues are real (measurement outcomes are real), and their eigenvectors are orthogonal (distinct outcomes are distinguishable).</p>
<p><strong>Example.</strong> The Hamiltonian \(\hat H\) is Hermitian; its eigenvalues are energy levels. The Pauli matrices \(\sigma_x, \sigma_y, \sigma_z\) are Hermitian; their eigenvalues \(\pm 1\) are spin measurement outcomes.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Observables are Hermitian operators.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Eigenvalues of the Hamiltonian \(\hat H\) are:", "options": ["complex", "energy levels", "probabilities", "imaginary"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Pauli matrices are ___.", "answer": "Hermitian"},
         {"type": "true-false", "question": "Eigenvectors of distinct eigenvalues of a Hermitian operator are orthogonal.", "correctAnswer": True},
         {"type": "true-false", "question": "All operators in QM are Hermitian.", "correctAnswer": False}]},
    {"title": "Eigenstates & Eigenvalues",
     "body_html": r"""
<p>An eigenvector of \(\hat A\) with eigenvalue \(a\) is called an <strong>eigenstate</strong> \(|a\rangle\):</p>
<div class="math-block">$$\hat A|a\rangle = a|a\rangle$$</div>
<p>If \(\hat A\) is Hermitian, the eigenstates form an orthonormal basis. Any state can be expanded as \(|\psi\rangle = \sum_a c_a |a\rangle\) with coefficients \(c_a = \langle a|\psi\rangle\).</p>
<p>The expansion coefficients are <strong>probability amplitudes</strong>: \(|c_a|^2\) is the probability of measuring eigenvalue \(a\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Eigenstate equation: \\(\\hat A|a\\rangle = a\\) ___.", "answer": "|a>"},
         {"type": "multiple-choice", "question": "Probability of measuring eigenvalue a:", "options": [r"\(c_a\)", r"\(|c_a|\)", r"\(|c_a|^2\)", r"\(c_a^*\)"], "correctIndex": 2},
         {"type": "true-false", "question": "Hermitian eigenstates form an orthonormal basis.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Coefficients are: \\(c_a = \\langle\\) ___ \\(|\\psi\\rangle\\).", "answer": "a"},
         {"type": "true-false", "question": r"\(|c_a|^2\) is a probability amplitude.", "correctAnswer": False}]},
    {"title": "Measurement Postulate",
     "body_html": r"""
<p>When you measure observable \(\hat A\) on state \(|\psi\rangle = \sum_a c_a |a\rangle\):</p>
<ol>
<li>The result is some eigenvalue \(a\), with probability \(|c_a|^2\).</li>
<li>The state <strong>collapses</strong> to the corresponding eigenstate \(|a\rangle\).</li>
</ol>
<p>So measurement is fundamentally probabilistic and irreversible (collapse). Repeated immediate measurements give the same result deterministically — the state is now an eigenstate.</p>
<p>Expected value: \(\langle\hat A\rangle = \langle\psi|\hat A|\psi\rangle = \sum_a a |c_a|^2\).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Measurement collapses the state.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Expected value of observable \(\hat A\):", "options": [r"\(\hat A|\psi\rangle\)", r"\(\langle\psi|\hat A|\psi\rangle\)", r"\(\hat A^2\)", r"\(|\psi|^2\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Probability of result a: \\(|c_a|^?\\). Fill: ___.", "answer": "2"},
         {"type": "true-false", "question": "Measurement is deterministic.", "correctAnswer": False},
         {"type": "true-false", "question": "Repeated measurements of the same eigenstate give the same outcome.", "correctAnswer": True}]},
    {"title": "Superposition & Linearity",
     "body_html": r"""
<p>The <strong>superposition principle</strong>: if \(|\psi_1\rangle\) and \(|\psi_2\rangle\) are valid states, so is any linear combination \(\alpha|\psi_1\rangle + \beta|\psi_2\rangle\) (with renormalization).</p>
<p>This is just the vector-space axiom — but in quantum mechanics it has dramatic consequences: a particle can be "in two places at once," in superpositions of energies, etc.</p>
<p>Time evolution is linear: \(|\psi(t)\rangle = \hat U(t) |\psi(0)\rangle\). Superpositions evolve into superpositions; the Schrödinger equation is linear.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Linear combinations of states are also states.", "correctAnswer": True},
         {"type": "multiple-choice", "question": r"Time evolution is via:", "options": ["matrix inversion", "unitary operators", "projections", "norms"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Schrödinger's equation is ___.", "answer": "linear"},
         {"type": "true-false", "question": "Superposition is a vector-space axiom in disguise.", "correctAnswer": True},
         {"type": "true-false", "question": "Quantum measurement is linear.", "correctAnswer": False}]},
    {"title": "The Hilbert Space Structure",
     "body_html": r"""
<p>A <strong>Hilbert space</strong> is a complete inner-product space. "Complete" means every Cauchy sequence has a limit (no missing points). Finite-dim Hilbert spaces are just \(\mathbb{C}^n\); infinite-dim ones include \(L^2(\mathbb{R})\) (square-integrable functions on the line).</p>
<p>Quantum states live in some Hilbert space \(H\) determined by the system. A particle on a line: \(L^2(\mathbb{R})\). A qubit: \(\mathbb{C}^2\). Two qubits: \(\mathbb{C}^4\) (tensor product). The structure is fully described by linear-algebra concepts you've already seen.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Hilbert spaces are complete inner-product spaces.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "A qubit's Hilbert space is:", "options": [r"\(\mathbb{R}^2\)", r"\(\mathbb{C}^2\)", r"\(L^2(\mathbb{R})\)", r"\(\mathbb{Z}_2\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Two qubits live in a Hilbert space of dimension ___.", "answer": "4"},
         {"type": "true-false", "question": "L²(R) is finite-dimensional.", "correctAnswer": False},
         {"type": "true-false", "question": "Tensor product of two qubit spaces is C⁴.", "correctAnswer": True}]},
    {"title": "Probability Amplitudes",
     "body_html": r"""
<p>Quantum mechanics uses <strong>probability amplitudes</strong> (complex numbers), not probabilities directly. The actual probability is \(|c|^2\).</p>
<p>Why? Amplitudes can <strong>interfere</strong>. Two paths from A to B with amplitudes \(c_1, c_2\) combine as \(c_1 + c_2\) — and \(|c_1+c_2|^2 \neq |c_1|^2 + |c_2|^2\) in general. This is the source of all wavelike phenomena: double-slit interference, diffraction, the existence of stable atoms.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Amplitudes combine by addition; probabilities don't (in general).", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Probability is:", "options": [r"the amplitude itself", r"the square of the amplitude magnitude (\(|c|^2\))", "the real part", "the phase"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Interference comes from ___ amplitudes.", "answer": "complex"},
         {"type": "true-false", "question": "Double-slit interference reflects amplitude addition.", "correctAnswer": True},
         {"type": "true-false", "question": r"Two amplitudes always satisfy \(|c_1+c_2|^2 = |c_1|^2 + |c_2|^2\).", "correctAnswer": False}]},
    {"title": "Spin-1/2 in Bra-Ket Notation",
     "body_html": r"""
<p>The simplest quantum system: a spin-1/2 particle (electron, qubit). Hilbert space is \(\mathbb{C}^2\) with basis \(|\!\uparrow\rangle, |\!\downarrow\rangle\).</p>
<p>Pauli operators (the spin observables in units of \(\hbar/2\)):</p>
<div class="math-block">$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix},\ \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix},\ \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$</div>
<p>Each has eigenvalues \(\pm 1\). \(\sigma_z\) eigenstates: \(|\!\uparrow\rangle, |\!\downarrow\rangle\). \(\sigma_x\) eigenstates: \((|\!\uparrow\rangle \pm |\!\downarrow\rangle)/\sqrt 2\).</p>""",
     "exercises": [
         {"type": "fill-blank", "question": "Eigenvalues of Pauli matrices: \\(\\pm\\) ___.", "answer": "1"},
         {"type": "multiple-choice", "question": r"\(\sigma_x\) eigenstate with \(+1\):", "options": [r"\(|\uparrow\rangle\)", r"\(|\downarrow\rangle\)", r"\((|\uparrow\rangle + |\downarrow\rangle)/\sqrt 2\)", r"\(|0\rangle\)"], "correctIndex": 2},
         {"type": "true-false", "question": "Pauli matrices are Hermitian.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Spin-1/2 Hilbert space is \(\mathbb{C}^?\). Fill: ___.", "answer": "2"},
         {"type": "true-false", "question": r"\(\sigma_z\) is diagonal in the \(|\uparrow\rangle, |\downarrow\rangle\) basis.", "correctAnswer": True}]},
    {"title": "Practice: Dirac Notation",
     "body_html": r"""
<p>Try these.</p>
<ol>
<li>For \(|\psi\rangle = \tfrac{1}{\sqrt 2}(|0\rangle + |1\rangle)\), \(\langle\psi|\psi\rangle = 1\). ✓</li>
<li>\(\langle 0|\psi\rangle = 1/\sqrt 2\). Probability of measuring \(0\): \(1/2\).</li>
<li>\(\sigma_z|\psi\rangle = \tfrac{1}{\sqrt 2}(|0\rangle - |1\rangle)\). Not an eigenstate of \(\sigma_z\).</li>
<li>Mean of \(\sigma_z\) on this state: \(\langle\psi|\sigma_z|\psi\rangle = 0\).</li>
<li>\(\sigma_x|\psi\rangle = |\psi\rangle\): \(|\psi\rangle\) is an eigenstate of \(\sigma_x\) with eigenvalue \(+1\).</li>
</ol>""",
     "exercises": [
         {"type": "fill-blank", "question": r"Probability of measuring 0 in \(\tfrac{1}{\sqrt 2}(|0\rangle+|1\rangle)\): ___.", "answer": "1/2"},
         {"type": "multiple-choice", "question": r"\(\langle\psi|\sigma_z|\psi\rangle\) for that state:", "options": ["0", "1", "-1", "1/2"], "correctIndex": 0},
         {"type": "true-false", "question": r"\(\tfrac{1}{\sqrt 2}(|0\rangle+|1\rangle)\) is an eigenstate of \(\sigma_x\).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Eigenvalue of \(\sigma_x\) for that state: ___.", "answer": "1"},
         {"type": "true-false", "question": "All states are eigenstates of σz.", "correctAnswer": False}]},
    {"title": "Quantum Vectors Checkpoint",
     "body_html": r"""
<p>Recap of Unit 36:</p>
<ul>
<li>Quantum states are unit vectors (kets) in a Hilbert space.</li>
<li>Bras are dual vectors; \(\langle\phi|\psi\rangle\) is the inner product (a complex number).</li>
<li>Outer products \(|\psi\rangle\langle\phi|\) are operators (rank-1).</li>
<li>Observables are Hermitian operators; their eigenvalues are measurement outcomes.</li>
<li>Probability of result \(a\): \(|c_a|^2\) where \(c_a = \langle a|\psi\rangle\).</li>
<li>Time evolution is unitary; superposition reflects vector-space linearity.</li>
<li>Pauli matrices \(\sigma_{x,y,z}\) are the standard spin-1/2 observables.</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Hermitian operators have real eigenvalues.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "A bra is the:", "options": ["complex conjugate transpose of a ket", "outer product", "projection", "matrix"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Probability of measuring a is \\(|c_a|^?\\). Fill: ___.", "answer": "2"},
         {"type": "true-false", "question": "Quantum measurement is reversible.", "correctAnswer": False},
         {"type": "true-false", "question": "Time evolution preserves inner products.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Pauli σ-matrices have eigenvalues ±___.", "answer": "1"},
         {"type": "true-false", "question": "Superposition is a consequence of linearity.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(36, "Dirac Notation & Quantum Vectors", 526, LESSONS)
