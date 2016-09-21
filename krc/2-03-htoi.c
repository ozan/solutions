/*
Write the function htoi(s) which converts a string of hexadecimal digits
(including an optional 0x or 0X) into ist equivalent integer value. The
allowable digits are 0 through 9, a through f and A through F.
*/

#include <ctype.h>
#include <stdio.h>

int htoi(char *hex) {
  int total = 0;
  char ch;

  while ((ch = tolower(*hex++))) {
    if (ch == 'x' && total == 0)
      continue;
    total <<= 4;
    if (isdigit(ch))
      total += ch - '0';
    else if (ch < 'a' || ch > 'f')
      return -1;
    else
      total += ch - 'a' + 10;
  }
  return total;
}

int main() {
  char fmt[] = "%s: %d (expected %d)\n";
  printf(fmt, "ae0f", htoi("ae0f"), 0xae0f);
  printf(fmt, "0xae0f", htoi("0xae0f"), 0xae0f);
  printf(fmt, "2x", htoi("2x"), -1);
  return 0;
}
