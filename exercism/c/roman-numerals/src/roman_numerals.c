#include <stdlib.h>

#include "roman_numerals.h"

int decimals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
char *romans[] = {"M",  "CM", "D",  "CD", "C",  "XC", "L",
                  "XL", "X",  "IX", "V",  "IV", "I"};

char *to_roman_numeral(int n) {
  char *converted = malloc(10), *cp = converted, *rp, c;
  int i = 0;

  while (n) {
    while (decimals[i] > n)
      i++;
    rp = romans[i];
    while ((c = *rp++) != '\0')
      *cp++ = c;
    n -= decimals[i];
  }
  *cp = '\0';
  return converted;
}
