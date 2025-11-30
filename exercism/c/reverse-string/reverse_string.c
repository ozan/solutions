#include "reverse_string.h"

#include <stdio.h>
#include <stdlib.h>

char *reverse(const char *str) {
  int n = 0;

  while (*str++)
    n += 1;

  char *out = (char *)malloc(n + 1);
  if (out == NULL)
    return NULL;

  str--;
  for (int i = 0; i < n; i++)
    out[i] = *--str;

  out[n] = '\0';
  return out;
}
