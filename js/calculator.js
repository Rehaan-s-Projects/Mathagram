// js/calculator.js
// Scientific calculator for Mathagram — shows real math symbols

export function createCalculator(container) {
  var calc = document.createElement('div');
  calc.id = 'mathagram-calc';
  calc.innerHTML =
    '<div class="calc-toggle" id="calc-toggle">\uD83D\uDD22 Calculator</div>' +
    '<div class="calc-body" id="calc-body" style="display:none;">' +
      '<div class="calc-display" id="calc-display">0</div>' +
      '<div class="calc-history" id="calc-history"></div>' +
      '<div class="calc-buttons">' +
        '<button class="cb func" id="cb-sin">sin</button>' +
        '<button class="cb func" id="cb-cos">cos</button>' +
        '<button class="cb func" id="cb-tan">tan</button>' +
        '<button class="cb func" id="cb-ln">ln</button>' +
        '<button class="cb func" id="cb-sqrt">\u221A</button>' +
        '<button class="cb func" id="cb-pow">x\u00B2</button>' +
        '<button class="cb func" id="cb-pi">\u03C0</button>' +
        '<button class="cb func" id="cb-e">e</button>' +
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
    '</div>';
  (container || document.body).appendChild(calc);

  // What user sees (display) vs what we calculate (expression)
  var display = '';
  var expression = '';

  function updateDisplay() {
    document.getElementById('calc-display').textContent = display || '0';
  }

  function addToCalc(showText, calcText) {
    display += showText;
    expression += calcText;
    updateDisplay();
  }

  // Toggle open/close
  document.getElementById('calc-toggle').addEventListener('click', function() {
    var body = document.getElementById('calc-body');
    body.style.display = body.style.display === 'none' ? 'block' : 'none';
  });

  // Number buttons
  ['0','1','2','3','4','5','6','7','8','9'].forEach(function(n) {
    document.getElementById('cb-' + n).addEventListener('click', function() { addToCalc(n, n); });
  });
  document.getElementById('cb-dot').addEventListener('click', function() { addToCalc('.', '.'); });

  // Operator buttons — show symbols, calculate with code
  document.getElementById('cb-add').addEventListener('click', function() { addToCalc(' + ', '+'); });
  document.getElementById('cb-sub').addEventListener('click', function() { addToCalc(' \u2212 ', '-'); });
  document.getElementById('cb-mul').addEventListener('click', function() { addToCalc(' \u00D7 ', '*'); });
  document.getElementById('cb-div').addEventListener('click', function() { addToCalc(' \u00F7 ', '/'); });
  document.getElementById('cb-open').addEventListener('click', function() { addToCalc('(', '('); });
  document.getElementById('cb-close').addEventListener('click', function() { addToCalc(')', ')'); });

  // Function buttons — show math notation, calculate with JS
  document.getElementById('cb-sin').addEventListener('click', function() { addToCalc('sin(', 'Math.sin('); });
  document.getElementById('cb-cos').addEventListener('click', function() { addToCalc('cos(', 'Math.cos('); });
  document.getElementById('cb-tan').addEventListener('click', function() { addToCalc('tan(', 'Math.tan('); });
  document.getElementById('cb-ln').addEventListener('click', function() { addToCalc('ln(', 'Math.log('); });
  document.getElementById('cb-sqrt').addEventListener('click', function() { addToCalc('\u221A(', 'Math.sqrt('); });
  document.getElementById('cb-pow').addEventListener('click', function() { addToCalc('\u00B2', '**2'); });
  document.getElementById('cb-pi').addEventListener('click', function() { addToCalc('\u03C0', 'Math.PI'); });
  document.getElementById('cb-e').addEventListener('click', function() { addToCalc('e', 'Math.E'); });

  // AC — clear all
  document.getElementById('cb-ac').addEventListener('click', function() {
    display = '';
    expression = '';
    document.getElementById('calc-history').textContent = '';
    updateDisplay();
  });

  // Delete — remove last character
  document.getElementById('cb-del').addEventListener('click', function() {
    display = display.slice(0, -1);
    expression = expression.slice(0, -1);
    updateDisplay();
  });

  // Equals — calculate
  document.getElementById('cb-eq').addEventListener('click', function() {
    try {
      var result = Function('"use strict"; return (' + expression + ')')();
      var rounded = Math.round(result * 1000000) / 1000000;
      document.getElementById('calc-history').textContent = display + ' = ' + rounded;
      display = String(rounded);
      expression = String(rounded);
      updateDisplay();
    } catch(e) {
      document.getElementById('calc-display').textContent = 'Error';
      setTimeout(function() {
        display = '';
        expression = '';
        updateDisplay();
      }, 1000);
    }
  });
}
