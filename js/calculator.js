// js/calculator.js
// Scientific calculator widget for Mathagram courses

export function createCalculator(container) {
  const calc = document.createElement('div');
  calc.id = 'mathagram-calc';
  calc.innerHTML = `
    <div class="calc-toggle" id="calc-toggle">🔢 Calculator</div>
    <div class="calc-body" id="calc-body" style="display:none;">
      <div class="calc-display" id="calc-display">0</div>
      <div class="calc-history" id="calc-history"></div>
      <div class="calc-buttons">
        <button class="cb func" onclick="C.fn('sin')">sin</button>
        <button class="cb func" onclick="C.fn('cos')">cos</button>
        <button class="cb func" onclick="C.fn('tan')">tan</button>
        <button class="cb func" onclick="C.fn('ln')">ln</button>
        <button class="cb func" onclick="C.fn('sqrt')">√</button>
        <button class="cb func" onclick="C.fn('pow')">x²</button>
        <button class="cb func" onclick="C.type('Math.PI')">π</button>
        <button class="cb func" onclick="C.type('Math.E')">e</button>

        <button class="cb num" onclick="C.type('7')">7</button>
        <button class="cb num" onclick="C.type('8')">8</button>
        <button class="cb num" onclick="C.type('9')">9</button>
        <button class="cb op" onclick="C.type('/')">/</button>

        <button class="cb num" onclick="C.type('4')">4</button>
        <button class="cb num" onclick="C.type('5')">5</button>
        <button class="cb num" onclick="C.type('6')">6</button>
        <button class="cb op" onclick="C.type('*')">×</button>

        <button class="cb num" onclick="C.type('1')">1</button>
        <button class="cb num" onclick="C.type('2')">2</button>
        <button class="cb num" onclick="C.type('3')">3</button>
        <button class="cb op" onclick="C.type('-')">−</button>

        <button class="cb num" onclick="C.type('0')">0</button>
        <button class="cb num" onclick="C.type('.')">.</button>
        <button class="cb op" onclick="C.type('(')">(</button>
        <button class="cb op" onclick="C.type('+')">+</button>

        <button class="cb op" onclick="C.type(')')">)</button>
        <button class="cb clear" onclick="C.clear()">AC</button>
        <button class="cb del" onclick="C.del()">⌫</button>
        <button class="cb equals" onclick="C.calc()">=</button>
      </div>
    </div>
  `;
  (container || document.body).appendChild(calc);

  // Toggle
  document.getElementById('calc-toggle').addEventListener('click', function() {
    var body = document.getElementById('calc-body');
    body.style.display = body.style.display === 'none' ? 'block' : 'none';
  });

  // Calculator logic
  window.C = {
    expr: '',
    type: function(v) {
      if (this.expr === '0' && v !== '.') this.expr = '';
      this.expr += v;
      document.getElementById('calc-display').textContent = this.expr;
    },
    fn: function(name) {
      if (name === 'sqrt') this.expr += 'Math.sqrt(';
      else if (name === 'pow') this.expr += '**2';
      else if (name === 'ln') this.expr += 'Math.log(';
      else this.expr += 'Math.' + name + '(';
      document.getElementById('calc-display').textContent = this.expr;
    },
    clear: function() {
      this.expr = '';
      document.getElementById('calc-display').textContent = '0';
    },
    del: function() {
      this.expr = this.expr.slice(0, -1);
      document.getElementById('calc-display').textContent = this.expr || '0';
    },
    calc: function() {
      try {
        var result = Function('"use strict"; return (' + this.expr + ')')();
        var rounded = Math.round(result * 1000000) / 1000000;
        document.getElementById('calc-history').textContent = this.expr + ' = ' + rounded;
        this.expr = String(rounded);
        document.getElementById('calc-display').textContent = rounded;
      } catch(e) {
        document.getElementById('calc-display').textContent = 'Error';
        this.expr = '';
      }
    }
  };
}
