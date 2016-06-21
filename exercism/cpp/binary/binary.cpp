#include "binary.h"

int binary::convert(const std::string &given) {
  const int places = given.length();
  int total = 0;

  for (int i = 0; i < places; i++) {
    char ch = given[places - i - 1];

    if (ch == '0')
      continue;
    else if (ch == '1')
      total += 1 << i;
    else
      return 0;
  }

  return total;
}
