#include "nth_prime.h"

int nth(int n) {
  if (n == 0)
    return 0;

  int primes[n], k = 0, p = 2, is_prime;

  while (k < n) {
    is_prime = 1;
    for (int i = 0; i < k; i++) {
      if (p % primes[i] == 0) {
        p++;
        is_prime = 0;
        break;
      }
    }
    if (is_prime) {
      primes[k++] = p++;
    }
  }

  return primes[n - 1];
}
