// Musical Practice — quiz question bank.
//
// BASICS keyed by lesson position (1–15) inside the Basics Piano unit.
//   Positions 1 (Meet the Piano) and 2 (Find Middle C) are real interactive
//   lessons in basics-1.html / basics-2.html, so they're not in this bank.
//
// SONG keyed by lesson position (1–15) inside any song unit. Each entry is a
// function that takes the song name and returns the 4 multiple-choice
// questions for that lesson. Position 1 of Twinkle (the very first song) is
// also a real interactive lesson (lesson-1.html), so on the wiring side we
// skip that specific song-lesson; the function in SONG[1] is still used for
// every OTHER song's "Listen" lesson.
//
// Distractors are intentionally Duolingo-absurd, never plausible near-misses.

// ─────────────────────────────────────────────────────────────────────────
// BASICS PIANO (Unit 1) lessons 3–15
// ─────────────────────────────────────────────────────────────────────────
export const BASICS = {
  3: [ // White Keys — C D E F G A B
    { q: 'How many white keys are on a full 88-key piano?',
      a: ['52', '3', 'One million', 'Whichever the cat says today'] },
    { q: 'White keys are named with which letters?',
      a: ['A through G', 'Q through Z', 'Greek emojis only', 'Pirate noises'] },
    { q: 'Each letter repeats up the keyboard in patterns called…',
      a: ['Octaves', 'Sardine cans', 'Tax brackets', 'Unwise decisions'] },
    { q: 'The white key just to the left of two black keys is always…',
      a: ['C', 'A penguin', 'A loaf of bread', 'The mayor of the piano'] }
  ],
  4: [ // Black Keys — Sharps & Flats
    { q: 'How many black keys does a full piano have?',
      a: ['36', '12', '7,000', 'Black keys are a myth'] },
    { q: 'Black keys are arranged in alternating groups of…',
      a: ['2 and 3', '7 and 11', 'Wiggly triangles', 'Polite vowels'] },
    { q: 'A "sharp" note is one half-step…',
      a: ['Higher', 'Lower than yesterday', 'Sideways like a crab', 'In the freezer'] },
    { q: 'A "flat" note is one half-step…',
      a: ['Lower', 'Slightly damp', 'Standing on its head', 'Inside an envelope'] }
  ],
  5: [ // Octaves
    { q: 'An octave is the distance between a note and…',
      a: ['The next note of the same name', 'Its cousin Bertha', 'A waiting room', 'A small kazoo'] },
    { q: 'A standard 88-key piano spans roughly how many octaves?',
      a: ['Just over 7', '½', '4,500', 'Whatever the moon decides'] },
    { q: 'Two notes an octave apart sound…',
      a: ['Like the same note, higher or lower', 'Like a squeaky shopping cart', 'Like a duck saying hello', 'Identical to a doorbell'] },
    { q: 'The frequency of a note one octave higher is…',
      a: ['Double', 'Negative', 'A long story', 'Whatever you want it to be'] }
  ],
  6: [ // Right Hand Finger Numbers (1–5)
    { q: 'On your right hand, finger 1 is the…',
      a: ['Thumb', 'Pinky', 'Elbow', 'Mr. Thumby III'] },
    { q: 'The right-hand pinky is finger number…',
      a: ['5', '17', '-3', 'The Forbidden Finger'] },
    { q: 'Why do pianists number their fingers?',
      a: ['So sheet music can tell you which finger to use', 'Because thumbs file complaints', 'To win a finger pageant', 'To confuse the chickens'] },
    { q: 'Finger numbering on the right hand starts from the…',
      a: ['Thumb', 'Eyebrow', 'Left ankle', 'Wherever the wind blows'] }
  ],
  7: [ // Left Hand Finger Numbers
    { q: 'On your LEFT hand, finger 1 is the…',
      a: ['Thumb', 'Pinky', 'Right ear', 'A sleepy badger'] },
    { q: 'The left-hand pinky is finger number…',
      a: ['5', '12', 'π', 'A polite scream'] },
    { q: 'Left and right hand finger numbers…',
      a: ['Both start at the thumb', 'Disagree on Tuesdays', 'Switch when no one is looking', 'Are spelled out in Latin'] },
    { q: 'Left-hand bass clef parts most often use which finger first on a low C?',
      a: ['Finger 5', 'Finger 11', 'No finger — use your nose', 'A spare violin bow'] }
  ],
  8: [ // Hand Position & Posture
    { q: 'Good piano posture means sitting…',
      a: ['Tall, with both feet flat on the floor', 'Curled into a sleepy comma', 'Standing on one leg like a flamingo', 'Sprawled across the bench like a cat'] },
    { q: 'Your wrists while playing should be…',
      a: ['Level and relaxed', 'Above your ears', 'Spinning like helicopter blades', 'Sealed in cling wrap'] },
    { q: 'The bench should be positioned so you sit…',
      a: ['Centered on Middle C', 'In the next room', 'Floating two feet above the floor', 'Wherever the snacks are'] },
    { q: 'Why does posture matter for piano?',
      a: ['It prevents strain and improves technique', 'Pianos refuse to play for slouchers', 'It impresses the spider in the corner', 'Otherwise the keys go to sleep'] }
  ],
  9: [ // Soft vs Loud — Dynamics
    { q: 'In music, "forte" means…',
      a: ['Loud', 'A small castle', 'Politely sneeze', 'The 4th letter of the alphabet'] },
    { q: '"Piano" as a dynamic marking means…',
      a: ['Soft', 'Crashing waves', 'Pretend to be a ferret', 'Sing only in opera voice'] },
    { q: 'Dynamics give a piece its sense of…',
      a: ['Emotional contrast', 'Tax compliance', 'Salt content', 'Bus schedule'] },
    { q: 'The marking "mf" stands for…',
      a: ['Mezzo forte — medium loud', 'Mostly fluffy', 'Microwaved foods', 'Mathematical fizz'] }
  ],
  10: [ // Holding a Note vs Staccato
    { q: '"Staccato" notes are played…',
      a: ['Short and detached', 'Underwater', 'Through a kazoo', 'With your elbows only'] },
    { q: '"Legato" notes are played…',
      a: ['Smoothly connected', 'Bouncing off the walls', 'Inside a paper bag', 'On Wednesdays only'] },
    { q: 'A staccato note is marked above the note with a…',
      a: ['Small dot', 'Tiny mustache', 'Cape', 'Confused emoji'] },
    { q: 'Holding a note for its full value is called playing it…',
      a: ['Sustained / legato', 'With suspicion', 'In a hat', 'Under protest'] }
  ],
  11: [ // Two Notes Together — Intervals
    { q: 'An "interval" in music is the distance between…',
      a: ['Two notes', 'A snack break', 'A polite cough', 'A small dog'] },
    { q: 'C to E (counted as a third) is what interval?',
      a: ['A third', 'A spiral', 'A traffic light', 'Three confused ducks'] },
    { q: 'Playing two notes at the same time produces…',
      a: ['Harmony', 'A banana', 'A startled goose', 'A referee with no whistle'] },
    { q: 'C to G is what interval?',
      a: ['A fifth', 'A teaspoon', 'A doorbell', 'A gentle handshake'] }
  ],
  12: [ // The C Major 5-Finger Position
    { q: 'In the C major 5-finger position, your thumb sits on…',
      a: ['C', 'Z', 'A jellybean', 'The doorknob'] },
    { q: 'The five notes covered are…',
      a: ['C, D, E, F, G', '1, banana, cat, blue, ouch', 'Hello, why, ok, fine, oof', 'All the keys ever'] },
    { q: 'Each finger plays…',
      a: ['One key', 'Three keys at once', 'None — it\'s decorative', 'Whichever it feels like'] },
    { q: 'Why start with this position?',
      a: ['It\'s easy to learn 5 notes in a row', 'Pianos demand it', 'It pleases the moon', 'You earn a free croissant'] }
  ],
  13: [ // Reading the Treble Clef
    { q: 'The treble clef is used mostly for the…',
      a: ['Right hand / higher notes', 'Left ankle', 'Whispered notes', 'Notes from underwater'] },
    { q: 'The LINES of the treble clef spell out…',
      a: ['E, G, B, D, F', 'XYZ ABC', 'Old Mac Donald', 'Pi'] },
    { q: 'The SPACES of the treble clef spell out…',
      a: ['F, A, C, E', 'Lol omg', 'Goofy goose', 'Cheese cheese cheese'] },
    { q: 'The treble clef is also called the…',
      a: ['G clef', 'Mango clef', 'Squeaky clef', 'Mailbox clef'] }
  ],
  14: [ // Reading the Bass Clef
    { q: 'The bass clef is used mostly for the…',
      a: ['Left hand / lower notes', 'Right elbow', 'Notes from Mars', 'Echo notes'] },
    { q: 'The LINES of the bass clef spell out…',
      a: ['G, B, D, F, A', 'LOL OMG', 'Doo wop', 'Pizza pizza'] },
    { q: 'The SPACES of the bass clef spell out…',
      a: ['A, C, E, G', 'Whoa, nope, why, fine', 'Beep boop bop', 'Mmm mmm mmm mmm'] },
    { q: 'The bass clef is also called the…',
      a: ['F clef', 'Walrus clef', 'Hidden clef', 'Tiny pirate clef'] }
  ],
  15: [ // Basics Piano Checkpoint
    { q: 'In 4/4 time, a quarter note gets how many beats?',
      a: ['1', 'π', 'Negative two', 'As many as it pleases'] },
    { q: 'Which fingers are numbered 1 on each hand?',
      a: ['Both thumbs', 'Both pinkies', 'Both noses', 'Neither — fingers reject numbers'] },
    { q: 'The 5-finger C major position covers which notes?',
      a: ['C–D–E–F–G', 'A–E–I–O–U', 'Tic, tac, toe, foe, doe', 'Whatever the piano feels'] },
    { q: 'The treble clef wraps around which line?',
      a: ['The G line', 'The escape line', 'The discount line', 'The line for free samples'] }
  ]
};

// ─────────────────────────────────────────────────────────────────────────
// SONG-LESSON BANK (positions 1–15 inside every song unit)
// Each function receives the song name so it can be quoted in the prompt.
// ─────────────────────────────────────────────────────────────────────────
function q(text, ans) { return { q: text, a: ans }; }

export const SONG = {
  1: (s) => [ // Listen
    q(`Before playing "${s}", what should you do?`,
      ['Listen to the full melody first', 'Whisper the lyrics to a houseplant', 'Replace your piano with a kazoo', 'Hide under the bench until safe']),
    q('Why is listening before playing helpful?',
      ['It builds a feel for the rhythm and shape', 'Pianos demand a polite warning', 'It scares away passing ghosts', 'It unlocks the secret bonus level']),
    q(`While listening to "${s}", you mainly use which sense?`,
      ['Hearing', 'Smell of fresh laundry', 'Taste of middle C', 'Touch with your elbows']),
    q('Active listening helps you identify the song\'s…',
      ['Melody and rhythm', 'Hidden microwave timer', 'The pianist\'s breakfast', 'Sea creatures inside the keys'])
  ],
  2: (s) => [ // Play First Note
    q(`What\'s the goal of the "Play First Note" lesson for "${s}"?`,
      ['Find and play the very first note of the song', 'Recite the alphabet backwards', 'Sneeze in 4/4 time', 'Compliment the piano on its hair']),
    q('Before pressing a key, you should…',
      ['Know which finger and which key', 'Apologize to the bench', 'Check the moon phase', 'Take a small bow to the floor lamp']),
    q('How should the very first note sound?',
      ['Clear and confident', 'Like a startled chicken', 'Like a sock in the dryer', 'Like a haunted refrigerator']),
    q('If you miss the first note, what do you do?',
      ['Stop, breathe, and try again', 'Run from the room', 'Sell the piano immediately', 'Write a strongly worded letter to physics'])
  ],
  3: (s) => [ // First Two Notes
    q(`In the "First Two Notes" lesson for "${s}", you focus on…`,
      ['The first two notes in the correct order', 'Knitting a tiny sweater', 'Counting your toes', 'Composing a haiku about cheese']),
    q('Between two notes, your finger should…',
      ['Move smoothly to the next key', 'Teleport', 'File a complaint', 'Take a 10-minute nap']),
    q('The space between two notes is called…',
      ['An interval', 'A snack', 'A nap', 'A small bureaucratic delay']),
    q('If the second note is wrong, the fix is…',
      ['Slow down and check your finger', 'Yell at the sheet music', 'Eat a banana', 'Pretend it was on purpose'])
  ],
  4: (s) => [ // Read Phrase 1
    q(`"Read Phrase 1" for "${s}" means…`,
      ['Reading the first musical phrase on the staff', 'Speaking to the piano in cursive', 'Squinting at clouds', 'Reading a phrase from any cookbook']),
    q('A musical "phrase" is like a…',
      ['Sentence in music', 'Tiny boat', 'Politely rude noise', 'Secret handshake']),
    q('When reading a phrase, you should…',
      ['Look at the notes and the rhythm together', 'Stare deeply into the bench', 'Whisper to your shoes', 'Make eye contact with the metronome']),
    q('Reading before playing helps you…',
      ['Avoid surprises and play with intention', 'Beat the piano in a thumb war', 'Win a small trophy', 'Communicate with dolphins'])
  ],
  5: (s) => [ // Play Phrase 1
    q(`"Play Phrase 1" of "${s}" comes AFTER which lesson?`,
      ['Read Phrase 1', 'Eat Phrase 1', 'Sing Phrase 1 backwards', 'Bury Phrase 1 in the yard']),
    q('When playing your first phrase, keep the…',
      ['Rhythm steady', 'Volume on the toaster low', 'Curtains drawn shut', 'Goldfish entertained']),
    q('If you stumble in the middle, the best move is to…',
      ['Pause, go back a beat, and continue', 'Start the entire piece over forever', 'Pretend it\'s a remix', 'Cry into the keys']),
    q('After playing a phrase, you should…',
      ['Notice what went well and what needs work', 'Demand a standing ovation', 'Write a memoir', 'Sell tickets for the next attempt'])
  ],
  6: (s) => [ // Rhythm
    q(`The "Rhythm" lesson for "${s}" focuses on…`,
      ['Timing each note correctly', 'How your shoes squeak', 'Tax-deductible expenses', 'Synchronized eyebrow lifts']),
    q('A metronome is a tool that…',
      ['Keeps a steady tempo for you', 'Communicates with bees', 'Predicts the weather', 'Tells you when pizza arrives']),
    q('"Tempo" in music means…',
      ['Speed', 'A small temple', 'A type of bean', 'A polite cousin']),
    q('Tapping your foot helps you…',
      ['Feel the pulse of the music', 'Win a foot tapping contest', 'Charge your phone wirelessly', 'Predict tomorrow\'s lottery numbers'])
  ],
  7: (s) => [ // Read Phrase 2
    q(`"Read Phrase 2" of "${s}" is…`,
      ['The second musical phrase on the staff', 'The first phrase reading you backwards', 'A bedtime story', 'The piano\'s autobiography']),
    q('Most songs use phrases that are…',
      ['Connected but distinct', 'All identical', 'Mostly invisible', 'Translated from goose']),
    q('When you read a new phrase, compare it to…',
      ['Phrase 1 — note what\'s the same or different', 'The price of avocados', 'Last year\'s tax forms', 'A mildly confused walrus']),
    q('Reading two phrases in a row helps you…',
      ['Build the song in your mind before playing', 'Earn frequent flyer miles', 'Win an argument with gravity', 'Annoy nearby raccoons'])
  ],
  8: (s) => [ // Play Phrase 2
    q(`Playing the second phrase of "${s}" works best when…`,
      ['You already know phrase 1 well', 'You shut your eyes the whole time', 'You play with mittens on', 'You hum the theme to a different song']),
    q('If phrase 2 starts on a different note than phrase 1, you should…',
      ['Adjust your finger position', 'Restart your life', 'Hide the metronome', 'Whisper "why" to the piano']),
    q('Connecting two phrases smoothly is called…',
      ['Phrasing', 'Flossing', 'Filing', 'Fluffing']),
    q('Before moving on, make sure phrase 2 is…',
      ['Confident and in time', 'Played upside down', 'Encrypted', 'Mailed to a friend'])
  ],
  9: (s) => [ // Combine 1 & 2
    q(`When you combine phrase 1 and 2 of "${s}", focus on…`,
      ['Connecting them with steady rhythm', 'Adding a kazoo solo', 'Yelling between phrases', 'Skipping every other note']),
    q('The "seam" between two phrases is where…',
      ['You\'re most likely to lose tempo', 'The piano stores secret snacks', 'Birds gather to gossip', 'Time briefly stops']),
    q('To smooth two phrases together, practice…',
      ['Just the last note of phrase 1 into phrase 2', 'A handstand', 'Speaking only in vowels', 'Petting your imaginary dog']),
    q('When phrases connect well, the song begins to…',
      ['Sound like a real song, not two fragments', 'Glow gently in the dark', 'Demand a salary', 'Vote in local elections'])
  ],
  10: (s) => [ // Final Phrase
    q(`The final phrase of "${s}" is special because…`,
      ['It often ends on the home note for a satisfying close', 'It vanishes if you blink', 'It only plays on Sundays', 'It includes a coupon']),
    q('A piece\'s last note often feels…',
      ['Resolved and grounded', 'Like a sneeze that escaped', 'Like a forgotten umbrella', 'Slightly insulted']),
    q('The very last note should be played…',
      ['Clearly and held for its full value', 'Then immediately denied', 'In Morse code', 'While doing a small dance']),
    q('Why end with confidence?',
      ['It tells the listener the song is over', 'It scares away nearby seagulls', 'It earns you a free croissant', 'It legally ends the song'])
  ],
  11: (s) => [ // Slow Tempo
    q(`Practicing "${s}" at slow tempo helps you…`,
      ['Lock in the correct notes and rhythm', 'Annoy your downstairs neighbor', 'Reach Nirvana', 'Communicate with snails']),
    q('You should only speed up after…',
      ['Slow tempo feels easy and accurate', 'Receiving permission from the moon', 'Filing form 1040-EZ', 'Doing 5 jumping jacks']),
    q('Slow practice is sometimes called…',
      ['Deliberate practice', 'Anti-practice', 'Sleep practice', 'Wet practice']),
    q('If a section is messy at slow tempo, you should…',
      ['Go even slower until it\'s clean', 'Skip it forever', 'Yell at it', 'Wrap it in foil'])
  ],
  12: (s) => [ // Speed Up
    q(`"Speed Up" for "${s}" means…`,
      ['Gradually increase tempo until you reach the target', 'Run while playing', 'Speak only in tongue twisters', 'Set the piano on a treadmill']),
    q('A good tool for speeding up gradually is…',
      ['A metronome bumped up a few BPM at a time', 'A magic wand', 'A polite shouting coach', 'A motivational squirrel']),
    q('If you make mistakes at the new tempo, you should…',
      ['Drop back to a slower BPM', 'Triple the tempo to confuse the song', 'Apologize to your hands', 'Eat a small snack and try again']),
    q('Why not jump straight to full speed?',
      ['Mistakes get baked in if you rush', 'The piano gets sleepy', 'It voids the warranty', 'The song refuses to play'])
  ],
  13: (s) => [ // Two Hands
    q(`Playing "${s}" with two hands means…`,
      ['Right hand and left hand together', 'Hands taking turns at lunch', 'Using both feet only', 'Two friends sharing one hand']),
    q('To learn hands together, first…',
      ['Master each hand separately', 'Use both feet', 'Memorize the dictionary', 'Win a staring contest with the piano']),
    q('When hands play together, listen for…',
      ['Both hands staying in time with each other', 'A small parade', 'The arrival of mail', 'A whispered conspiracy']),
    q('If your hands fall apart, you should…',
      ['Slow down and try a smaller section', 'Switch hands with a stranger', 'Tape them together', 'Negotiate with each one separately'])
  ],
  14: (s) => [ // Full Run
    q(`A "Full Run" of "${s}" means…`,
      ['Playing the entire song from start to end', 'Sprinting around the piano', 'Filing a complete tax return', 'Eating the entire pantry']),
    q('Before your full run, you should…',
      ['Warm up briefly and breathe', 'Eat a kilogram of jellybeans', 'Re-organize your sock drawer', 'Apologize to the metronome']),
    q('If you make a mistake during a full run, you should…',
      ['Keep going — fix it on the next pass', 'Restart your life', 'Refund the song', 'Hide under a blanket']),
    q('A successful full run should feel…',
      ['Steady and musical from start to finish', 'Like falling down stairs', 'Like a small business meeting', 'Like wearing the wrong shoes'])
  ],
  15: (s) => [ // Checkpoint
    q(`The "${s}" Checkpoint is mainly for…`,
      ['Confirming you can play the song confidently', 'Stamping your hand', 'Receiving a small fish', 'Whispering goodbye to phrase 1']),
    q('If you don\'t feel ready, you should…',
      ['Replay earlier lessons until it\'s solid', 'Skip ahead anyway', 'Sell the piano', 'Compose a sad poem']),
    q('A "checkpoint" in Mathagram tracks…',
      ['Progress and earns you XP', 'Local weather', 'Pizza preferences', 'The number of clouds you\'ve seen']),
    q('After passing a song checkpoint, you can…',
      ['Move on to the next song', 'Demand a knighthood', 'Open a small business', 'Take the piano on vacation'])
  ]
};
