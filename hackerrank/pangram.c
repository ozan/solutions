#include <ctype.h>
#include <stdio.h>

int main() {
  char s[1000], ch;
  scanf("%[^\n]s", s);
  int set = 0;
  for (int i = 0; i < 1000; i++) {
    ch = s[i];
    if (ch == '\0')
      break;
    if (ch == ' ')
      continue;
    ch = tolower(ch);
    set |= (1 << (ch - 'a'));
  }
  printf("%s", set + 1 == (1 << 26) ? "pangram" : "not pangram");
}
