#include "binary.h"

int convert(char *digits) {
  int total = 0;
  char d;

  while ((d = *digits++) != '\0') {
    if (d != '0' && d != '1')
      return INVALID;
    total = (total << 1) + (d - '0');
  }
  return total;
}
