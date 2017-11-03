#include "binary_search.h"
#include <stdio.h>

int *binary_search(int n, int array[], int length) {
  int a = 0, b = length - 1, mid, probe;

  while (a <= b) {
    mid = a + (b - a) / 2; // note: (a + b) / 2 could overflow
    probe = array[mid];
    if (probe == n)
      return &array[mid];
    if (probe < n) {
      a = mid + 1;
    } else {
      b = mid - 1;
    }
  }
  return (void *)0;
}
