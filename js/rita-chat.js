/**
 * Rita the Cat — AI Chat Assistant
 * Pop-up chat widget with Rita's personality.
 */

const RITA_RESPONSES = {
  greetings: [
    "Miau! Hey there! What can I help you with? 🐱",
    "Purr... Hi! Rita here. Ask me anything! 🐾",
    "Meow! Welcome! I'm Rita, your study buddy. 😺"
  ],
  math: [
    "Purr... math is my favorite! What topic are you stuck on? Try breaking the problem into smaller steps. 🐱",
    "Miau! For math problems, always start by reading the question carefully. What's the specific topic? 📐",
    "Meow! Math can be tricky, but you've got this. Practice makes purrfect! 🐾"
  ],
  limits: [
    "Limits! Try direct substitution first. If you get 0/0, try factoring or L'Hôpital's Rule. Purr! 📊",
    "Miau! Remember: the limit is what the function APPROACHES, not necessarily what it equals. 🐱",
    "For limits at infinity, compare the highest degree terms in numerator and denominator! Meow! 🎯"
  ],
  derivatives: [
    "Derivatives = slope of the tangent line! Remember: power rule, product rule, quotient rule, chain rule. Purr! 📈",
    "Miau! The chain rule is the trickiest — work from outside in. d/dx[f(g(x))] = f'(g(x)) · g'(x) 🐱",
    "Don't forget: derivative of sin(x) is cos(x), and derivative of cos(x) is -sin(x)! Meow! 🎓"
  ],
  integrals: [
    "Integration is the reverse of differentiation! Try u-substitution first, then integration by parts. Purr! ∫",
    "Miau! Remember: ∫xⁿ dx = xⁿ⁺¹/(n+1) + C. Don't forget the +C! 🐱",
    "For trig integrals, know your identities! sin²x + cos²x = 1 is your best friend. Meow! 🐾"
  ],
  calculus: [
    "Calculus is all about change! Derivatives measure rate of change, integrals measure accumulation. Purr! 📚",
    "Miau! Start with limits, then derivatives, then integrals. Each builds on the last! 🐱",
    "The Fundamental Theorem of Calculus connects derivatives and integrals — it's purrfectly beautiful! 🎯"
  ],
  trig: [
    "SOH-CAH-TOA! Sin = Opposite/Hypotenuse, Cos = Adjacent/Hypotenuse, Tan = Opposite/Adjacent. Purr! 📐",
    "Miau! The unit circle is key — memorize the values at 0°, 30°, 45°, 60°, 90°. 🐱",
    "Remember: sin²θ + cos²θ = 1. This identity solves SO many problems! Meow! 🐾"
  ],
  study: [
    "Purr... my study tips: 1) Short sessions (25 min), 2) Practice problems, 3) Teach it to someone else! 📖",
    "Miau! Don't just read — DO the problems. Active practice beats passive reading every time! 🐱",
    "Take breaks! Your brain needs rest to absorb new info. The Pomodoro technique works great! Meow! ⏰"
  ],
  help: [
    "I can help with math, science, study tips, and using Mathagram! Just ask me anything. Purr! 🐱",
    "Miau! Try asking about: limits, derivatives, integrals, trig, study tips, or any course topic! 🐾",
    "Need help? I'm here! Ask about a specific topic or just say what's confusing you. Meow! 😺"
  ],
  motivation: [
    "You've got this! Every expert was once a beginner. Keep going! Purr! 💪🐱",
    "Miau! Mistakes are how we learn. Don't be afraid to get things wrong — that's purrfectly normal! 🌟",
    "Meow! I believe in you! One lesson at a time, one question at a time. You're doing great! 🐾✨"
  ],
  thanks: [
    "You're welcome! Purr... always happy to help! 🐱💕",
    "Miau! Anytime! That's what I'm here for! 😺",
    "Meow! No problem at all! Keep up the great work! 🐾"
  ],
  funny: [
    "Why did the cat sit on the computer? To keep an eye on the mouse! Purr... 🐱😂",
    "Miau! What's a cat's favorite subject? MEW-sic... just kidding, it's MATH! 😹",
    "Meow! I tried to do my homework but my cat ate it... wait, I AM the cat! 🐾😂"
  ],
  science: [
    "Science is all about asking WHY and HOW! Observe, hypothesize, experiment, conclude. Purr! 🔬",
    "Miau! The scientific method is your best friend. Always test your ideas! 🐱",
    "Meow! Remember: correlation doesn't equal causation. Think critically! 🐾🧪"
  ],
  language: [
    "Learning a language? Practice every day, even just 5 minutes! Consistency is key. Purr! 🌍",
    "Miau! Try thinking in the new language instead of translating. It speeds things up! 🐱",
    "Meow! Don't be afraid to make mistakes when speaking. That's how you learn! 🐾"
  ],
  bye: [
    "Oant sjen! I mean... goodbye! Come back anytime! Purr! 🐱👋",
    "Miau! See you later! Keep studying! 😺",
    "Meow! Bye-bye! Remember: you're doing amazing! 🐾✨"
  ],
  default: [
    "Hmm, interesting question! I'm still learning too. Try asking about math, study tips, or a specific topic! Purr! 🐱",
    "Miau! I'm not sure about that one. Can you tell me more? Or try asking about a course topic! 😺",
    "Meow! Good question! I work best with math, science, and study questions. What are you working on? 🐾"
  ]
};

function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function getRitaResponse(input) {
  const lower = input.toLowerCase();
  if (/^(hi|hello|hey|hola|goeie|sup|yo|what'?s up)/.test(lower)) return pickRandom(RITA_RESPONSES.greetings);
  if (/limit|l'?hopital|squeeze|continuity|discontinu/.test(lower)) return pickRandom(RITA_RESPONSES.limits);
  if (/derivat|differentiat|chain rule|product rule|power rule|quotient/.test(lower)) return pickRandom(RITA_RESPONSES.derivatives);
  if (/integr|antiderivat|substitut|by parts|fundamental theorem/.test(lower)) return pickRandom(RITA_RESPONSES.integrals);
  if (/calculus/.test(lower)) return pickRandom(RITA_RESPONSES.calculus);
  if (/trig|sin|cos|tan|unit circle|soh.?cah.?toa|angle/.test(lower)) return pickRandom(RITA_RESPONSES.trig);
  if (/math|algebra|equation|solve|formula|number/.test(lower)) return pickRandom(RITA_RESPONSES.math);
  if (/science|physics|chemistry|biology|experiment/.test(lower)) return pickRandom(RITA_RESPONSES.science);
  if (/language|catalan|frisian|spanish|french|learn.*lang/.test(lower)) return pickRandom(RITA_RESPONSES.language);
  if (/study|learn|tip|advice|how to|focus|exam|test|homework/.test(lower)) return pickRandom(RITA_RESPONSES.study);
  if (/help|stuck|confused|don'?t understand|what can you/.test(lower)) return pickRandom(RITA_RESPONSES.help);
  if (/motivat|encourage|hard|difficult|give up|can'?t|impossible/.test(lower)) return pickRandom(RITA_RESPONSES.motivation);
  if (/thank|thanks|thx|appreciate/.test(lower)) return pickRandom(RITA_RESPONSES.thanks);
  if (/joke|funny|laugh|haha|lol/.test(lower)) return pickRandom(RITA_RESPONSES.funny);
  if (/bye|goodbye|see you|later|gtg|gotta go/.test(lower)) return pickRandom(RITA_RESPONSES.bye);
  return pickRandom(RITA_RESPONSES.default);
}

/**
 * Initialize Rita chat widget.
 * @param {string} basePath — path to assets root
 */
export function initRitaChat(basePath = '') {
  if (document.getElementById('rita-chat-widget')) return;

  const widget = document.createElement('div');
  widget.id = 'rita-chat-widget';
  widget.innerHTML = `
    <style>
      #rita-chat-btn {
        position: fixed; bottom: 24px; right: 24px; z-index: 900;
        width: 60px; height: 60px; border-radius: 50%;
        border: 3px solid #ec4899; background: #fff;
        cursor: pointer; box-shadow: 0 4px 20px rgba(236,72,153,0.3);
        transition: all 0.3s; overflow: hidden; padding: 0;
      }
      #rita-chat-btn:hover { transform: scale(1.1); box-shadow: 0 6px 28px rgba(236,72,153,0.4); }
      #rita-chat-btn img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
      #rita-chat-btn .chat-badge {
        position: absolute; top: -2px; right: -2px;
        width: 18px; height: 18px; border-radius: 50%;
        background: #ec4899; border: 2px solid #fff;
        font-size: 0.55rem; color: #fff; font-weight: 800;
        display: flex; align-items: center; justify-content: center;
      }

      #rita-chat-popup {
        position: fixed; bottom: 96px; right: 24px; z-index: 901;
        width: 340px; max-height: 480px; border-radius: 20px;
        background: #fff; border: 1px solid #e2e8f0;
        box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        display: none; flex-direction: column; overflow: hidden;
      }
      #rita-chat-popup.open { display: flex; animation: chatSlideUp 0.3s ease; }
      @keyframes chatSlideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
      }

      .rita-chat-header {
        background: linear-gradient(135deg, #ec4899, #db2777);
        color: #fff; padding: 14px 18px;
        display: flex; align-items: center; gap: 10px;
      }
      .rita-chat-header img { width: 36px; height: 36px; border-radius: 50%; border: 2px solid rgba(255,255,255,0.4); }
      .rita-chat-header .rita-info { flex: 1; }
      .rita-chat-header .rita-name { font-weight: 800; font-size: 0.95rem; }
      .rita-chat-header .rita-status { font-size: 0.7rem; opacity: 0.85; }
      .rita-chat-close {
        background: none; border: none; color: #fff; font-size: 1.3rem;
        cursor: pointer; padding: 4px 8px; border-radius: 8px; transition: background 0.2s;
      }
      .rita-chat-close:hover { background: rgba(255,255,255,0.2); }

      .rita-chat-messages {
        flex: 1; overflow-y: auto; padding: 16px; display: flex;
        flex-direction: column; gap: 12px; min-height: 200px; max-height: 300px;
      }
      .rita-msg {
        max-width: 85%; padding: 10px 14px; border-radius: 16px;
        font-size: 0.88rem; line-height: 1.5; animation: msgFade 0.3s ease;
      }
      @keyframes msgFade { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
      .rita-msg.rita {
        background: #fdf2f8; color: #831843; border-bottom-left-radius: 4px;
        align-self: flex-start;
      }
      .rita-msg.user {
        background: #ec4899; color: #fff; border-bottom-right-radius: 4px;
        align-self: flex-end;
      }

      .rita-chat-input {
        display: flex; gap: 8px; padding: 12px 14px;
        border-top: 1px solid #e2e8f0; background: #fafafa;
      }
      .rita-chat-input input {
        flex: 1; padding: 10px 14px; border: 2px solid #e2e8f0;
        border-radius: 999px; font-size: 0.88rem; font-family: inherit;
        background: #fff; outline: none; transition: border-color 0.2s;
      }
      .rita-chat-input input:focus { border-color: #ec4899; }
      .rita-chat-input button {
        width: 38px; height: 38px; border-radius: 50%;
        background: #ec4899; color: #fff; border: none;
        cursor: pointer; font-size: 1rem; transition: all 0.2s;
        display: flex; align-items: center; justify-content: center;
      }
      .rita-chat-input button:hover { background: #db2777; transform: scale(1.05); }

      @media (max-width: 480px) {
        #rita-chat-popup { width: calc(100vw - 32px); right: 16px; bottom: 88px; }
        #rita-chat-btn { bottom: 16px; right: 16px; width: 54px; height: 54px; }
      }
    </style>

    <button id="rita-chat-btn" title="Chat with Rita">
      <img src="${basePath}assets/characters/rita.svg" alt="Rita">
      <span class="chat-badge">?</span>
    </button>

    <div id="rita-chat-popup">
      <div class="rita-chat-header">
        <img src="${basePath}assets/characters/rita.svg" alt="Rita">
        <div class="rita-info">
          <div class="rita-name">Rita the Cat</div>
          <div class="rita-status">Online — ready to help!</div>
        </div>
        <button class="rita-chat-close" id="rita-close">&times;</button>
      </div>
      <div class="rita-chat-messages" id="rita-messages"></div>
      <div class="rita-chat-input">
        <input type="text" id="rita-input" placeholder="Ask Rita anything..." maxlength="200" autocomplete="off">
        <button id="rita-send">&#10148;</button>
      </div>
    </div>
  `;
  document.body.appendChild(widget);

  const btn = document.getElementById('rita-chat-btn');
  const popup = document.getElementById('rita-chat-popup');
  const closeBtn = document.getElementById('rita-close');
  const input = document.getElementById('rita-input');
  const sendBtn = document.getElementById('rita-send');
  const messages = document.getElementById('rita-messages');

  let isOpen = false;
  let firstOpen = true;

  btn.addEventListener('click', () => {
    isOpen = !isOpen;
    popup.classList.toggle('open', isOpen);
    if (isOpen && firstOpen) {
      firstOpen = false;
      addRitaMsg(pickRandom(RITA_RESPONSES.greetings));
    }
    if (isOpen) input.focus();
  });

  closeBtn.addEventListener('click', () => {
    isOpen = false;
    popup.classList.remove('open');
  });

  function addRitaMsg(text) {
    const div = document.createElement('div');
    div.className = 'rita-msg rita';
    div.textContent = text;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function addUserMsg(text) {
    const div = document.createElement('div');
    div.className = 'rita-msg user';
    div.textContent = text;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function send() {
    const text = input.value.trim();
    if (!text) return;
    addUserMsg(text);
    input.value = '';
    // Rita "typing" delay
    setTimeout(() => {
      addRitaMsg(getRitaResponse(text));
    }, 400 + Math.random() * 600);
  }

  sendBtn.addEventListener('click', send);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') { e.preventDefault(); send(); }
  });
}
