// Mathagram — Soroban widget
// Builds an interactive 5-rod Japanese soroban inside any container element.
// Returns an API for programmatic control + click-to-slide bead physics.
//
//   const soroban = createSoroban(document.getElementById('rods'), {
//     onChange: (value) => { ... },
//     interactive: true
//   });
//   soroban.set(123);          // programmatically display 123
//   soroban.value();           // → current number on the abacus
//   soroban.clear();           // reset to 0

export function createSoroban(rodsEl, opts = {}) {
  const { onChange = () => {}, interactive = true, numRods = 5 } = opts;
  const ROD_LABELS = ['10,000s', '1,000s', '100s', '10s', '1s'];
  const rods = [];

  rodsEl.innerHTML = '';

  for (let r = 0; r < numRods; r++) {
    const rodEl = document.createElement('div');
    rodEl.className = 'rod';

    const stem = document.createElement('div');
    stem.className = 'rod-stem';
    rodEl.appendChild(stem);

    const heaven = document.createElement('div');
    heaven.className = 'heaven';
    const heavenBead = document.createElement('div');
    heavenBead.className = 'bead';
    heavenBead.dataset.rod = r;
    heavenBead.dataset.role = 'heaven';
    heaven.appendChild(heavenBead);
    rodEl.appendChild(heaven);

    const bar = document.createElement('div');
    bar.className = 'bar';
    rodEl.appendChild(bar);

    const earth = document.createElement('div');
    earth.className = 'earth';
    const earthBeads = [];
    for (let i = 0; i < 4; i++) {
      const eb = document.createElement('div');
      eb.className = 'bead';
      eb.dataset.rod = r;
      eb.dataset.role = 'earth';
      eb.dataset.idx = i;
      earth.appendChild(eb);
      earthBeads.push(eb);
    }
    rodEl.appendChild(earth);

    const label = document.createElement('div');
    label.className = 'rod-label';
    label.textContent = ROD_LABELS[ROD_LABELS.length - numRods + r] || '';
    rodEl.appendChild(label);

    rodsEl.appendChild(rodEl);
    rods.push({ heavenBead, earthBeads, heavenActive: false, earthCount: 0 });
  }

  function setRod(r, heavenActive, earthCount) {
    const { heavenBead, earthBeads } = rods[r];
    rods[r].heavenActive = !!heavenActive;
    rods[r].earthCount   = Math.max(0, Math.min(4, earthCount));
    heavenBead.classList.toggle('active', rods[r].heavenActive);
    earthBeads.forEach((b, i) => {
      const shouldActivate = i < rods[r].earthCount;
      b.classList.toggle('active', shouldActivate);
      if (shouldActivate) {
        const rest = (3 - i) * 30;
        b.style.transform = `translateY(-${rest}px)`;
      } else {
        b.style.transform = '';
      }
    });
    onChange(value());
  }

  function value() {
    let total = 0;
    rods.forEach((rod, r) => {
      const placeValue = Math.pow(10, numRods - 1 - r);
      const digit = (rod.heavenActive ? 5 : 0) + rod.earthCount;
      total += digit * placeValue;
    });
    return total;
  }

  function set(num) {
    num = Math.max(0, Math.floor(num || 0));
    const padded = num.toString().padStart(numRods, '0').slice(-numRods);
    for (let r = 0; r < numRods; r++) {
      const d = parseInt(padded[r], 10) || 0;
      const heaven = d >= 5 ? 1 : 0;
      const earth  = d - heaven * 5;
      setRod(r, heaven, earth);
    }
  }

  function clear() { set(0); }

  if (interactive) {
    rods.forEach((rod, r) => {
      rod.heavenBead.addEventListener('click', () => {
        setRod(r, !rod.heavenActive, rod.earthCount);
      });
      rod.earthBeads.forEach((b, i) => {
        b.addEventListener('click', () => {
          const desired = 4 - i;
          const next = (rod.earthCount === desired) ? desired - 1 : desired;
          setRod(r, rod.heavenActive, next);
        });
      });
    });
  }

  return { set, value, clear, setRod };
}
