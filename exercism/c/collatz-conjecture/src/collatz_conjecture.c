#include "collatz_conjecture.h"

int steps(int start) {
  if (start <= 0)
    return ERROR_VALUE;
  int count = 0;
  while (start != 1) {
    start = start & 1 ? 3 * start + 1 : start >> 1;
    count++;
  }
  return count;
}
