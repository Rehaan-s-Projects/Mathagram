/* ============================================================
   Mathagram.org — Characters Module
   Character data, buddy popup logic, and picker helpers
   ============================================================ */

export const CHARACTERS = {
  edam: {
    name: 'Edam',
    type: 'Bear',
    file: 'edam.svg',
    messages: {
      correct: 'You got this! Great job!',
      wrong: 'No worries, try again!',
      hint: 'Think about it...',
      perfect: 'Absolutely perfect!'
    }
  },
  steve: {
    name: 'Steve',
    type: 'Fox',
    file: 'steve.svg',
    messages: {
      correct: "Sly move, that's correct!",
      wrong: 'Tricky one! Give it another shot.',
      hint: 'Hmm, what if you tried...',
      perfect: 'Brilliant! Outsmarted it!'
    }
  },
  james: {
    name: 'James',
    type: 'Strong Man',
    file: 'james.svg',
    messages: {
      correct: "Crush it! Let's go!",
      wrong: 'Shake it off, try again!',
      hint: 'Power through this one...',
      perfect: 'BEAST MODE! Flawless!'
    }
  },
  diego: {
    name: 'Diego',
    type: 'Researcher',
    file: 'diego.svg',
    messages: {
      correct: 'Fascinating! Correct!',
      wrong: 'Interesting... not quite. Retry?',
      hint: 'Consider the data...',
      perfect: 'Remarkable precision!'
    }
  },
  rita: {
    name: 'Rita',
    type: 'Cat',
    file: 'rita.svg',
    messages: {
      correct: 'Purrfect answer.',
      wrong: 'Nah, try again.',
      hint: 'Hmm, curious...',
      perfect: 'Purrfectly flawless!'
    }
  },
  sam: {
    name: 'Sam',
    type: 'Kid',
    file: 'sam.svg',
    messages: {
      correct: 'Woohoo! You nailed it!',
      wrong: 'Oops! One more try!',
      hint: 'Ooh, what about...',
      perfect: 'YESSS! Perfect score!'
    }
  },
  william: {
    name: 'William',
    type: 'Old Man',
    file: 'william.svg',
    messages: {
      correct: 'Well done, young scholar.',
      wrong: 'Patience. Try once more.',
      hint: 'In my experience...',
      perfect: 'Exemplary work, truly.'
    }
  },
  gosia: {
    name: 'Gosia',
    type: 'Girl',
    file: 'gosia.svg',
    messages: {
      correct: 'Amazing work!',
      wrong: "Almost! You've got this!",
      hint: "Here's a thought...",
      perfect: 'Absolutely stunning!'
    }
  }
};

/* Map reactions to expression classes */
const REACTION_MAP = {
  correct: 'happy',
  wrong: 'encouraging',
  hint: 'thinking',
  perfect: 'happy'
};

/**
 * Voice settings per character — gives each a unique voice personality.
 * pitch: 0.1 (deep) to 2.0 (high), rate: 0.5 (slow) to 2.0 (fast)
 */
const VOICE_SETTINGS = {
  edam:    { pitch: 0.8,  rate: 0.9,  volume: 0.8 },  // Bear: warm, low, steady
  steve:   { pitch: 1.2,  rate: 1.15, volume: 0.8 },  // Fox: quick, sly
  james:   { pitch: 0.6,  rate: 0.85, volume: 0.9 },  // Strong man: deep, powerful
  diego:   { pitch: 1.0,  rate: 1.0,  volume: 0.7 },  // Researcher: calm, measured
  rita:    { pitch: 1.8,  rate: 1.2,  volume: 0.85 }, // Cat: HIGH pitch, playful
  sam:     { pitch: 1.6,  rate: 1.3,  volume: 0.85 }, // Kid: high, energetic, fast
  william: { pitch: 0.5,  rate: 0.75, volume: 0.8 },  // Old man: deep, slow, wise
  gosia:   { pitch: 1.4,  rate: 1.05, volume: 0.8 }   // Girl: bright, friendly
};

/**
 * Speak a message using Web Speech API with character-specific voice.
 * @param {string} text - message to speak
 * @param {string} characterId - character key for voice settings
 */
function speak(text, characterId) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  const settings = VOICE_SETTINGS[characterId] || { pitch: 1.0, rate: 1.0, volume: 0.8 };

  utterance.pitch = settings.pitch;
  utterance.rate = settings.rate;
  utterance.volume = settings.volume;

  // Try to pick a fitting system voice
  const voices = window.speechSynthesis.getVoices();
  if (voices.length > 0) {
    // Prefer female voice for Rita, Gosia, Sam; male for James, William, Edam
    const preferFemale = ['rita', 'gosia', 'sam'].includes(characterId);
    const preferMale = ['william', 'james', 'edam', 'steve', 'diego'].includes(characterId);
    const filtered = voices.filter(v => v.lang.startsWith('en'));
    if (filtered.length > 0) {
      let match = null;
      if (preferMale) {
        // Try male voices first
        match = filtered.find(v => /\bmale\b|daniel|alex|tom|fred|ralph|aaron|arthur|gordon|lee|rishi|oliver/i.test(v.name) && !/female/i.test(v.name));
      } else if (preferFemale) {
        match = filtered.find(v => /female|samantha|karen|fiona|victoria|tessa|moira|susan|kate|zoe/i.test(v.name));
      }
      utterance.voice = match || filtered[0];
    }
  }

  window.speechSynthesis.speak(utterance);
}

let hideTimer = null;

/**
 * Initialize the side character panel for quiz pages.
 * Creates a character that stands alongside the exercise area (Duolingo-style).
 * Call this once when the quiz page loads.
 * @param {string} characterId — key in CHARACTERS (e.g. 'edam')
 * @param {string} basePath — path to assets (e.g. '../../')
 */
export function initSideCharacter(characterId, basePath = '') {
  const character = CHARACTERS[characterId];
  if (!character) return;

  let panel = document.getElementById('side-character');
  if (panel) panel.remove();

  panel = document.createElement('div');
  panel.id = 'side-character';
  panel.className = 'side-character';
  panel.innerHTML = `
    <img class="side-char-img" src="${basePath}assets/characters/${character.file}" alt="${character.name}">
    <div class="side-char-name">${character.name}</div>
    <div class="side-char-speech" id="side-char-speech"></div>
  `;
  document.body.appendChild(panel);
}

/**
 * Show the character buddy — updates side panel + speaks message.
 * @param {string} characterId — key in CHARACTERS (e.g. 'edam')
 * @param {string} reaction — one of 'correct', 'wrong', 'hint', 'perfect'
 */
export function showBuddy(characterId, reaction) {
  const character = CHARACTERS[characterId];
  if (!character) return;

  const message = character.messages[reaction] || character.messages.correct;
  const expression = REACTION_MAP[reaction] || 'happy';

  /* Update side character panel if it exists */
  const sidePanel = document.getElementById('side-character');
  if (sidePanel) {
    const img = sidePanel.querySelector('.side-char-img');
    const name = sidePanel.querySelector('.side-char-name');
    const speech = sidePanel.querySelector('.side-char-speech');

    // Determine base path from current img src
    const currentSrc = img.src;
    const basePath = currentSrc.substring(0, currentSrc.lastIndexOf('assets/'));

    img.src = `${basePath}assets/characters/${character.file}`;
    img.alt = character.name;
    name.textContent = character.name;
    speech.textContent = message;

    // Set expression styling
    sidePanel.classList.remove('happy', 'encouraging', 'thinking');
    sidePanel.classList.add(expression);
    sidePanel.classList.add('reacting');
    setTimeout(() => sidePanel.classList.remove('reacting'), 600);
  }

  /* Also show the bottom popup for mobile */
  let popup = document.getElementById('character-buddy');
  if (!popup) {
    popup = document.createElement('div');
    popup.id = 'character-buddy';
    popup.className = 'character-buddy';
    popup.innerHTML = `
      <img class="buddy-img" src="" alt="" />
      <p class="buddy-msg"></p>
    `;
    document.body.appendChild(popup);
  }

  const popupImg = popup.querySelector('.buddy-img');
  const popupMsg = popup.querySelector('.buddy-msg');
  popupImg.src = `assets/characters/${character.file}`;
  popupImg.alt = `${character.name} the ${character.type}`;
  popupMsg.textContent = message;

  /* Speak the message out loud with character-specific voice */
  speak(message, characterId);

  popup.classList.remove('happy', 'encouraging', 'thinking');
  popup.classList.add(expression);
  requestAnimationFrame(() => popup.classList.add('show'));

  if (hideTimer) clearTimeout(hideTimer);
  hideTimer = setTimeout(() => popup.classList.remove('show'), 3000);
}

/**
 * Get all characters as an array for the picker UI.
 * @returns {Array<{id: string, name: string, type: string, file: string, messages: object}>}
 */
export function getAllCharacters() {
  return Object.entries(CHARACTERS).map(([id, data]) => ({
    id,
    name: data.name,
    type: data.type,
    file: data.file,
    messages: data.messages
  }));
}

/**
 * Pick a random character ID from the 8 available characters.
 * @returns {string} character ID (e.g., 'edam', 'steve', 'rita')
 */
export function randomCharacterId() {
  const ids = Object.keys(CHARACTERS);
  return ids[Math.floor(Math.random() * ids.length)];
}
