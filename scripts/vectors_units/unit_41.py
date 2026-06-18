#!/usr/bin/env python3
"""Unit 41 — Vectors in Robotics & Signal Processing (lessons 601-615)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gen_vectors import render_unit

LESSONS = [
    {"title": "Robot Pose: Position & Orientation",
     "body_html": r"""
<p>A robot's <strong>pose</strong> in 3D combines position (a vector \(\vec{p} \in \mathbb{R}^3\)) and orientation (a rotation \(R \in SO(3)\)). Together they live in \(SE(3)\), the special Euclidean group.</p>
<p>Common representations of orientation:</p>
<ul>
<li>Rotation matrices (\(3 \times 3\), 9 numbers, 3 effective DOFs).</li>
<li>Euler angles (3 numbers — risk of gimbal lock).</li>
<li>Axis-angle (rotation axis + angle).</li>
<li>Unit quaternions (4 numbers, double-cover of \(SO(3)\)).</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Pose combines position and orientation.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "SO(3) is:", "options": ["the set of rotations", "the set of translations", "scalars", "matrices"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Position is a vector in R^___.", "answer": "3"},
         {"type": "true-false", "question": "Quaternions can represent rotations without gimbal lock.", "correctAnswer": True},
         {"type": "true-false", "question": "Euler angles are immune to gimbal lock.", "correctAnswer": False}]},
    {"title": "Forward Kinematics",
     "body_html": r"""
<p><strong>Forward kinematics:</strong> given joint angles \(\vec{\theta}\), compute the pose of the end effector.</p>
<p>For a chain of \(n\) joints, the end-effector pose is the product of joint transforms:</p>
<div class="math-block">$$T_\text{end} = T_1(\theta_1) T_2(\theta_2) \cdots T_n(\theta_n)$$</div>
<p>Each \(T_i\) is a \(4 \times 4\) homogeneous transform encoding rotation + translation. The Denavit-Hartenberg (DH) convention parametrizes each link with 4 numbers.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Forward kinematics maps joint angles to end-effector pose.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "DH parameters per link:", "options": ["2", "3", "4", "6"], "correctIndex": 2},
         {"type": "fill-blank", "question": "End-effector pose is the ___ of joint transforms.", "answer": "product"},
         {"type": "true-false", "question": "Homogeneous transforms are 4×4.", "correctAnswer": True},
         {"type": "true-false", "question": "Forward kinematics is generally easy to compute.", "correctAnswer": True}]},
    {"title": "Inverse Kinematics",
     "body_html": r"""
<p><strong>Inverse kinematics (IK):</strong> given a desired end-effector pose, find joint angles. Much harder than forward.</p>
<p>For some robots (analytical IK exists for 6-DOF arms with specific geometry), there's a closed-form solution. For most, you use:</p>
<ul>
<li><strong>Numerical IK:</strong> iterate using the Jacobian (next lesson).</li>
<li><strong>Optimization:</strong> minimize \(\|f(\vec{\theta}) - \vec{p}_\text{target}\|\).</li>
</ul>
<p>IK can have multiple solutions, no solution, or infinite solutions depending on the robot and target.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Inverse kinematics is harder than forward kinematics.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "IK solutions can be:", "options": ["always unique", "multiple, none, or infinite", "always infinite", "never exist"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Numerical IK uses the ___ matrix.", "answer": "Jacobian"},
         {"type": "true-false", "question": "Closed-form IK exists for every robot.", "correctAnswer": False},
         {"type": "true-false", "question": "Optimization-based IK minimizes a residual.", "correctAnswer": True}]},
    {"title": "Robot Arm Jacobian",
     "body_html": r"""
<p>The Jacobian \(J(\vec{\theta})\) maps joint velocities to end-effector velocities:</p>
<div class="math-block">$$\dot{\vec{x}} = J(\vec{\theta})\dot{\vec{\theta}}$$</div>
<p>For a redundant robot (\(n &gt; 6\) joints), \(J\) has more columns than rows; you need a pseudoinverse. The Jacobian's null space corresponds to <strong>internal motions</strong> — joint movements that don't move the end effector.</p>
<p><strong>Singularities</strong>: configurations where \(J\) loses rank (collinear joints, fully extended arm). Avoid them — they cause large joint speeds for small end-effector motion.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Jacobian relates joint velocities to end-effector velocities.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Singularities are:", "options": ["good", "configurations where J loses rank", "always at zero", "physical impossibilities"], "correctIndex": 1},
         {"type": "fill-blank", "question": r"Redundant robots use a ___ of the Jacobian.", "answer": "pseudoinverse"},
         {"type": "true-false", "question": "Null-space motions don't move the end effector.", "correctAnswer": True},
         {"type": "true-false", "question": "Singular configurations cause numerical issues.", "correctAnswer": True}]},
    {"title": "Quaternions for Orientation",
     "body_html": r"""
<p>A unit quaternion \(q = (w, \vec{v})\) with \(\|q\| = 1\) represents rotation by \(2\theta\) around \(\hat{v}\), where \(w = \cos\theta\) and \(\vec{v} = \sin\theta\,\hat{v}\).</p>
<p>Composition of rotations = quaternion multiplication. Inverse of a unit quaternion = its conjugate. Spherical linear interpolation (SLERP) gives smooth rotation paths.</p>
<p>Quaternions avoid gimbal lock, are numerically stable, and use only 4 numbers (vs. 9 for a rotation matrix). Standard in graphics, robotics, aerospace.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Unit quaternions parametrize rotations.", "correctAnswer": True},
         {"type": "fill-blank", "question": "Composition of rotations = quaternion ___.", "answer": "multiplication"},
         {"type": "multiple-choice", "question": "SLERP is for:", "options": ["sliding", "smooth rotation interpolation", "linear interpolation", "scaling"], "correctIndex": 1},
         {"type": "true-false", "question": "Quaternions suffer from gimbal lock.", "correctAnswer": False},
         {"type": "true-false", "question": "Quaternions use 4 numbers; rotation matrices use 9.", "correctAnswer": True}]},
    {"title": "Path Planning",
     "body_html": r"""
<p>Path planning finds a sequence of poses from start to goal avoiding obstacles. Common algorithms:</p>
<ul>
<li><strong>A*:</strong> grid-based, optimal, heuristic-driven.</li>
<li><strong>RRT (Rapidly-exploring Random Tree):</strong> sample random configs, build a tree.</li>
<li><strong>PRM (Probabilistic Roadmap):</strong> sample, connect, find shortest path through the roadmap.</li>
<li><strong>Trajectory optimization:</strong> minimize cost (energy, time) subject to constraints.</li>
</ul>
<p>The configuration space is high-dimensional (one dim per joint), so randomized methods often win over exhaustive search.</p>""",
     "exercises": [
         {"type": "true-false", "question": "RRT samples random configurations to build a tree.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "A* is:", "options": ["randomized", "heuristic-driven, optimal on grids", "non-deterministic", "useless"], "correctIndex": 1},
         {"type": "fill-blank", "question": "PRM stands for ___ roadmap.", "answer": "probabilistic"},
         {"type": "true-false", "question": "Configuration space dimension equals number of joints.", "correctAnswer": True},
         {"type": "true-false", "question": "Trajectory optimization minimizes a cost subject to constraints.", "correctAnswer": True}]},
    {"title": "SLAM Preview",
     "body_html": r"""
<p><strong>SLAM (Simultaneous Localization And Mapping):</strong> the robot estimates its own pose <em>and</em> builds a map at the same time. State vector includes the robot's pose plus all landmark positions — potentially thousands.</p>
<p>Methods:</p>
<ul>
<li><strong>EKF-SLAM:</strong> Kalman filter on the joint state.</li>
<li><strong>Particle filter SLAM (FastSLAM):</strong> represent posterior as samples.</li>
<li><strong>Graph SLAM:</strong> build a constraint graph, solve via least squares.</li>
</ul>
<p>The SLAM problem is fundamentally about Bayesian estimation in a high-dim state space.</p>""",
     "exercises": [
         {"type": "true-false", "question": "SLAM estimates pose and map simultaneously.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "FastSLAM uses:", "options": ["EKF", "particle filter", "PCA", "SVD"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Graph SLAM solves a constraint graph via ___ squares.", "answer": "least"},
         {"type": "true-false", "question": "SLAM state space is generally low-dimensional.", "correctAnswer": False},
         {"type": "true-false", "question": "SLAM is fundamentally a Bayesian estimation problem.", "correctAnswer": True}]},
    {"title": "Sensor Fusion: Kalman Filter Preview",
     "body_html": r"""
<p>The <strong>Kalman filter</strong> fuses noisy measurements over time to estimate a state. Iterates two steps:</p>
<ol>
<li><strong>Predict:</strong> propagate state and covariance forward in time using a model.</li>
<li><strong>Update:</strong> incorporate a new measurement using a Bayesian update.</li>
</ol>
<p>Optimal under Gaussian noise + linear model. Extended (EKF) and Unscented (UKF) variants handle nonlinearity.</p>
<p>Used everywhere: GPS, inertial navigation, target tracking, robotics, finance, even your smartphone's screen-orientation logic.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Kalman filter has predict and update steps.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "EKF handles:", "options": ["only linear models", "nonlinear models", "discrete states", "graphics"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Kalman filter is optimal under ___ noise and linear models.", "answer": "Gaussian"},
         {"type": "true-false", "question": "Kalman filters are used in GPS.", "correctAnswer": True},
         {"type": "true-false", "question": "UKF stands for Universal Kalman Filter.", "correctAnswer": False}]},
    {"title": "Signals as Vectors in L²",
     "body_html": r"""
<p>A signal \(f(t)\) (audio, image, sensor data) is naturally an element of \(L^2\) — square-integrable functions. The inner product:</p>
<div class="math-block">$$\langle f, g\rangle = \int f(t) \overline{g(t)}\,dt$$</div>
<p>Energy of the signal: \(\|f\|^2 = \int |f(t)|^2\,dt\). The whole language of finite-dim linear algebra (orthogonality, projections, decomposition) lifts to signals.</p>
<p>Discrete signals \(x[n]\) live in \(\ell^2\) (sequences with finite energy). The same linear-algebra tools apply.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Signals are vectors in L² (or ℓ² for discrete).", "correctAnswer": True},
         {"type": "fill-blank", "question": r"Energy: \(\|f\|^2 = \int |f(t)|^?\,dt\). Fill: ___.", "answer": "2"},
         {"type": "multiple-choice", "question": "Continuous signals live in:", "options": [r"\(L^2\)", r"\(\ell^2\)", r"\(\mathbb{R}\)", r"\(\mathbb{Z}\)"], "correctIndex": 0},
         {"type": "true-false", "question": "Discrete signals don't admit inner products.", "correctAnswer": False},
         {"type": "true-false", "question": "Linear-algebra tools (orthogonality, projections) apply to signals.", "correctAnswer": True}]},
    {"title": "Inner Products of Signals",
     "body_html": r"""
<p>The inner product \(\langle f, g\rangle\) measures <strong>how similar</strong> two signals are.</p>
<p>For two sinusoids: \(\langle\sin(\omega_1 t), \sin(\omega_2 t)\rangle = 0\) over a period if \(\omega_1 \neq \omega_2\) — distinct frequencies are orthogonal.</p>
<p>This orthogonality is what makes Fourier analysis work: any signal decomposes into sinusoids whose contributions are independent. The coefficients are inner products with the basis sinusoids.</p>""",
     "exercises": [
         {"type": "true-false", "question": "Distinct sinusoids are orthogonal over a full period.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Fourier coefficients are:", "options": ["inner products with basis sinusoids", "differences", "averages", "products of values"], "correctIndex": 0},
         {"type": "fill-blank", "question": "Signal similarity is measured by inner ___.", "answer": "product"},
         {"type": "true-false", "question": "Same sinusoids at different phases give zero inner product.", "correctAnswer": False},
         {"type": "true-false", "question": "Orthogonality of sinusoids is the foundation of Fourier analysis.", "correctAnswer": True}]},
    {"title": "Convolution as Vector Operation",
     "body_html": r"""
<p>The <strong>convolution</strong> of two signals:</p>
<div class="math-block">$$(f * g)(t) = \int f(\tau) g(t - \tau)\,d\tau$$</div>
<p>It's a linear operation; in vector terms, it's <strong>shift-and-sum</strong>. Convolution is what filters compute. <em>Causal</em> filters use only past inputs (\(g(\tau) = 0\) for \(\tau &lt; 0\)).</p>
<p><strong>Convolution theorem:</strong> in the frequency domain, convolution becomes pointwise multiplication: \(\widehat{f*g} = \hat f \cdot \hat g\). This is why FFT-based convolution is fast.</p>""",
     "exercises": [
         {"type": "fill-blank", "question": r"\((f*g)(t) = \int f(\tau) g(t - \tau)\,d\) ___.", "answer": "tau"},
         {"type": "multiple-choice", "question": "Convolution becomes ___ in frequency domain.", "options": ["division", "pointwise multiplication", "subtraction", "still convolution"], "correctIndex": 1},
         {"type": "true-false", "question": "Convolution is a linear operation.", "correctAnswer": True},
         {"type": "fill-blank", "question": r"FFT-based convolution exploits the ___ theorem.", "answer": "convolution"},
         {"type": "true-false", "question": "Causal filters use future inputs.", "correctAnswer": False}]},
    {"title": "Fourier Transform as Basis Change",
     "body_html": r"""
<p>The Fourier transform changes basis from "samples in time" to "amplitudes at each frequency":</p>
<div class="math-block">$$\hat f(\omega) = \int f(t) e^{-i\omega t}\,dt$$</div>
<p>It's a unitary transformation (preserves inner products): Parseval's theorem says \(\int |f|^2\,dt = \tfrac{1}{2\pi}\int |\hat f|^2\,d\omega\).</p>
<p>Because Fourier basis vectors (complex exponentials) are orthonormal and complete in \(L^2\), the transform is invertible. The DFT (discrete Fourier transform) is its finite analogue, computed efficiently by the FFT in \(O(n\log n)\).</p>""",
     "exercises": [
         {"type": "true-false", "question": "Fourier transform is a basis change.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "FFT cost:", "options": [r"\(O(n)\)", r"\(O(n\log n)\)", r"\(O(n^2)\)", r"\(O(n^3)\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Fourier transform preserves ___ products (Parseval).", "answer": "inner"},
         {"type": "true-false", "question": "Fourier basis exponentials are orthonormal.", "correctAnswer": True},
         {"type": "true-false", "question": "DFT is the discrete analog of the continuous Fourier transform.", "correctAnswer": True}]},
    {"title": "Compression: Fourier & Wavelets",
     "body_html": r"""
<p>Compression exploits the fact that natural signals have structure: most of their energy concentrates in a few basis coefficients.</p>
<ul>
<li><strong>Fourier (DCT):</strong> good for stationary signals. JPEG uses 2D DCT on \(8 \times 8\) blocks.</li>
<li><strong>Wavelets:</strong> localize in both time and frequency. JPEG 2000, MP3 use wavelets.</li>
<li><strong>SVD:</strong> for matrix-valued signals (images, video). Low-rank approximation throws away small singular values.</li>
</ul>
<p>Each is a basis change that concentrates energy into a few components — exactly the linear-algebra picture from PCA.</p>""",
     "exercises": [
         {"type": "true-false", "question": "JPEG uses 2D DCT on 8×8 blocks.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Wavelets localize in:", "options": ["time only", "frequency only", "both", "neither"], "correctIndex": 2},
         {"type": "fill-blank", "question": "JPEG ___ uses wavelets.", "answer": "2000"},
         {"type": "true-false", "question": "SVD is used for image/video compression.", "correctAnswer": True},
         {"type": "true-false", "question": "Compression ignores signal structure.", "correctAnswer": False}]},
    {"title": "Practice: Robotics & DSP",
     "body_html": r"""
<p>Examples to think through:</p>
<ol>
<li>A 6-DOF arm has Jacobian \(J \in \mathbb{R}^{6\times 6}\). At a singular configuration, \(\det J = 0\).</li>
<li>Rotating a quaternion \(q\) by another \(p\): \(q' = pq\) (or \(qp\), depending on convention).</li>
<li>Convolving an audio signal with a low-pass filter removes high frequencies.</li>
<li>FFT of a sine wave at frequency \(f_0\): two sharp spikes at \(\pm f_0\).</li>
<li>An \(N\)-sample signal has FFT cost \(N\log N\), but inverse FFT is also \(N\log N\).</li>
</ol>""",
     "exercises": [
         {"type": "true-false", "question": "Singular Jacobian configurations have det J = 0.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "FFT cost on N samples:", "options": [r"\(N\)", r"\(N\log N\)", r"\(N^2\)", r"\(2^N\)"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Composition of two quaternions: ___ multiplication.", "answer": "quaternion"},
         {"type": "true-false", "question": "Low-pass filters remove high frequencies.", "correctAnswer": True},
         {"type": "true-false", "question": "Inverse FFT is much slower than forward FFT.", "correctAnswer": False}]},
    {"title": "Robotics & DSP Checkpoint",
     "body_html": r"""
<p>Recap of Unit 41:</p>
<ul>
<li>Robot pose lives in \(SE(3)\): position + rotation. Quaternions are the practical orientation representation.</li>
<li>Forward kinematics is easy; inverse kinematics is hard (and uses the Jacobian).</li>
<li>SLAM and Kalman filtering are about Bayesian estimation in vector state spaces.</li>
<li>Path planning explores high-dim configuration space (RRT, PRM, A*).</li>
<li>Signals are vectors in \(L^2\) (or \(\ell^2\)). Fourier transform is just a basis change.</li>
<li>Convolution is a linear operation; multiplication in frequency domain.</li>
<li>Compression exploits sparsity in good bases (DCT, wavelets, SVD).</li>
</ul>""",
     "exercises": [
         {"type": "true-false", "question": "Robotics uses linear algebra extensively.", "correctAnswer": True},
         {"type": "multiple-choice", "question": "Quaternions parametrize:", "options": ["translations", "rotations", "scalings", "shears"], "correctIndex": 1},
         {"type": "fill-blank", "question": "Convolution in time = ___ in frequency.", "answer": "multiplication"},
         {"type": "true-false", "question": "FFT computes Fourier in O(n log n).", "correctAnswer": True},
         {"type": "true-false", "question": "Inverse kinematics is generally easy.", "correctAnswer": False},
         {"type": "fill-blank", "question": "SLAM = Simultaneous Localization And ___.", "answer": "Mapping"},
         {"type": "true-false", "question": "Kalman filter is optimal for linear Gaussian models.", "correctAnswer": True}]},
]

if __name__ == "__main__":
    render_unit(41, "Vectors in Robotics & Signal Processing", 601, LESSONS)
