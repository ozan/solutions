#include <ctype.h>
#include <math.h>
#include <stdlib.h>

#define MAX_LENGTH 100

char *ciphertext(const char *input) {
  char ch, *sanitized = malloc(MAX_LENGTH), *out = malloc(MAX_LENGTH);
  int n = 0, c, r, i, j;

  // Sanitize the input by downcasing and removing non-alphanumeric characters,
  // and simultaneously determine the length of the input
  while ((ch = *input++) != '\0') {
    if (isupper(ch))
      ch = tolower(ch);
    if (isalnum(ch)) {
      *(sanitized + n) = ch;
      n++;
    }
  }

  // Find dimensions
  c = ceil(sqrt(n));
  r = ceil(n / (float)c);

  // Fill an additional row with spaces. Once transposed, these will appear
  // between chunks of the output.
  for (i = n; i < r * c + r; i++)
    sanitized[i] = ' ';

  // Perform the transpose
  for (i = 0; i < r + 1; i++)
    for (j = 0; j < c; j++)
      out[j * (r + 1) + i] = sanitized[i * c + j];

  out[(r + 1) * c - 1] = '\0';
  return out;
}
