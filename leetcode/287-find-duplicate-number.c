#include <stdlib.h>

int cmp(const void *a, const void *b) { return *(int *)a - *(int *)b; }

int findDuplicate(int *nums, int numsSize) {
  qsort(nums, numsSize, sizeof(int), &cmp);
  int prior = -1;
  for (int i = 0; i < numsSize; i++) {
    if (nums[i] == prior)
      return prior;
    prior = nums[i];
  }
  return prior;
}
