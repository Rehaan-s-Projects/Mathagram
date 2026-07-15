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
    },
    messagesCa: {
      correct: 'Molt bé! Bona feina!',
      wrong: 'No passa res, torna-ho a provar!',
      hint: 'Pensa-hi bé...',
      perfect: 'Absolutament perfecte!'
    },
    messagesEs: {
      correct: '¡Lo tienes! ¡Gran trabajo!',
      wrong: '¡No te preocupes, inténtalo de nuevo!',
      hint: 'Piénsalo bien...',
      perfect: '¡Absolutamente perfecto!'
    },
    messagesPt: {
      correct: 'Você conseguiu! Ótimo trabalho!',
      wrong: 'Sem problemas, tente novamente!',
      hint: 'Pense bem nisso...',
      perfect: 'Absolutamente perfeito!'
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
    },
    messagesCa: {
      correct: 'Jugada astuta, correcte!',
      wrong: 'Complicat! Prova-ho una altra vegada.',
      hint: 'Hmm, i si probessis...',
      perfect: 'Brillant! L\'has superat!'
    },
    messagesEs: {
      correct: '¡Jugada astuta, correcto!',
      wrong: '¡Complicado! Dale otra oportunidad.',
      hint: 'Hmm, ¿y si probaras...',
      perfect: '¡Brillante! ¡Lo superaste!'
    },
    messagesPt: {
      correct: 'Jogada astuta, correto!',
      wrong: 'Complicado! Tente de novo.',
      hint: 'Hmm, e se você tentasse...',
      perfect: 'Brilhante! Você superou!'
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
    },
    messagesCa: {
      correct: 'Endavant! Correcte!',
      wrong: 'Amunt! Torna-ho a intentar!',
      hint: 'Força! Tu pots...',
      perfect: 'MODE BÈSTIA! Impecable!'
    },
    messagesEs: {
      correct: '¡Aplástalo! ¡Vamos!',
      wrong: '¡Sacúdetelo, inténtalo otra vez!',
      hint: 'Atraviésalo con fuerza...',
      perfect: '¡MODO BESTIA! ¡Impecable!'
    },
    messagesPt: {
      correct: 'Arrase! Vamos lá!',
      wrong: 'Deixa pra lá, tente de novo!',
      hint: 'Force a passagem nesse...',
      perfect: 'MODO FERA! Impecável!'
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
    },
    messagesCa: {
      correct: 'Fascinant! Correcte!',
      wrong: 'Interessant... no del tot. Reintenta?',
      hint: 'Considera les dades...',
      perfect: 'Precisió extraordinària!'
    },
    messagesEs: {
      correct: '¡Fascinante! ¡Correcto!',
      wrong: 'Interesante... no del todo. ¿Reintentar?',
      hint: 'Considera los datos...',
      perfect: '¡Precisión extraordinaria!'
    },
    messagesPt: {
      correct: 'Fascinante! Correto!',
      wrong: 'Interessante... nem tanto. Tentar de novo?',
      hint: 'Considere os dados...',
      perfect: 'Precisão extraordinária!'
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
    },
    messagesCa: {
      correct: 'Ronc! Resposta purr-fecta!',
      wrong: 'Miau... torna-ho a provar.',
      hint: 'Hmm, curiós...',
      perfect: 'Purr-fectament impecable!'
    },
    messagesEs: {
      correct: 'Respuesta purr-fecta.',
      wrong: 'Nah, inténtalo otra vez.',
      hint: 'Hmm, curioso...',
      perfect: '¡Purr-fectamente impecable!'
    },
    messagesPt: {
      correct: 'Resposta purr-feita.',
      wrong: 'Nada, tente de novo.',
      hint: 'Hmm, curioso...',
      perfect: 'Purr-feitamente impecável!'
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
    },
    messagesCa: {
      correct: 'Uau! L\'has encertat!',
      wrong: 'Ui! Un intent més!',
      hint: 'Oh, i si...',
      perfect: 'SÍIII! Puntuació perfecta!'
    },
    messagesEs: {
      correct: '¡Yujuu! ¡Lo lograste!',
      wrong: '¡Uy! ¡Un intento más!',
      hint: 'Oh, ¿qué tal si...',
      perfect: '¡SÍÍÍ! ¡Puntuación perfecta!'
    },
    messagesPt: {
      correct: 'Uhuu! Você acertou!',
      wrong: 'Opa! Mais uma tentativa!',
      hint: 'Oh, e se...',
      perfect: 'SIIIM! Pontuação perfeita!'
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
    },
    messagesCa: {
      correct: 'Ben fet, jove estudiant.',
      wrong: 'Paciència. Prova una vegada més.',
      hint: 'Segons la meva experiència...',
      perfect: 'Treball exemplar, de veritat.'
    },
    messagesEs: {
      correct: 'Bien hecho, joven estudiante.',
      wrong: 'Paciencia. Inténtalo una vez más.',
      hint: 'En mi experiencia...',
      perfect: 'Trabajo ejemplar, de verdad.'
    },
    messagesPt: {
      correct: 'Muito bem, jovem estudante.',
      wrong: 'Paciência. Tente mais uma vez.',
      hint: 'Na minha experiência...',
      perfect: 'Trabalho exemplar, de verdade.'
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
    },
    messagesCa: {
      correct: 'Treball increïble!',
      wrong: 'Gairebé! Tu pots!',
      hint: 'Una idea...',
      perfect: 'Absolutament impressionant!'
    },
    messagesEs: {
      correct: '¡Trabajo increíble!',
      wrong: '¡Casi! ¡Tú puedes!',
      hint: 'Una idea...',
      perfect: '¡Absolutamente impresionante!'
    },
    messagesPt: {
      correct: 'Trabalho incrível!',
      wrong: 'Quase! Você consegue!',
      hint: 'Uma ideia...',
      perfect: 'Absolutamente impressionante!'
    }
  },
  lingo: {
    name: 'Lingo',
    type: 'Parrot',
    file: 'lingo.svg',
    messages: {
      correct: 'Squawk! Right in any language!',
      wrong: 'Try again — say it your way!',
      hint: "Translate it in your head...",
      perfect: 'Polyglot perfection!'
    },
    messagesCa: {
      correct: 'Squawk! Correcte en qualsevol llengua!',
      wrong: 'Torna-ho a provar — digues-ho a la teva manera!',
      hint: 'Tradueix-ho al teu cap...',
      perfect: 'Perfecció poliglota!'
    },
    messagesEs: {
      correct: '¡Squawk! ¡Correcto en cualquier idioma!',
      wrong: 'Inténtalo de nuevo — ¡dilo a tu manera!',
      hint: 'Tradúcelo en tu cabeza...',
      perfect: '¡Perfección políglota!'
    },
    messagesPt: {
      correct: 'Squawk! Certo em qualquer idioma!',
      wrong: 'Tente de novo — diga do seu jeito!',
      hint: 'Traduza isso na sua cabeça...',
      perfect: 'Perfeição poliglota!'
    }
  },
  babel: {
    name: 'Babel',
    type: 'Owl',
    file: 'babel.svg',
    messages: {
      correct: 'Hoo! Wisely answered.',
      wrong: 'Hoo... patience. Try once more.',
      hint: 'In every tongue, the answer is near...',
      perfect: 'A scholar of the world!'
    },
    messagesCa: {
      correct: 'Hoo! Resposta sàvia.',
      wrong: 'Hoo... paciència. Torna-ho a provar.',
      hint: 'En totes les llengües, la resposta és a prop...',
      perfect: 'Un erudit del món!'
    },
    messagesEs: {
      correct: '¡Hoo! Sabia respuesta.',
      wrong: 'Hoo... paciencia. Inténtalo una vez más.',
      hint: 'En cada lengua, la respuesta está cerca...',
      perfect: '¡Un erudito del mundo!'
    },
    messagesPt: {
      correct: 'Hoo! Resposta sábia.',
      wrong: 'Hoo... paciência. Tente mais uma vez.',
      hint: 'Em cada idioma, a resposta está perto...',
      perfect: 'Um erudito do mundo!'
    }
  }
};

// Frisian messages for all characters
const FRISIAN_MESSAGES = {
  edam: {
    correct: 'Hiel goed! Goed dien!',
    wrong: 'Gjin soargen, besykje it nochris!',
    hint: 'Tink der oer nei...',
    perfect: 'Absolút perfekt!'
  },
  steve: {
    correct: 'Tûk! Dat is goed!',
    wrong: 'Lestich! Besykje it nochris.',
    hint: 'Hmm, wat as do...',
    perfect: 'Briljant! Goed dien!'
  },
  james: {
    correct: 'Kom op! Goed!',
    wrong: 'Skodzje it ôf, besykje it nochris!',
    hint: 'Krêft troch...',
    perfect: 'BIST MODUS! Flekkenleas!'
  },
  diego: {
    correct: 'Bysûnder! Goed!',
    wrong: 'Ynteressant... net hielendal. Nochris?',
    hint: 'Beskôgje de gegevens...',
    perfect: 'Opfallende presyzje!'
  },
  rita: {
    correct: 'Miau! Purr-fekt antwurd!',
    wrong: 'Miau... besykje it nochris.',
    hint: 'Hmm, nijsgjirrich...',
    perfect: 'Purr-fekt flekkenleas!'
  },
  sam: {
    correct: 'Wauw! Do hast it!',
    wrong: 'Oeps! Noch ien kear!',
    hint: 'Oh, wat as...',
    perfect: 'JAAAA! Perfekte skoare!'
  },
  william: {
    correct: 'Goed dien, jonge studint.',
    wrong: 'Geduld. Besykje it nochris.',
    hint: 'Neffens myn ûnderfining...',
    perfect: 'Foarbyldich wurk, echt wier.'
  },
  gosia: {
    correct: 'Geweldich wurk!',
    wrong: 'Hast! Do kinst it!',
    hint: 'In idee...',
    perfect: 'Absolút prachtich!'
  },
  lingo: {
    correct: 'Squawk! Goed yn elke taal!',
    wrong: 'Besykje it nochris — sis it op dyn manier!',
    hint: 'Set it oer yn dyn holle...',
    perfect: 'Polyglot-perfeksje!'
  },
  babel: {
    correct: 'Hoo! Wiis antwurde.',
    wrong: 'Hoo... geduld. Besykje it nochris.',
    hint: 'Yn elke taal is it antwurd tichtby...',
    perfect: 'In gelearde fan de wrâld!'
  }
};

/** Current language for character messages (default: English) */
let _charLang = 'en';

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
// English voice mapping per character. `voice` is the macOS `say` voice we
// used to pre-record character intros (assets/audio/characters/intro-*.m4a)
// and is also the preferred voice name when Web Speech API is available.
const VOICE_SETTINGS = {
  edam:    { pitch: 0.8,  rate: 0.9,  volume: 1.0, voice: 'Daniel'   },  // Bear: warm, low, steady (en-GB)
  steve:   { pitch: 1.2,  rate: 1.15, volume: 1.0, voice: 'Fred'     },  // Fox: quick, sly (en-US)
  james:   { pitch: 0.6,  rate: 0.85, volume: 1.0, voice: 'Albert'   },  // Strong man: deep, powerful (en-US)
  diego:   { pitch: 1.0,  rate: 1.0,  volume: 1.0, voice: 'Ralph'    },  // Researcher: calm, measured (en-US)
  rita:    { pitch: 1.8,  rate: 1.2,  volume: 1.0, voice: 'Karen'    },  // Cat: HIGH pitch, playful (en-AU)
  sam:     { pitch: 1.6,  rate: 1.3,  volume: 1.0, voice: 'Samantha' },  // Kid: high, energetic, fast (en-US)
  william: { pitch: 0.5,  rate: 0.75, volume: 1.0, voice: 'Rishi'    },  // Old man: deep, slow, wise (en-IN)
  gosia:   { pitch: 1.4,  rate: 1.05, volume: 1.0, voice: 'Moira'    },  // Girl: bright, friendly (en-IE)
  lingo:   { pitch: 1.7,  rate: 1.25, volume: 1.0, voice: 'Karen'    },  // Parrot: bright, chatty
  babel:   { pitch: 0.9,  rate: 0.85, volume: 1.0, voice: 'Daniel'   }   // Owl: deep, deliberate
};

// Pre-recorded character intro clips — reliable audio that doesn't depend on
// the browser's speech engine being healthy. Plays via <audio> element.
const CHARACTER_INTRO_FILES = {
  edam:    'intro-edam.m4a',
  steve:   'intro-steve.m4a',
  james:   'intro-james.m4a',
  diego:   'intro-diego.m4a',
  rita:    'intro-rita.m4a',
  sam:     'intro-sam.m4a',
  william: 'intro-william.m4a',
  gosia:   'intro-gosia.m4a'
};

// Pre-recorded quiz reaction clips — one per character × reaction. Used by
// showBuddy() as a reliable fallback when Web Speech API is hung.
// Lives at /assets/audio/characters/reactions/<char>-<reaction>.m4a.
const REACTION_CHARS = new Set(['edam','steve','james','diego','rita','sam','william','gosia']);
const REACTION_KEYS  = new Set(['correct','wrong','hint','perfect']);

let _reactionPlayer = null;
function _playReactionAudio(characterId, reaction) {
  if (!REACTION_CHARS.has(characterId) || !REACTION_KEYS.has(reaction)) return;
  try {
    if (_reactionPlayer) { _reactionPlayer.pause(); _reactionPlayer.currentTime = 0; }
    // Absolute path — works from any page depth (the only assumption is
    // mathagram-style root-served deployment, which matches every page on the site).
    _reactionPlayer = new Audio(`/assets/audio/characters/reactions/${characterId}-${reaction}.m4a`);
    _reactionPlayer.volume = 1.0;
    const p = _reactionPlayer.play();
    if (p && p.catch) p.catch(() => {});
  } catch {}
}

// Hybrid: tries Web Speech first, falls back to recorded reaction audio if
// the speech engine doesn't actually start within 800ms (hung Chrome case).
function _speakReactionHybrid(characterId, reaction, message) {
  // Non-English: only the live speech path has translated lines.
  if (_charLang && _charLang !== 'en') { speak(message, characterId); return; }

  if (!('speechSynthesis' in window)) { _playReactionAudio(characterId, reaction); return; }
  _warmUpEngine();
  _voicesReady().then(() => {
    const u = new SpeechSynthesisUtterance(message);
    _applySettings(u, characterId, null);
    let started = false;
    let triggered = false;
    u.onstart = () => { started = true; };
    // If onstart never fires within 800ms, play the recording.
    setTimeout(() => {
      if (started || triggered) return;
      triggered = true;
      try { window.speechSynthesis.cancel(); } catch {}
      _playReactionAudio(characterId, reaction);
    }, 800);
    try { window.speechSynthesis.speak(u); } catch {
      triggered = true;
      _playReactionAudio(characterId, reaction);
    }
  });
}

let _charIntroPlayer = null;
/**
 * Play a character's pre-recorded English intro clip.
 * @param {string} characterId — one of the 8 main characters
 * @param {string} [basePath='/'] — path prefix to the audio directory (use '../../' from a lesson page)
 * @returns {Promise<void>} resolves when playback ends (or fails)
 */
export function playCharacterIntro(characterId, basePath = '/') {
  return new Promise((resolve) => {
    const file = CHARACTER_INTRO_FILES[characterId];
    if (!file) { resolve(); return; }
    try {
      if (_charIntroPlayer) { _charIntroPlayer.pause(); _charIntroPlayer.currentTime = 0; }
      _charIntroPlayer = new Audio(basePath + 'assets/audio/characters/' + file);
      let settled = false;
      const done = () => { if (!settled) { settled = true; resolve(); } };
      _charIntroPlayer.onended = done;
      _charIntroPlayer.onerror = done;
      const p = _charIntroPlayer.play();
      if (p && p.catch) p.catch(done);
      setTimeout(done, 10000); // safety
    } catch { resolve(); }
  });
}

export function stopCharacterIntro() {
  if (_charIntroPlayer) {
    try { _charIntroPlayer.pause(); _charIntroPlayer.currentTime = 0; } catch {}
  }
}

// ── Chrome speechSynthesis hardening ──────────────────────────────────
// Chrome's speech engine has two well-documented failure modes:
//   1. Utterances with no `voice` set sometimes get silently swallowed,
//      especially after long-running tabs. Always pick an explicit voice.
//   2. The engine can hang — speak() returns silently and onstart/onend
//      never fire. We detect this via onstart watchdog and retry once
//      with a FRESH utterance (never re-speak the same one).

let _voicesReadyPromise = null;
function _voicesReady() {
  if (_voicesReadyPromise) return _voicesReadyPromise;
  _voicesReadyPromise = new Promise((resolve) => {
    if (!('speechSynthesis' in window)) { resolve([]); return; }
    let v = window.speechSynthesis.getVoices();
    if (v.length > 0) { resolve(v); return; }
    let done = false;
    const finish = () => {
      if (done) return; done = true;
      resolve(window.speechSynthesis.getVoices());
    };
    try { window.speechSynthesis.addEventListener('voiceschanged', finish, { once: true }); } catch {}
    setTimeout(finish, 1500);
  });
  return _voicesReadyPromise;
}

function _pickVoiceForCharacter(characterId) {
  const voices = window.speechSynthesis.getVoices();
  if (!voices.length) return null;
  const preferredName = VOICE_SETTINGS[characterId] && VOICE_SETTINGS[characterId].voice;
  // First: exact character voice (Daniel, Albert, Karen, etc.)
  if (preferredName) {
    const named = voices.find(v => v.name === preferredName)
               || voices.find(v => v.name.toLowerCase().includes(preferredName.toLowerCase()));
    if (named) return named;
  }
  // Fallback: any English voice
  return voices.find(v => v.lang === 'en-US' && v.default)
      || voices.find(v => v.lang === 'en-US')
      || voices.find(v => v.lang.startsWith('en'))
      || voices[0];
}

function _applySettings(utterance, characterId, overrideSettings) {
  const baseline = VOICE_SETTINGS[characterId] || { pitch: 1.0, rate: 1.0, volume: 1.0 };
  const settings = overrideSettings ? { ...baseline, ...overrideSettings } : baseline;
  utterance.pitch = settings.pitch;
  utterance.rate = settings.rate;
  utterance.volume = settings.volume;
  utterance.lang = 'en-US';
  const v = _pickVoiceForCharacter(characterId);
  if (v) utterance.voice = v;
}

// Warm-up: Chrome cold-starts its TTS engine, and the FIRST speak() call
// after page load can be silently dropped. Speak a silent utterance on the
// first user gesture to wake the engine before the real ask hits.
let _engineWarmed = false;
function _warmUpEngine() {
  if (_engineWarmed || !('speechSynthesis' in window)) return;
  _engineWarmed = true;
  try {
    const w = new SpeechSynthesisUtterance(' ');
    w.volume = 0; w.rate = 10;
    window.speechSynthesis.speak(w);
  } catch {}
}
if (typeof document !== 'undefined') {
  ['click', 'touchstart', 'keydown'].forEach(ev => {
    document.addEventListener(ev, _warmUpEngine, { once: true, capture: true });
  });
}

/**
 * Speak a message using Web Speech API with character-specific pitch/rate.
 * @param {string} text - message to speak
 * @param {string} characterId - character key for voice settings
 */
export function speak(text, characterId) {
  if (!('speechSynthesis' in window)) return;
  _warmUpEngine();
  _voicesReady().then(() => {
    const utterance = new SpeechSynthesisUtterance(text);
    _applySettings(utterance, characterId, null);
    window.speechSynthesis.speak(utterance);
  });
}

/**
 * Speak a message and return a Promise that resolves when speech ends.
 * Has a hung-engine watchdog: if onstart never fires, retries once with a
 * fresh utterance (never re-speaks the same one — that's a Chrome no-op).
 * @param {string} text
 * @param {string} characterId
 * @param {{pitch?:number, rate?:number, volume?:number}} [overrideSettings] - per-call voice override
 * @returns {Promise<void>}
 */
export function speakAsync(text, characterId, overrideSettings = null) {
  return new Promise(async (resolve) => {
    if (!('speechSynthesis' in window)) { resolve(); return; }
    _warmUpEngine();
    await _voicesReady();

    let resolved = false;
    const finish = () => { if (!resolved) { resolved = true; resolve(); } };

    let attempts = 0;
    function attempt() {
      attempts++;
      const u = new SpeechSynthesisUtterance(text);
      _applySettings(u, characterId, overrideSettings);

      let started = false;
      u.onstart  = () => { started = true; };
      u.onend    = finish;
      u.onerror  = finish;

      window.speechSynthesis.speak(u);

      // Hung-engine watchdog. If speech hasn't started in 700ms AND we
      // haven't already retried, force a reset and retry with a fresh u.
      setTimeout(() => {
        if (started || resolved) return;
        if (attempts < 2) {
          try { window.speechSynthesis.cancel(); window.speechSynthesis.resume(); } catch {}
          setTimeout(attempt, 60);
        } else {
          // Two attempts and still nothing — give up, but free the UI after 5s.
          setTimeout(finish, 5000);
        }
      }, 700);
    }
    attempt();
  });
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
 * Set the language for character messages.
 * @param {string} lang — 'en', 'ca', etc.
 */
export function setCharacterLang(lang) {
  _charLang = lang;
}

/**
 * Show the character buddy — updates side panel + speaks message.
 * Uses the current language set by setCharacterLang().
 * @param {string} characterId — key in CHARACTERS (e.g. 'edam')
 * @param {string} reaction — one of 'correct', 'wrong', 'hint', 'perfect'
 */
export function showBuddy(characterId, reaction) {
  const character = CHARACTERS[characterId];
  if (!character) return;

  // Pick messages based on current language
  let msgs = character.messages;
  if (_charLang === 'ca' && character.messagesCa) msgs = character.messagesCa;
  if (_charLang === 'es' && character.messagesEs) msgs = character.messagesEs;
  if (_charLang === 'pt' && character.messagesPt) msgs = character.messagesPt;
  if (_charLang === 'fy' && FRISIAN_MESSAGES[characterId]) msgs = FRISIAN_MESSAGES[characterId];
  const message = msgs[reaction] || msgs.correct;
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

  /* Speak the message: try Web Speech API first (live character voice), then
   * fall back to the pre-recorded reaction clip if the browser engine never
   * starts within 800ms (Chrome hung-engine case). English reactions only. */
  _speakReactionHybrid(characterId, reaction, message);

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
