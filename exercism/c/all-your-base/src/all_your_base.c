#include "all_your_base.h"
#include <stdio.h>

size_t rebase(int8_t digits[DIGITS_ARRAY_SIZE], int16_t input_base,
              int16_t output_base, size_t input_length) {
  // TODO: this strategy breaks if binary rep overflows unsigned long
  size_t n = 0, output_length = 0, i;
  int8_t swap, d;

  if (input_base < 0 || output_base <= 1)
    return 0;

  // roll input into a single long
  for (i = 0; i < input_length; i++) {
    d = digits[i];
    if (d < 0 || d >= input_base || (n == 0 && d == 0))
      return 0;
    n = n * input_base + d;
  }

  // create output in reverse order
  while (n > 0) {
    digits[output_length] = n % output_base;
    n /= output_base;
    output_length += 1;
  }

  // rectify order
  for (i = 0; i < output_length / 2; i++) {
    swap = digits[i];
    digits[i] = digits[output_length - i - 1];
    digits[output_length - i - 1] = swap;
  }

  return output_length;
}
