#include "say.h"
#include <string>

std::string say::in_english(uint64_t n, std::string prefix) {
  if (n >= 1000ULL * 1000ULL * 1000ULL * 1000ULL)
    throw std::domain_error("Number out of range");

  for (auto part : parts) {
    uint64_t high = n / part.amount;
    if (high == 0)
      continue;

    uint64_t low = n % part.amount;
    std::string tail_prefix = part.amount < 100 ? "-" : " ";
    std::string tail = low == 0 ? "" : in_english(low, tail_prefix);

    if (part.amount < 100)
      return prefix + part.name + tail;

    std::string head = in_english(high, prefix.length() ? " " : "");
    return head + " " + part.name + tail;
  }
  return "zero";
}
