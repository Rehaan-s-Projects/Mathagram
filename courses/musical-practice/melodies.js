// Musical Practice — melody data for the song units.
//
// Each entry is a list of notes in melodic order. A note is:
//   { p: 'C4', d: 1 }   ← pitch + duration in beats (1 = quarter, 2 = half, 0.5 = eighth)
//   { rest: true, d: 1 } ← a beat of rest (no pitch played)
//
// For songs we don't have melody data for, practice.html falls back to
// DEFAULT_MELODY (C major up & back down). 30+ well-known songs are
// transcribed below so the practice flow gets real melodies on the songs
// most beginners actually want to play first.

export const DEFAULT_MELODY = [
  { p: 'C4', d: 1 }, { p: 'D4', d: 1 }, { p: 'E4', d: 1 }, { p: 'F4', d: 1 },
  { p: 'G4', d: 1 }, { p: 'F4', d: 1 }, { p: 'E4', d: 1 }, { p: 'D4', d: 1 },
  { p: 'C4', d: 2 }
];

export const MELODIES = {
  "Twinkle, Twinkle, Little Star": [
    { p:'C4',d:1 },{ p:'C4',d:1 },{ p:'G4',d:1 },{ p:'G4',d:1 },
    { p:'A4',d:1 },{ p:'A4',d:1 },{ p:'G4',d:2 },
    { p:'F4',d:1 },{ p:'F4',d:1 },{ p:'E4',d:1 },{ p:'E4',d:1 },
    { p:'D4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 }
  ],
  "Mary Had a Little Lamb": [
    { p:'E4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:1 },{ p:'D4',d:1 },
    { p:'E4',d:1 },{ p:'E4',d:1 },{ p:'E4',d:2 },
    { p:'D4',d:1 },{ p:'D4',d:1 },{ p:'D4',d:2 },
    { p:'E4',d:1 },{ p:'G4',d:1 },{ p:'G4',d:2 }
  ],
  "Hot Cross Buns": [
    { p:'E4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 },
    { p:'E4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 },
    { p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'C4',d:0.5 },
    { p:'D4',d:0.5 },{ p:'D4',d:0.5 },{ p:'D4',d:0.5 },{ p:'D4',d:0.5 },
    { p:'E4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 }
  ],
  "Old MacDonald Had a Farm": [
    { p:'C4',d:1 },{ p:'C4',d:1 },{ p:'C4',d:1 },{ p:'G3',d:1 },
    { p:'A3',d:1 },{ p:'A3',d:1 },{ p:'G3',d:2 },
    { p:'E4',d:1 },{ p:'E4',d:1 },{ p:'D4',d:1 },{ p:'D4',d:1 },
    { p:'C4',d:2 },{ rest:true,d:1 }
  ],
  "Row, Row, Row Your Boat": [
    { p:'C4',d:1 },{ p:'C4',d:1 },{ p:'C4',d:0.75 },{ p:'D4',d:0.25 },{ p:'E4',d:1 },
    { p:'E4',d:0.75 },{ p:'D4',d:0.25 },{ p:'E4',d:0.5 },{ p:'F4',d:0.5 },{ p:'G4',d:2 },
    { p:'C5',d:0.5 },{ p:'C5',d:0.5 },{ p:'G4',d:0.5 },{ p:'G4',d:0.5 },
    { p:'E4',d:0.5 },{ p:'E4',d:0.5 },{ p:'C4',d:0.5 },{ p:'C4',d:0.5 }
  ],
  "London Bridge Is Falling Down": [
    { p:'G4',d:1.5 },{ p:'A4',d:0.5 },{ p:'G4',d:1 },{ p:'F4',d:1 },
    { p:'E4',d:1 },{ p:'F4',d:1 },{ p:'G4',d:2 },
    { p:'D4',d:1 },{ p:'E4',d:1 },{ p:'F4',d:2 },
    { p:'E4',d:1 },{ p:'F4',d:1 },{ p:'G4',d:2 }
  ],
  "Frère Jacques": [
    { p:'C4',d:1 },{ p:'D4',d:1 },{ p:'E4',d:1 },{ p:'C4',d:1 },
    { p:'C4',d:1 },{ p:'D4',d:1 },{ p:'E4',d:1 },{ p:'C4',d:1 },
    { p:'E4',d:1 },{ p:'F4',d:1 },{ p:'G4',d:2 },
    { p:'E4',d:1 },{ p:'F4',d:1 },{ p:'G4',d:2 }
  ],
  "Three Blind Mice": [
    { p:'E4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 },
    { p:'E4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 },
    { p:'G4',d:1 },{ p:'F4',d:0.5 },{ p:'F4',d:0.5 },{ p:'E4',d:2 }
  ],
  "Itsy Bitsy Spider": [
    { p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'D4',d:0.5 },{ p:'E4',d:0.5 },{ p:'E4',d:0.5 },
    { p:'E4',d:0.5 },{ p:'D4',d:0.5 },{ p:'C4',d:0.5 },{ p:'D4',d:0.5 },{ p:'E4',d:0.5 },{ p:'C4',d:0.5 }
  ],
  "The Wheels on the Bus": [
    { p:'C4',d:1 },{ p:'F4',d:1 },{ p:'F4',d:1 },{ p:'F4',d:1 },
    { p:'F4',d:1 },{ p:'A4',d:1 },{ p:'C5',d:2 },
    { p:'A4',d:1 },{ p:'F4',d:1 },{ p:'G4',d:1 },{ p:'G4',d:1 },
    { p:'C4',d:1 },{ p:'E4',d:1 },{ p:'F4',d:2 }
  ],
  "B-I-N-G-O": [
    { p:'C4',d:1 },{ p:'C4',d:1 },{ p:'G4',d:1 },{ p:'G4',d:1 },
    { p:'A4',d:1 },{ p:'A4',d:1 },{ p:'G4',d:2 },
    { p:'F4',d:0.5 },{ p:'F4',d:0.5 },{ p:'E4',d:1 },{ p:'D4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 }
  ],
  "ABC Song": [
    { p:'C4',d:1 },{ p:'C4',d:1 },{ p:'G4',d:1 },{ p:'G4',d:1 },
    { p:'A4',d:1 },{ p:'A4',d:1 },{ p:'G4',d:2 },
    { p:'F4',d:1 },{ p:'F4',d:1 },{ p:'E4',d:1 },{ p:'E4',d:1 },
    { p:'D4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 }
  ],
  "Yankee Doodle": [
    { p:'C4',d:1 },{ p:'C4',d:1 },{ p:'D4',d:1 },{ p:'E4',d:1 },
    { p:'C4',d:1 },{ p:'E4',d:1 },{ p:'D4',d:1 },{ p:'G3',d:1 },
    { p:'C4',d:1 },{ p:'C4',d:1 },{ p:'D4',d:1 },{ p:'E4',d:1 },
    { p:'C4',d:2 },{ p:'B3',d:1 },{ p:'C4',d:1 }
  ],
  "This Old Man": [
    { p:'G4',d:1 },{ p:'E4',d:1 },{ p:'G4',d:1 },{ p:'G4',d:1 },
    { p:'E4',d:1 },{ p:'G4',d:1 },{ p:'A4',d:1 },{ p:'G4',d:1 },
    { p:'F4',d:1 },{ p:'E4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:2 }
  ],
  "Pop Goes the Weasel": [
    { p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'D4',d:0.5 },{ p:'D4',d:0.5 },
    { p:'E4',d:0.5 },{ p:'G4',d:0.5 },{ p:'E4',d:1 },
    { p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'D4',d:0.5 },{ p:'D4',d:0.5 },
    { p:'E4',d:0.5 },{ p:'C4',d:0.5 },{ p:'G3',d:1 }
  ],
  "Jingle Bells": [
    { p:'E4',d:1 },{ p:'E4',d:1 },{ p:'E4',d:2 },
    { p:'E4',d:1 },{ p:'E4',d:1 },{ p:'E4',d:2 },
    { p:'E4',d:1 },{ p:'G4',d:1 },{ p:'C4',d:1.5 },{ p:'D4',d:0.5 },{ p:'E4',d:2 }
  ],
  "Silent Night": [
    { p:'G4',d:1.5 },{ p:'A4',d:0.5 },{ p:'G4',d:1 },{ p:'E4',d:2 },
    { p:'G4',d:1.5 },{ p:'A4',d:0.5 },{ p:'G4',d:1 },{ p:'E4',d:2 },
    { p:'D5',d:2 },{ p:'D5',d:1 },{ p:'B4',d:2 },
    { p:'C5',d:2 },{ p:'C5',d:1 },{ p:'G4',d:2 }
  ],
  "Deck the Halls": [
    { p:'F4',d:1 },{ p:'E4',d:1 },{ p:'D4',d:1 },{ p:'C4',d:1 },
    { p:'B3',d:1 },{ p:'C4',d:1 },{ p:'D4',d:1 },{ p:'B3',d:1 },
    { p:'C4',d:0.5 },{ p:'D4',d:0.5 },{ p:'E4',d:0.5 },{ p:'C4',d:0.5 },
    { p:'D4',d:0.5 },{ p:'E4',d:0.5 },{ p:'F4',d:0.5 },{ p:'D4',d:0.5 },
    { p:'E4',d:0.5 },{ p:'D4',d:0.5 },{ p:'C4',d:0.5 },{ p:'B3',d:0.5 },{ p:'A3',d:1 }
  ],
  "We Wish You a Merry Christmas": [
    { p:'C4',d:1 },{ p:'F4',d:1 },{ p:'F4',d:0.5 },{ p:'G4',d:0.5 },
    { p:'F4',d:0.5 },{ p:'E4',d:0.5 },{ p:'D4',d:1 },{ p:'D4',d:1 },
    { p:'D4',d:1 },{ p:'G4',d:1 },{ p:'G4',d:0.5 },{ p:'A4',d:0.5 },
    { p:'G4',d:0.5 },{ p:'F4',d:0.5 },{ p:'E4',d:1 },{ p:'C4',d:1 },{ p:'C4',d:1 }
  ],
  "Auld Lang Syne": [
    { p:'C4',d:0.75 },{ p:'F4',d:1.25 },{ p:'F4',d:0.5 },{ p:'F4',d:0.5 },
    { p:'A4',d:1 },{ p:'G4',d:0.5 },{ p:'F4',d:0.5 },{ p:'G4',d:1 },{ p:'A4',d:1 },
    { p:'F4',d:0.75 },{ p:'F4',d:0.25 },{ p:'A4',d:1 },{ p:'C5',d:1 },{ p:'D5',d:2 }
  ],
  "Ode to Joy — Beethoven": [
    { p:'E4',d:1 },{ p:'E4',d:1 },{ p:'F4',d:1 },{ p:'G4',d:1 },
    { p:'G4',d:1 },{ p:'F4',d:1 },{ p:'E4',d:1 },{ p:'D4',d:1 },
    { p:'C4',d:1 },{ p:'C4',d:1 },{ p:'D4',d:1 },{ p:'E4',d:1 },
    { p:'E4',d:1.5 },{ p:'D4',d:0.5 },{ p:'D4',d:2 }
  ],
  "Für Elise — Beethoven": [
    { p:'E5',d:0.5 },{ p:'D#5',d:0.5 },{ p:'E5',d:0.5 },{ p:'D#5',d:0.5 },
    { p:'E5',d:0.5 },{ p:'B4',d:0.5 },{ p:'D5',d:0.5 },{ p:'C5',d:0.5 },
    { p:'A4',d:1 },{ p:'C4',d:0.5 },{ p:'E4',d:0.5 },{ p:'A4',d:0.5 },
    { p:'B4',d:1 },{ p:'E4',d:0.5 },{ p:'G#4',d:0.5 },{ p:'B4',d:0.5 },{ p:'C5',d:1 }
  ],
  "Minuet in G — Bach": [
    { p:'D5',d:1 },{ p:'G4',d:0.5 },{ p:'A4',d:0.5 },{ p:'B4',d:0.5 },{ p:'C5',d:0.5 },
    { p:'D5',d:1 },{ p:'G4',d:0.5 },{ p:'G4',d:0.5 },
    { p:'E5',d:1 },{ p:'C5',d:0.5 },{ p:'D5',d:0.5 },{ p:'E5',d:0.5 },{ p:'F#5',d:0.5 },
    { p:'G5',d:1 },{ p:'G4',d:0.5 },{ p:'G4',d:0.5 }
  ],
  "Canon in D — Pachelbel": [
    { p:'F#5',d:2 },{ p:'E5',d:2 },{ p:'D5',d:2 },{ p:'C#5',d:2 },
    { p:'B4',d:2 },{ p:'A4',d:2 },{ p:'B4',d:2 },{ p:'C#5',d:2 }
  ],
  "Eine kleine Nachtmusik — Mozart": [
    { p:'G4',d:1 },{ p:'D5',d:1 },{ p:'G4',d:0.5 },{ p:'D5',d:0.5 },{ p:'G4',d:1 },
    { p:'B4',d:0.5 },{ p:'A4',d:0.5 },{ p:'G4',d:0.5 },{ p:'A4',d:0.5 },
    { p:'B4',d:0.5 },{ p:'C5',d:0.5 },{ p:'D5',d:1 }
  ],
  // Linus and Lucy — the iconic Vince Guaraldi Peanuts theme. Transposed
  // from Ab major into C major so it plays on the white keys, but with
  // the song's real rhythm preserved: syncopated bass-ostinato bouncing
  // intro, held WHOLE notes on the right-hand melodic peaks, fast
  // eighth-note jazz licks, and a long held resolution at the end.
  // Duration units: 0.5 = eighth, 1 = quarter, 2 = half, 4 = whole.
  "Linus and Lucy — Charlie Brown Theme (Vince Guaraldi)": [
    // ── Intro: bouncing bass ostinato with mixed durations ──
    { p:'C3',d:1 },   { p:'C3',d:0.5 },{ p:'G3',d:0.5 },
    { p:'D4',d:1 },   { p:'F4',d:1 },
    { p:'D4',d:0.5 },{ p:'F4',d:0.5 },{ p:'G3',d:0.5 },{ p:'D4',d:0.5 },
    { p:'C3',d:2 },                                         // half-note bass landing
    // ── Right-hand theme A: a HELD high note, then a quick lick ──
    { p:'G4',d:4 },                                         // WHOLE NOTE (held)
    { p:'A4',d:0.5 },{ p:'G4',d:0.5 },{ p:'F4',d:0.5 },{ p:'D4',d:0.5 },
    { p:'F4',d:2 },                                         // half note
    // ── Descending jazz figure ──
    { p:'A4',d:1 },   { p:'G4',d:0.5 },{ p:'F4',d:0.5 },
    { p:'D4',d:0.5 },{ p:'C4',d:0.5 },{ p:'D4',d:2 },       // half note
    // ── Rising response — peaks on a HELD high C ──
    { p:'E4',d:0.5 },{ p:'G4',d:0.5 },{ p:'A4',d:1 },
    { p:'C5',d:4 },                                         // WHOLE NOTE peak
    { p:'A4',d:0.5 },{ p:'G4',d:0.5 },{ p:'E4',d:1 },
    { p:'G4',d:1 },
    // ── Closing — long held home note ──
    { p:'C4',d:4 }                                          // WHOLE NOTE resolution
  ],
  "Happy Birthday to You": [
    { p:'C4',d:0.75 },{ p:'C4',d:0.25 },{ p:'D4',d:1 },{ p:'C4',d:1 },{ p:'F4',d:1 },{ p:'E4',d:2 },
    { p:'C4',d:0.75 },{ p:'C4',d:0.25 },{ p:'D4',d:1 },{ p:'C4',d:1 },{ p:'G4',d:1 },{ p:'F4',d:2 },
    { p:'C4',d:0.75 },{ p:'C4',d:0.25 },{ p:'C5',d:1 },{ p:'A4',d:1 },{ p:'F4',d:1 },{ p:'E4',d:1 },{ p:'D4',d:2 }
  ],
  "Amazing Grace": [
    { p:'D4',d:1 },{ p:'G4',d:2 },{ p:'B4',d:0.5 },{ p:'G4',d:0.5 },{ p:'B4',d:1 },{ p:'A4',d:1 },
    { p:'G4',d:1 },{ p:'E4',d:1 },{ p:'D4',d:2 },
    { p:'D4',d:1 },{ p:'G4',d:2 },{ p:'B4',d:0.5 },{ p:'G4',d:0.5 },{ p:'B4',d:1 },{ p:'A4',d:1 },
    { p:'D5',d:3 }
  ],
  "Greensleeves": [
    { p:'A4',d:1 },{ p:'C5',d:2 },{ p:'D5',d:1 },{ p:'E5',d:1.5 },{ p:'F5',d:0.5 },
    { p:'E5',d:1 },{ p:'D5',d:2 },{ p:'B4',d:1 },{ p:'G4',d:1.5 },{ p:'A4',d:0.5 },
    { p:'B4',d:1 },{ p:'C5',d:2 },{ p:'A4',d:3 }
  ],
  "Star-Spangled Banner": [
    { p:'G4',d:1.5 },{ p:'E4',d:0.5 },{ p:'C4',d:1 },{ p:'E4',d:1 },{ p:'G4',d:1 },{ p:'C5',d:2 },
    { p:'E5',d:1.5 },{ p:'D5',d:0.5 },{ p:'C5',d:1 },{ p:'E4',d:1 },{ p:'F#4',d:1 },{ p:'G4',d:2 }
  ],
  "La Cucaracha — Traditional": [
    { p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'F4',d:1 },{ p:'A4',d:1 },
    { p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'F4',d:1 },{ p:'A4',d:1 },
    { p:'F4',d:0.5 },{ p:'F4',d:0.5 },{ p:'E4',d:0.5 },{ p:'E4',d:0.5 },{ p:'D4',d:0.5 },{ p:'D4',d:0.5 },{ p:'C4',d:1 }
  ],
  "Finger Family — Daddy Finger": [
    // Verse: "Daddy finger, daddy finger, where are you?"
    { p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'E4',d:0.5 },{ p:'E4',d:0.5 },
    { p:'C4',d:0.5 },{ p:'C4',d:0.5 },{ p:'E4',d:0.5 },{ p:'E4',d:0.5 },
    { p:'G4',d:0.5 },{ p:'G4',d:0.5 },{ p:'E4',d:1 },
    // "Here I am, here I am."
    { p:'F4',d:0.5 },{ p:'F4',d:0.5 },{ p:'D4',d:1 },
    { p:'F4',d:0.5 },{ p:'F4',d:0.5 },{ p:'D4',d:1 },
    // "How do you do?"
    { p:'G4',d:0.5 },{ p:'F4',d:0.5 },{ p:'E4',d:0.5 },{ p:'D4',d:0.5 },{ p:'C4',d:2 }
  ],
  "Cielito Lindo — Traditional": [
    { p:'G4',d:1 },{ p:'A4',d:1 },{ p:'B4',d:1 },{ p:'C5',d:2 },
    { p:'B4',d:1 },{ p:'A4',d:1 },{ p:'G4',d:2 },
    { p:'C5',d:1 },{ p:'B4',d:1 },{ p:'A4',d:1 },{ p:'G4',d:2 }
  ],
  "Vivir Mi Vida — Marc Anthony": [
    // Chorus hook (transposed into C/Am for the C3–C5 keyboard).
    // "Voy a re-ír"
    { p:'G4',d:0.5 },{ p:'G4',d:0.5 },{ p:'C5',d:1 },
    // "Voy a bai-lar"
    { p:'G4',d:0.5 },{ p:'G4',d:0.5 },{ p:'D5',d:1 },
    // "Vi-vir mi vi-da"
    { p:'C5',d:0.5 },{ p:'D5',d:0.5 },{ p:'C5',d:0.5 },{ p:'B4',d:0.5 },{ p:'G4',d:1 },
    // "la la la la"
    { p:'A4',d:0.5 },{ p:'G4',d:0.5 },{ p:'F4',d:0.5 },{ p:'E4',d:0.5 },
    // "Vi-vir mi vi-da"
    { p:'C5',d:0.5 },{ p:'D5',d:0.5 },{ p:'C5',d:0.5 },{ p:'B4',d:0.5 },{ p:'G4',d:1 },
    // "la la la la" (descending tag, resolving to tonic)
    { p:'A4',d:0.5 },{ p:'G4',d:0.5 },{ p:'E4',d:0.5 },{ p:'C4',d:1 }
  ]
};

// Returns the slice of a melody to use for a given lesson position (1–6).
// Each song unit teaches a DIFFERENT skill (no two lessons feel the same):
//   1 Listen           → hear the melody (auto-play)
//   2 Rhythm Tap       → tap ANY key in time with each note (pitch ignored)
//   3 First Phrase     → play just the first half (pitch + rhythm)
//   4 Second Phrase    → play just the second half
//   5 Read the Staff   → sight-read the whole song — NO key glow to help you
//   6 Performance      → full song with key hints — your recital take
export function lessonSlice(melody, lesson) {
  const half = Math.max(1, Math.ceil(melody.length / 2));
  switch (lesson) {
    case 1:  return { notes: melody,                  mode: 'listen' };
    case 2:  return { notes: melody,                  mode: 'rhythm' };
    case 3:  return { notes: melody.slice(0, half),   mode: 'play' };
    case 4:  return { notes: melody.slice(half),      mode: 'play' };
    case 5:  return { notes: melody,                  mode: 'sight-read' };
    case 6:  return { notes: melody,                  mode: 'play' };
    default: return { notes: melody,                  mode: 'play' };
  }
}

// Lookup helper. If the song has a transcription, return it; otherwise the
// default 5-finger C major exercise.
export function getMelody(songName) {
  return MELODIES[songName] || DEFAULT_MELODY;
}
