/*
Write a program to "fold" long input lines into two or more shorter lines after
the last non-blank character that occurs before the n-th column of input. Make
sure your program does something intelligent with very long lines, and if there
are no blanks or tabs before the specified column.
*/

#include <stdio.h>

void fold(width) {
  // maintain a buffer for a token
  // when width is encountered, simply print a newline and reset col counter
  // when a space or tab is encountered, print and continue
  char buffer[width + 1], ch;
  int col = 0, i = 0;

  while ((ch = getchar()) != EOF) {
    // If blank, print buffered token
    if (ch == ' ' || ch == '\t') {
      if (i > 0) {
        buffer[i] = '\0';
        printf("%s", buffer);
        i = 0;
      }
      putchar(ch);
    } else {
      // else accumulate char into token buffer
      buffer[i++] = ch;
    }
    col++;

    // Accumulated token is larger than one line, so just write it all
    if (i == width) {
      buffer[i] = '\0';
      printf("%s", buffer);
      i = 0;
    }

    // Column width reached, print newline and reset col count
    if (col == width) {
      putchar('\n');
      col = 0;
    }
  }

  // Clean up - write final token, possibly preceded by a newline
  buffer[i] = '\0';
  if (i + col > width)
    putchar('\n');
  printf("%s\n", buffer);
}

int main() {
  fold(80);
  return 0;
}
