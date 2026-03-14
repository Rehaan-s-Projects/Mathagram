// js/problem-generator.js
// Generates randomized math problems for calculus exercises.
// Each function returns an exercise object compatible with exercises.js

/**
 * Pick a random element from an array.
 */
function pick(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

/**
 * Random integer between min and max (inclusive).
 */
function randInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Shuffle an array (Fisher-Yates).
 */
function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// ─────────────────────────────────────────────
// LIMITS
// ─────────────────────────────────────────────

export function limitDirectEval() {
  const a = randInt(1, 8);
  const n = randInt(2, 4);
  const result = Math.pow(a, n);
  return {
    type: 'fill-blank',
    question: `Evaluate: lim(x→${a}) x^${n}`,
    answer: String(result)
  };
}

export function limitAtInfinity() {
  const a = randInt(1, 5);
  const b = randInt(1, 5);
  const options = [
    `${a}/${b}`,
    `${a * 2}/${b}`,
    '0',
    '∞'
  ];
  return {
    type: 'multiple-choice',
    question: `What is lim(x→∞) (${a}x² + 3x) / (${b}x² + 1)?`,
    options: shuffle([`${a}/${b}`, `${b}/${a}`, '0', '∞']),
    correctIndex: null, // set below
    _correctAnswer: `${a}/${b}`,
    get correctIndex() {
      return this.options.indexOf(this._correctAnswer);
    }
  };
}

// ─────────────────────────────────────────────
// POWER RULE DERIVATIVES
// ─────────────────────────────────────────────

export function powerRuleDerivative() {
  const coeff = randInt(2, 9);
  const exp = randInt(2, 6);
  const newCoeff = coeff * exp;
  const newExp = exp - 1;
  const answer = newExp === 1 ? `${newCoeff}x` : `${newCoeff}x^${newExp}`;
  return {
    type: 'fill-blank',
    question: `Find the derivative: d/dx [${coeff}x^${exp}]`,
    answer: answer
  };
}

export function powerRuleDerivativeMC() {
  const coeff = randInt(2, 7);
  const exp = randInt(2, 5);
  const correct = `${coeff * exp}x^${exp - 1}`;
  const wrong1 = `${coeff}x^${exp - 1}`;
  const wrong2 = `${coeff * exp}x^${exp}`;
  const wrong3 = `${coeff * (exp + 1)}x^${exp}`;
  const options = [correct, wrong1, wrong2, wrong3];
  const shuffled = shuffle(options);
  return {
    type: 'multiple-choice',
    question: `What is the derivative of ${coeff}x^${exp}?`,
    options: shuffled,
    correctIndex: shuffled.indexOf(correct)
  };
}

export function sumRuleDerivative() {
  const a = randInt(2, 6);
  const b = randInt(1, 5);
  const c = randInt(1, 9);
  const correct = `${a * 2}x + ${b}`;
  const wrong1 = `${a}x + ${b}`;
  const wrong2 = `${a * 2}x + ${c}`;
  const wrong3 = `${a}x² + ${b}`;
  const options = [correct, wrong1, wrong2, wrong3];
  const shuffled = shuffle(options);
  return {
    type: 'multiple-choice',
    question: `Find d/dx [${a}x² + ${b}x + ${c}]`,
    options: shuffled,
    correctIndex: shuffled.indexOf(correct)
  };
}

// ─────────────────────────────────────────────
// PRODUCT RULE
// ─────────────────────────────────────────────

export function productRuleTF() {
  const statements = [
    { text: "The product rule states: d/dx[f·g] = f'·g + f·g'", answer: true },
    { text: "The product rule states: d/dx[f·g] = f'·g'", answer: false },
    { text: "The derivative of x·sin(x) is sin(x) + x·cos(x)", answer: true },
    { text: "The derivative of x·sin(x) is x·cos(x)", answer: false },
    { text: "The derivative of x²·eˣ is eˣ(x² + 2x)", answer: true },
    { text: "The derivative of x²·eˣ is 2x·eˣ", answer: false },
  ];
  const s = pick(statements);
  return {
    type: 'true-false',
    question: s.text,
    correctAnswer: s.answer
  };
}

// ─────────────────────────────────────────────
// CHAIN RULE
// ─────────────────────────────────────────────

export function chainRuleMC() {
  const problems = [
    {
      q: "Find d/dx [sin(3x)]",
      correct: "3cos(3x)",
      wrongs: ["cos(3x)", "3sin(3x)", "-3cos(3x)"]
    },
    {
      q: "Find d/dx [(2x+1)³]",
      correct: "6(2x+1)²",
      wrongs: ["3(2x+1)²", "2(2x+1)³", "6(2x+1)³"]
    },
    {
      q: "Find d/dx [e^(2x)]",
      correct: "2e^(2x)",
      wrongs: ["e^(2x)", "2xe^(2x)", "e^(2)"]
    },
    {
      q: "Find d/dx [ln(5x)]",
      correct: "1/x",
      wrongs: ["5/x", "1/(5x)", "5ln(x)"]
    },
    {
      q: "Find d/dx [cos(x²)]",
      correct: "-2x·sin(x²)",
      wrongs: ["-sin(x²)", "2x·cos(x²)", "-2x·cos(x²)"]
    },
    {
      q: "Find d/dx [(x³+1)⁴]",
      correct: "12x²(x³+1)³",
      wrongs: ["4(x³+1)³", "3x²(x³+1)⁴", "12x(x³+1)³"]
    }
  ];
  const p = pick(problems);
  const options = shuffle([p.correct, ...p.wrongs]);
  return {
    type: 'multiple-choice',
    question: p.q,
    options: options,
    correctIndex: options.indexOf(p.correct)
  };
}

// ─────────────────────────────────────────────
// INTEGRALS — POWER RULE
// ─────────────────────────────────────────────

export function integralPowerRule() {
  const exp = randInt(2, 6);
  const newExp = exp + 1;
  const answer = `x^${newExp}/${newExp} + C`;
  return {
    type: 'fill-blank',
    question: `Evaluate: ∫ x^${exp} dx`,
    answer: answer
  };
}

export function integralPowerRuleMC() {
  const coeff = randInt(2, 5);
  const exp = randInt(1, 4);
  const newExp = exp + 1;
  const newCoeff = coeff;
  const correct = `${newCoeff}x^${newExp}/${newExp} + C`;
  const wrong1 = `${newCoeff}x^${exp}/${exp} + C`;
  const wrong2 = `${newCoeff * newExp}x^${newExp} + C`;
  const wrong3 = `${newCoeff}x^${newExp} + C`;
  const options = shuffle([correct, wrong1, wrong2, wrong3]);
  return {
    type: 'multiple-choice',
    question: `Evaluate: ∫ ${coeff}x^${exp} dx`,
    options: options,
    correctIndex: options.indexOf(correct)
  };
}

// ─────────────────────────────────────────────
// INTEGRALS — TRIG
// ─────────────────────────────────────────────

export function integralTrigMC() {
  const problems = [
    { q: "∫ cos(x) dx = ?", correct: "sin(x) + C", wrongs: ["-sin(x) + C", "cos(x) + C", "-cos(x) + C"] },
    { q: "∫ sin(x) dx = ?", correct: "-cos(x) + C", wrongs: ["cos(x) + C", "sin(x) + C", "-sin(x) + C"] },
    { q: "∫ sec²(x) dx = ?", correct: "tan(x) + C", wrongs: ["sec(x) + C", "-tan(x) + C", "sec(x)tan(x) + C"] },
    { q: "∫ csc²(x) dx = ?", correct: "-cot(x) + C", wrongs: ["cot(x) + C", "csc(x) + C", "-csc(x) + C"] },
    { q: "∫ sec(x)tan(x) dx = ?", correct: "sec(x) + C", wrongs: ["tan(x) + C", "-sec(x) + C", "sec²(x) + C"] },
  ];
  const p = pick(problems);
  const options = shuffle([p.correct, ...p.wrongs]);
  return {
    type: 'multiple-choice',
    question: p.q,
    options: options,
    correctIndex: options.indexOf(p.correct)
  };
}

// ─────────────────────────────────────────────
// DEFINITE INTEGRALS
// ─────────────────────────────────────────────

export function definiteIntegralEval() {
  const a = randInt(0, 3);
  const b = a + randInt(1, 4);
  const coeff = randInt(1, 4);
  // ∫ coeff*x dx from a to b = coeff * (b²-a²)/2
  const result = coeff * (b * b - a * a) / 2;
  return {
    type: 'fill-blank',
    question: `Evaluate: ∫ from ${a} to ${b} of ${coeff}x dx`,
    answer: String(result)
  };
}

// ─────────────────────────────────────────────
// U-SUBSTITUTION
// ─────────────────────────────────────────────

export function uSubstitutionMC() {
  const problems = [
    { q: "For ∫ 2x·e^(x²) dx, what is the best u substitution?", correct: "u = x²", wrongs: ["u = 2x", "u = e^(x²)", "u = x"] },
    { q: "For ∫ cos(3x) dx, what is the best u substitution?", correct: "u = 3x", wrongs: ["u = cos(x)", "u = 3", "u = sin(3x)"] },
    { q: "For ∫ x·√(x²+1) dx, what is the best u substitution?", correct: "u = x²+1", wrongs: ["u = x", "u = √(x²+1)", "u = x²"] },
    { q: "For ∫ sin(x)·cos(x) dx, which substitution works?", correct: "u = sin(x)", wrongs: ["u = cos(x)·sin(x)", "u = x", "u = sin(x)·cos(x)"] },
  ];
  const p = pick(problems);
  const options = shuffle([p.correct, ...p.wrongs]);
  return {
    type: 'multiple-choice',
    question: p.q,
    options: options,
    correctIndex: options.indexOf(p.correct)
  };
}

// ─────────────────────────────────────────────
// MATCHING EXERCISES
// ─────────────────────────────────────────────

export function derivativeMatching() {
  const allPairs = [
    { left: "d/dx [x³]", right: "3x²" },
    { left: "d/dx [sin(x)]", right: "cos(x)" },
    { left: "d/dx [eˣ]", right: "eˣ" },
    { left: "d/dx [ln(x)]", right: "1/x" },
    { left: "d/dx [cos(x)]", right: "-sin(x)" },
    { left: "d/dx [tan(x)]", right: "sec²(x)" },
    { left: "d/dx [x⁴]", right: "4x³" },
    { left: "d/dx [√x]", right: "1/(2√x)" },
  ];
  const pairs = shuffle(allPairs).slice(0, 4);
  return {
    type: 'matching',
    question: "Match each function with its derivative.",
    pairs: pairs
  };
}

export function integralMatching() {
  const allPairs = [
    { left: "∫ x² dx", right: "x³/3 + C" },
    { left: "∫ cos(x) dx", right: "sin(x) + C" },
    { left: "∫ eˣ dx", right: "eˣ + C" },
    { left: "∫ 1/x dx", right: "ln|x| + C" },
    { left: "∫ sin(x) dx", right: "-cos(x) + C" },
    { left: "∫ sec²(x) dx", right: "tan(x) + C" },
    { left: "∫ x³ dx", right: "x⁴/4 + C" },
    { left: "∫ 1 dx", right: "x + C" },
  ];
  const pairs = shuffle(allPairs).slice(0, 4);
  return {
    type: 'matching',
    question: "Match each integral with its result.",
    pairs: pairs
  };
}

// ─────────────────────────────────────────────
// ORDERING EXERCISES
// ─────────────────────────────────────────────

export function derivativeStepsOrdering() {
  const problems = [
    {
      question: "Order the steps to find the derivative using the chain rule:",
      correctOrder: [
        "Identify the outer and inner functions",
        "Differentiate the outer function",
        "Keep the inner function unchanged",
        "Multiply by the derivative of the inner function"
      ]
    },
    {
      question: "Order the steps to find the derivative using the product rule:",
      correctOrder: [
        "Identify f(x) and g(x)",
        "Find f'(x) and g'(x)",
        "Compute f'(x)·g(x)",
        "Compute f(x)·g'(x)",
        "Add the two results"
      ]
    },
    {
      question: "Order the steps to evaluate a definite integral:",
      correctOrder: [
        "Find the antiderivative F(x)",
        "Evaluate F(b) at the upper bound",
        "Evaluate F(a) at the lower bound",
        "Compute F(b) - F(a)"
      ]
    }
  ];
  const p = pick(problems);
  return {
    type: 'ordering',
    question: p.question,
    correctOrder: p.correctOrder,
    shuffled: shuffle(p.correctOrder)
  };
}

export function uSubStepsOrdering() {
  return {
    type: 'ordering',
    question: "Order the steps for u-substitution:",
    correctOrder: [
      "Choose u = g(x)",
      "Find du = g'(x) dx",
      "Rewrite the integral in terms of u",
      "Integrate with respect to u",
      "Substitute back the original variable"
    ],
    shuffled: shuffle([
      "Choose u = g(x)",
      "Find du = g'(x) dx",
      "Rewrite the integral in terms of u",
      "Integrate with respect to u",
      "Substitute back the original variable"
    ])
  };
}

// ─────────────────────────────────────────────
// APPLICATIONS
// ─────────────────────────────────────────────

export function tangentLineMC() {
  const a = randInt(1, 4);
  const slope = 2 * a; // derivative of x² at x=a
  const yVal = a * a;
  const correct = `y = ${slope}x - ${slope * a - yVal}`;
  const wrong1 = `y = ${a}x + ${yVal}`;
  const wrong2 = `y = ${slope}x + ${yVal}`;
  const wrong3 = `y = ${slope + 1}x - ${a}`;
  const options = shuffle([correct, wrong1, wrong2, wrong3]);
  return {
    type: 'multiple-choice',
    question: `Find the equation of the tangent line to f(x) = x² at x = ${a}.`,
    options: options,
    correctIndex: options.indexOf(correct)
  };
}

export function increasingDecreasingTF() {
  const statements = [
    { text: "If f'(x) > 0 on an interval, then f is increasing on that interval.", answer: true },
    { text: "If f'(x) < 0 on an interval, then f is increasing on that interval.", answer: false },
    { text: "If f''(x) > 0 on an interval, then f is concave up on that interval.", answer: true },
    { text: "If f''(x) > 0 on an interval, then f is concave down on that interval.", answer: false },
    { text: "A critical point occurs where f'(x) = 0 or f'(x) is undefined.", answer: true },
    { text: "Every critical point is a local extremum.", answer: false },
    { text: "If f'(c) = 0 and f''(c) > 0, then x = c is a local minimum.", answer: true },
    { text: "If f'(c) = 0 and f''(c) > 0, then x = c is a local maximum.", answer: false },
  ];
  return pick(statements);
}

export function applicationTF() {
  const s = increasingDecreasingTF();
  return {
    type: 'true-false',
    question: s.text,
    correctAnswer: s.answer
  };
}

// ─────────────────────────────────────────────
// GENERATE A RANDOM SET OF EXERCISES
// ─────────────────────────────────────────────

/**
 * Generate a set of random calculus exercises.
 * @param {string} topic - 'limits' | 'derivatives' | 'integrals' | 'applications' | 'mixed'
 * @param {number} count - number of exercises (default 6)
 * @returns {object[]} array of exercise objects
 */
export function generateExercises(topic = 'mixed', count = 6) {
  const generators = {
    limits: [limitDirectEval, limitAtInfinity],
    derivatives: [powerRuleDerivative, powerRuleDerivativeMC, sumRuleDerivative, productRuleTF, chainRuleMC, derivativeMatching, derivativeStepsOrdering],
    integrals: [integralPowerRule, integralPowerRuleMC, integralTrigMC, definiteIntegralEval, uSubstitutionMC, integralMatching, uSubStepsOrdering],
    applications: [tangentLineMC, applicationTF, derivativeStepsOrdering],
    mixed: [
      powerRuleDerivative, powerRuleDerivativeMC, sumRuleDerivative,
      chainRuleMC, productRuleTF, integralPowerRule, integralPowerRuleMC,
      integralTrigMC, definiteIntegralEval, uSubstitutionMC,
      derivativeMatching, integralMatching, derivativeStepsOrdering,
      tangentLineMC, applicationTF, limitDirectEval, limitAtInfinity
    ]
  };

  const pool = generators[topic] || generators.mixed;
  const exercises = [];

  // Ensure variety — try not to repeat the same generator
  const usedGenerators = new Set();
  for (let i = 0; i < count; i++) {
    let gen;
    // Try to pick an unused generator first
    const unused = pool.filter(g => !usedGenerators.has(g));
    if (unused.length > 0) {
      gen = pick(unused);
    } else {
      gen = pick(pool);
    }
    usedGenerators.add(gen);
    exercises.push(gen());
  }

  return exercises;
}
