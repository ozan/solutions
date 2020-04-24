#include "../src/sublist.h"
#include <stdbool.h>

bool is_sublist(int *xs, int *ys, int n_xs, int n_ys) {
  bool all_match;
  for (n_ys -= n_xs; n_ys >= 0; n_ys--) {
    all_match = true;
    for (int i = 0; i < n_xs; i++) {
      if (xs[i] != ys[n_ys + i]) {
        all_match = false;
        break;
      }
    }
    if (all_match)
      return true;
  }
  return n_xs == 0;
}

const comparison_result_t results[] = {UNEQUAL, SUBLIST, SUPERLIST, EQUAL};

comparison_result_t check_lists(int *xs, int *ys, size_t n_xs, size_t n_ys) {
  int i = is_sublist(xs, ys, n_xs, n_ys);
  i ^= is_sublist(ys, xs, n_ys, n_xs) << 1;
  return results[i];
}
