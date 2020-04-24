#include "wordy.h"
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int plus(int a, int b) { return a + b; }
int minus(int a, int b) { return a - b; }
int multiplied(int a, int b) { return a * b; }
int divided(int a, int b) { return a / b; }
int second(int a, int b) {
  (void)a;
  return b;
}

bool answer(const char *question, int *result) {
  char *tofree, *string, *token;
  int (*op)(int, int) = second;

  tofree = string = strdup(question + 8);

  while ((token = strsep(&string, " "))) {
    if (token[0] == '-' || isdigit(token[0]))
      *result = op(*result, atoi(token));
    else if (strcmp(token, "by") == 0)
      continue;
    else if (strcmp(token, "plus") == 0)
      op = plus;
    else if (strcmp(token, "minus") == 0)
      op = minus;
    else if (strcmp(token, "multiplied") == 0)
      op = multiplied;
    else if (strcmp(token, "divided") == 0)
      op = divided;
    else
      return false;
  }

  free(tofree);
  return true;
}

