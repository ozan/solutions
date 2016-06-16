#include "etl.h"

std::map<char, int> etl::transform(std::map<int, std::vector<char>> old) {
  std::map<char, int> transformed;
  for (auto const &kv : old) {
    int n = kv.first;
    for (const char &ch : kv.second) {
      transformed[tolower(ch)] = n;
    }
  }
  return transformed;
}
