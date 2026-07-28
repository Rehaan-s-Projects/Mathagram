// Super Calculator — a floating, modal calculator with Basic / Trig / Stats / Calc tabs.
// Idempotent: initSuperCalculator() is safe to call on every page.
//
// Modes
//   Basic    arithmetic, ()  ^  √  log  ln  e^  10^  |x|  n!  1/x  constants π e
//   Trig     sin cos tan + inverses + hyperbolic, DEG/RAD toggle
//   Stats    mean median mode stdev variance sum count min max range
//            distributions: normalcdf  invNorm  zscore  binompdf  nCk  nPk
//   Calc     numerical derivative d/dx f(x) at x=a, definite integral ∫ₐᵇ f(x)dx
//            (Simpson's rule, n=1000)

const CALC_SVG = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <rect x="5" y="2.5" width="14" height="19" rx="2.5"/>
  <rect x="7.5" y="5" width="9" height="3.5" rx="0.6" fill="currentColor" stroke="none" opacity="0.85"/>
  <circle cx="8.5" cy="12" r="0.95" fill="currentColor" stroke="none"/>
  <circle cx="12"  cy="12" r="0.95" fill="currentColor" stroke="none"/>
  <circle cx="15.5" cy="12" r="0.95" fill="currentColor" stroke="none"/>
  <circle cx="8.5" cy="15.4" r="0.95" fill="currentColor" stroke="none"/>
  <circle cx="12"  cy="15.4" r="0.95" fill="currentColor" stroke="none"/>
  <circle cx="15.5" cy="15.4" r="0.95" fill="currentColor" stroke="none"/>
  <circle cx="8.5" cy="18.8" r="0.95" fill="currentColor" stroke="none"/>
  <circle cx="12"  cy="18.8" r="0.95" fill="currentColor" stroke="none"/>
  <circle cx="15.5" cy="18.8" r="0.95" fill="currentColor" stroke="none"/>
</svg>`;

const FAB_HTML = `
  <button id="sc-fab" type="button" aria-label="Open Super Calculator" title="Super Calculator">
    ${CALC_SVG}
  </button>
`;

const STYLES = `
  #sc-fab {
    position: fixed; bottom: 20px; left: 20px; z-index: 9990;
    width: 56px; height: 56px; border-radius: 50%;
    background: linear-gradient(135deg, #00e5c8, #00b89f);
    color: #fff; border: none;
    display: inline-flex; align-items: center; justify-content: center;
    box-shadow: 0 6px 14px rgba(0,0,0,0.18); cursor: pointer;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  #sc-fab svg { width: 28px; height: 28px; }
  #sc-fab:hover { transform: translateY(-2px) scale(1.04); box-shadow: 0 8px 18px rgba(0,0,0,0.24); }
  #sc-fab:active { transform: scale(0.96); }
  @media (max-width: 480px) { #sc-fab { width: 50px; height: 50px; bottom: 16px; left: 16px; } #sc-fab svg { width: 24px; height: 24px; } }

  #sc-overlay {
    position: fixed; inset: 0; z-index: 9991;
    background: rgba(15, 23, 42, 0.55);
    display: none; align-items: center; justify-content: center;
    padding: 16px; backdrop-filter: blur(3px);
  }
  #sc-overlay.open { display: flex; }
  #sc-modal {
    width: 100%; max-width: 460px; max-height: 92vh; overflow: auto;
    background: #fff; border-radius: 18px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.30);
    font-family: inherit; color: #1f1108;
    display: flex; flex-direction: column;
  }
  .sc-head {
    display: flex; align-items: center; gap: 10px;
    padding: 14px 16px;
    background: linear-gradient(135deg, #00e5c8, #00b89f);
    color: #fff; border-radius: 18px 18px 0 0;
  }
  .sc-head h2 { font-size: 1.1rem; font-weight: 800; flex: 1; margin: 0; display: flex; align-items: center; gap: 8px; }
  .sc-title-icon { display: inline-flex; }
  .sc-title-icon svg { width: 22px; height: 22px; }
  .sc-head button {
    background: rgba(255,255,255,0.22); color: #fff; border: none;
    width: 32px; height: 32px; border-radius: 50%;
    font-size: 1.1rem; cursor: pointer; line-height: 1;
  }
  .sc-head button:hover { background: rgba(255,255,255,0.32); }

  .sc-tabs {
    display: flex; gap: 4px; padding: 10px 12px 0;
    border-bottom: 1px solid #e2e8f0;
    flex-wrap: wrap;
  }
  .sc-tab {
    flex: 1; min-width: 70px; padding: 8px 6px;
    background: #f1f5f9; color: #475569; border: none;
    border-radius: 10px 10px 0 0;
    font-weight: 700; font-size: 0.85rem; cursor: pointer;
  }
  .sc-tab.active { background: #fff; color: #00b89f; border-bottom: 2px solid #00e5c8; }

  .sc-display {
    margin: 14px 16px 8px; padding: 12px 14px;
    background: #0f172a; color: #f8fafc;
    border-radius: 12px; min-height: 78px;
    font-family: 'SFMono-Regular', Consolas, monospace;
    display: flex; flex-direction: column; justify-content: flex-end;
  }
  .sc-expr {
    font-size: 0.9rem; color: #94a3b8; min-height: 1.2em;
    word-break: break-all; text-align: right;
  }
  .sc-result {
    font-size: 1.8rem; font-weight: 800; text-align: right;
    word-break: break-all;
  }
  .sc-result.err { color: #fca5a5; font-size: 1rem; }

  .sc-pane { display: none; padding: 0 14px 14px; }
  .sc-pane.active { display: block; }

  .sc-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;
  }
  .sc-grid button {
    padding: 14px 4px; border: none; border-radius: 10px;
    background: #f1f5f9; color: #1f1108;
    font-size: 1rem; font-weight: 700; cursor: pointer;
    transition: background 0.1s ease;
  }
  .sc-grid button:hover { background: #e2e8f0; }
  .sc-grid button.sc-op { background: #e0f7f4; color: #00b89f; }
  .sc-grid button.sc-op:hover { background: #b9efe8; }
  .sc-grid button.sc-eq { background: #00e5c8; color: #fff; grid-column: span 1; }
  .sc-grid button.sc-eq:hover { background: #00b89f; }
  .sc-grid button.sc-fn { background: #fef3c7; color: #92400e; font-size: 0.85rem; }
  .sc-grid button.sc-fn:hover { background: #fde68a; }
  .sc-grid button.sc-clear { background: #fee2e2; color: #b91c1c; }
  .sc-grid button.sc-clear:hover { background: #fecaca; }

  .sc-anglemode {
    display: inline-flex; gap: 4px;
    margin: 0 0 10px;
    background: #f1f5f9; padding: 4px; border-radius: 999px; font-size: 0.78rem;
  }
  .sc-anglemode button {
    border: none; background: transparent; padding: 4px 12px; border-radius: 999px;
    cursor: pointer; font-weight: 700; color: #64748b;
  }
  .sc-anglemode button.active { background: #fff; color: #00b89f; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }

  .sc-data-input {
    width: 100%; padding: 10px 12px;
    border: 1.5px solid #e2e8f0; border-radius: 10px;
    font-family: inherit; font-size: 0.95rem; margin-bottom: 10px;
  }
  .sc-data-input:focus { outline: none; border-color: #00e5c8; }

  .sc-section-title {
    font-size: 0.75rem; font-weight: 800; color: #64748b;
    text-transform: uppercase; letter-spacing: 0.05em;
    margin: 12px 0 6px;
  }

  .sc-stat-grid, .sc-dist-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;
  }
  .sc-stat-grid button, .sc-dist-grid button {
    padding: 10px 4px; border: none; border-radius: 8px;
    background: #f1f5f9; color: #1f1108;
    font-size: 0.85rem; font-weight: 700; cursor: pointer;
  }
  .sc-stat-grid button:hover, .sc-dist-grid button:hover { background: #e2e8f0; }
  .sc-stat-grid button.run, .sc-dist-grid button.run { background: #00e5c8; color: #fff; }

  .sc-fn-input-row { display: flex; gap: 6px; align-items: center; margin-bottom: 8px; }
  .sc-fn-input-row label { font-size: 0.8rem; color: #64748b; font-weight: 700; min-width: 50px; }
  .sc-fn-input-row input { flex: 1; padding: 8px 10px; border: 1.5px solid #e2e8f0; border-radius: 8px; font-family: 'SFMono-Regular', Consolas, monospace; font-size: 0.9rem; }
  .sc-fn-input-row input:focus { outline: none; border-color: #00e5c8; }

  .sc-history {
    margin: 10px 16px 16px; padding: 10px 12px;
    background: #f8fafc; border-radius: 10px;
    max-height: 130px; overflow-y: auto;
    font-size: 0.82rem;
  }
  .sc-history-title {
    font-size: 0.7rem; font-weight: 800; color: #94a3b8;
    text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;
    display: flex; justify-content: space-between; align-items: center;
  }
  .sc-history-title button {
    background: transparent; border: none; color: #94a3b8;
    cursor: pointer; font-size: 0.7rem; font-weight: 700;
  }
  .sc-history-item {
    padding: 4px 0; border-bottom: 1px solid #e2e8f0;
    cursor: pointer; font-family: 'SFMono-Regular', Consolas, monospace;
  }
  .sc-history-item:last-child { border-bottom: none; }
  .sc-history-item:hover { color: #00b89f; }

  .sc-subtabs {
    display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 10px;
  }
  .sc-subtab {
    padding: 5px 10px; border: 1.5px solid #e2e8f0; background: #fff;
    border-radius: 999px; font-size: 0.78rem; font-weight: 700;
    color: #64748b; cursor: pointer;
  }
  .sc-subtab.active { background: #00e5c8; color: #fff; border-color: #00e5c8; }
  .sc-subpane { display: none; }
  .sc-subpane.active { display: block; }

  .sc-pane select.sc-data-input { padding: 8px 10px; font-size: 0.9rem; height: auto; }
`;

const MODAL_HTML = `
  <div id="sc-modal" role="dialog" aria-modal="true" aria-labelledby="sc-title">
    <div class="sc-head">
      <h2 id="sc-title"><span class="sc-title-icon">${CALC_SVG}</span>Super Calculator</h2>
      <button type="button" id="sc-close" aria-label="Close">×</button>
    </div>
    <div class="sc-tabs">
      <button type="button" class="sc-tab active" data-tab="basic">Basic</button>
      <button type="button" class="sc-tab" data-tab="trig">Trig</button>
      <button type="button" class="sc-tab" data-tab="stats">Stats</button>
      <button type="button" class="sc-tab" data-tab="calc">Calc</button>
      <button type="button" class="sc-tab" data-tab="more">More ✨</button>
    </div>
    <div class="sc-display">
      <div class="sc-expr" id="sc-expr"></div>
      <div class="sc-result" id="sc-result">0</div>
    </div>

    <div class="sc-pane active" data-pane="basic">
      <div class="sc-grid">
        <button class="sc-clear" data-act="clear">AC</button>
        <button data-ins="(">(</button>
        <button data-ins=")">)</button>
        <button class="sc-op" data-act="back">⌫</button>

        <button class="sc-fn" data-ins="sqrt(">√</button>
        <button class="sc-fn" data-ins="^">x^y</button>
        <button class="sc-fn" data-ins="!">n!</button>
        <button class="sc-op" data-ins="/">÷</button>

        <button data-ins="7">7</button>
        <button data-ins="8">8</button>
        <button data-ins="9">9</button>
        <button class="sc-op" data-ins="*">×</button>

        <button data-ins="4">4</button>
        <button data-ins="5">5</button>
        <button data-ins="6">6</button>
        <button class="sc-op" data-ins="-">−</button>

        <button data-ins="1">1</button>
        <button data-ins="2">2</button>
        <button data-ins="3">3</button>
        <button class="sc-op" data-ins="+">+</button>

        <button data-ins="0">0</button>
        <button data-ins=".">.</button>
        <button class="sc-fn" data-ins="pi">π</button>
        <button class="sc-eq" data-act="eval">=</button>

        <button class="sc-fn" data-ins="log(">log</button>
        <button class="sc-fn" data-ins="ln(">ln</button>
        <button class="sc-fn" data-ins="e^(">eˣ</button>
        <button class="sc-fn" data-ins="abs(">|x|</button>
      </div>
    </div>

    <div class="sc-pane" data-pane="trig">
      <div class="sc-anglemode" role="tablist">
        <button type="button" class="active" data-angle="deg">DEG</button>
        <button type="button" data-angle="rad">RAD</button>
      </div>
      <div class="sc-grid">
        <button class="sc-fn" data-ins="sin(">sin</button>
        <button class="sc-fn" data-ins="cos(">cos</button>
        <button class="sc-fn" data-ins="tan(">tan</button>
        <button class="sc-op" data-ins="/">÷</button>

        <button class="sc-fn" data-ins="asin(">sin⁻¹</button>
        <button class="sc-fn" data-ins="acos(">cos⁻¹</button>
        <button class="sc-fn" data-ins="atan(">tan⁻¹</button>
        <button class="sc-op" data-ins="*">×</button>

        <button class="sc-fn" data-ins="sinh(">sinh</button>
        <button class="sc-fn" data-ins="cosh(">cosh</button>
        <button class="sc-fn" data-ins="tanh(">tanh</button>
        <button class="sc-op" data-ins="-">−</button>

        <button class="sc-fn" data-ins="pi">π</button>
        <button class="sc-fn" data-ins="e">e</button>
        <button class="sc-fn" data-ins="^2">x²</button>
        <button class="sc-op" data-ins="+">+</button>

        <button data-ins="7">7</button>
        <button data-ins="8">8</button>
        <button data-ins="9">9</button>
        <button class="sc-op" data-act="back">⌫</button>

        <button data-ins="4">4</button>
        <button data-ins="5">5</button>
        <button data-ins="6">6</button>
        <button data-ins="(">(</button>

        <button data-ins="1">1</button>
        <button data-ins="2">2</button>
        <button data-ins="3">3</button>
        <button data-ins=")">)</button>

        <button data-ins="0">0</button>
        <button data-ins=".">.</button>
        <button class="sc-clear" data-act="clear">AC</button>
        <button class="sc-eq" data-act="eval">=</button>
      </div>
    </div>

    <div class="sc-pane" data-pane="stats">
      <div class="sc-section-title">Dataset (commas or spaces)</div>
      <input type="text" class="sc-data-input" id="sc-data" placeholder="e.g. 12, 18, 23, 27, 31, 42">
      <div class="sc-stat-grid">
        <button class="run" data-stat="mean">Mean</button>
        <button class="run" data-stat="median">Median</button>
        <button class="run" data-stat="mode">Mode</button>
        <button class="run" data-stat="stdev">σ (StDev)</button>
        <button class="run" data-stat="variance">σ² (Var)</button>
        <button class="run" data-stat="range">Range</button>
        <button class="run" data-stat="sum">Sum</button>
        <button class="run" data-stat="count">Count</button>
        <button class="run" data-stat="min">Min</button>
        <button class="run" data-stat="max">Max</button>
        <button class="run" data-stat="q1">Q1</button>
        <button class="run" data-stat="q3">Q3</button>
      </div>
      <div class="sc-section-title">Distributions &amp; Combinatorics</div>
      <div class="sc-fn-input-row">
        <label>z =</label>
        <input type="text" id="sc-z" placeholder="z-score" value="1.96">
        <button class="run" data-dist="normalcdf">P(Z ≤ z)</button>
      </div>
      <div class="sc-fn-input-row">
        <label>p =</label>
        <input type="text" id="sc-p" placeholder="probability 0–1" value="0.975">
        <button class="run" data-dist="invnorm">Inv Norm</button>
      </div>
      <div class="sc-fn-input-row">
        <label>n, k</label>
        <input type="text" id="sc-nk" placeholder="n, k (e.g. 10, 3)" value="10, 3">
        <button class="run" data-dist="nCk">nCk</button>
        <button class="run" data-dist="nPk">nPk</button>
      </div>
      <div class="sc-fn-input-row">
        <label>n,k,p</label>
        <input type="text" id="sc-bnk" placeholder="n, k, p (e.g. 10, 3, 0.5)" value="10, 3, 0.5">
        <button class="run" data-dist="binompdf">Binom PMF</button>
      </div>
      <div class="sc-fn-input-row">
        <label>λ, k</label>
        <input type="text" id="sc-poi" placeholder="λ, k (e.g. 3, 2)" value="3, 2">
        <button class="run" data-dist="poisson">Poisson PMF</button>
      </div>
      <div class="sc-fn-input-row">
        <label>λ, x</label>
        <input type="text" id="sc-exp" placeholder="rate, x (e.g. 0.5, 2)" value="0.5, 2">
        <button class="run" data-dist="exp">Exp CDF</button>
      </div>
      <div class="sc-fn-input-row">
        <label>df, t</label>
        <input type="text" id="sc-tdist" placeholder="df, t (e.g. 10, 1.96)" value="10, 1.96">
        <button class="run" data-dist="tcdf">T CDF</button>
      </div>
      <div class="sc-fn-input-row">
        <label>df, x</label>
        <input type="text" id="sc-chi" placeholder="df, x (e.g. 5, 7.5)" value="5, 7.5">
        <button class="run" data-dist="chi2">χ² CDF</button>
      </div>

      <div class="sc-section-title">Linear Regression — fit y = mx + b</div>
      <input type="text" class="sc-data-input" id="sc-regx" placeholder="x values: 1, 2, 3, 4, 5" value="1, 2, 3, 4, 5">
      <input type="text" class="sc-data-input" id="sc-regy" placeholder="y values: 2.1, 3.9, 6.0, 8.1, 9.9" value="2.1, 3.9, 6.0, 8.1, 9.9">
      <div class="sc-fn-input-row">
        <button class="run" data-dist="linreg" style="width: 100%;">Linear Regression (slope, intercept, r²)</button>
      </div>
    </div>

    <div class="sc-pane" data-pane="calc">
      <div class="sc-section-title">f(x) =</div>
      <input type="text" class="sc-data-input" id="sc-fx" placeholder="e.g. x^2 + sin(x)" value="x^2 + sin(x)">

      <div class="sc-fn-input-row">
        <label>at x =</label>
        <input type="text" id="sc-derivx" placeholder="point" value="2">
        <button class="run" data-calc="deriv">d/dx f(x)</button>
      </div>
      <div class="sc-fn-input-row">
        <label>x =</label>
        <input type="text" id="sc-evalx" placeholder="point" value="0">
        <button class="run" data-calc="eval">Evaluate f(x)</button>
      </div>
      <div class="sc-fn-input-row">
        <label>from</label>
        <input type="text" id="sc-inta" placeholder="a" value="0" style="max-width: 80px;">
        <label>to</label>
        <input type="text" id="sc-intb" placeholder="b" value="1" style="max-width: 80px;">
        <button class="run" data-calc="integ">∫ f(x)dx</button>
      </div>
      <div class="sc-fn-input-row">
        <label>x →</label>
        <input type="text" id="sc-limx" placeholder="limit point" value="0">
        <button class="run" data-calc="limit">lim f(x)</button>
      </div>
      <div class="sc-fn-input-row">
        <label>at x =</label>
        <input type="text" id="sc-deriv2x" placeholder="point" value="2">
        <button class="run" data-calc="deriv2">d²/dx² f(x)</button>
        <button class="run" data-calc="deriv3">d³/dx³</button>
      </div>

      <div class="sc-section-title">Σ Summation &amp; Π Product — function of k</div>
      <input type="text" class="sc-data-input" id="sc-sigmaf" placeholder="e.g. 1/k^2" value="1/k^2">
      <div class="sc-fn-input-row">
        <label>k =</label>
        <input type="text" id="sc-sigma-a" value="1" style="max-width: 80px;">
        <label>to</label>
        <input type="text" id="sc-sigma-b" value="100" style="max-width: 80px;">
        <button class="run" data-calc="sigma">Σ</button>
        <button class="run" data-calc="prod">Π</button>
      </div>

      <div class="sc-section-title">Taylor Series of f(x)</div>
      <div class="sc-fn-input-row">
        <label>around</label>
        <input type="text" id="sc-tay-a" value="0" style="max-width: 80px;">
        <label>terms</label>
        <input type="text" id="sc-tay-n" value="5" style="max-width: 80px;">
        <button class="run" data-calc="taylor">Taylor</button>
      </div>

      <div class="sc-section-title">Partial Derivatives — g(x, y)</div>
      <input type="text" class="sc-data-input" id="sc-gxy" placeholder="e.g. x^2*y + sin(y)" value="x^2*y + sin(y)">
      <div class="sc-fn-input-row">
        <label>(x, y)</label>
        <input type="text" id="sc-gxy-pt" value="1, 2">
        <button class="run" data-calc="partx">∂/∂x</button>
        <button class="run" data-calc="party">∂/∂y</button>
      </div>

      <p style="font-size: 0.75rem; color: #94a3b8; margin-top: 10px; line-height: 1.5;">
        Numerical methods: derivative via central difference (h = 10⁻⁵), integral via Simpson's rule (n = 1000),
        limit via two-sided approach. Trig in calc mode is always radians.
      </p>
    </div>

    <div class="sc-pane" data-pane="more">
      <div class="sc-subtabs">
        <button type="button" class="sc-subtab active" data-sub="solve">Solve</button>
        <button type="button" class="sc-subtab" data-sub="plot">Plot</button>
        <button type="button" class="sc-subtab" data-sub="convert">Convert</button>
        <button type="button" class="sc-subtab" data-sub="base">Base</button>
        <button type="button" class="sc-subtab" data-sub="ntheory">N-Theory</button>
        <button type="button" class="sc-subtab" data-sub="matrix">Matrix</button>
        <button type="button" class="sc-subtab" data-sub="geom">Geometry</button>
        <button type="button" class="sc-subtab" data-sub="complex">Complex</button>
        <button type="button" class="sc-subtab" data-sub="vector">Vector</button>
        <button type="button" class="sc-subtab" data-sub="seq">Sequence</button>
        <button type="button" class="sc-subtab" data-sub="roman">Roman</button>
        <button type="button" class="sc-subtab" data-sub="date">Date</button>
        <button type="button" class="sc-subtab" data-sub="circuit">Circuit ⚡</button>
      </div>

      <div class="sc-subpane active" data-subpane="solve">
        <div class="sc-section-title">Solve f(x) = 0  (Newton's method)</div>
        <input type="text" class="sc-data-input" id="sc-solve-fx" placeholder="e.g. x^2 - 2" value="x^2 - 2">
        <div class="sc-fn-input-row">
          <label>guess</label>
          <input type="text" id="sc-solve-x0" value="1">
          <button class="run" data-more="solve">Solve</button>
        </div>
        <div class="sc-section-title">Quadratic ax² + bx + c = 0</div>
        <div class="sc-fn-input-row">
          <label>a, b, c</label>
          <input type="text" id="sc-quad" value="1, -3, 2">
          <button class="run" data-more="quadratic">Quadratic</button>
        </div>
        <div class="sc-section-title">2×2 Linear System</div>
        <div class="sc-fn-input-row">
          <label>Row 1</label>
          <input type="text" id="sc-lin-r1" value="2, 3, 8" placeholder="a, b, =c">
        </div>
        <div class="sc-fn-input-row">
          <label>Row 2</label>
          <input type="text" id="sc-lin-r2" value="1, -1, 1">
          <button class="run" data-more="linsys2">Solve System</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="plot">
        <div class="sc-section-title">Plot f(x)</div>
        <input type="text" class="sc-data-input" id="sc-plot-fx" placeholder="e.g. sin(x)" value="sin(x)">
        <div class="sc-fn-input-row">
          <label>x-min</label>
          <input type="text" id="sc-plot-xmin" value="-10" style="max-width: 80px;">
          <label>x-max</label>
          <input type="text" id="sc-plot-xmax" value="10" style="max-width: 80px;">
          <button class="run" data-more="plot">Plot</button>
        </div>
        <canvas id="sc-canvas" width="420" height="240" style="width:100%; max-width:420px; height:auto; background:#0f172a; border-radius:10px; margin-top:6px;"></canvas>
        <p style="font-size: 0.72rem; color: #94a3b8; margin-top: 6px;">Plotted in radians. y-axis auto-scales.</p>
      </div>

      <div class="sc-subpane" data-subpane="convert">
        <div class="sc-section-title">Unit Conversion</div>
        <div class="sc-fn-input-row">
          <label>Category</label>
          <select id="sc-conv-cat" class="sc-data-input" style="margin-bottom:0;">
            <option value="length">Length</option>
            <option value="mass">Mass</option>
            <option value="temperature">Temperature</option>
            <option value="time">Time</option>
            <option value="speed">Speed</option>
            <option value="area">Area</option>
            <option value="volume">Volume</option>
            <option value="energy">Energy</option>
          </select>
        </div>
        <div class="sc-fn-input-row">
          <label>From</label>
          <input type="text" id="sc-conv-val" value="1" style="max-width: 100px;">
          <select id="sc-conv-from" class="sc-data-input" style="margin-bottom:0;"></select>
        </div>
        <div class="sc-fn-input-row">
          <label>To</label>
          <select id="sc-conv-to" class="sc-data-input" style="margin-bottom:0;"></select>
          <button class="run" data-more="convert">Convert</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="base">
        <div class="sc-section-title">Base Conversion (binary / octal / hex / decimal)</div>
        <div class="sc-fn-input-row">
          <label>Number</label>
          <input type="text" id="sc-base-val" value="255">
        </div>
        <div class="sc-fn-input-row">
          <label>From</label>
          <select id="sc-base-from" class="sc-data-input" style="margin-bottom:0;">
            <option value="10">Decimal (10)</option>
            <option value="2">Binary (2)</option>
            <option value="8">Octal (8)</option>
            <option value="16">Hex (16)</option>
          </select>
          <label>To</label>
          <select id="sc-base-to" class="sc-data-input" style="margin-bottom:0;">
            <option value="2">Binary (2)</option>
            <option value="8">Octal (8)</option>
            <option value="10">Decimal (10)</option>
            <option value="16">Hex (16)</option>
          </select>
          <button class="run" data-more="base">Go</button>
        </div>
        <button class="run" data-more="baseall" style="background:#f1f5f9;color:#1f1108;padding:8px;border:none;border-radius:8px;width:100%;font-weight:700;cursor:pointer;margin-top:6px;">Show all 4 bases</button>
      </div>

      <div class="sc-subpane" data-subpane="ntheory">
        <div class="sc-section-title">GCD & LCM (comma-separated)</div>
        <div class="sc-fn-input-row">
          <label>Numbers</label>
          <input type="text" id="sc-nt-nums" value="48, 36">
          <button class="run" data-more="gcd">GCD</button>
          <button class="run" data-more="lcm">LCM</button>
        </div>
        <div class="sc-section-title">Prime Factorization &amp; Divisors</div>
        <div class="sc-fn-input-row">
          <label>n</label>
          <input type="text" id="sc-nt-n" value="360">
          <button class="run" data-more="factorize">Factorize</button>
          <button class="run" data-more="isprime">Is Prime?</button>
        </div>
        <div class="sc-fn-input-row">
          <label>n</label>
          <input type="text" id="sc-nt-fib" value="10">
          <button class="run" data-more="fib">Fibonacci(n)</button>
          <button class="run" data-more="nthprime">nᵗʰ Prime</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="matrix">
        <div class="sc-section-title">2×2 Matrix</div>
        <div class="sc-fn-input-row">
          <label>Row 1</label>
          <input type="text" id="sc-m22-r1" value="1, 2">
        </div>
        <div class="sc-fn-input-row">
          <label>Row 2</label>
          <input type="text" id="sc-m22-r2" value="3, 4">
          <button class="run" data-more="m22det">det</button>
          <button class="run" data-more="m22inv">inverse</button>
        </div>
        <div class="sc-section-title">3×3 Matrix</div>
        <div class="sc-fn-input-row">
          <label>Row 1</label>
          <input type="text" id="sc-m33-r1" value="1, 2, 3">
        </div>
        <div class="sc-fn-input-row">
          <label>Row 2</label>
          <input type="text" id="sc-m33-r2" value="4, 5, 6">
        </div>
        <div class="sc-fn-input-row">
          <label>Row 3</label>
          <input type="text" id="sc-m33-r3" value="7, 8, 10">
          <button class="run" data-more="m33det">det</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="geom">
        <div class="sc-section-title">Geometry — Area, Perimeter &amp; Volume</div>
        <div class="sc-fn-input-row">
          <label>Triangle</label>
          <input type="text" id="sc-geo-tri" placeholder="3 sides: a, b, c" value="3, 4, 5">
          <button class="run" data-more="heron">Heron's Area</button>
        </div>
        <div class="sc-fn-input-row">
          <label>Circle r</label>
          <input type="text" id="sc-geo-cir" value="5" style="max-width:100px;">
          <button class="run" data-more="circle">Area &amp; Circumf.</button>
        </div>
        <div class="sc-fn-input-row">
          <label>Sphere r</label>
          <input type="text" id="sc-geo-sph" value="3" style="max-width:100px;">
          <button class="run" data-more="sphere">Vol &amp; Surface</button>
        </div>
        <div class="sc-fn-input-row">
          <label>Cone r,h</label>
          <input type="text" id="sc-geo-cone" value="3, 4" style="max-width:120px;">
          <button class="run" data-more="cone">Volume &amp; Lateral</button>
        </div>
        <div class="sc-fn-input-row">
          <label>Cylinder r,h</label>
          <input type="text" id="sc-geo-cyl" value="3, 5" style="max-width:120px;">
          <button class="run" data-more="cyl">Vol &amp; Surface</button>
        </div>
        <div class="sc-fn-input-row">
          <label>Rectangle l,w</label>
          <input type="text" id="sc-geo-rect" value="6, 4">
          <button class="run" data-more="rect">Area &amp; Perimeter</button>
        </div>
        <div class="sc-fn-input-row">
          <label>Trapezoid a,b,h</label>
          <input type="text" id="sc-geo-trap" value="3, 5, 4">
          <button class="run" data-more="trap">Area</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="complex">
        <div class="sc-section-title">Complex Numbers (a + bi)</div>
        <div class="sc-fn-input-row">
          <label>z₁ (a, b)</label>
          <input type="text" id="sc-cx-z1" value="3, 4">
        </div>
        <div class="sc-fn-input-row">
          <label>z₂ (c, d)</label>
          <input type="text" id="sc-cx-z2" value="1, 2">
          <button class="run" data-more="cx-add">z₁ + z₂</button>
          <button class="run" data-more="cx-sub">z₁ − z₂</button>
        </div>
        <div class="sc-fn-input-row">
          <button class="run" data-more="cx-mul">z₁ × z₂</button>
          <button class="run" data-more="cx-div">z₁ ÷ z₂</button>
          <button class="run" data-more="cx-mag">|z₁|</button>
          <button class="run" data-more="cx-arg">arg(z₁)</button>
        </div>
        <div class="sc-fn-input-row">
          <button class="run" data-more="cx-exp" style="width: 100%;">e^z₁  (Euler's formula)</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="vector">
        <div class="sc-section-title">3D Vectors</div>
        <div class="sc-fn-input-row">
          <label>A = </label>
          <input type="text" id="sc-vec-a" value="1, 2, 3">
        </div>
        <div class="sc-fn-input-row">
          <label>B = </label>
          <input type="text" id="sc-vec-b" value="4, -5, 6">
          <button class="run" data-more="vec-dot">A · B</button>
          <button class="run" data-more="vec-cross">A × B</button>
        </div>
        <div class="sc-fn-input-row">
          <button class="run" data-more="vec-mag">|A|</button>
          <button class="run" data-more="vec-angle">∠ (degrees)</button>
          <button class="run" data-more="vec-proj">proj A onto B</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="seq">
        <div class="sc-section-title">Arithmetic Sequence</div>
        <div class="sc-fn-input-row">
          <label>a₁, d, n</label>
          <input type="text" id="sc-seq-ari" value="2, 3, 10">
          <button class="run" data-more="arith-nth">aₙ</button>
          <button class="run" data-more="arith-sum">Sum Sₙ</button>
        </div>
        <div class="sc-section-title">Geometric Sequence</div>
        <div class="sc-fn-input-row">
          <label>a₁, r, n</label>
          <input type="text" id="sc-seq-geo" value="2, 3, 10">
          <button class="run" data-more="geo-nth">aₙ</button>
          <button class="run" data-more="geo-sum">Sum Sₙ</button>
          <button class="run" data-more="geo-inf">S∞ (if |r|&lt;1)</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="roman">
        <div class="sc-section-title">Roman Numerals</div>
        <div class="sc-fn-input-row">
          <label>Number</label>
          <input type="text" id="sc-rom-n" value="1944">
          <button class="run" data-more="to-roman">→ Roman</button>
        </div>
        <div class="sc-fn-input-row">
          <label>Roman</label>
          <input type="text" id="sc-rom-s" value="MCMXLIV">
          <button class="run" data-more="from-roman">→ Number</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="date">
        <div class="sc-section-title">Date Math</div>
        <div class="sc-fn-input-row">
          <label>Date 1</label>
          <input type="date" id="sc-date-1" value="2000-01-01">
        </div>
        <div class="sc-fn-input-row">
          <label>Date 2</label>
          <input type="date" id="sc-date-2" value="2026-05-11">
          <button class="run" data-more="date-diff">Days between</button>
        </div>
        <div class="sc-section-title">Add Days</div>
        <div class="sc-fn-input-row">
          <label>Date</label>
          <input type="date" id="sc-date-base" value="2026-01-01">
          <label>+ days</label>
          <input type="text" id="sc-date-n" value="100" style="max-width:100px;">
          <button class="run" data-more="date-add">Result</button>
        </div>
        <div class="sc-fn-input-row">
          <label>Day of week</label>
          <input type="date" id="sc-date-dow" value="2026-05-11">
          <button class="run" data-more="dow">Day name</button>
        </div>
      </div>

      <div class="sc-subpane" data-subpane="circuit">
        <div class="sc-section-title">Ohm's Law — V = IR  (leave one blank)</div>
        <div class="sc-fn-input-row">
          <label>V (volts)</label>
          <input type="text" id="sc-ohm-v" placeholder="?" value="">
          <label>I (amps)</label>
          <input type="text" id="sc-ohm-i" placeholder="?" value="0.5">
        </div>
        <div class="sc-fn-input-row">
          <label>R (ohms)</label>
          <input type="text" id="sc-ohm-r" placeholder="?" value="220">
          <button class="run" data-more="ohm">Solve V/I/R + P</button>
        </div>

        <div class="sc-section-title">Voltage Divider — V_out = V_in × R₂/(R₁+R₂)</div>
        <div class="sc-fn-input-row">
          <label>V_in</label>
          <input type="text" id="sc-vd-vin" value="9" style="max-width:90px;">
          <label>R₁ (Ω)</label>
          <input type="text" id="sc-vd-r1" value="1000" style="max-width:100px;">
          <label>R₂ (Ω)</label>
          <input type="text" id="sc-vd-r2" value="2200" style="max-width:100px;">
          <button class="run" data-more="vdiv">V_out</button>
        </div>

        <div class="sc-section-title">Resistors (series &amp; parallel)</div>
        <div class="sc-fn-input-row">
          <label>R values</label>
          <input type="text" id="sc-rlist" placeholder="comma separated" value="100, 220, 470, 1000">
          <button class="run" data-more="rser">Series</button>
          <button class="run" data-more="rpar">Parallel</button>
        </div>

        <div class="sc-section-title">Capacitors (μF — same combiner rules, inverted)</div>
        <div class="sc-fn-input-row">
          <label>C values</label>
          <input type="text" id="sc-clist" placeholder="μF, comma separated" value="10, 22, 47">
          <button class="run" data-more="cser">Series</button>
          <button class="run" data-more="cpar">Parallel</button>
        </div>

        <div class="sc-section-title">Time Constants &amp; LC Resonance</div>
        <div class="sc-fn-input-row">
          <label>R, C</label>
          <input type="text" id="sc-rc" placeholder="R(Ω), C(F) e.g. 1000, 0.000001" value="1000, 0.000001">
          <button class="run" data-more="rc">τ = RC</button>
        </div>
        <div class="sc-fn-input-row">
          <label>R, L</label>
          <input type="text" id="sc-rl" placeholder="R(Ω), L(H)" value="1000, 0.01">
          <button class="run" data-more="rl">τ = L/R</button>
        </div>
        <div class="sc-fn-input-row">
          <label>L, C</label>
          <input type="text" id="sc-lc" placeholder="L(H), C(F)" value="0.01, 0.000001">
          <button class="run" data-more="lcres">LC f₀</button>
        </div>

        <div class="sc-section-title">Reactance &amp; Impedance at frequency f</div>
        <div class="sc-fn-input-row">
          <label>f (Hz)</label>
          <input type="text" id="sc-freq" value="1000" style="max-width:110px;">
          <label>L (H)</label>
          <input type="text" id="sc-xl" value="0.01" style="max-width:110px;">
          <button class="run" data-more="xl">X_L</button>
        </div>
        <div class="sc-fn-input-row">
          <label>f (Hz)</label>
          <input type="text" id="sc-freq2" value="1000" style="max-width:110px;">
          <label>C (F)</label>
          <input type="text" id="sc-xc" value="0.000001" style="max-width:110px;">
          <button class="run" data-more="xc">X_C</button>
        </div>

        <div class="sc-section-title">Resistor Color Code (4-band)</div>
        <div class="sc-fn-input-row">
          <label>Bands</label>
          <input type="text" id="sc-rcc" placeholder="e.g. red red brown gold" value="red red brown gold">
          <button class="run" data-more="rcc">Decode → Ω</button>
        </div>
      </div>
    </div>

    <div class="sc-history">
      <div class="sc-history-title">
        <span>History</span>
        <button type="button" id="sc-clear-hist">clear</button>
      </div>
      <div id="sc-history-list"></div>
    </div>
  </div>
`;

// ──── Math evaluator ────────────────────────────────────────────────────────
// Preprocess a user expression into JS-evaluable form using Math.* and helpers.

function preprocess(expr, angleMode /* 'deg' or 'rad' */) {
  if (typeof expr !== 'string') return '';
  let s = expr.replace(/\s+/g, '');
  // Constants
  s = s.replace(/\bpi\b/g, 'Math.PI');
  s = s.replace(/(?<![A-Za-z0-9_])e(?![A-Za-z0-9_])/g, 'Math.E');
  s = s.replace(/\bphi\b/g, '((1+sqrt(5))/2)');
  // Power operator x^y → Math.pow(x,y), processed right-to-left so chains
  // like 2^3^2 parse as 2^(3^2). Uses a character-level scan so the base
  // can include function calls (sqrt(2)^2) without commas leaking out.
  for (let safety = 0; safety < 100; safety++) {
    const idx = s.lastIndexOf('^');
    if (idx === -1) break;
    let baseStart, baseEnd = idx;
    const prev = s[baseEnd - 1];
    if (prev === ')') {
      let d = 1, i = baseEnd - 2;
      while (i >= 0 && d > 0) {
        if (s[i] === ')') d++;
        else if (s[i] === '(') d--;
        i--;
      }
      baseStart = i + 1;
      while (baseStart > 0 && /[\w.]/.test(s[baseStart - 1])) baseStart--;
    } else if (/[\w.]/.test(prev)) {
      baseStart = baseEnd - 1;
      while (baseStart > 0 && /[\w.]/.test(s[baseStart - 1])) baseStart--;
    } else {
      break;
    }
    let expEnd = idx + 1;
    if (s[expEnd] === '-' || s[expEnd] === '+') expEnd++;
    if (s[expEnd] === '(') {
      let d = 1; expEnd++;
      while (expEnd < s.length && d > 0) {
        if (s[expEnd] === '(') d++;
        else if (s[expEnd] === ')') d--;
        expEnd++;
      }
    } else if (/[\w.]/.test(s[expEnd])) {
      while (expEnd < s.length && /[\w.]/.test(s[expEnd])) expEnd++;
      if (s[expEnd] === '(') {
        let d = 1; expEnd++;
        while (expEnd < s.length && d > 0) {
          if (s[expEnd] === '(') d++;
          else if (s[expEnd] === ')') d--;
          expEnd++;
        }
      }
    } else {
      break;
    }
    const base = s.slice(baseStart, baseEnd);
    const exp = s.slice(idx + 1, expEnd);
    s = s.slice(0, baseStart) + 'Math.pow(' + base + ',' + exp + ')' + s.slice(expEnd);
  }
  // Factorial: 5! → fact(5), (expr)! → fact((expr))
  for (let i = 0; i < 20; i++) {
    const before = s;
    s = s.replace(/(\d+(?:\.\d+)?|\([^()]*\)|[A-Za-z_][A-Za-z0-9_.]*)!/, (m, a) => `fact(${a})`);
    if (s === before) break;
  }
  // Functions (whole-word) — angle conversion for trig
  const trigMap = ['sin','cos','tan'];
  const invTrigMap = ['asin','acos','atan'];
  // If degree mode, sin(x) → Math.sin(x*PI/180); asin(x) → asin(x)*180/PI.
  // We rewrite by wrapping the argument of trig calls.
  if (angleMode === 'deg') {
    for (const fn of trigMap) {
      const re = new RegExp(`\\b${fn}\\(`, 'g');
      s = s.replace(re, `Math.${fn}((Math.PI/180)*`);
    }
    for (const fn of invTrigMap) {
      const re = new RegExp(`\\b${fn}\\(`, 'g');
      s = s.replace(re, `((180/Math.PI)*Math.${fn}(`);
      // We add an extra closing paren; we account for that by adding ) at end of arg.
      // Easier: rely on user-provided closing paren and add a single ) at very end of each replaced call.
      // To make this robust, do it differently below.
    }
  } else {
    for (const fn of trigMap.concat(invTrigMap)) {
      const re = new RegExp(`\\b${fn}\\(`, 'g');
      s = s.replace(re, `Math.${fn}(`);
    }
  }
  // The asin/acos/atan deg-mode replacement above introduced an extra "(" we
  // need to close. Count unbalanced and append matching ")".
  // Detect by counting "((180/Math.PI)*Math.asin(" tokens.
  if (angleMode === 'deg') {
    // For each occurrence of "((180/Math.PI)*Math." we owe one ")".
    const extra = (s.match(/\(\(180\/Math\.PI\)\*Math\.(asin|acos|atan)\(/g) || []).length;
    s = s + ')'.repeat(extra);
  }
  // Hyperbolic & other simple Math.* prefixes
  ['sinh','cosh','tanh','sqrt','cbrt','log10','log2','abs','exp','floor','ceil','round','sign'].forEach(fn => {
    const re = new RegExp(`\\b${fn}\\(`, 'g');
    if (fn === 'log10' || fn === 'log2') s = s.replace(re, `Math.${fn}(`);
    else s = s.replace(re, `Math.${fn}(`);
  });
  // Map "log(x)" (common-log style) → Math.log10(x); "ln(x)" → Math.log(x)
  s = s.replace(/\blog\(/g, 'Math.log10(');
  s = s.replace(/\bln\(/g, 'Math.log(');
  return s;
}

function evalExpr(expr, angleMode) {
  const processed = preprocess(expr, angleMode);
  const fn = new Function('fact', `"use strict"; return (${processed});`);
  return fn(factorial);
}

function factorial(n) {
  if (n < 0 || !Number.isFinite(n)) return NaN;
  if (n !== Math.floor(n)) {
    // Real gamma function approximation (Lanczos for non-integers)
    return gamma(n + 1);
  }
  let r = 1;
  for (let i = 2; i <= n; i++) r *= i;
  return r;
}

// Lanczos gamma approximation for factorial(real)
function gamma(z) {
  const g = 7;
  const C = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
             771.32342877765313, -176.61502916214059, 12.507343278686905,
             -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
  if (z < 0.5) return Math.PI / (Math.sin(Math.PI * z) * gamma(1 - z));
  z -= 1;
  let x = C[0];
  for (let i = 1; i < g + 2; i++) x += C[i] / (z + i);
  const t = z + g + 0.5;
  return Math.sqrt(2 * Math.PI) * Math.pow(t, z + 0.5) * Math.exp(-t) * x;
}

// ──── Stats helpers ─────────────────────────────────────────────────────────

function parseData(s) {
  return (s || '').split(/[\s,]+/).map(x => x.trim()).filter(x => x.length).map(Number).filter(x => !Number.isNaN(x));
}
function mean(a) { return a.reduce((s, x) => s + x, 0) / a.length; }
function median(a) {
  const b = [...a].sort((x, y) => x - y);
  const m = Math.floor(b.length / 2);
  return b.length % 2 ? b[m] : (b[m - 1] + b[m]) / 2;
}
function mode(a) {
  const c = new Map();
  a.forEach(x => c.set(x, (c.get(x) || 0) + 1));
  let best = null, bestN = 0;
  c.forEach((n, x) => { if (n > bestN) { bestN = n; best = x; } });
  return best;
}
function variance(a) {
  const m = mean(a);
  return a.reduce((s, x) => s + (x - m) ** 2, 0) / a.length;
}
function stdev(a) { return Math.sqrt(variance(a)); }
function quartile(a, q) {
  const b = [...a].sort((x, y) => x - y);
  const pos = q * (b.length - 1);
  const lo = Math.floor(pos), hi = Math.ceil(pos);
  return b[lo] + (b[hi] - b[lo]) * (pos - lo);
}

// Normal CDF via Abramowitz & Stegun
function normalCdf(z) {
  const sign = z < 0 ? -1 : 1;
  z = Math.abs(z) / Math.SQRT2;
  // erf approximation
  const t = 1.0 / (1.0 + 0.3275911 * z);
  const y = 1.0 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-z * z);
  return 0.5 * (1.0 + sign * y);
}
// Inverse normal via Beasley-Springer-Moro
function invNorm(p) {
  if (p <= 0 || p >= 1) return NaN;
  const a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02, 1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00];
  const b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02, 6.680131188771972e+01, -1.328068155288572e+01];
  const c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00, -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00];
  const d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00, 3.754408661907416e+00];
  const plow = 0.02425, phigh = 1 - plow;
  let q, r;
  if (p < plow) {
    q = Math.sqrt(-2 * Math.log(p));
    return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1);
  } else if (p <= phigh) {
    q = p - 0.5; r = q * q;
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1);
  } else {
    q = Math.sqrt(-2 * Math.log(1 - p));
    return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1);
  }
}
function nCk(n, k) {
  if (k < 0 || k > n) return 0;
  k = Math.min(k, n - k);
  let r = 1;
  for (let i = 0; i < k; i++) r = r * (n - i) / (i + 1);
  return r;
}
function nPk(n, k) {
  let r = 1;
  for (let i = 0; i < k; i++) r *= (n - i);
  return r;
}
function binomPdf(n, k, p) {
  return nCk(n, k) * Math.pow(p, k) * Math.pow(1 - p, n - k);
}

// ──── Calculus helpers (numerical) ─────────────────────────────────────────

function makeFx(expr) {
  // expr already preprocessed for radian-mode trig (Calc mode is always radians)
  const processed = preprocess(expr, 'rad');
  return new Function('x', 'fact', `"use strict"; return (${processed});`);
}
function derivAt(expr, x0) {
  const f = makeFx(expr);
  const h = 1e-5;
  return (f(x0 + h, factorial) - f(x0 - h, factorial)) / (2 * h);
}
function integrateSimpson(expr, a, b, n = 1000) {
  const f = makeFx(expr);
  if (n % 2) n++;
  const h = (b - a) / n;
  let s = f(a, factorial) + f(b, factorial);
  for (let i = 1; i < n; i++) {
    const x = a + i * h;
    s += (i % 2 === 0 ? 2 : 4) * f(x, factorial);
  }
  return (h / 3) * s;
}
function limitAt(expr, x0) {
  const f = makeFx(expr);
  // Two-sided limit via small h
  const hs = [1e-2, 1e-4, 1e-6];
  const vals = [];
  for (const h of hs) {
    try { vals.push((f(x0 + h, factorial) + f(x0 - h, factorial)) / 2); } catch (e) {}
  }
  // Return the smallest-h value if all finite, else NaN
  return vals.find(v => Number.isFinite(v));
}

// ──── "More" tab helpers ───────────────────────────────────────────────────

// Newton's method root finder. Tries x0 ± perturbations to find any root.
function solveNewton(expr, x0) {
  const f = makeFx(expr);
  const df = (x) => (f(x + 1e-5, factorial) - f(x - 1e-5, factorial)) / 2e-5;
  for (let attempt of [x0, x0 + 1, x0 - 1, x0 + 5, x0 - 5, 0.1, 1, -1]) {
    let x = attempt;
    for (let i = 0; i < 200; i++) {
      const fv = f(x, factorial);
      const dv = df(x);
      if (Math.abs(fv) < 1e-12) return x;
      if (Math.abs(dv) < 1e-14) break;
      x = x - fv / dv;
      if (!Number.isFinite(x)) break;
    }
    if (Number.isFinite(x) && Math.abs(f(x, factorial)) < 1e-8) return x;
  }
  throw new Error('no root found near guess');
}

function quadratic(a, b, c) {
  if (a === 0) return b === 0 ? (c === 0 ? 'all x' : 'no solution') : `x = ${-c / b}`;
  const d = b * b - 4 * a * c;
  if (d > 0) {
    const sq = Math.sqrt(d);
    return `x = ${(-b + sq) / (2 * a)}  or  x = ${(-b - sq) / (2 * a)}`;
  }
  if (d === 0) return `x = ${-b / (2 * a)}  (double root)`;
  const re = -b / (2 * a), im = Math.sqrt(-d) / (2 * a);
  return `x = ${formatResult(re)} ± ${formatResult(im)}i`;
}

function linsys2(r1, r2) {
  const [a, b, c] = r1, [d, e, f] = r2;
  const det = a * e - b * d;
  if (Math.abs(det) < 1e-14) return 'no unique solution (parallel or coincident)';
  return `x = ${formatResult((c * e - b * f) / det)},  y = ${formatResult((a * f - c * d) / det)}`;
}

// Unit conversions ─ everything converts via a canonical SI unit per category.
const UNIT_DEFS = {
  length: {
    m: 1, km: 1000, cm: 0.01, mm: 0.001, mi: 1609.344, yd: 0.9144, ft: 0.3048, in: 0.0254,
    nmi: 1852, ly: 9.461e15, AU: 1.496e11
  },
  mass: { kg: 1, g: 0.001, mg: 1e-6, ton: 1000, lb: 0.45359237, oz: 0.0283495, stone: 6.35029 },
  time: { s: 1, ms: 0.001, min: 60, hr: 3600, day: 86400, week: 604800, year: 31557600 },
  speed: { 'm/s': 1, 'km/h': 1/3.6, 'mph': 0.44704, 'kn': 0.514444, 'ft/s': 0.3048 },
  area: { 'm²': 1, 'km²': 1e6, 'cm²': 1e-4, 'mm²': 1e-6, 'ha': 10000, 'acre': 4046.86, 'ft²': 0.092903 },
  volume: { L: 1, mL: 0.001, 'm³': 1000, 'cm³': 0.001, 'gal_us': 3.78541, 'gal_uk': 4.54609, 'qt_us': 0.946353, 'pt_us': 0.473176, 'fl_oz': 0.0295735 },
  energy: { J: 1, kJ: 1000, cal: 4.184, kcal: 4184, Wh: 3600, kWh: 3.6e6, eV: 1.602e-19, BTU: 1055.06 },
};
// Temperature is special — handled separately.
function convertUnits(category, value, fromU, toU) {
  if (category === 'temperature') {
    let K;
    if (fromU === '°C') K = value + 273.15;
    else if (fromU === '°F') K = (value - 32) * 5/9 + 273.15;
    else K = value; // K
    if (toU === '°C') return K - 273.15;
    if (toU === '°F') return (K - 273.15) * 9/5 + 32;
    return K;
  }
  const defs = UNIT_DEFS[category];
  if (!defs) throw new Error('unknown category');
  return value * defs[fromU] / defs[toU];
}
function unitsFor(category) {
  if (category === 'temperature') return ['°C', '°F', 'K'];
  return Object.keys(UNIT_DEFS[category]);
}

// Number theory
function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a; }
function gcdN(arr) { return arr.reduce((a, b) => gcd(a, b)); }
function lcm(a, b) { return Math.abs(a * b) / gcd(a, b); }
function lcmN(arr) { return arr.reduce((a, b) => lcm(a, b)); }
function factorize(n) {
  n = Math.abs(n); if (n < 2) return [];
  const factors = [];
  for (let p = 2; p * p <= n; p++) {
    while (n % p === 0) { factors.push(p); n = n / p; }
  }
  if (n > 1) factors.push(n);
  // Group as p^k
  const counts = new Map();
  factors.forEach(p => counts.set(p, (counts.get(p) || 0) + 1));
  return [...counts.entries()].map(([p, k]) => k === 1 ? `${p}` : `${p}^${k}`).join(' × ');
}
function isPrime(n) {
  if (n < 2 || !Number.isInteger(n)) return false;
  if (n < 4) return true;
  if (n % 2 === 0) return false;
  for (let i = 3; i * i <= n; i += 2) if (n % i === 0) return false;
  return true;
}
function fibonacci(n) {
  if (n < 0) return NaN;
  let a = 0, b = 1;
  for (let i = 0; i < n; i++) [a, b] = [b, a + b];
  return a;
}
function nthPrime(n) {
  if (n < 1) return NaN;
  let count = 0, p = 1;
  while (count < n) { p++; if (isPrime(p)) count++; }
  return p;
}

// Matrices
function det2(m) { return m[0][0]*m[1][1] - m[0][1]*m[1][0]; }
function inv2(m) {
  const d = det2(m);
  if (Math.abs(d) < 1e-14) return null;
  return [[m[1][1]/d, -m[0][1]/d], [-m[1][0]/d, m[0][0]/d]];
}
function det3(m) {
  return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
       - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
       + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]);
}

// Convert number to a given base (2..36) supporting negative & fractional values.
function toBase(value, base) {
  if (!Number.isFinite(value)) return String(value);
  if (Number.isInteger(value)) return value.toString(base).toUpperCase();
  // Fractional: keep 12 digits after the point.
  const neg = value < 0; value = Math.abs(value);
  const intPart = Math.floor(value);
  let s = intPart.toString(base).toUpperCase() + '.';
  let frac = value - intPart;
  for (let i = 0; i < 12 && frac > 1e-15; i++) {
    frac *= base;
    const d = Math.floor(frac);
    s += d.toString(base).toUpperCase();
    frac -= d;
  }
  return (neg ? '-' : '') + s.replace(/\.?0+$/, '');
}

// Plot: draw f(x) on a canvas.
function drawPlot(canvas, expr, xmin, xmax) {
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  ctx.clearRect(0, 0, W, H);
  ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, W, H);

  // Sample
  const N = 400;
  const f = makeFx(expr);
  const xs = [], ys = [];
  let ymin = Infinity, ymax = -Infinity;
  for (let i = 0; i <= N; i++) {
    const x = xmin + (xmax - xmin) * i / N;
    let y;
    try { y = f(x, factorial); } catch (e) { y = NaN; }
    xs.push(x); ys.push(y);
    if (Number.isFinite(y)) { ymin = Math.min(ymin, y); ymax = Math.max(ymax, y); }
  }
  if (!Number.isFinite(ymin)) { ymin = -1; ymax = 1; }
  if (ymin === ymax) { ymin -= 1; ymax += 1; }
  const pad = (ymax - ymin) * 0.08;
  ymin -= pad; ymax += pad;

  // Axis transforms (pixel padding 32 each side)
  const PAD = 32;
  const toPx = (x) => PAD + (x - xmin) / (xmax - xmin) * (W - 2 * PAD);
  const toPy = (y) => H - PAD - (y - ymin) / (ymax - ymin) * (H - 2 * PAD);

  // Gridlines
  ctx.strokeStyle = '#1e293b'; ctx.lineWidth = 1;
  for (let gx = 0; gx <= 8; gx++) {
    const px = PAD + gx * (W - 2 * PAD) / 8;
    ctx.beginPath(); ctx.moveTo(px, PAD); ctx.lineTo(px, H - PAD); ctx.stroke();
  }
  for (let gy = 0; gy <= 6; gy++) {
    const py = PAD + gy * (H - 2 * PAD) / 6;
    ctx.beginPath(); ctx.moveTo(PAD, py); ctx.lineTo(W - PAD, py); ctx.stroke();
  }

  // Axes (x=0, y=0 if visible)
  ctx.strokeStyle = '#475569'; ctx.lineWidth = 1.5;
  if (0 >= xmin && 0 <= xmax) {
    const px = toPx(0);
    ctx.beginPath(); ctx.moveTo(px, PAD); ctx.lineTo(px, H - PAD); ctx.stroke();
  }
  if (0 >= ymin && 0 <= ymax) {
    const py = toPy(0);
    ctx.beginPath(); ctx.moveTo(PAD, py); ctx.lineTo(W - PAD, py); ctx.stroke();
  }

  // Labels
  ctx.fillStyle = '#cbd5e1'; ctx.font = '10px monospace';
  ctx.fillText(formatResult(xmin), PAD, H - 12);
  ctx.fillText(formatResult(xmax), W - PAD - 30, H - 12);
  ctx.fillText(formatResult(ymax), 4, PAD + 4);
  ctx.fillText(formatResult(ymin), 4, H - PAD);

  // Curve
  ctx.strokeStyle = '#00e5c8'; ctx.lineWidth = 2; ctx.beginPath();
  let pendown = false;
  for (let i = 0; i <= N; i++) {
    const x = xs[i], y = ys[i];
    if (!Number.isFinite(y)) { pendown = false; continue; }
    const px = toPx(x), py = toPy(y);
    if (!pendown) { ctx.moveTo(px, py); pendown = true; }
    else ctx.lineTo(px, py);
  }
  ctx.stroke();
}

// ──── Extended calculus: Σ Π Taylor partial-derivative higher-derivatives ──

// Build f(k) where the variable name is `k` (or whatever string is passed).
function makeFofVar(expr, varName) {
  const processed = preprocess(expr, 'rad');
  return new Function(varName, 'fact', `"use strict"; return (${processed});`);
}
function summation(expr, varName, a, b) {
  const f = makeFofVar(expr, varName);
  let s = 0;
  for (let k = a; k <= b; k++) s += f(k, factorial);
  return s;
}
function productOf(expr, varName, a, b) {
  const f = makeFofVar(expr, varName);
  let p = 1;
  for (let k = a; k <= b; k++) p *= f(k, factorial);
  return p;
}
function nthDerivativeNumeric(expr, x0, n) {
  if (n === 0) return makeFx(expr)(x0, factorial);
  const h = 1e-2; // larger h for stability of higher derivatives
  // Central difference formula for nth derivative
  let s = 0;
  for (let k = 0; k <= n; k++) {
    const sign = k % 2 === 0 ? 1 : -1;
    const c = nCk(n, k);
    s += sign * c * makeFx(expr)(x0 + (n - 2 * k) * h / 2, factorial);
  }
  return s / Math.pow(h, n);
}
function taylor(expr, a, N) {
  const terms = [];
  for (let n = 0; n <= N; n++) {
    const d = nthDerivativeNumeric(expr, a, n);
    const coef = d / factorial(n);
    if (Math.abs(coef) < 1e-9) continue;
    const sign = coef >= 0 ? (terms.length ? ' + ' : '') : (terms.length ? ' − ' : '−');
    const absCoef = formatResult(Math.abs(coef));
    const xterm = n === 0 ? '' : (a === 0 ? `x^${n}` : `(x − ${a})^${n}`);
    terms.push(`${sign}${absCoef}${xterm ? '·' + xterm : ''}`);
  }
  return terms.join('') || '0';
}
function partial(expr, varIdx, pt) {
  // g(x, y) → partial wrt x (idx 0) or y (idx 1) using central difference
  const processed = preprocess(expr, 'rad');
  const g = new Function('x', 'y', 'fact', `"use strict"; return (${processed});`);
  const h = 1e-5;
  const [x, y] = pt;
  if (varIdx === 0) return (g(x + h, y, factorial) - g(x - h, y, factorial)) / (2 * h);
  return (g(x, y + h, factorial) - g(x, y - h, factorial)) / (2 * h);
}

// ──── Extended distributions & regression ──────────────────────────────────

function poissonPmf(lam, k) {
  return Math.exp(-lam) * Math.pow(lam, k) / factorial(k);
}
function expCdf(rate, x) {
  return x < 0 ? 0 : 1 - Math.exp(-rate * x);
}
// Lower-incomplete-gamma / regularized P(a, x) via series + continued fraction
function gammaIncomplete(a, x) {
  // Regularized: P(a,x) = γ(a,x) / Γ(a)
  if (x < 0 || a <= 0) return NaN;
  if (x === 0) return 0;
  if (x < a + 1) {
    // Series
    let ap = a, sum = 1 / a, del = sum;
    for (let n = 1; n < 200; n++) {
      ap += 1;
      del *= x / ap;
      sum += del;
      if (Math.abs(del) < Math.abs(sum) * 1e-12) break;
    }
    return sum * Math.exp(-x + a * Math.log(x) - gammaLn(a));
  } else {
    // Continued fraction
    let b = x + 1 - a, c = 1e30, d = 1 / b, h = d;
    for (let i = 1; i < 200; i++) {
      const an = -i * (i - a);
      b += 2;
      d = an * d + b;
      if (Math.abs(d) < 1e-30) d = 1e-30;
      c = b + an / c;
      if (Math.abs(c) < 1e-30) c = 1e-30;
      d = 1 / d;
      const del = d * c;
      h *= del;
      if (Math.abs(del - 1) < 1e-12) break;
    }
    return 1 - Math.exp(-x + a * Math.log(x) - gammaLn(a)) * h;
  }
}
function gammaLn(z) {
  // log gamma via Lanczos
  return Math.log(gamma(z));
}
function chiSquareCdf(df, x) {
  return gammaIncomplete(df / 2, x / 2);
}
// Student's t CDF via relationship to regularized incomplete beta
function betaIncomplete(a, b, x) {
  if (x <= 0) return 0;
  if (x >= 1) return 1;
  // Continued fraction for I_x(a, b)
  const lbeta = gammaLn(a) + gammaLn(b) - gammaLn(a + b);
  const front = Math.exp(Math.log(x) * a + Math.log(1 - x) * b - lbeta) / a;
  // Lentz's algorithm
  let fpmin = 1e-30;
  let c = 1, d = 1 - (a + b) * x / (a + 1);
  if (Math.abs(d) < fpmin) d = fpmin;
  d = 1 / d;
  let h = d;
  for (let m = 1; m < 200; m++) {
    const m2 = 2 * m;
    let aa = m * (b - m) * x / ((a + m2 - 1) * (a + m2));
    d = 1 + aa * d;
    if (Math.abs(d) < fpmin) d = fpmin;
    c = 1 + aa / c;
    if (Math.abs(c) < fpmin) c = fpmin;
    d = 1 / d;
    h *= d * c;
    aa = -(a + m) * (a + b + m) * x / ((a + m2) * (a + m2 + 1));
    d = 1 + aa * d;
    if (Math.abs(d) < fpmin) d = fpmin;
    c = 1 + aa / c;
    if (Math.abs(c) < fpmin) c = fpmin;
    d = 1 / d;
    const del = d * c;
    h *= del;
    if (Math.abs(del - 1) < 1e-12) break;
  }
  return front * h;
}
function tCdf(df, t) {
  // P(T ≤ t) = 1 - 0.5 I_{df/(df+t²)}(df/2, 1/2) for t>0, and reflected for t<0
  const x = df / (df + t * t);
  const I = betaIncomplete(df / 2, 0.5, x);
  return t >= 0 ? 1 - 0.5 * I : 0.5 * I;
}
function linearRegression(xs, ys) {
  const n = xs.length;
  const mx = mean(xs), my = mean(ys);
  let num = 0, den = 0;
  for (let i = 0; i < n; i++) { num += (xs[i] - mx) * (ys[i] - my); den += (xs[i] - mx) ** 2; }
  const m = num / den;
  const b = my - m * mx;
  // r²
  let ssTot = 0, ssRes = 0;
  for (let i = 0; i < n; i++) { ssTot += (ys[i] - my) ** 2; ssRes += (ys[i] - (m * xs[i] + b)) ** 2; }
  const r2 = 1 - ssRes / ssTot;
  return { m, b, r2 };
}

// ──── Geometry ──────────────────────────────────────────────────────────────

function heron(a, b, c) {
  const s = (a + b + c) / 2;
  const A = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  return `area = ${formatResult(A)}, perimeter = ${formatResult(a + b + c)}`;
}
function geoCircle(r) {
  return `area = ${formatResult(Math.PI * r * r)}, circumference = ${formatResult(2 * Math.PI * r)}`;
}
function geoSphere(r) {
  return `volume = ${formatResult((4/3) * Math.PI * r ** 3)}, surface = ${formatResult(4 * Math.PI * r * r)}`;
}
function geoCone(r, h) {
  const lateral = Math.PI * r * Math.sqrt(r * r + h * h);
  return `volume = ${formatResult((1/3) * Math.PI * r * r * h)}, lateral = ${formatResult(lateral)}`;
}
function geoCylinder(r, h) {
  return `volume = ${formatResult(Math.PI * r * r * h)}, surface = ${formatResult(2 * Math.PI * r * (r + h))}`;
}
function geoRect(l, w) {
  return `area = ${formatResult(l * w)}, perimeter = ${formatResult(2 * (l + w))}`;
}
function geoTrap(a, b, h) {
  return `area = ${formatResult((a + b) / 2 * h)}`;
}

// ──── Complex numbers ─────────────────────────────────────────────────────

function cxFmt(a, b) {
  if (Math.abs(b) < 1e-12) return formatResult(a);
  if (Math.abs(a) < 1e-12) return `${formatResult(b)}i`;
  return `${formatResult(a)} ${b >= 0 ? '+' : '−'} ${formatResult(Math.abs(b))}i`;
}
const cxAdd = (a, b, c, d) => cxFmt(a + c, b + d);
const cxSub = (a, b, c, d) => cxFmt(a - c, b - d);
const cxMul = (a, b, c, d) => cxFmt(a * c - b * d, a * d + b * c);
function cxDiv(a, b, c, d) {
  const den = c * c + d * d;
  if (den === 0) return 'undefined (division by 0)';
  return cxFmt((a * c + b * d) / den, (b * c - a * d) / den);
}
const cxMag = (a, b) => Math.sqrt(a * a + b * b);
const cxArg = (a, b) => Math.atan2(b, a);
function cxExp(a, b) {
  return cxFmt(Math.exp(a) * Math.cos(b), Math.exp(a) * Math.sin(b));
}

// ──── 3D Vectors ────────────────────────────────────────────────────────────

function vDot(A, B) { return A[0]*B[0] + A[1]*B[1] + A[2]*B[2]; }
function vCross(A, B) {
  return [A[1]*B[2]-A[2]*B[1], A[2]*B[0]-A[0]*B[2], A[0]*B[1]-A[1]*B[0]];
}
function vMag(A) { return Math.sqrt(A[0]**2 + A[1]**2 + A[2]**2); }
function vAngle(A, B) {
  return Math.acos(vDot(A, B) / (vMag(A) * vMag(B))) * 180 / Math.PI;
}
function vProj(A, B) {
  const scale = vDot(A, B) / (vMag(B) ** 2);
  return [scale * B[0], scale * B[1], scale * B[2]];
}

// ──── Sequences ────────────────────────────────────────────────────────────

function arithNth(a1, d, n) { return a1 + (n - 1) * d; }
function arithSum(a1, d, n) { return n * (2 * a1 + (n - 1) * d) / 2; }
function geoNth(a1, r, n) { return a1 * Math.pow(r, n - 1); }
function geoSum(a1, r, n) {
  if (r === 1) return a1 * n;
  return a1 * (1 - Math.pow(r, n)) / (1 - r);
}
function geoInfSum(a1, r) {
  if (Math.abs(r) >= 1) return 'diverges (|r| ≥ 1)';
  return a1 / (1 - r);
}

// ──── Roman numerals ───────────────────────────────────────────────────────

const ROMAN = [
  [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
  [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
  [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
];
function toRoman(n) {
  if (!Number.isInteger(n) || n < 1 || n > 3999) return 'out of range (1–3999)';
  let out = '';
  for (const [v, s] of ROMAN) { while (n >= v) { out += s; n -= v; } }
  return out;
}
function fromRoman(s) {
  s = (s || '').trim().toUpperCase();
  const map = { I:1, V:5, X:10, L:50, C:100, D:500, M:1000 };
  let total = 0;
  for (let i = 0; i < s.length; i++) {
    const cur = map[s[i]], next = map[s[i + 1]];
    if (!cur) return NaN;
    total += (next && next > cur) ? -cur : cur;
  }
  return total;
}

// ──── Date math ─────────────────────────────────────────────────────────────

function daysBetween(s1, s2) {
  const d1 = new Date(s1), d2 = new Date(s2);
  return Math.round((d2 - d1) / (1000 * 60 * 60 * 24));
}
function addDays(s, n) {
  const d = new Date(s);
  d.setDate(d.getDate() + Number(n));
  return d.toISOString().slice(0, 10);
}
function dayOfWeek(s) {
  const names = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  return names[new Date(s).getDay()];
}

// ──── Circuit / electronics ────────────────────────────────────────────────

function siNumber(v, unit) {
  // Format a number with SI prefix (kΩ, mA, μF, etc.).
  const abs = Math.abs(v);
  if (abs === 0) return `0 ${unit}`;
  const prefixes = [[1e9,'G'],[1e6,'M'],[1e3,'k'],[1,''],[1e-3,'m'],[1e-6,'µ'],[1e-9,'n'],[1e-12,'p']];
  for (const [mag, pre] of prefixes) {
    if (abs >= mag) return `${formatResult(v / mag)} ${pre}${unit}`;
  }
  return `${formatResult(v)} ${unit}`;
}

function ohmSolve(V, I, R) {
  // Solve for the missing variable. Returns object {V, I, R, P}.
  const has = { V: V !== '' && !isNaN(parseFloat(V)),
                I: I !== '' && !isNaN(parseFloat(I)),
                R: R !== '' && !isNaN(parseFloat(R)) };
  const count = Object.values(has).filter(Boolean).length;
  if (count < 2) throw new Error('need at least 2 of V, I, R');
  V = has.V ? parseFloat(V) : null;
  I = has.I ? parseFloat(I) : null;
  R = has.R ? parseFloat(R) : null;
  if (V === null) V = I * R;
  if (I === null) I = V / R;
  if (R === null) R = V / I;
  const P = V * I;
  return { V, I, R, P };
}

function voltageDivider(Vin, R1, R2) { return Vin * R2 / (R1 + R2); }
function resistorsSeries(rs) { return rs.reduce((s, r) => s + r, 0); }
function resistorsParallel(rs) { return 1 / rs.reduce((s, r) => s + 1 / r, 0); }
// Capacitors are inverse: series 1/Ctot = Σ1/Ci; parallel Ctot = ΣCi
function capacitorsSeries(cs) { return 1 / cs.reduce((s, c) => s + 1 / c, 0); }
function capacitorsParallel(cs) { return cs.reduce((s, c) => s + c, 0); }
function lcResonance(L, C) { return 1 / (2 * Math.PI * Math.sqrt(L * C)); }
function reactanceL(f, L) { return 2 * Math.PI * f * L; }
function reactanceC(f, C) { return 1 / (2 * Math.PI * f * C); }

// Resistor 4-band color code
const RESISTOR_DIGITS = {
  black: 0, brown: 1, red: 2, orange: 3, yellow: 4,
  green: 5, blue: 6, violet: 7, purple: 7, gray: 8, grey: 8, white: 9
};
const RESISTOR_MULT = {
  black: 1, brown: 10, red: 100, orange: 1000, yellow: 10000,
  green: 100000, blue: 1000000, violet: 10000000, purple: 10000000,
  gray: 100000000, grey: 100000000, white: 1000000000,
  gold: 0.1, silver: 0.01
};
const RESISTOR_TOL = { brown: 1, red: 2, green: 0.5, blue: 0.25, violet: 0.1, purple: 0.1, gray: 0.05, grey: 0.05, gold: 5, silver: 10, none: 20 };
function decodeResistor(bandStr) {
  const bands = bandStr.trim().toLowerCase().split(/\s+/);
  if (bands.length < 3) throw new Error('need at least 3 color bands');
  const d1 = RESISTOR_DIGITS[bands[0]];
  const d2 = RESISTOR_DIGITS[bands[1]];
  const mult = RESISTOR_MULT[bands[2]];
  if (d1 === undefined || d2 === undefined || mult === undefined) throw new Error('unknown color band');
  const value = (d1 * 10 + d2) * mult;
  const tol = bands[3] ? (RESISTOR_TOL[bands[3]] ?? '?') : 20;
  return `${siNumber(value, 'Ω')}  ±${tol}%`;
}

// ──── UI plumbing ──────────────────────────────────────────────────────────

const HIST_KEY = 'mga_supercalc_history_v1';
function readHist() {
  try { return JSON.parse(localStorage.getItem(HIST_KEY) || '[]'); } catch (e) { return []; }
}
function writeHist(arr) {
  try { localStorage.setItem(HIST_KEY, JSON.stringify(arr.slice(0, 30))); } catch (e) {}
}

function formatResult(v) {
  if (typeof v !== 'number') return String(v);
  if (Number.isNaN(v)) return 'NaN';
  if (!Number.isFinite(v)) return v > 0 ? '∞' : '-∞';
  // Trim trailing tiny float noise
  if (Math.abs(v - Math.round(v)) < 1e-10) return String(Math.round(v));
  const rounded = parseFloat(v.toPrecision(12));
  return String(rounded);
}

export function initSuperCalculator() {
  if (document.getElementById('sc-fab')) return; // idempotent
  // Inject styles once
  if (!document.getElementById('sc-styles')) {
    const style = document.createElement('style');
    style.id = 'sc-styles';
    style.textContent = STYLES;
    document.head.appendChild(style);
  }
  // Inject FAB
  const fabHost = document.createElement('div');
  fabHost.innerHTML = FAB_HTML;
  document.body.appendChild(fabHost.firstElementChild);
  // Inject overlay (created on first open to keep TTI fast — but small enough, build now)
  const overlay = document.createElement('div');
  overlay.id = 'sc-overlay';
  overlay.innerHTML = MODAL_HTML;
  document.body.appendChild(overlay);

  const exprEl = overlay.querySelector('#sc-expr');
  const resEl = overlay.querySelector('#sc-result');
  const histList = overlay.querySelector('#sc-history-list');

  let exprStr = '';
  let angleMode = 'deg';
  let activeTab = 'basic';

  function renderHistory() {
    const items = readHist();
    histList.innerHTML = items.map(it =>
      `<div class="sc-history-item" data-expr="${escapeHtml(it.e)}">${escapeHtml(it.e)} = <strong>${escapeHtml(it.r)}</strong></div>`
    ).join('') || '<div style="color:#94a3b8;">No calculations yet.</div>';
  }
  function pushHistory(e, r) {
    const items = readHist();
    items.unshift({ e, r });
    writeHist(items);
    renderHistory();
  }
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }

  function setExpr(s) {
    exprStr = s;
    exprEl.textContent = exprStr;
  }
  function showResult(v, isErr) {
    resEl.classList.toggle('err', !!isErr);
    resEl.textContent = isErr ? String(v) : formatResult(v);
  }
  function runEval() {
    if (!exprStr.trim()) return;
    try {
      const v = evalExpr(exprStr, angleMode);
      showResult(v, false);
      pushHistory(exprStr, formatResult(v));
    } catch (e) {
      showResult('Error: ' + (e.message || e), true);
    }
  }

  // ─── Sign-in gate ──────────────────────────────────────────────────────
  // Build a small sign-in overlay shown when an unauthenticated user clicks
  // the FAB. The calculator itself is only opened for signed-in users.
  let currentUser = null;
  // Resolve login URL from the current page depth (e.g., /courses/X/Y → ../../login.html).
  const loginUrl = (() => {
    const path = location.pathname.replace(/\/$/, '');
    const depth = path.split('/').filter(Boolean).length - (path.endsWith('.html') ? 1 : 0);
    return depth <= 0 ? 'login.html' : '../'.repeat(depth) + 'login.html';
  })();
  const signinOverlay = document.createElement('div');
  signinOverlay.id = 'sc-signin-overlay';
  signinOverlay.innerHTML = `
    <style>
      #sc-signin-overlay {
        position: fixed; inset: 0; z-index: 9992;
        background: rgba(15, 23, 42, 0.55);
        display: none; align-items: center; justify-content: center;
        padding: 16px; backdrop-filter: blur(3px);
      }
      #sc-signin-overlay.open { display: flex; }
      .sc-signin-card {
        background: #fff; border-radius: 18px; padding: 36px 28px 28px;
        max-width: 380px; width: 100%; text-align: center;
        box-shadow: 0 20px 60px rgba(0,0,0,0.30);
      }
      .sc-signin-card .lock { font-size: 2.4rem; margin-bottom: 8px; }
      .sc-signin-card h3 { font-size: 1.3rem; font-weight: 800; margin-bottom: 6px; color: #1f1108; }
      .sc-signin-card p { font-size: 0.92rem; color: #64748b; margin-bottom: 22px; line-height: 1.55; }
      .sc-signin-card .btn-sign {
        display: inline-block; padding: 12px 28px;
        background: linear-gradient(135deg, #00e5c8, #00b89f);
        color: #fff; font-weight: 800; font-size: 1rem;
        border-radius: 12px; text-decoration: none;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
      }
      .sc-signin-card .btn-sign:hover { transform: translateY(-1px); box-shadow: 0 6px 14px rgba(0,184,159,0.30); }
      .sc-signin-card .cancel {
        display: block; margin-top: 14px;
        background: transparent; border: none; color: #94a3b8;
        font-size: 0.85rem; cursor: pointer; text-decoration: underline;
      }
    </style>
    <div class="sc-signin-card" role="dialog" aria-modal="true" aria-labelledby="sc-signin-title">
      <div class="lock" aria-hidden="true">&#128274;</div>
      <h3 id="sc-signin-title">Sign in to use the Super Calculator</h3>
      <p>The Super Calculator — 5 tabs, sigma summation, Taylor series, plotting, Ohm's law, and 12 other tools — is free for signed-in learners.</p>
      <a href="${loginUrl}" class="btn-sign">Sign In or Sign Up</a>
      <button type="button" class="cancel" id="sc-signin-cancel">Cancel</button>
    </div>
  `;
  document.body.appendChild(signinOverlay);
  signinOverlay.addEventListener('click', (e) => {
    if (e.target === signinOverlay || e.target.id === 'sc-signin-cancel') signinOverlay.classList.remove('open');
  });

  // Track auth state. Loaded lazily so this module has no hard dep on auth.js
  // when Firebase isn't configured (e.g. translate.goog pages).
  import('./auth.js').then(({ onAuthChange }) => {
    onAuthChange((user) => { currentUser = user; });
  }).catch(() => { /* ignore — gate will still appear, redirecting to login */ });

  // FAB → open (gated)
  document.getElementById('sc-fab').addEventListener('click', () => {
    if (!currentUser) {
      signinOverlay.classList.add('open');
      return;
    }
    overlay.classList.add('open');
    renderHistory();
  });
  // Close
  overlay.querySelector('#sc-close').addEventListener('click', () => overlay.classList.remove('open'));
  overlay.addEventListener('click', (e) => { if (e.target === overlay) overlay.classList.remove('open'); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (overlay.classList.contains('open')) overlay.classList.remove('open');
      if (signinOverlay.classList.contains('open')) signinOverlay.classList.remove('open');
    }
  });

  // Tabs
  overlay.querySelectorAll('.sc-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      activeTab = btn.dataset.tab;
      overlay.querySelectorAll('.sc-tab').forEach(b => b.classList.toggle('active', b === btn));
      overlay.querySelectorAll('.sc-pane').forEach(p => p.classList.toggle('active', p.dataset.pane === activeTab));
    });
  });

  // Angle mode toggle (Trig)
  overlay.querySelectorAll('.sc-anglemode button').forEach(btn => {
    btn.addEventListener('click', () => {
      angleMode = btn.dataset.angle;
      overlay.querySelectorAll('.sc-anglemode button').forEach(b => b.classList.toggle('active', b === btn));
    });
  });

  // Basic/Trig number+function buttons (insert / clear / back / eval)
  overlay.querySelectorAll('.sc-grid button').forEach(btn => {
    btn.addEventListener('click', () => {
      const ins = btn.dataset.ins;
      const act = btn.dataset.act;
      if (ins !== undefined) setExpr(exprStr + ins);
      else if (act === 'clear') { setExpr(''); showResult(0, false); }
      else if (act === 'back') setExpr(exprStr.slice(0, -1));
      else if (act === 'eval') runEval();
    });
  });

  // Stats — dataset statistics
  overlay.querySelectorAll('[data-stat]').forEach(btn => {
    btn.addEventListener('click', () => {
      const stat = btn.dataset.stat;
      const data = parseData(overlay.querySelector('#sc-data').value);
      if (data.length === 0) { showResult('Enter at least one number', true); return; }
      let v;
      switch (stat) {
        case 'mean': v = mean(data); break;
        case 'median': v = median(data); break;
        case 'mode': v = mode(data); break;
        case 'stdev': v = stdev(data); break;
        case 'variance': v = variance(data); break;
        case 'range': v = Math.max(...data) - Math.min(...data); break;
        case 'sum': v = data.reduce((s, x) => s + x, 0); break;
        case 'count': v = data.length; break;
        case 'min': v = Math.min(...data); break;
        case 'max': v = Math.max(...data); break;
        case 'q1': v = quartile(data, 0.25); break;
        case 'q3': v = quartile(data, 0.75); break;
      }
      setExpr(`${stat}([${data.join(',')}])`);
      showResult(v, false);
      pushHistory(`${stat}([${data.length}])`, formatResult(v));
    });
  });

  // Stats — distributions
  overlay.querySelectorAll('[data-dist]').forEach(btn => {
    btn.addEventListener('click', () => {
      const dist = btn.dataset.dist;
      try {
        let v, label;
        if (dist === 'normalcdf') {
          const z = parseFloat(overlay.querySelector('#sc-z').value);
          v = normalCdf(z); label = `P(Z ≤ ${z})`;
        } else if (dist === 'invnorm') {
          const p = parseFloat(overlay.querySelector('#sc-p').value);
          v = invNorm(p); label = `invNorm(${p})`;
        } else if (dist === 'nCk' || dist === 'nPk') {
          const [n, k] = parseData(overlay.querySelector('#sc-nk').value);
          v = dist === 'nCk' ? nCk(n, k) : nPk(n, k);
          label = `${dist}(${n}, ${k})`;
        } else if (dist === 'binompdf') {
          const [n, k, p] = parseData(overlay.querySelector('#sc-bnk').value);
          v = binomPdf(n, k, p);
          label = `binompdf(${n}, ${k}, ${p})`;
        } else if (dist === 'poisson') {
          const [lam, k] = parseData(overlay.querySelector('#sc-poi').value);
          v = poissonPmf(lam, k);
          label = `Poisson(λ=${lam}, k=${k})`;
        } else if (dist === 'exp') {
          const [rate, x] = parseData(overlay.querySelector('#sc-exp').value);
          v = expCdf(rate, x);
          label = `Exp CDF (λ=${rate}, x=${x})`;
        } else if (dist === 'tcdf') {
          const [df, t] = parseData(overlay.querySelector('#sc-tdist').value);
          v = tCdf(df, t);
          label = `T CDF (df=${df}, t=${t})`;
        } else if (dist === 'chi2') {
          const [df, x] = parseData(overlay.querySelector('#sc-chi').value);
          v = chiSquareCdf(df, x);
          label = `χ² CDF (df=${df}, x=${x})`;
        } else if (dist === 'linreg') {
          const xs = parseData(overlay.querySelector('#sc-regx').value);
          const ys = parseData(overlay.querySelector('#sc-regy').value);
          if (xs.length !== ys.length || xs.length < 2) throw new Error('need equal-length x,y with ≥2 points');
          const { m, b, r2 } = linearRegression(xs, ys);
          v = `y = ${formatResult(m)}x ${b >= 0 ? '+' : '−'} ${formatResult(Math.abs(b))}   (r² = ${formatResult(r2)})`;
          label = `linreg of ${xs.length} points`;
        }
        setExpr(label);
        showResult(v, false);
        pushHistory(label, typeof v === 'string' ? v : formatResult(v));
      } catch (e) {
        showResult('Error: ' + (e.message || e), true);
      }
    });
  });

  // Calculus
  overlay.querySelectorAll('[data-calc]').forEach(btn => {
    btn.addEventListener('click', () => {
      const op = btn.dataset.calc;
      const fxExpr = overlay.querySelector('#sc-fx').value;
      try {
        let v, label;
        if (op === 'deriv') {
          const x0 = parseFloat(overlay.querySelector('#sc-derivx').value);
          v = derivAt(fxExpr, x0); label = `d/dx [${fxExpr}] at x=${x0}`;
        } else if (op === 'eval') {
          const x0 = parseFloat(overlay.querySelector('#sc-evalx').value);
          v = makeFx(fxExpr)(x0, factorial); label = `f(${x0}) where f(x) = ${fxExpr}`;
        } else if (op === 'integ') {
          const a = parseFloat(overlay.querySelector('#sc-inta').value);
          const b = parseFloat(overlay.querySelector('#sc-intb').value);
          v = integrateSimpson(fxExpr, a, b); label = `∫[${a},${b}] ${fxExpr} dx`;
        } else if (op === 'limit') {
          const x0 = parseFloat(overlay.querySelector('#sc-limx').value);
          v = limitAt(fxExpr, x0); label = `lim x→${x0} [${fxExpr}]`;
        } else if (op === 'deriv2') {
          const x0 = parseFloat(overlay.querySelector('#sc-deriv2x').value);
          v = nthDerivativeNumeric(fxExpr, x0, 2); label = `d²/dx² [${fxExpr}] at x=${x0}`;
        } else if (op === 'deriv3') {
          const x0 = parseFloat(overlay.querySelector('#sc-deriv2x').value);
          v = nthDerivativeNumeric(fxExpr, x0, 3); label = `d³/dx³ [${fxExpr}] at x=${x0}`;
        } else if (op === 'sigma') {
          const expr = overlay.querySelector('#sc-sigmaf').value;
          const a = parseInt(overlay.querySelector('#sc-sigma-a').value, 10);
          const b = parseInt(overlay.querySelector('#sc-sigma-b').value, 10);
          v = summation(expr, 'k', a, b); label = `Σ[k=${a}..${b}] ${expr}`;
        } else if (op === 'prod') {
          const expr = overlay.querySelector('#sc-sigmaf').value;
          const a = parseInt(overlay.querySelector('#sc-sigma-a').value, 10);
          const b = parseInt(overlay.querySelector('#sc-sigma-b').value, 10);
          v = productOf(expr, 'k', a, b); label = `Π[k=${a}..${b}] ${expr}`;
        } else if (op === 'taylor') {
          const a = parseFloat(overlay.querySelector('#sc-tay-a').value);
          const N = parseInt(overlay.querySelector('#sc-tay-n').value, 10);
          v = taylor(fxExpr, a, N); label = `Taylor[${fxExpr}, a=${a}, N=${N}]`;
        } else if (op === 'partx' || op === 'party') {
          const expr = overlay.querySelector('#sc-gxy').value;
          const [x, y] = parseData(overlay.querySelector('#sc-gxy-pt').value);
          const idx = op === 'partx' ? 0 : 1;
          v = partial(expr, idx, [x, y]);
          label = `${op === 'partx' ? '∂/∂x' : '∂/∂y'} [${expr}] at (${x}, ${y})`;
        }
        setExpr(label);
        showResult(v, false);
        pushHistory(label, typeof v === 'string' ? v : formatResult(v));
      } catch (e) {
        showResult('Error: ' + (e.message || e), true);
      }
    });
  });

  // ─── "More" tab — sub-tab switcher
  overlay.querySelectorAll('.sc-subtab').forEach(btn => {
    btn.addEventListener('click', () => {
      const sub = btn.dataset.sub;
      overlay.querySelectorAll('.sc-subtab').forEach(b => b.classList.toggle('active', b === btn));
      overlay.querySelectorAll('.sc-subpane').forEach(p => p.classList.toggle('active', p.dataset.subpane === sub));
    });
  });

  // ─── "More" tab — unit converter dropdown population
  const convCat = overlay.querySelector('#sc-conv-cat');
  const convFrom = overlay.querySelector('#sc-conv-from');
  const convTo = overlay.querySelector('#sc-conv-to');
  function refreshConvUnits() {
    const cat = convCat.value;
    const units = unitsFor(cat);
    convFrom.innerHTML = units.map(u => `<option value="${u}">${u}</option>`).join('');
    convTo.innerHTML = units.map(u => `<option value="${u}">${u}</option>`).join('');
    if (units.length > 1) convTo.selectedIndex = 1;
  }
  convCat.addEventListener('change', refreshConvUnits);
  refreshConvUnits();

  // ─── "More" tab — tool handlers
  overlay.querySelectorAll('[data-more]').forEach(btn => {
    btn.addEventListener('click', () => {
      const op = btn.dataset.more;
      try {
        let v, label;
        if (op === 'solve') {
          const expr = overlay.querySelector('#sc-solve-fx').value;
          const x0 = parseFloat(overlay.querySelector('#sc-solve-x0').value);
          v = solveNewton(expr, x0); label = `root of ${expr} = 0`;
        } else if (op === 'quadratic') {
          const [a, b, c] = parseData(overlay.querySelector('#sc-quad').value);
          v = quadratic(a, b, c); label = `${a}x² + ${b}x + ${c} = 0`;
        } else if (op === 'linsys2') {
          const r1 = parseData(overlay.querySelector('#sc-lin-r1').value);
          const r2 = parseData(overlay.querySelector('#sc-lin-r2').value);
          v = linsys2(r1, r2); label = '2×2 linear system';
        } else if (op === 'plot') {
          const expr = overlay.querySelector('#sc-plot-fx').value;
          const xmin = parseFloat(overlay.querySelector('#sc-plot-xmin').value);
          const xmax = parseFloat(overlay.querySelector('#sc-plot-xmax').value);
          drawPlot(overlay.querySelector('#sc-canvas'), expr, xmin, xmax);
          v = `plot of ${expr} on [${xmin}, ${xmax}]`; label = `plot ${expr}`;
        } else if (op === 'convert') {
          const cat = convCat.value;
          const val = parseFloat(overlay.querySelector('#sc-conv-val').value);
          v = convertUnits(cat, val, convFrom.value, convTo.value);
          label = `${val} ${convFrom.value} → ${convTo.value}`;
          v = `${formatResult(v)} ${convTo.value}`;
        } else if (op === 'base') {
          const val = overlay.querySelector('#sc-base-val').value.trim();
          const from = parseInt(overlay.querySelector('#sc-base-from').value, 10);
          const to = parseInt(overlay.querySelector('#sc-base-to').value, 10);
          const n = parseInt(val, from);
          if (Number.isNaN(n)) throw new Error('invalid number for base ' + from);
          v = toBase(n, to); label = `${val}₍${from}₎ → base ${to}`;
        } else if (op === 'baseall') {
          const val = overlay.querySelector('#sc-base-val').value.trim();
          const from = parseInt(overlay.querySelector('#sc-base-from').value, 10);
          const n = parseInt(val, from);
          if (Number.isNaN(n)) throw new Error('invalid number for base ' + from);
          v = `bin: ${toBase(n,2)} · oct: ${toBase(n,8)} · dec: ${toBase(n,10)} · hex: ${toBase(n,16)}`;
          label = `${val}₍${from}₎ in all 4 bases`;
        } else if (op === 'gcd') {
          const nums = parseData(overlay.querySelector('#sc-nt-nums').value);
          v = gcdN(nums); label = `gcd(${nums.join(', ')})`;
        } else if (op === 'lcm') {
          const nums = parseData(overlay.querySelector('#sc-nt-nums').value);
          v = lcmN(nums); label = `lcm(${nums.join(', ')})`;
        } else if (op === 'factorize') {
          const n = parseInt(overlay.querySelector('#sc-nt-n').value, 10);
          const f = factorize(n); v = f || `${n} (prime)`; label = `factorize ${n}`;
        } else if (op === 'isprime') {
          const n = parseInt(overlay.querySelector('#sc-nt-n').value, 10);
          v = isPrime(n) ? `${n} is PRIME` : `${n} is composite`;
          label = `isPrime(${n})`;
        } else if (op === 'fib') {
          const n = parseInt(overlay.querySelector('#sc-nt-fib').value, 10);
          v = fibonacci(n); label = `Fibonacci(${n})`;
        } else if (op === 'nthprime') {
          const n = parseInt(overlay.querySelector('#sc-nt-fib').value, 10);
          v = nthPrime(n); label = `${n}ᵗʰ prime`;
        } else if (op === 'm22det') {
          const r1 = parseData(overlay.querySelector('#sc-m22-r1').value);
          const r2 = parseData(overlay.querySelector('#sc-m22-r2').value);
          v = det2([r1, r2]); label = 'det of 2×2';
        } else if (op === 'm22inv') {
          const r1 = parseData(overlay.querySelector('#sc-m22-r1').value);
          const r2 = parseData(overlay.querySelector('#sc-m22-r2').value);
          const inv = inv2([r1, r2]);
          v = inv ? `[[${formatResult(inv[0][0])}, ${formatResult(inv[0][1])}], [${formatResult(inv[1][0])}, ${formatResult(inv[1][1])}]]` : 'matrix is singular';
          label = 'inverse of 2×2';
        } else if (op === 'm33det') {
          const r1 = parseData(overlay.querySelector('#sc-m33-r1').value);
          const r2 = parseData(overlay.querySelector('#sc-m33-r2').value);
          const r3 = parseData(overlay.querySelector('#sc-m33-r3').value);
          v = det3([r1, r2, r3]); label = 'det of 3×3';
        }

        // Geometry
        else if (op === 'heron') {
          const [a, b, c] = parseData(overlay.querySelector('#sc-geo-tri').value);
          v = heron(a, b, c); label = `triangle (${a}, ${b}, ${c})`;
        } else if (op === 'circle') {
          const r = parseFloat(overlay.querySelector('#sc-geo-cir').value);
          v = geoCircle(r); label = `circle r=${r}`;
        } else if (op === 'sphere') {
          const r = parseFloat(overlay.querySelector('#sc-geo-sph').value);
          v = geoSphere(r); label = `sphere r=${r}`;
        } else if (op === 'cone') {
          const [r, h] = parseData(overlay.querySelector('#sc-geo-cone').value);
          v = geoCone(r, h); label = `cone r=${r}, h=${h}`;
        } else if (op === 'cyl') {
          const [r, h] = parseData(overlay.querySelector('#sc-geo-cyl').value);
          v = geoCylinder(r, h); label = `cylinder r=${r}, h=${h}`;
        } else if (op === 'rect') {
          const [l, w] = parseData(overlay.querySelector('#sc-geo-rect').value);
          v = geoRect(l, w); label = `rectangle ${l}×${w}`;
        } else if (op === 'trap') {
          const [a, b, h] = parseData(overlay.querySelector('#sc-geo-trap').value);
          v = geoTrap(a, b, h); label = `trapezoid a=${a}, b=${b}, h=${h}`;
        }

        // Complex numbers
        else if (op.startsWith('cx-')) {
          const [a, b] = parseData(overlay.querySelector('#sc-cx-z1').value);
          const [c, d] = parseData(overlay.querySelector('#sc-cx-z2').value);
          if (op === 'cx-add') { v = cxAdd(a, b, c, d); label = '(z₁ + z₂)'; }
          else if (op === 'cx-sub') { v = cxSub(a, b, c, d); label = '(z₁ − z₂)'; }
          else if (op === 'cx-mul') { v = cxMul(a, b, c, d); label = '(z₁ × z₂)'; }
          else if (op === 'cx-div') { v = cxDiv(a, b, c, d); label = '(z₁ ÷ z₂)'; }
          else if (op === 'cx-mag') { v = cxMag(a, b); label = `|z₁| where z₁ = ${a}+${b}i`; }
          else if (op === 'cx-arg') { v = `${formatResult(cxArg(a, b) * 180 / Math.PI)}° (${formatResult(cxArg(a, b))} rad)`; label = `arg(z₁)`; }
          else if (op === 'cx-exp') { v = cxExp(a, b); label = `e^z₁ where z₁ = ${a}+${b}i`; }
        }

        // 3D Vectors
        else if (op.startsWith('vec-')) {
          const A = parseData(overlay.querySelector('#sc-vec-a').value);
          const B = parseData(overlay.querySelector('#sc-vec-b').value);
          while (A.length < 3) A.push(0);
          while (B.length < 3) B.push(0);
          if (op === 'vec-dot') { v = vDot(A, B); label = `A · B`; }
          else if (op === 'vec-cross') {
            const cr = vCross(A, B);
            v = `(${formatResult(cr[0])}, ${formatResult(cr[1])}, ${formatResult(cr[2])})`;
            label = `A × B`;
          }
          else if (op === 'vec-mag') { v = vMag(A); label = `|A|`; }
          else if (op === 'vec-angle') { v = vAngle(A, B); label = `angle(A, B)`; }
          else if (op === 'vec-proj') {
            const p = vProj(A, B);
            v = `(${formatResult(p[0])}, ${formatResult(p[1])}, ${formatResult(p[2])})`;
            label = `proj_B(A)`;
          }
        }

        // Sequences
        else if (op === 'arith-nth' || op === 'arith-sum') {
          const [a1, d, n] = parseData(overlay.querySelector('#sc-seq-ari').value);
          v = op === 'arith-nth' ? arithNth(a1, d, n) : arithSum(a1, d, n);
          label = op === 'arith-nth' ? `a_${n} (arithmetic)` : `S_${n} (arithmetic)`;
        } else if (op === 'geo-nth' || op === 'geo-sum' || op === 'geo-inf') {
          const [a1, r, n] = parseData(overlay.querySelector('#sc-seq-geo').value);
          if (op === 'geo-nth') { v = geoNth(a1, r, n); label = `a_${n} (geometric)`; }
          else if (op === 'geo-sum') { v = geoSum(a1, r, n); label = `S_${n} (geometric)`; }
          else { v = geoInfSum(a1, r); label = `S_∞ (geometric)`; }
        }

        // Roman
        else if (op === 'to-roman') {
          const n = parseInt(overlay.querySelector('#sc-rom-n').value, 10);
          v = toRoman(n); label = `${n} → Roman`;
        } else if (op === 'from-roman') {
          const s = overlay.querySelector('#sc-rom-s').value;
          v = fromRoman(s); label = `${s} → Number`;
        }

        // Date
        else if (op === 'date-diff') {
          const d1 = overlay.querySelector('#sc-date-1').value;
          const d2 = overlay.querySelector('#sc-date-2').value;
          v = `${daysBetween(d1, d2)} days`; label = `${d1} → ${d2}`;
        } else if (op === 'date-add') {
          const d = overlay.querySelector('#sc-date-base').value;
          const n = overlay.querySelector('#sc-date-n').value;
          v = addDays(d, n); label = `${d} + ${n} days`;
        } else if (op === 'dow') {
          const d = overlay.querySelector('#sc-date-dow').value;
          v = dayOfWeek(d); label = `${d} is a`;
        }

        // Circuit / electronics
        else if (op === 'ohm') {
          const Vr = overlay.querySelector('#sc-ohm-v').value;
          const Ir = overlay.querySelector('#sc-ohm-i').value;
          const Rr = overlay.querySelector('#sc-ohm-r').value;
          const r = ohmSolve(Vr, Ir, Rr);
          v = `V = ${siNumber(r.V,'V')},  I = ${siNumber(r.I,'A')},  R = ${siNumber(r.R,'Ω')},  P = ${siNumber(r.P,'W')}`;
          label = `Ohm's Law solve`;
        } else if (op === 'vdiv') {
          const Vin = parseFloat(overlay.querySelector('#sc-vd-vin').value);
          const R1 = parseFloat(overlay.querySelector('#sc-vd-r1').value);
          const R2 = parseFloat(overlay.querySelector('#sc-vd-r2').value);
          v = siNumber(voltageDivider(Vin, R1, R2), 'V');
          label = `V_out from ${Vin}V across R₁=${R1}Ω, R₂=${R2}Ω`;
        } else if (op === 'rser' || op === 'rpar') {
          const rs = parseData(overlay.querySelector('#sc-rlist').value);
          const total = op === 'rser' ? resistorsSeries(rs) : resistorsParallel(rs);
          v = siNumber(total, 'Ω');
          label = `${op === 'rser' ? 'Series' : 'Parallel'} of ${rs.length} resistors`;
        } else if (op === 'cser' || op === 'cpar') {
          const cs = parseData(overlay.querySelector('#sc-clist').value).map(x => x * 1e-6); // μF → F
          const total = op === 'cser' ? capacitorsSeries(cs) : capacitorsParallel(cs);
          v = siNumber(total, 'F');
          label = `${op === 'cser' ? 'Series' : 'Parallel'} of ${cs.length} caps`;
        } else if (op === 'rc') {
          const [R, C] = parseData(overlay.querySelector('#sc-rc').value);
          v = siNumber(R * C, 's');
          label = `τ = RC (${R}Ω × ${C}F)`;
        } else if (op === 'rl') {
          const [R, L] = parseData(overlay.querySelector('#sc-rl').value);
          v = siNumber(L / R, 's');
          label = `τ = L/R (${L}H / ${R}Ω)`;
        } else if (op === 'lcres') {
          const [L, C] = parseData(overlay.querySelector('#sc-lc').value);
          v = siNumber(lcResonance(L, C), 'Hz');
          label = `LC resonant frequency`;
        } else if (op === 'xl') {
          const f = parseFloat(overlay.querySelector('#sc-freq').value);
          const L = parseFloat(overlay.querySelector('#sc-xl').value);
          v = siNumber(reactanceL(f, L), 'Ω');
          label = `X_L = 2πfL  (f=${f}Hz, L=${L}H)`;
        } else if (op === 'xc') {
          const f = parseFloat(overlay.querySelector('#sc-freq2').value);
          const C = parseFloat(overlay.querySelector('#sc-xc').value);
          v = siNumber(reactanceC(f, C), 'Ω');
          label = `X_C = 1/(2πfC)  (f=${f}Hz, C=${C}F)`;
        } else if (op === 'rcc') {
          const bands = overlay.querySelector('#sc-rcc').value;
          v = decodeResistor(bands);
          label = `Resistor: ${bands}`;
        }
        setExpr(label);
        showResult(v, false);
        pushHistory(label, typeof v === 'string' ? v : formatResult(v));
      } catch (e) {
        showResult('Error: ' + (e.message || e), true);
      }
    });
  });

  // Click history item → restore as expression
  histList.addEventListener('click', (e) => {
    const it = e.target.closest('.sc-history-item');
    if (it) {
      setExpr(it.dataset.expr);
      showResult(0, false);
      // Switch to basic tab so user sees the keypad
      overlay.querySelector('.sc-tab[data-tab="basic"]').click();
    }
  });
  document.getElementById('sc-clear-hist').addEventListener('click', () => {
    writeHist([]); renderHistory();
  });

  // Keyboard support inside modal: when overlay open, allow typing into expression
  // and Enter to evaluate.
  document.addEventListener('keydown', (e) => {
    if (!overlay.classList.contains('open')) return;
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return; // typing in input fields
    if (activeTab !== 'basic' && activeTab !== 'trig') return;
    if (e.key === 'Enter' || e.key === '=') { e.preventDefault(); runEval(); return; }
    if (e.key === 'Backspace') { e.preventDefault(); setExpr(exprStr.slice(0, -1)); return; }
    if (e.key === 'Escape') return; // close handler above
    if (/^[0-9.+\-*/^()!]$/.test(e.key)) { e.preventDefault(); setExpr(exprStr + e.key); }
  });
}
