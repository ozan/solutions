/*
Write a program `detab` that replaces tabs in the input with the proper number
of blanks to space to the next tab stop. Assume a fixed set of tab stops, say
every `n` columns. Should n be a variable or a symbolic paramater?
*/

#include <stdio.h>

void put_spaces(int n) {
  while (n--)
    putchar(' ');
}

void detab(int width) {
  char ch;
  int col = 0, diff;

  while ((ch = getchar()) != EOF) {
    if (ch == '\t') {
      diff = width - (col % width);
      put_spaces(diff);
      col += diff;
    } else {
      putchar(ch);
      col = ch == '\n' ? 0 : col + 1;
    }
  }
}

int main() {
  detab(4);
  return 0;
}
