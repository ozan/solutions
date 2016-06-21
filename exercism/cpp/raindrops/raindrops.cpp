#include "raindrops.h"
#include <sstream>

std::string raindrops::convert(int n) {
  std::stringstream ss;
  if (n % 3 == 0)
    ss << "Pling";
  if (n % 5 == 0)
    ss << "Plang";
  if (n % 7 == 0)
    ss << "Plong";
  auto s = ss.str();
  return s.empty() ? std::to_string(n) : s;
}
