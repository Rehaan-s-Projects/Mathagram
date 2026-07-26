// Pure builders for the delimited HTML blocks injected into course pages.
export const META_START = '<!-- pin:meta:start -->';
export const META_END = '<!-- pin:meta:end -->';
export const PIN_START = '<!-- pin:media:start -->';
export const PIN_END = '<!-- pin:media:end -->';

const SITE = 'https://mathagram.org';
const OG_IMAGE = `${SITE}/assets/lighthouse/og-card.png`;

export function escapeAttr(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

export function buildMetaBlock(course) {
  const title = escapeAttr(`${course.title} — Mathagram`);
  const desc = escapeAttr(course.description);
  const url = escapeAttr(course.url);
  const lines = [
    META_START,
    `  <meta name="description" content="${desc}">`,
    `  <link rel="canonical" href="${url}">`,
    `  <meta property="og:type" content="article">`,
    `  <meta property="og:site_name" content="Mathagram">`,
    `  <meta property="og:title" content="${title}">`,
    `  <meta property="og:description" content="${desc}">`,
    `  <meta property="og:url" content="${url}">`,
    `  <meta property="og:image" content="${OG_IMAGE}">`,
    `  <meta property="og:image:width" content="1200">`,
    `  <meta property="og:image:height" content="630">`,
  ];
  if (course.category) {
    lines.push(`  <meta property="article:section" content="${escapeAttr(course.category)}">`);
  }
  lines.push(
    `  <meta name="twitter:card" content="summary_large_image">`,
    `  <meta name="twitter:title" content="${title}">`,
    `  <meta name="twitter:description" content="${desc}">`,
    `  <meta name="twitter:image" content="${OG_IMAGE}">`,
    META_END,
  );
  return lines.join('\n');
}

export function buildPinElement(course, pinPath) {
  const desc = escapeAttr(`${course.title} — free interactive lessons on Mathagram`);
  const src = escapeAttr(pinPath);
  const media = escapeAttr(`${SITE}${pinPath}`);
  return [
    PIN_START,
    `  <img src="${src}" alt="" width="1000" height="1500" style="display:none"`,
    `       data-pin-media="${media}" data-pin-description="${desc}">`,
    PIN_END,
  ].join('\n');
}
