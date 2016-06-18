#include "sum_of_multiples.h"

int sum_of_multiples::to(int limit) { return to({3, 5}, limit); }

int sum_of_multiples::to(std::vector<int> divisors, int limit) {
  int sum = 0;
  for (int n = 1; n < limit; n++) {
    for (auto d : divisors) {
      if (n % d == 0) {
        sum += n;
        break;
      }
    }
  }
  return sum;
}
