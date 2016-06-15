#include "hamming.h"

std::size_t hamming::compute(const std::string &xs, const std::string &ys) {

  if (xs.length() != ys.length())
    throw std::domain_error("String lengths don't match");

  std::size_t count = 0;
  for (int i = 0; i < xs.length(); i++) {
    if (xs[i] != ys[i])
      count++;
  }
  return count;
}
