#include <ctype.h>
#include <stdio.h>

#define MAX_STRING_LEN 100000

int main() {
  char s[MAX_STRING_LEN], ch;
  scanf("%s", s);
  int total = 1;
  for (int i = 0; i < MAX_STRING_LEN; i++) {
    ch = s[i];
    if (ch == '\0')
      break;
    if (isupper(ch))
      total++;
  }
  printf("%d", total);
}
