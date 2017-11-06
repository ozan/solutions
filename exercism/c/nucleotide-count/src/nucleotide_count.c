#include <stdio.h>
#include <stdlib.h>

#include "nucleotide_count.h"

char *count(const char *strand) {
  int a = 0, c = 0, g = 0, t = 0;
  char ch, *result = malloc(30);

  while ((ch = *strand++) != '\0') {
    switch (ch) {
    case 'A':
      a += 1;
      break;
    case 'C':
      c += 1;
      break;
    case 'G':
      g += 1;
      break;
    case 'T':
      t += 1;
      break;
    default:
      result[0] = '\0';
      return result;
    }
  }
  sprintf(result, "A:%d C:%d G:%d T:%d", a, c, g, t);
  return result;
}
