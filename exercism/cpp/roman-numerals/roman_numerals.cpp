#include "roman_numerals.h"

std::string roman::convert(int decimal) {

  struct d_r_mapping {
    int decimal;
    std::string roman;
  };

  static const d_r_mapping parts[] = {
      {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"},
      {90, "XC"},  {50, "L"},   {49, "IL"}, {40, "XL"},  {10, "X"},
      {9, "IX"},   {5, "V"},    {4, "IV"},  {1, "I"},
  };

  std::string result;

  for (auto d_r : parts) {
    while (d_r.decimal <= decimal) {
      result += d_r.roman;
      decimal -= d_r.decimal;
    }
  }

  return result;
}
