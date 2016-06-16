#include "difference_of_squares.h"

const int squares::sum_of_squares(const int n) {
  int sum = 0;
  for (int i = 1; i <= n; i++)
    sum += i * i;
  return sum;
}

const int squares::square_of_sums(const int n) {
  int sum = n * (1 + n) / 2;
  return sum * sum;
}

const int squares::difference(const int n) {
  return square_of_sums(n) - sum_of_squares(n);
}
