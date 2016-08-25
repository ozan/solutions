#include "hamming.h"

int compute(char *xs, int nx, char *ys, int ny) {
  int n = nx > ny ? ny : nx;
  int total = 0;

  for (int i = 0; i < n; i++)
    total += xs[i] != ys[i];

  return total;
}
