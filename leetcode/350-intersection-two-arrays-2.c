#include <stdio.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *intersect(int *larger, int largerSize, int *smaller, int smallerSize,
               int *returnSize) {

  if (smallerSize > largerSize)
    return intersect(smaller, smallerSize, larger, largerSize, returnSize);

  int *ret = (int *)malloc(sizeof(int) * smallerSize);

  int used[largerSize];
  for (int i = 0; i < largerSize; i++)
    used[i] = 0;

  int reti = 0;
  for (int i = 0; i < smallerSize; i++) {
    for (int j = 0; j < largerSize; j++) {
      if (smaller[i] == larger[j] && !used[j]) {
        used[j] = 1;
        ret[reti] = smaller[i];
        reti++;
        break;
      }
    }
  }
  *returnSize = reti;
  return ret;
}

int main(int argc, char const *argv[]) {
  int nums2[] = {1, 2, 2, 1};
  int nums1[] = {2, 2};
  int returnSize;
  int *result = intersect(nums1, sizeof(nums1) / sizeof(int), nums2,
                          sizeof(nums2) / sizeof(int), &returnSize);
  printf("[%d, %d], size: %d\n", result[0], result[1], returnSize);
  return 0;
}
