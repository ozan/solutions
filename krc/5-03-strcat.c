#include <assert.h>
#include <stdio.h>

void strcat_(char *s, char *t) {
  while (*++s)
    ;
  while ((*s++ = *t++))
    ;
}
