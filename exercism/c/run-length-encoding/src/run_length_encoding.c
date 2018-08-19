#include <stdio.h>
#include <stdlib.h>

int MAX_LENGTH = 128;

/* Encode e.g. AAAB -> 3AB */
char *encode(char *in) {
  char ch, count = 1, i = 0, *out = malloc(MAX_LENGTH);
  while ((ch = *in++) != '\0') {
    if (ch != *in) { // encode a single run when next char is different
      if (count > 1)
        i += sprintf(out + i, "%d", count); // for runs > 1, include count
      *(out + i++) = ch;
      count = 0;
    }
    count++;
  }
  *(out + i) = '\0';
  return out;
}

/* Decode e.g. 3AB -> AAAB */
char *decode(char *s) {
  char ch, count = 0, i = 0, *out = malloc(MAX_LENGTH);
  while ((ch = *s++) != '\0') {
    if ('0' <= ch && ch <= '9') {
      count = count * 10 + (ch - '0');
      continue;
    }
    if (count == 0)
      count = 1;
    do
      *(out + i++) = ch;
    while (--count); // write `count` many instances of char to string
  }
  *(out + i) = '\0';
  return out;
}
