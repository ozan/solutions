/*
TODO: there's actually a way to do this in sublinear time using the
inclusion-exclusion principle as well as the formula for the sum of
an aritmetic sequence.
*/

#include <stdio.h>
unsigned int sum_of_multiples(const unsigned int multiples[],
                              unsigned int n_multiples, unsigned int limit) {
  unsigned int sum = 0, n, i_mult;

  if (multiples == NULL)
    return 0;

  for (i_mult = 0; i_mult < n_multiples; i_mult++)
    if (multiples[i_mult] == 0)
      return 0;

  for (n = 1; n < limit; n++) {
    for (i_mult = 0; i_mult < n_multiples; i_mult++) {
      if (n % multiples[i_mult] == 0) {
        sum += n;
        break;
      }
    }
  }
  return sum;
}
