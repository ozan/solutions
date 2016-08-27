#include <stdio.h>

int main() {
  char s[100], ch;
  scanf("%s", s);
  char stack[100];
  int sp = 0;
  for (int i = 0; i < 100; i++) {
    ch = s[i];
    if (ch == '\0')
      break;
    if (sp > 0 && stack[sp - 1] == ch) {
      sp--;
    } else {
      stack[sp] = ch;
      sp++;
    }
  }
  if (sp == 0) {
    printf("Empty String");
  } else {
    stack[sp] = '\0';
    printf("%s", stack);
  }
  return 0;
}
