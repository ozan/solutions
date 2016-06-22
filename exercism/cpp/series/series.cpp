#include "series.h"
#include <iostream>
#include <string>
#include <vector>

std::vector<int> series::digits(std::string chars) {
  std::vector<int> digits;
  for (auto &ch : chars) {
    int d = ch - '0';
    if (d < 0 || d > 9)
      throw std::domain_error("Invalid char");
    digits.push_back(d);
  }
  return digits;
}

std::vector<std::vector<int>> series::slice(std::string chars, int n) {
  std::vector<int> digits = series::digits(chars);
  int size = digits.size();

  if (size < n)
    throw std::domain_error("Insufficient digits to slice");

  int num_slices = size - n + 1;
  std::vector<std::vector<int>> slices(num_slices, std::vector<int>(n));

  for (int i = 0; i < num_slices; i++) {
    for (int j = 0; j < n; j++) {
      slices[i][j] = digits.at(i + j);
    }
  }
  return slices;
}
