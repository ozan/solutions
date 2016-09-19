/*
Write a program to remove all comments for a C program. Don't forget to handle
quoted strings and character constants properly. C comments do not nest.
*/

#include <stdio.h>

#define FALSE 0
#define TRUE 1

enum container_t {
  DEFAULT,
  SINGLE_QUOTE,
  DOUBLE_QUOTE,
  LINE_COMMENT,
  BLOCK_COMMENT
};

void strip_comments() {
  enum container_t state = DEFAULT;
  char prior = 0, ch;

  while ((ch = getchar()) != EOF) {

    // cases for switching into a contained state
    switch (ch) {
    case '/':
      if (state == DEFAULT && prior == '/')
        state = LINE_COMMENT;
    case '*':
      if (state == DEFAULT && prior == '/')
        state = BLOCK_COMMENT;
    case '\'':
      if (state == DEFAULT)
        state = SINGLE_QUOTE;
    case '"':
      if (state == DEFAULT)
        state = DOUBLE_QUOTE;
    }

    // print prior character if we know it was not inside or part of a comment
    if (state != LINE_COMMENT && state != BLOCK_COMMENT)
      putchar(prior);

    // cases for switching back to default, from a contained state
    switch (ch) {
    case '\n':
      if (state == LINE_COMMENT)
        state = DEFAULT;
    case '/':
      if (state == BLOCK_COMMENT && prior == '*')
        state = DEFAULT;
    case '\'':
      if (state == SINGLE_QUOTE && prior != '\\')
        state = DEFAULT;
    case '\"':
      if (state == DOUBLE_QUOTE && prior != '\\')
        state = DEFAULT;
    }

    prior = ch;
  }

  // print final character if appropriate
  if (state != LINE_COMMENT && state != BLOCK_COMMENT)
    putchar(prior);
}

int main() {
  strip_comments();
  return 0;
}
