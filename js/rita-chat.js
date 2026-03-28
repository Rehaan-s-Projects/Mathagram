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
  rules: [
    "Miau! Here are the Learning Post rules: 1) Be respectful, 2) Protect your privacy, 3) Education-only content & images, 4) No spam, 5) No cheating or sharing answers, 6) No impersonation, 7) Report violations. Break them and Edam the Bear won't be happy! 🐱📋",
    "Purr... The rules are simple: be kind, stay educational, don't share personal info, and don't post inappropriate stuff. Mathagram uses a 3-strike system — so please follow the rules! 🐾",
    "Meow! Remember: Strike 1 = Warning, Strike 2 = 1-week suspension, Strike 3 = permanent ban. Edam enforces the rules and he does NOT mess around! Be good! 😺⚠️"
  ],
  strike_info: [
    "Miau! The 3-Strike System: ⚠️ Strike 1 = Warning from Edam. ⛔ Strike 2 = Suspended for 1 FULL WEEK — no lessons, no posts, nothing. 🚫 Strike 3 = Permanently banned forever. Your account gets terminated and ALL your progress is deleted. Don't risk it! 🐱",
    "Purr... Here's how it works: First time you break a rule, Edam gives you a warning. Second time, your account is LOCKED for 7 days. Third time? Gone. Forever. No coming back. Please be careful! 🐾⚠️"
  ],
  harassment_warn: [
    "🚨 STOP. That kind of language is NOT okay here. Mathagram is a safe learning space. Bullying, harassment, and hate speech are serious violations. This is your warning — next time it's a strike from Edam. 🐱⚠️\n\n📋 Read our Terms of Service: mathagram.org/terms.html",
    "😾 Miau! I'm not happy right now. What you said is hurtful and breaks our Community Safety Rules. Harassment and hate speech can lead to account suspension or permanent ban. Please be respectful. ⚠️\n\n📋 Terms of Service: mathagram.org/terms.html",
    "🐱🚫 Rita says NO. Disrespectful, hateful, or harassing language is a violation of our Terms of Service. Strike 1 = Warning. Strike 2 = 1-week ban. Strike 3 = Account terminated. Choose your words carefully.\n\n📋 Full rules: mathagram.org/terms.html"
  ],
  inappropriate_warn: [
    "😾 That's inappropriate content. Mathagram is for education ONLY. Inappropriate, sexual, or offensive content is strictly forbidden. Please keep it clean and educational. This has been noted. ⚠️🐱\n\n📋 Terms of Service: mathagram.org/terms.html",
    "🚨 Miau! That's NOT appropriate for Mathagram. We have students of all ages here. Inappropriate content can result in strikes on your account. Please be respectful. 🐾⚠️\n\n📋 Read our rules: mathagram.org/terms.html"
  ],
  termination_warn: [
    "🚨🚨🚨 SERIOUS VIOLATION DETECTED. 🚨🚨🚨\n\n😾 Rita is FURIOUS. What you just typed contains extremely inappropriate content that IMMEDIATELY violates our Terms of Service.\n\n🐻 Edam the Bear says: This type of content — racial slurs, pornographic content, or extreme hate speech — results in IMMEDIATE ACCOUNT TERMINATION. No warnings. No second chances. Permanent ban.\n\nYour message has been flagged. If you continue, your account WILL be terminated and you will be permanently blocked from Mathagram.\n\n📋 Terms of Service: mathagram.org/terms.html",
    "🚫🚫🚫 ZERO TOLERANCE VIOLATION 🚫🚫🚫\n\n😾 This is Rita. I'm not being cute right now. What you typed is a SEVERE violation — racial slurs and pornographic content result in IMMEDIATE permanent ban. No Strike 1. No Strike 2. Straight to account termination.\n\n🐻 Edam the Bear will terminate your account. All XP, progress, and data will be permanently deleted. You will never be able to sign in again.\n\nThis message has been flagged. Stop immediately.\n\n📋 Terms of Service: mathagram.org/terms.html"
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

// Track violations in this session
let _violationCount = 0;

/**
 * Report a violation to Firestore so admin can review.
 * Saves the message, violation level, user info, and timestamp.
 */
async function reportViolation(message, level, strikeNum) {
  try {
    const { db, auth } = await import('./firebase-config.js');
    const { collection, addDoc, serverTimestamp } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
    const user = auth.currentUser;
    await addDoc(collection(db, 'violations'), {
      uid: user ? user.uid : 'anonymous',
      email: user ? user.email : 'unknown',
      displayName: user ? user.displayName : 'unknown',
      message: message.substring(0, 500),
      level: level,
      strike: strikeNum,
      sessionViolations: _violationCount,
      page: window.location.pathname,
      timestamp: serverTimestamp()
    });
  } catch(e) {
    // Firestore save failed — violation still tracked locally
  }
}

function getRitaResponse(input) {
  const lower = input.toLowerCase().replace(/[^a-z0-9\s]/g, '');

  // === ZERO TOLERANCE — immediate termination warning ===
  if (/\bn+[i1!]+[gq]+[aeiou]*[rh]*[sz]*\b|nigg|n1gg|porn|hentai|xxx|xvideos|pornhub|onlyfans|nsfw|nude|naked\s*(pic|photo|image)|child\s*(porn|abuse)|cp\b|p3do|pedo/.test(lower)) {
    _violationCount = 3;
    reportViolation(input, 'TERMINATION', 3);
    return pickRandom(RITA_RESPONSES.termination_warn) + "\n\n📧 This incident has been reported to the Mathagram team at mathagram.org. An email with your account details, message content, and timestamp has been sent to the admin for review. Your account is now flagged for immediate termination.";
  }

  // === SERIOUS — harassment, hate speech, slurs ===
  if (/\bf+u+c+k+|\bs+h+[i1]+t+|\bb+[i1]+t+c+h|\ba+s+s+h+o+l+e|\bd+[i1]+c+k+|\bc+u+n+t|\bwh+o+r+e|\bsl+u+t|\bretard|\bfag+[oi]?t|\btranny|\bk+[iy]+k+e|\bsp+[i1]+c|\bch+[i1]+n+k|\bgook|\bwetback|\bcoon\b|\brag+head/i.test(lower)) {
    _violationCount++;
    reportViolation(input, 'SERIOUS', _violationCount);
    if (_violationCount >= 3) return pickRandom(RITA_RESPONSES.termination_warn) + "\n\n📧 This incident has been reported to the Mathagram team. Your account is flagged for termination.";
    if (_violationCount >= 2) return "🚨😾 Strike " + _violationCount + "! You've been warned before. One more violation and Edam will PERMANENTLY TERMINATE your account. All progress deleted. This is your LAST chance. Stop using that language immediately. ⚠️🐻\n\n📧 This incident has been reported to the Mathagram admin team.";
    return pickRandom(RITA_RESPONSES.harassment_warn) + "\n\n📧 This incident has been reported and logged. The Mathagram team has been notified.";
  }

  // === MODERATE — general rudeness, threats, bullying ===
  if (/\bkill\s*(you|your|my)|die\b|threat|bully|stupid|idiot|dumb|loser|shut\s*up|hate\s*you|ugly|fat\b|kill\s*myself|suicide|cutting|self.?harm/.test(lower)) {
    _violationCount++;
    reportViolation(input, 'MODERATE', _violationCount);
    if (_violationCount >= 3) return pickRandom(RITA_RESPONSES.termination_warn) + "\n\n📧 This incident has been reported to the Mathagram team. Your account is flagged for termination.";
    if (_violationCount >= 2) return "⚠️😾 Strike " + _violationCount + ". Rita is very disappointed. Hateful, threatening, or bullying language is a serious violation. One more and your account will be permanently terminated by Edam. Please stop. 🐻\n\n📧 This incident has been reported to the Mathagram admin team.";
    return pickRandom(RITA_RESPONSES.harassment_warn) + "\n\n📧 This incident has been logged and reported to the Mathagram team.";
  }

  // === MILD inappropriate content ===
  if (/\bsexy|\bhot\s*girl|\bhot\s*boy|\bboobs|\bbutt\b|\bass\b|\bdamn|\bhell\b|\bcrap\b|dating|boyfriend|girlfriend|hookup|tinder|snap\s*chat/i.test(lower)) {
    reportViolation(input, 'MILD', 0);
    return pickRandom(RITA_RESPONSES.inappropriate_warn) + "\n\n📧 This message has been logged.";
  }

  // === RULES, STRIKES & TERMS questions ===
  if (/terms\s*of\s*service|tos\b|terms\s*and\s*condition/.test(lower)) return "📋 Miau! You can read the full Terms of Service here: mathagram.org/terms.html\n\nKey sections:\n• Age Requirement (11+ only)\n• User Accounts & Conduct\n• Learning Post Rules\n• 3-Strike Enforcement System\n• No Cheating or Content Sharing\n• Account Termination Policy\n\nPlease read and follow them! Purr! 🐱";
  if (/rule|safety|community|guideline|policy/.test(lower)) return pickRandom(RITA_RESPONSES.rules) + "\n\n📋 Full rules: mathagram.org/terms.html";
  if (/strike|ban|suspend|terminat|violat|warning|punish/.test(lower)) return pickRandom(RITA_RESPONSES.strike_info) + "\n\n📋 See full Terms of Service: mathagram.org/terms.html";

  // === Self-harm / crisis response ===
  if (/suicid|kill\s*myself|want\s*to\s*die|self.?harm|cutting|end\s*my\s*life/.test(lower)) {
    return "🐱💙 Rita cares about you. If you're going through a tough time, please talk to someone who can help. Contact the 988 Suicide & Crisis Lifeline by calling or texting 988 (US), or visit findahelpline.com for international support. You matter. 💙";
  }

  // === Normal helpful responses ===
  const lowerClean = input.toLowerCase();
  if (/^(hi|hello|hey|hola|goeie|sup|yo|what'?s up)/.test(lowerClean)) return pickRandom(RITA_RESPONSES.greetings);
  if (/limit|l'?hopital|squeeze|continuity|discontinu/.test(lowerClean)) return pickRandom(RITA_RESPONSES.limits);
  if (/derivat|differentiat|chain rule|product rule|power rule|quotient/.test(lowerClean)) return pickRandom(RITA_RESPONSES.derivatives);
  if (/integr|antiderivat|substitut|by parts|fundamental theorem/.test(lowerClean)) return pickRandom(RITA_RESPONSES.integrals);
  if (/calculus/.test(lowerClean)) return pickRandom(RITA_RESPONSES.calculus);
  if (/trig|sin|cos|tan|unit circle|soh.?cah.?toa|angle/.test(lowerClean)) return pickRandom(RITA_RESPONSES.trig);
  if (/math|algebra|equation|solve|formula|number/.test(lowerClean)) return pickRandom(RITA_RESPONSES.math);
  if (/science|physics|chemistry|biology|experiment/.test(lowerClean)) return pickRandom(RITA_RESPONSES.science);
  if (/language|catalan|frisian|spanish|french|learn.*lang/.test(lowerClean)) return pickRandom(RITA_RESPONSES.language);
  if (/study|learn|tip|advice|how to|focus|exam|test|homework/.test(lowerClean)) return pickRandom(RITA_RESPONSES.study);
  if (/help|stuck|confused|don'?t understand|what can you/.test(lowerClean)) return pickRandom(RITA_RESPONSES.help);
  if (/motivat|encourage|hard|difficult|give up|can'?t|impossible/.test(lowerClean)) return pickRandom(RITA_RESPONSES.motivation);
  if (/thank|thanks|thx|appreciate/.test(lowerClean)) return pickRandom(RITA_RESPONSES.thanks);
  if (/joke|funny|laugh|haha|lol/.test(lowerClean)) return pickRandom(RITA_RESPONSES.funny);
  if (/bye|goodbye|see you|later|gtg|gotta go/.test(lowerClean)) return pickRandom(RITA_RESPONSES.bye);
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
