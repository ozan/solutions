/*
Write a function escape(s, t) that converts characters like newline and tab into
visible escape sequences like \n and \t as it copies the string t to s. Use a
switch. Write a function for the other direction as well, converting escape
sequences into the real characters.
*/

#include <assert.h>
#include <string.h>

#define MAX_STR 100

void escape(char *s, char *t) {
  char c;
  while ((c = *s++)) {
    switch (c) {
    case '\t':
      *t++ = '\\';
      *t++ = 't';
      break;
    case '\n':
      *t++ = '\\';
      *t++ = 'n';
      break;
    default:
      *t++ = c;
    }
  }
  *t = '\0';
}

void unescape(char *s, char *t) {
  char c, p = '\0';
  while ((c = *s++)) {
    if (p == '\\' && c == 'n') {
      *(t - 1) = '\n';
    } else if (p == '\\' && c == 't') {
      *(t - 1) = '\t';
    } else {
      *t++ = c;
    }
    p = c;
  }
  *t = '\0';
}

int main() {
  char buf[MAX_STR], *from = "foto\tbar\nbaz", *to = "foto\\tbar\\nbaz";

  escape(from, buf);
  assert(strcmp(buf, to) == 0);

  unescape(to, buf);
  assert(strcmp(buf, from) == 0);

  return 0;
}
