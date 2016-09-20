#include "pangram.h"
#include <ctype.h>
#include <stdlib.h>

int is_pangram(const char *sentence) {
  char c;
  unsigned int flags = 0;

  if (sentence == NULL)
    return 0;

  while ((c = tolower(*sentence++)) != '\0') {
    if (c < 'a' || c > 'z')
      continue;
    flags |= 1 << (c - 'a');
  }
  return flags == (1 << 26) - 1;
}
