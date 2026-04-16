// js/calculator.js
// Scientific + Calculus calculator for Mathagram
// Shows real math symbols: ∫, ∑, d/dx, ∞, π, √

export function createCalculator(container) {
  var calc = document.createElement('div');
  calc.id = 'mathagram-calc';
  calc.innerHTML =
    '<div class="calc-toggle" id="calc-toggle">\u222B Calculator</div>' +
    '<div class="calc-body" id="calc-body" style="display:none;">' +
      '<div class="calc-display" id="calc-display">0</div>' +
      '<div class="calc-history" id="calc-history"></div>' +

      // Tab switcher
      '<div class="calc-tabs">' +
        '<button class="calc-tab active" id="tab-num">123</button>' +
        '<button class="calc-tab" id="tab-sci">sin</button>' +
        '<button class="calc-tab" id="tab-calc">\u222B</button>' +
      '</div>' +

      // Number pad (default)
      '<div class="calc-buttons" id="pad-num">' +
        '<button class="cb num" id="cb-7">7</button>' +
        '<button class="cb num" id="cb-8">8</button>' +
        '<button class="cb num" id="cb-9">9</button>' +
        '<button class="cb op" id="cb-div">\u00F7</button>' +
        '<button class="cb num" id="cb-4">4</button>' +
        '<button class="cb num" id="cb-5">5</button>' +
        '<button class="cb num" id="cb-6">6</button>' +
        '<button class="cb op" id="cb-mul">\u00D7</button>' +
        '<button class="cb num" id="cb-1">1</button>' +
        '<button class="cb num" id="cb-2">2</button>' +
        '<button class="cb num" id="cb-3">3</button>' +
        '<button class="cb op" id="cb-sub">\u2212</button>' +
        '<button class="cb num" id="cb-0">0</button>' +
        '<button class="cb num" id="cb-dot">.</button>' +
        '<button class="cb op" id="cb-open">(</button>' +
        '<button class="cb op" id="cb-add">+</button>' +
        '<button class="cb op" id="cb-close">)</button>' +
        '<button class="cb clear" id="cb-ac">AC</button>' +
        '<button class="cb del" id="cb-del">\u232B</button>' +
        '<button class="cb equals" id="cb-eq">=</button>' +
      '</div>' +

      // Scientific pad
      '<div class="calc-buttons" id="pad-sci" style="display:none;">' +
        '<button class="cb func" id="cb-sin">sin</button>' +
        '<button class="cb func" id="cb-cos">cos</button>' +
        '<button class="cb func" id="cb-tan">tan</button>' +
        '<button class="cb func" id="cb-ln">ln</button>' +
        '<button class="cb func" id="cb-sqrt">\u221A</button>' +
        '<button class="cb func" id="cb-pow">x\u00B2</button>' +
        '<button class="cb func" id="cb-cube">x\u00B3</button>' +
        '<button class="cb func" id="cb-abs">|x|</button>' +
        '<button class="cb func" id="cb-pi">\u03C0</button>' +
        '<button class="cb func" id="cb-e">e</button>' +
        '<button class="cb func" id="cb-exp">e\u02E3</button>' +
        '<button class="cb func" id="cb-log">log</button>' +
        '<button class="cb func" id="cb-inv">1/x</button>' +
        '<button class="cb func" id="cb-fact">n!</button>' +
        '<button class="cb func" id="cb-powy">x\u02B8</button>' +
        '<button class="cb func" id="cb-mod">mod</button>' +
        '<button class="cb op" id="cb-open2">(</button>' +
        '<button class="cb clear" id="cb-ac2">AC</button>' +
        '<button class="cb del" id="cb-del2">\u232B</button>' +
        '<button class="cb equals" id="cb-eq2">=</button>' +
      '</div>' +

      // Calculus pad — real symbols!
      '<div class="calc-buttons calc-pad-wide" id="pad-calc" style="display:none;">' +
        '<button class="cb calc-sym" id="cb-int">\u222B</button>' +          // ∫
        '<button class="cb calc-sym" id="cb-dint">\u222B\u1D43\u1D47</button>' + // ∫ᵃᵇ
        '<button class="cb calc-sym" id="cb-ddx">d/dx</button>' +            // d/dx
        '<button class="cb calc-sym" id="cb-prt">\u2202</button>' +          // ∂
        '<button class="cb calc-sym" id="cb-sum">\u2211</button>' +          // ∑
        '<button class="cb calc-sym" id="cb-prod">\u220F</button>' +         // ∏
        '<button class="cb calc-sym" id="cb-lim">lim</button>' +            // lim
        '<button class="cb calc-sym" id="cb-inf">\u221E</button>' +          // ∞
        '<button class="cb calc-sym" id="cb-dx">dx</button>' +              // dx
        '<button class="cb calc-sym" id="cb-dy">dy</button>' +              // dy
        '<button class="cb calc-sym" id="cb-dt">dt</button>' +              // dt
        '<button class="cb calc-sym" id="cb-arr">\u2192</button>' +          // →
        '<button class="cb calc-sym" id="cb-neq">\u2260</button>' +          // ≠
        '<button class="cb calc-sym" id="cb-leq">\u2264</button>' +          // ≤
        '<button class="cb calc-sym" id="cb-geq">\u2265</button>' +          // ≥
        '<button class="cb calc-sym" id="cb-pm">\u00B1</button>' +           // ±
        '<button class="cb calc-sym" id="cb-delta">\u0394</button>' +        // Δ
        '<button class="cb clear" id="cb-ac3">AC</button>' +
        '<button class="cb del" id="cb-del3">\u232B</button>' +
        '<button class="cb equals" id="cb-eq3">=</button>' +
      '</div>' +

    '</div>';
  (container || document.body).appendChild(calc);

  var display = '';
  var expression = '';

  function updateDisplay() {
    document.getElementById('calc-display').textContent = display || '0';
  }
  function addD(show, calc) {
    display += show;
    expression += calc;
    updateDisplay();
  }

  // Toggle
  document.getElementById('calc-toggle').addEventListener('click', function() {
    var body = document.getElementById('calc-body');
    body.style.display = body.style.display === 'none' ? 'block' : 'none';
  });

  // Tab switching
  function showPad(name) {
    ['num','sci','calc'].forEach(function(p) {
      document.getElementById('pad-' + p).style.display = p === name ? 'grid' : 'none';
    });
    document.querySelectorAll('.calc-tab').forEach(function(t) { t.classList.remove('active'); });
    document.getElementById('tab-' + name).classList.add('active');
  }
  document.getElementById('tab-num').addEventListener('click', function() { showPad('num'); });
  document.getElementById('tab-sci').addEventListener('click', function() { showPad('sci'); });
  document.getElementById('tab-calc').addEventListener('click', function() { showPad('calc'); });

  // Numbers
  ['0','1','2','3','4','5','6','7','8','9'].forEach(function(n) {
    document.getElementById('cb-' + n).addEventListener('click', function() { addD(n, n); });
  });
  document.getElementById('cb-dot').addEventListener('click', function() { addD('.', '.'); });

  // Operators
  document.getElementById('cb-add').addEventListener('click', function() { addD(' + ', '+'); });
  document.getElementById('cb-sub').addEventListener('click', function() { addD(' \u2212 ', '-'); });
  document.getElementById('cb-mul').addEventListener('click', function() { addD(' \u00D7 ', '*'); });
  document.getElementById('cb-div').addEventListener('click', function() { addD(' \u00F7 ', '/'); });
  document.getElementById('cb-open').addEventListener('click', function() { addD('(', '('); });
  document.getElementById('cb-close').addEventListener('click', function() { addD(')', ')'); });
  document.getElementById('cb-open2').addEventListener('click', function() { addD('(', '('); });

  // Scientific functions
  document.getElementById('cb-sin').addEventListener('click', function() { addD('sin(', 'Math.sin('); });
  document.getElementById('cb-cos').addEventListener('click', function() { addD('cos(', 'Math.cos('); });
  document.getElementById('cb-tan').addEventListener('click', function() { addD('tan(', 'Math.tan('); });
  document.getElementById('cb-ln').addEventListener('click', function() { addD('ln(', 'Math.log('); });
  document.getElementById('cb-log').addEventListener('click', function() { addD('log\u2081\u2080(', 'Math.log10('); });
  document.getElementById('cb-sqrt').addEventListener('click', function() { addD('\u221A(', 'Math.sqrt('); });
  document.getElementById('cb-pow').addEventListener('click', function() { addD('\u00B2', '**2'); });
  document.getElementById('cb-cube').addEventListener('click', function() { addD('\u00B3', '**3'); });
  document.getElementById('cb-abs').addEventListener('click', function() { addD('|', 'Math.abs('); });
  document.getElementById('cb-pi').addEventListener('click', function() { addD('\u03C0', 'Math.PI'); });
  document.getElementById('cb-e').addEventListener('click', function() { addD('e', 'Math.E'); });
  document.getElementById('cb-exp').addEventListener('click', function() { addD('e^(', 'Math.exp('); });
  document.getElementById('cb-inv').addEventListener('click', function() { addD('1/(', '1/('); });
  document.getElementById('cb-powy').addEventListener('click', function() { addD('^(', '**('); });
  document.getElementById('cb-mod').addEventListener('click', function() { addD(' mod ', '%'); });
  document.getElementById('cb-fact').addEventListener('click', function() {
    // Calculate factorial of current number
    try {
      var n = parseInt(expression);
      var f = 1; for (var i=2;i<=n;i++) f*=i;
      display = n + '! = ' + f;
      expression = String(f);
      updateDisplay();
    } catch(e) { }
  });

  // Calculus symbols — display only (for building expressions to show)
  var calcSymbols = {
    'int': ['\u222B', '\u222B'],
    'dint': ['\u222B\u1D43\u1D47 ', '\u222B'],
    'ddx': ['d/dx ', 'd/dx '],
    'prt': ['\u2202', '\u2202'],
    'sum': ['\u2211', '\u2211'],
    'prod': ['\u220F', '\u220F'],
    'lim': ['lim ', 'lim '],
    'inf': ['\u221E', 'Infinity'],
    'dx': [' dx', ' dx'],
    'dy': [' dy', ' dy'],
    'dt': [' dt', ' dt'],
    'arr': [' \u2192 ', ' -> '],
    'neq': [' \u2260 ', '!='],
    'leq': [' \u2264 ', '<='],
    'geq': [' \u2265 ', '>='],
    'pm': [' \u00B1 ', '+-'],
    'delta': ['\u0394', 'D']
  };
  Object.keys(calcSymbols).forEach(function(key) {
    document.getElementById('cb-' + key).addEventListener('click', function() {
      addD(calcSymbols[key][0], calcSymbols[key][1]);
    });
  });

  // AC, DEL, EQUALS — all 3 pads
  ['','2','3'].forEach(function(suffix) {
    document.getElementById('cb-ac' + suffix).addEventListener('click', function() {
      display = ''; expression = '';
      document.getElementById('calc-history').textContent = '';
      updateDisplay();
    });
    document.getElementById('cb-del' + suffix).addEventListener('click', function() {
      display = display.slice(0, -1);
      expression = expression.slice(0, -1);
      updateDisplay();
    });
    document.getElementById('cb-eq' + suffix).addEventListener('click', function() {
      try {
        // Clean expression for eval
        var clean = expression.replace(/\u222B/g,'').replace(/d\/dx/g,'').replace(/\u2211/g,'')
          .replace(/\u220F/g,'').replace(/lim/g,'').replace(/ dx/g,'').replace(/ dy/g,'')
          .replace(/ dt/g,'').replace(/ -> /g,'').replace(/\u2202/g,'').replace(/D/g,'');
        var result = Function('"use strict"; return (' + clean + ')')();
        var rounded = Math.round(result * 1000000) / 1000000;
        document.getElementById('calc-history').textContent = display + ' = ' + rounded;
        display = String(rounded);
        expression = String(rounded);
        updateDisplay();
      } catch(e) {
        document.getElementById('calc-display').textContent = 'Error';
        setTimeout(function() { display=''; expression=''; updateDisplay(); }, 1000);
      }
    });
  });
}
