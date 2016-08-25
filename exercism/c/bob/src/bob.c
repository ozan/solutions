#include "bob.h"
#include <ctype.h>

char *hey_bob(char *phrase) {
  int is_question = 0;
  int any_upper = 0;
  int any_lower = 0;
  int all_empty = 1;

  char ch;
  while ((ch = *phrase++) != '\0') {
    if (ch != ' ')
      is_question = 0;
    if (ch == '?')
      is_question = 1;
    if (ch != ' ')
      all_empty = 0;
    if (islower(ch))
      any_lower = 1;
    if (isupper(ch))
      any_upper = 1;
  }

  if (any_upper && !any_lower)
    return "Whoa, chill out!";
  if (is_question)
    return "Sure.";
  if (all_empty)
    return "Fine. Be that way!";
  return "Whatever.";
}
