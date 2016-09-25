/*
In a two's complement number representation, our version of itoa does not handle
the largest negative number. Explain why not. Modify it to print that value
correctly, regardless of the machine on which it runs.
*/

#include <stdlib.h>

void itoa(int n, char s[]) {
  int i, neg = n < 0;

  i = 0;
  do {
    s[i++] = abs(n % 10) + '0';
  } while (n /= 10);
  if (neg)
    s[i++] = '-';

  s[i] = '\0';
  reverse(s);
}
