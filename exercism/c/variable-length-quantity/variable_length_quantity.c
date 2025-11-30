#include "variable_length_quantity.h"

#include <stdio.h>

int encode(const uint32_t *integers, size_t integers_len, uint8_t *output) {
  int out_i = 0;  // index into output
  uint8_t buf[5]; // temporary buffer since we will need to reverse byte order

  for (size_t i = 0; i < integers_len; i++) {
    uint32_t n = integers[i];

    if (n == 0) {
      output[out_i++] = 0;
      continue;
    }

    int ni = 0;
    while (n > 0) {
      buf[ni++] = n & 0x7f;
      n >>= 7;
    }

    // add buf bytes back to out, in reverse order, with correct continuation
    while (--ni >= 0) {
      output[out_i++] = buf[ni] + (ni == 0 ? 0 : 0x80);
    }
  }

  return out_i;
}

int decode(const uint8_t *bytes, size_t buffer_len, uint32_t *output)
{
  uint32_t n = 0;
  int oi = 0;
  int valid = 0;
  for (size_t i = 0; i < buffer_len; i++) {
    uint8_t b = bytes[i];
    n = (n << 7) | (b & 0x7f);
    valid = 0;
    if (b < 0x80) {
      output[oi++] = n;
      n = 0;
      valid = 1;
    }
  }
  return valid == 1 ? oi : -1;
}
