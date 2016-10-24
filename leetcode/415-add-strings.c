/*

Given two non-negative numbers num1 and num2 represented as string, return the
sum of num1 and num2

Plan:

copy pointers, initialize a counter
progress pointers to null byte, keeping count of maxlen
initialize that much + 2 in space for total string
starting from _end_ do schoolyard math (ie with a carry digit) until both starts
are reached
in each case, add digit to output string
finally reverse the output string
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverse(char *str, int len) {
  char tmp;
  for (int i = 0; i < len / 2; i++) {
    tmp = str[i];
    str[i] = str[len - i - 1];
    str[len - i - 1] = tmp;
  }
}

char *addStrings(char *num1, char *num2) {
  char *n1end = num1, *n2end = num2;
  int len = 0;

  while (*n1end || *n2end) {
    len++;
    if (*n1end)
      n1end++;
    if (*n2end)
      n2end++;
  }

  char *sum = malloc(len + 2);
  int res, sumi = 0, carry = 0;

  while (n1end > num1 || n2end > num2) {
    res = carry + (n1end == num1 ? 0 : (*--n1end - '0')) +
          (n2end == num2 ? 0 : (*--n2end - '0'));
    carry = res / 10;
    sum[sumi++] = '0' + res % 10;
  }
  if (carry > 0)
    sum[sumi++] = '0' + carry;
  sum[sumi] = '\0';

  reverse(sum, sumi);
  return sum;
}

int main(int argc, char const *argv[]) {
  assert(0 == strcmp(addStrings("123", "456"), "579"));
  assert(0 == strcmp(addStrings("7", "8"), "15"));
  assert(0 == strcmp(addStrings("1", "999"), "1000"));
  assert(0 == strcmp(addStrings("999", "1"), "1000"));
  assert(0 == strcmp(addStrings("0", "0"), "0"));
  assert(0 == strcmp(addStrings("3", "0"), "3"));
  return 0;
}
