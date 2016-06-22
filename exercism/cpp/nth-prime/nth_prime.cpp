#include "nth_prime.h"
#include <vector>

unsigned long prime::nth(unsigned long n) {
  if (n == 0)
    throw std::domain_error("There is no 0th prime");

  auto primes = std::vector<unsigned long>();
  unsigned long p = 2;

  while (primes.size() < n) {
    bool is_prime = true;
    for (auto q : primes) {
      if (p % q == 0) {
        p++;
        is_prime = false;
        break;
      }
    }
    if (is_prime) {
      primes.push_back(p);
      p++;
    }
  }
  return primes[n - 1];
}
