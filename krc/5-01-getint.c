#include <ctype.h>
#include <stdio.h>

int getint(int *pn, FILE *stream) {
  int c, sign;

  while (isspace(c = getc(stream)))
    ;
  if (!isdigit(c) && c != EOF && c != '+' && c != '-') {
    ungetc(c, stream);
    return 0;
  }
  sign = (c == '-') ? -1 : 1;
  if (c == '+' || c == '-')
    c = getc(stream);
  // '-' or '+' not followed by a digit is invalid
  if (!isdigit(c)) {
    ungetc(c, stream);
    return 0;
  }
  for (*pn = 0; isdigit(c); c = getc(stream))
    *pn = 10 * *pn + (c - '0');
  *pn *= sign;
  if (c != EOF)
    ungetc(c, stream);
  return c;
}

int main() {
  int n, ret;
  while (1) {
    ret = getint(&n, stdin);
    printf("ret: %d, n: %d\n", ret, n);
  }
}
