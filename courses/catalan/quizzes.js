// Catalan — Unit 1 "Alphabet & Pronunciation" quiz bank.
//
// Keyed by lesson number within Unit 1 (1–25). Lessons 1–5 already have full
// interactive lesson pages, so this bank covers 6–25. Each lesson holds 4
// multiple-choice questions. The FIRST entry in each answer array is the
// correct answer; quiz.html shuffles the options at render time so the
// student doesn't just memorize position.
//
// Distractors are Duolingo-absurd by design — never plausible near-misses —
// per the Mathagram quiz style.

function q(text, ans) { return { q: text, a: ans }; }

export const UNIT1 = {
  6: [ // The NY & LL Sounds
    q('In Catalan, "NY" sounds most like…',
      ['Spanish Ñ — the "ny" in "canyon"', 'A microwave humming jazz', 'Two coconuts arguing', 'A polite scream from a sock']),
    q('The Catalan word "any" means…',
      ['Year', 'A small bureaucratic stamp', 'A pajama with regrets', 'Three confused ducks']),
    q('Catalan "LL" is pronounced as…',
      ['A palatal "ly" — like Italian "gli"', 'A jellyfish ringtone', 'The smell of fresh bookshelves', 'A spider doing taxes']),
    q('Which Catalan word means "moon"?',
      ['Lluna', 'Spaghetti', 'A polite gust of wind', 'Wet socks of destiny'])
  ],
  7: [ // TX, IG, & TJ Sounds
    q('Catalan "TX" sounds most like…',
      ['English "ch" in "chair"', 'A trombone sneezing', 'The Wi-Fi password whispered backwards', 'A startled lampshade']),
    q('The "IG" at the END of a Catalan word sounds like…',
      ['English "tch" — same as TX', 'A polite refusal', 'A turtle filing taxes', 'Whispered confetti']),
    q('Catalan "TJ" makes the sound of…',
      ['English "j" in "jam" or French "j" in "joue"', 'A snoring fridge', 'A spider giving directions', 'A trombone learning Spanish']),
    q('Which word demonstrates the TX sound?',
      ['Cotxe (car)', 'Octopus on Tuesday', 'A small confused walrus', 'Pancakes filing complaints'])
  ],
  8: [ // Silent H & Other Silent Letters
    q('The letter "H" in Catalan is…',
      ['Always silent', 'Pronounced like a vacuum', 'Optional on Sundays', 'A polite suggestion']),
    q('The word "hola" in Catalan begins with a sound that is…',
      ['Just the vowel — H is silent', 'A small explosion', 'Three trumpets in agreement', 'A gentle door slam']),
    q('A "silent" letter is one that…',
      ['Is written but not pronounced', 'Apologizes for its presence', 'Glows when nobody looks', 'Charges by the hour']),
    q('Which Catalan letter is silent like H?',
      ['The "r" at the end of most infinitives (parlar, menjar)', 'The cucumber', 'The hidden Wi-Fi password', 'The 17th alphabet'])
  ],
  9: [ // Stress Rules & Accents
    q('In Catalan, an accent mark on a vowel usually indicates…',
      ['Where the word is stressed', 'How sad the vowel is', 'How many cousins it has', 'A discount of 20%']),
    q('The acute accent (´) over a vowel signals…',
      ['A closed vowel', 'The vowel\'s favorite color', 'A polite cough', 'An emergency exit']),
    q('The grave accent (`) over a vowel signals…',
      ['An open vowel', 'A small confused goose', 'A coupon code', 'Cold pizza']),
    q('Words ending in a vowel, n, or s usually stress the…',
      ['Second-to-last syllable', 'Last consonant\'s elbow', 'Mood of the speaker', 'Phase of the moon'])
  ],
  10: [ // Pronunciation of B/V
    q('In most Catalan-speaking regions, B and V are pronounced…',
      ['The same way (a /b/ or /β/ sound)', 'In Morse code', 'With a polite sneeze', 'Only on Wednesdays']),
    q('Some Catalan dialects DO distinguish B and V — including…',
      ['Valencian and Balearic', 'Pirates and submarines', 'Cooks and electricians', 'Cats with hats']),
    q('A "betacisme" is the linguistic term for…',
      ['Pronouncing V like B', 'A small Mediterranean bird', 'A polite typo', 'Pretending to know Spanish']),
    q('Which word demonstrates the B/V merger in Central Catalan?',
      ['"Vi" (wine) — sounds like "bi"', 'Spaghetti on Sunday', 'A startled umbrella', 'The number that doesn\'t exist'])
  ],
  11: [ // Liaison & Elision
    q('Elision in Catalan typically removes…',
      ['A vowel before another vowel — "l\'home" instead of "la home"', 'A vowel\'s self-esteem', 'A vowel\'s tax return', 'A vowel\'s social media account']),
    q('Catalan articles like "el" and "la" become "l\'" when…',
      ['The next word starts with a vowel', 'It rains on a Tuesday', 'Pizza is mentioned', 'The vowel files an appeal']),
    q('"Liaison" means linking words by…',
      ['Carrying sounds between them in speech', 'Whispering in 5/4 time', 'Folding the words into origami', 'Renting them by the hour']),
    q('Which is properly elided?',
      ['l\'amic (the friend)', 'la-amic (with a hug)', 'le amic (in French)', 'amic-of-the-vowel'])
  ],
  12: [ // Eastern vs Western Pronunciation
    q('Eastern Catalan (Barcelona, Girona) reduces unstressed A and E to…',
      ['A schwa /ə/ sound', 'A small accordion', 'A polite "uh"', 'A startled gerbil']),
    q('Western Catalan (Lleida, Valencia) keeps unstressed vowels…',
      ['Clear and distinct', 'In a glass jar', 'On layaway', 'In a frozen pancake']),
    q('Which city is in the Eastern Catalan region?',
      ['Barcelona', 'Tokyo', 'A polite zip code', 'The inside of a thermos']),
    q('A speaker of Western Catalan would pronounce "casa" with…',
      ['A clear /a/ at the end', 'A small dance routine', 'A whispered "Hola" first', 'A side of fries'])
  ],
  13: [ // Catalan Diacritics — À, É, È, Í, Ò, Ó, Ú
    q('How many vowels in Catalan can carry a diacritic?',
      ['All five — A, E, I, O, U', 'Only consonants do that', 'Just one — and it\'s in hiding', 'Vowels refuse on principle']),
    q('"Í" is used to mark…',
      ['A stressed, closed I — usually on an unexpected syllable', 'A surprised I', 'An I that lost its key', 'An I with a side job']),
    q('Both é and è exist in Catalan because…',
      ['Catalan has both closed and open E sounds', 'One is just for show', 'They\'re different on holidays', 'They\'re a married couple']),
    q('Which word uses an accent to mark stress?',
      ['Música (music)', 'Pizza-uh', 'Whatever the wind decides', 'Octopus-é-le'])
  ],
  14: [ // Reading Catalan Aloud
    q('When reading Catalan aloud, the H is…',
      ['Always silent', 'A surprise sneeze', 'A signal to whisper', 'A polite request to stop']),
    q('Final "-r" in infinitives like "parlar" is often…',
      ['Silent in many dialects', 'Played on a tiny trumpet', 'A small cucumber', 'Shouted with great enthusiasm']),
    q('Reading practice should focus on…',
      ['Stress, vowel openness, and elision', 'Becoming a small thunderstorm', 'Yelling at the ceiling', 'Tasting each syllable']),
    q('A common mistake is pronouncing Catalan as if it were…',
      ['Spanish', 'Mongolian throat singing', 'A washing machine', 'Telegram messages from 1932'])
  ],
  15: [ // Numbers 1-20
    q('The Catalan word for "one" (masculine) is…',
      ['Un', 'Banana', 'Whispered air', 'Three confused snowmen']),
    q('"Cinc" means…',
      ['Five', 'A small comb', 'Tuesday\'s emotion', 'A wet button']),
    q('Which is the Catalan word for "ten"?',
      ['Deu', 'A polite balloon', 'A confused walrus', 'Half of pizza']),
    q('The Catalan word for "twenty" is…',
      ['Vint', 'A whispered code', 'Three socks', 'A small parade'])
  ],
  16: [ // Numbers 21-100
    q('"Trenta" means…',
      ['Thirty', 'A small umbrella', 'A startled raccoon', 'Almost-pizza']),
    q('Twenty-one in Catalan is…',
      ['Vint-i-un', 'Twenty-banana', 'The number that hides', 'Vingt-plus-one-please']),
    q('"Cinquanta" means…',
      ['Fifty', 'A noodle convention', 'Half a hat', 'The mood of a sock']),
    q('"Cent" means…',
      ['One hundred', 'A penny\'s cousin', 'The smell of clouds', 'A small monastery'])
  ],
  17: [ // Numbers 100-1000 & Beyond
    q('"Mil" in Catalan means…',
      ['One thousand', 'A small grain', 'Half of a comma', 'A polite shoe']),
    q('"Cinc-cents" means…',
      ['Five hundred', 'Five small wishes', 'Five pancakes', 'Five quiet socks']),
    q('How do you express 1,500 in Catalan?',
      ['Mil cinc-cents', 'Mil pancakes', 'Mil mostly', 'Mil under protest']),
    q('The word for "million" in Catalan is…',
      ['Milió', 'Bazillion-uh', 'Polite-billion', 'Whatever the moon decides'])
  ],
  18: [ // Ordinal Numbers
    q('"Primer" means…',
      ['First', 'Before-pizza', 'The angry one', 'The whispered hat']),
    q('"Segon" means…',
      ['Second', 'Half-a-banana', 'Tuesday\'s nephew', 'Polite-third']),
    q('"Tercer" means…',
      ['Third', 'A small fork', 'The mood of a doorbell', 'Three confused ducks']),
    q('Ordinals in Catalan agree with the noun in…',
      ['Gender and number', 'Weather forecast', 'Pizza topping', 'The number of cats nearby'])
  ],
  19: [ // Days, Months & Seasons
    q('The Catalan word for Monday is…',
      ['Dilluns', 'Mondayitis', 'A small armistice', 'The grumpy day']),
    q('"Diumenge" means…',
      ['Sunday', 'A polite Tuesday', 'Tomorrow\'s pancake', 'Nothing in particular']),
    q('"Gener" is the Catalan word for…',
      ['January', 'A small genie', 'The first sneeze of the year', 'A confused calendar']),
    q('"Primavera" means…',
      ['Spring', 'First-sock', 'A noodle festival', 'Almost-summer'])
  ],
  20: [ // Colors in Catalan
    q('"Vermell" means…',
      ['Red', 'A small worm of joy', 'Sunset on a hat', 'A blushing pancake']),
    q('"Blau" means…',
      ['Blue', 'A polite "boo"', 'Half a sigh', 'A whispered hat']),
    q('"Verd" means…',
      ['Green', 'A salad\'s opinion', 'A confused frog', 'The mood of envy on Tuesdays']),
    q('"Groc" means…',
      ['Yellow', 'A small angry duck', 'The sound of corn', 'A grumpy lemon'])
  ],
  21: [ // Telling Time
    q('Catalan has a unique system for telling time involving…',
      ['Quarters of the upcoming hour (un quart de, dos quarts de, tres quarts de)', 'Whispering to the clock', 'Polite negotiations with the moon', 'A small parade per minute']),
    q('"Són les dues" means…',
      ['It\'s two o\'clock', 'It is the duet', 'Two o\'clock is sad', 'Two ducks have arrived']),
    q('"Un quart de cinc" means…',
      ['4:15 — a quarter PAST 4 (one quarter of the way to 5)', 'A small dance at 5', 'A polite 4:00', 'Whatever the moon decides']),
    q('"Dos quarts de tres" means…',
      ['2:30 — halfway to 3', 'Two-and-a-half pancakes', 'A polite tea time', 'Three cats agreeing'])
  ],
  22: [ // Basic Spelling Rules
    q('Catalan often doubles the "L" with a middle dot — l·l — to indicate…',
      ['A long, geminated L sound', 'A small bowling ball', 'A polite hyphenated cousin', 'Two L\'s in love']),
    q('Final "-a" usually marks a noun as…',
      ['Feminine', 'Tuesday\'s emotion', 'Half-pizza', 'A polite sigh']),
    q('Catalan letter "Ç" appears before…',
      ['A, O, U — to keep the soft "s" sound', 'A small parade', 'A confused walrus', 'The mood of a sneeze']),
    q('The hard "g" of "gat" becomes soft before…',
      ['E or I', 'A small celebration', 'Tuesday and Sunday', 'A whispered apology'])
  ],
  23: [ // Apostrophe & Contractions
    q('The Catalan apostrophe is used to mark…',
      ['Elision — a dropped vowel', 'A small confused button', 'A polite gasp', 'Cucumber pricing']),
    q('"De" + "el" contracts to…',
      ['Del', 'Pizza-de', 'Whispered-an', 'Polite-of-the']),
    q('"A" + "el" contracts to…',
      ['Al', 'Cucumber', 'A small parade', 'Lunch-with-the-moon']),
    q('"L\'aigua" instead of "la aigua" shows…',
      ['Elision of the article before a vowel', 'A startled lake', 'A polite invitation', 'A small monastery'])
  ],
  24: [ // Practice: Pronunciation Drills
    q('A "tongue twister" in Catalan is called an…',
      ['Embarbussament', 'Embarrassment-uh', 'Spaghetti recitation', 'Polite scream of confusion']),
    q('Daily pronunciation drills help you…',
      ['Internalize sounds and rhythm', 'Win a small competition', 'Charge by the minute', 'Predict weather in Latin']),
    q('A great drill targets which Catalan-specific sound?',
      ['NY, LL, l·l, and schwa', 'Whispered consonants from Mars', 'Tax-deductible vowels', 'Pancakes on Tuesdays']),
    q('Recording yourself helps you…',
      ['Hear your real pronunciation and improve it', 'Charge your phone faster', 'Predict tomorrow\'s pizza', 'Communicate with sea otters'])
  ],
  25: [ // Alphabet & Pronunciation Checkpoint
    q('Catalan H is…',
      ['Always silent', 'A small explosion', 'A polite cough', 'A surprise inspection']),
    q('Eastern Catalan reduces unstressed A and E to…',
      ['Schwa /ə/', 'A small armistice', 'A startled cucumber', 'A polite handshake']),
    q('Catalan TX sounds like English…',
      ['Ch in "chair"', 'Th in Tuesday', 'A small trumpet sneezing', 'The mood of olive oil']),
    q('Catalan l·l represents…',
      ['A geminated long L', 'A polite double-take', 'Two L\'s having a chat', 'A tiny parade of L\'s'])
  ]
};
