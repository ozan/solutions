#include "prime_factors.h"

size_t find_factors(uint64_t n, uint64_t out[]) {
  int k = 0, p = 2;
  while (n > 1) {
    if (n % p == 0) {
      out[k++] = p;
      n /= p;
    } else
      p++;
  }
  return k;
}
