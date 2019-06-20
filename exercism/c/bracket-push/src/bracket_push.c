#include "bracket_push.h"

const char *match =
    "........................................X(................................"
    ".................X.[.............................X.{..";

bool is_paired(const char *input) {
  char stack[100], x;
  int c, n = 0;

  while ((c = *input++)) {
    switch (x = match[c]) {
    case '.':
      continue;
    case 'X':
      stack[n++] = c;
      continue;
    default:
      if (n == 0 || stack[n - 1] != x)
        return false;
      n--;
    }
  }
  return n == 0;
}
