/**
 * Input sanitization utilities for Mathagram.org
 */

/**
 * Escapes HTML entities to prevent XSS.
 * @param {string} str - Raw string to sanitize.
 * @returns {string} Sanitized string with HTML entities escaped.
 */
export function sanitizeHTML(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

/**
 * Sanitizes a fill-in-the-blank exercise answer.
 * Converts to string, trims whitespace, and limits length.
 * @param {*} input - The user's answer input.
 * @param {number} [maxLength=200] - Maximum allowed character length.
 * @returns {string} Cleaned answer string.
 */
export function sanitizeAnswer(input, maxLength = 200) {
  return String(input).trim().slice(0, maxLength);
}
