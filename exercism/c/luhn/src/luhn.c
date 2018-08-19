#include "luhn.h"

#include <stdio.h>

static char map[] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};

bool luhn(char *s) {
  char d, *t = s, total = 0, even = 0, count = 0;

  // find end of input
  while (*++t != '\0')
    ;

  // consider digits, backwards
  while (t-- != s) {

    // spaces are ok...
    if (*t == ' ')
      continue;

    // ...but other characters are not
    d = *t - '0';
    if (d > 9)
      return false;

    // apply the main luhn property per digit
    total += even ? *(map + d) : d;
    even ^= 1;
    count++;
  }

  return count > 1 && total % 10 == 0;
}
