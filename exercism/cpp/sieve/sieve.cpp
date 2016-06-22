#include "sieve.h"
#include <vector>

std::vector<int> sieve::primes(int upto) {
  int sieve[upto + 1];
  std::fill_n(sieve, upto + 1, 1);
  std::vector<int> primes;

  for (int p = 2; p <= upto; p++) {
    if (!sieve[p])
      continue;
    primes.push_back(p);
    for (int q = p; q <= upto; q += p)
      sieve[q] = 0;
  }

  return primes;
}
