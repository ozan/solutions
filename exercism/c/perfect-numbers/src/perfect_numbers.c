#include "perfect_numbers.h"

kind classify_number(int n) {
  int total = 0, i;

  if (n <= 0)
    return ERROR;

  for (i = 1; i < n; i++)
    if (n % i == 0)
      total += i;

  if (total == n)
    return PERFECT_NUMBER;

  if (total < n)
    return DEFICIENT_NUMBER;

  return ABUNDANT_NUMBER;
}
