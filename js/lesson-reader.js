/**
 * Mathagram — Lesson Reader (Duolingo-style)
 * Adds a character avatar + listen button next to each paragraph
 * in lesson content. Clicking reads the paragraph aloud with the
 * character's unique voice.
 */

import { CHARACTERS } from './characters.js';

const VOICE_SETTINGS = {
  edam:    { pitch: 0.8,  rate: 0.9  },
  steve:   { pitch: 1.2,  rate: 1.15 },
  james:   { pitch: 0.6,  rate: 0.85 },
  diego:   { pitch: 1.0,  rate: 1.0  },
  rita:    { pitch: 1.8,  rate: 1.2  },
  sam:     { pitch: 1.6,  rate: 1.3  },
  william: { pitch: 0.5,  rate: 0.75 },
  gosia:   { pitch: 1.4,  rate: 1.05 }
};

const charIds = Object.keys(CHARACTERS);

/**
 * Initialize the lesson reader — adds listen buttons to all paragraphs
 * in .lesson-content sections.
 * @param {string} basePath - relative path to root (e.g. '../../')
 */
export function initLessonReader(basePath = '../../') {
  const content = document.querySelector('.lesson-content');
  if (!content) return;

  // Add CSS
  if (!document.getElementById('reader-styles')) {
    const style = document.createElement('style');
    style.id = 'reader-styles';
    style.textContent = `
      .reader-row {
        display: flex;
        gap: 14px;
        align-items: flex-start;
        margin-bottom: 16px;
      }
      .reader-avatar-wrap {
        flex-shrink: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        margin-top: 2px;
      }
      .reader-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 2px solid #e2e8f0;
        cursor: pointer;
        transition: all 0.2s;
      }
      .reader-avatar:hover {
        border-color: #00e5c8;
        transform: scale(1.1);
      }
      .reader-avatar.speaking {
        border-color: #00e5c8;
        box-shadow: 0 0 0 3px rgba(0,229,200,0.3);
        animation: speakPulse 1s ease infinite;
      }
      @keyframes speakPulse {
        0%, 100% { box-shadow: 0 0 0 3px rgba(0,229,200,0.3); }
        50% { box-shadow: 0 0 0 6px rgba(0,229,200,0.1); }
      }
      .reader-listen-btn {
        background: none;
        border: none;
        cursor: pointer;
        font-size: 0.65rem;
        color: #00b89f;
        font-weight: 700;
        padding: 2px 6px;
        border-radius: 6px;
        transition: background 0.2s;
      }
      .reader-listen-btn:hover {
        background: rgba(0,229,200,0.1);
      }
      .reader-text {
        flex: 1;
        min-width: 0;
      }
      .reader-text p {
        margin-bottom: 0 !important;
      }
      .reader-name {
        font-size: 0.6rem;
        font-weight: 700;
        color: #94a3b8;
        text-align: center;
      }
      /* Don't wrap math blocks or headings */
      .lesson-content .math-block,
      .lesson-content h1,
      .lesson-content h2,
      .lesson-content ul,
      .lesson-content ol {
        /* Keep as-is */
      }
    `;
    document.head.appendChild(style);
  }

  // Find all paragraphs in lesson content
  const paragraphs = content.querySelectorAll('p');
  let charIndex = 0;

  paragraphs.forEach((p) => {
    // Skip very short paragraphs or ones already wrapped
    const text = p.textContent.trim();
    if (text.length < 20 || p.closest('.reader-row')) return;

    // Pick a character (cycle through them)
    const charId = charIds[charIndex % charIds.length];
    const char = CHARACTERS[charId];
    charIndex++;

    // Create wrapper row
    const row = document.createElement('div');
    row.className = 'reader-row';

    // Avatar + listen button
    const avatarWrap = document.createElement('div');
    avatarWrap.className = 'reader-avatar-wrap';

    const avatar = document.createElement('img');
    avatar.className = 'reader-avatar';
    avatar.src = basePath + 'assets/characters/' + char.file;
    avatar.alt = char.name;
    avatar.title = 'Click to listen — ' + char.name;

    const nameLabel = document.createElement('span');
    nameLabel.className = 'reader-name';
    nameLabel.textContent = char.name;

    const listenBtn = document.createElement('button');
    listenBtn.className = 'reader-listen-btn';
    listenBtn.textContent = 'Listen';
    listenBtn.type = 'button';

    avatarWrap.appendChild(avatar);
    avatarWrap.appendChild(nameLabel);
    avatarWrap.appendChild(listenBtn);

    // Text content
    const textWrap = document.createElement('div');
    textWrap.className = 'reader-text';

    // Replace paragraph with row
    p.parentNode.insertBefore(row, p);
    textWrap.appendChild(p);
    row.appendChild(avatarWrap);
    row.appendChild(textWrap);

    // Click to speak
    function speak() {
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();

      // Clean text for speech (strip math notation)
      const clean = text
        .replace(/\\\(.*?\\\)/g, 'math expression')
        .replace(/\$\$.*?\$\$/g, 'math expression')
        .replace(/\\displaystyle/g, '')
        .replace(/\\[a-zA-Z]+/g, '')
        .replace(/[{}]/g, '')
        .replace(/\s+/g, ' ')
        .trim();
      if (!clean) return;

      const utterance = new SpeechSynthesisUtterance(clean);
      const settings = VOICE_SETTINGS[charId] || { pitch: 1.0, rate: 1.0 };
      utterance.pitch = settings.pitch;
      utterance.rate = settings.rate;
      utterance.volume = 0.8;

      // Try to find a good voice
      const voices = window.speechSynthesis.getVoices();
      if (voices.length > 0) {
        const preferred = voices.find(v => v.lang.startsWith('en') && !v.name.includes('female') && v.name.includes('Male')) ||
                          voices.find(v => v.lang.startsWith('en')) ||
                          voices[0];
        if (preferred) utterance.voice = preferred;
      }

      // Highlight while speaking
      avatar.classList.add('speaking');
      listenBtn.textContent = 'Speaking...';
      utterance.onend = () => {
        avatar.classList.remove('speaking');
        listenBtn.textContent = 'Listen';
      };
      utterance.onerror = () => {
        avatar.classList.remove('speaking');
        listenBtn.textContent = 'Listen';
      };

      window.speechSynthesis.speak(utterance);
    }

    avatar.addEventListener('click', speak);
    listenBtn.addEventListener('click', speak);
  });
}
