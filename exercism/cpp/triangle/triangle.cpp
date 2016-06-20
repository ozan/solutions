#include "triangle.h"
#include <set>

triangle::kinds triangle::kind(float a, float b, float c) {
  if (a <= 0 || b <= 0 || c <= 0)
    throw std::domain_error("Sides must be > 0");

  int mx = std::max(a, std::max(b, c));
  if (a + b + c - mx <= mx)
    throw std::domain_error("Invalid triangle");

  int n = (std::set<float>{a, b, c}).size();
  return (kinds)(n - 1);
}
