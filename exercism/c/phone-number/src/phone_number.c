#include <stdlib.h>
#include <string.h>

const char *invalid = "0000000000";

char *phone_number_clean(const char *given) {
  char c, *out, *op, *op2;

  out = op = op2 = malloc(12);
  while ((c = *given++) != '\0') {
    if (c == ' ' || c == '.' || c == '(' || c == ')' || c == '-')
      continue;
    if (c >= '0' && c <= '9') {
      *op++ = c;
    } else {
      strcpy(out, invalid);
      return out;
    }
  }
  *op = '\0';
  if (op - out == 11 && *out == '1') {
    while (*(op2 + 1) != '\0') {
      *op2 = *(op2 + 1);
      op2++;
    }
    *op2 = '\0';
  } else if (op - out != 10)
    strcpy(out, invalid);
  return out;
}

char *phone_number_get_area_code(const char *given) {
  char c, *out, *op;
  int i = 3;

  out = op = malloc(4);
  while ((c = *given++) != '\0' && i) {
    if (c >= '0' && c <= '9') {
      *op++ = c;
      i--;
    }
  }
  *op = '\0';
  return out;
}

char *phone_number_format(const char *given) {
  char *cleaned, *cp, *formatted, *fp;

  cleaned = cp = phone_number_clean(given);
  formatted = fp = malloc(15);

  *fp++ = '(';
  *fp++ = *cp++;
  *fp++ = *cp++;
  *fp++ = *cp++;
  *fp++ = ')';
  *fp++ = ' ';
  *fp++ = *cp++;
  *fp++ = *cp++;
  *fp++ = *cp++;
  *fp++ = '-';
  *fp++ = *cp++;
  *fp++ = *cp++;
  *fp++ = *cp++;
  *fp++ = *cp++;
  *fp = '\0';

  free(cleaned);
  return formatted;
}
