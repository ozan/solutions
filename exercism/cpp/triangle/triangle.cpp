#include "triangle.h"
#include <set>

triangle::kinds triangle::kind(double a, double b, double c) {
  if (a > b)
    std::swap(a, b);
  if (a > c)
    std::swap(a, c);
  if (b > c)
    std::swap(b, c);

  if (a <= 0 || a + b <= c)
    throw std::domain_error("Invalid triangle");

  int n = (std::set<double>{a, b, c}).size();
  return static_cast<kinds>(n - 1);
}
