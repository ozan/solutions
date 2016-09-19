/*
Write a program `entab` that replaces strings of blanks by the minimum number of
tabs and blanks to achieve the same spacing. Use the same tab stops as for
detab. When either a tab or a single blank would suffice to reach a tab stop,
which should be given preference?
*/

#include <stdio.h>

void print_spaces(int n) {
  while (n--)
    putchar(' ');
}

void entab(int width) {
  char ch;
  int col = 0, spaces = 0;

  while ((ch = getchar()) != EOF) {
    if ((col + 1) % width == 0 && spaces > 0) {
      putchar('\t');
      spaces = 0;
    }
    if (ch == ' ') {
      spaces++;
      col++;
    } else {
      if (spaces > 0) {
        print_spaces(spaces);
        spaces = 0;
      }
      putchar(ch);
      col = ch == '\n' ? 0 : col + 1;
    }
  }
}

int main() {
  entab(4);
  return 0;
}
