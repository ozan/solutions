#include <stdio.h>
#include <string.h>

#include "sieve.h"

unsigned int sieve(const unsigned int limit, primes_array_t primes) {
  char sieve[limit + 1]; // TODO could use bitset instead of array
  unsigned int p = 2, q, i = 0;

  memset(sieve, 1, limit + 1);
  for (p = 2; p <= limit; p++) {
    if (!sieve[p])
      continue;
    primes[i++] = p;
    for (q = p; q <= limit; q += p)
      sieve[q] = 0;
  }
  return i;
}
