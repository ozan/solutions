#include <ctype.h>
#include <stdio.h>

int getfloat(float *pn, FILE *stream) {
  int c, sign;
  float power;

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
    *pn = 10.0 * *pn + (c - '0');
  if (c == '.')
    c = getc(stream);
  for (power = 1.0; isdigit(c); c = getc(stream)) {
    *pn = 10.0 * *pn + (c - '0');
    power *= 10.0;
  }
  *pn /= power;
  *pn *= sign;
  if (c != EOF)
    ungetc(c, stream);
  return c;
}

int main() {
  float n;
  int ret;
  while (1) {
    ret = getfloat(&n, stdin);
    printf("ret: %d, n: %f\n", ret, n);
  }
}
