#include "hexadecimal.h"

uint64_t hexadecimal::convert(std::string digits) {
  std::string hex = "0123456789abcdef";
  int len = digits.length();
  int sum = 0;
  for (int i = 0; i < len; i++) {
    int val = hex.find(digits[i], 0);
    if (val < 0 || val > 15)
      return 0;
    sum <<= 4;
    sum += val;
  }
  return sum;
}
