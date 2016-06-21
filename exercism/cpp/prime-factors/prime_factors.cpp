#include "prime_factors.h"

std::vector<int> prime_factors::of(int n) {
  std::vector<int> factors;
  int k = 2;

  while (n >= k) {
    if (n % k == 0) {
      factors.push_back(k);
      n /= k;
    } else {
      k += 1;
    }
  }

  return factors;
}
