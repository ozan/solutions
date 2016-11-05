#include <assert.h>
#include <limits.h>
#include <stdbool.h>

bool increasingTriplet(int *nums, int numsSize) {
  int n, a = INT_MAX, b = INT_MAX;
  for (int i = 0; i < numsSize; i++) {
    n = nums[i];
    if (n > b)
      return true;
    if (n < a)
      a = n;
    if (n > a && n < b)
      b = n;
  }
  return false;
}

int main() {
  int asc[3] = {1, 2, 3};
  assert(true == increasingTriplet(asc, 3));

  int dec[3] = {3, 2, 1};
  assert(false == increasingTriplet(dec, 3));

  int alt[6] = {10, 1, 10, 2, 10, 3};
  assert(true == increasingTriplet(alt, 6));
  return 0;
}
