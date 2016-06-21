#include "trinary.h"

int trinary::to_decimal(const std::string &digits) {
  int total = 0;
  int base = 1;

  for (auto i = digits.crbegin(); i < digits.crend(); i++) {
    int val = *i - '0';
    if (val < 0 || val > 2)
      return 0;
    total += val * base;
    base *= 3;
  }

  return total;
}
