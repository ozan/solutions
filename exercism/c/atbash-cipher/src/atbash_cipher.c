#include <ctype.h>
#include <stdlib.h>

char *atbash_encode(char *given) {
  int n = 0, i = 0;
  char ch, *encoded, *ep;

  while (given[n++] != '\0')
    ;
  encoded = ep = malloc(1.2 * n); // may have an extra space every 5 of input

  while ((ch = *given++) != '\0') {
    if (!isalnum(ch))
      continue;
    // add a space every 5
    if (i > 0 && i % 5 == 0)
      *ep++ = ' ';
    i++;
    // encode via cipher... 219 == 'a' + 'z'
    *ep++ = isdigit(ch) ? ch : (219 - tolower(ch));
  }

  *ep = '\0';
  return encoded;
}

char *atbash_decode(char *given) {
  int n = 0;
  char ch, *decoded, *dp;

  while (given[n++] != '\0')
    ;

  decoded = dp = malloc(n);

  while ((ch = *given++) != '\0') {
    if (ch == ' ')
      continue;
    // decode via cipher... 219 == 'a' + 'z'
    *dp++ = isdigit(ch) ? ch : (219 - ch);
  }

  *dp = '\0';
  return decoded;
}
