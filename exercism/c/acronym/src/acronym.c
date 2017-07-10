#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* abbreviate(char* phrase) {
  char ch, prior = ' ', *out = (char*) malloc(strlen(phrase) + 1), *oi = out;
  while ((ch = *phrase++) != '\0') {
    if (prior == ' ' || prior == '-') {
      if (ch > 'Z') ch -= 32;
      *oi++ = ch;
    }
    prior = ch;
  }
  *oi = '\0';
  return out;
}
