#include <stdio.h>
#include <stdlib.h>

int comp(const void *x, const void *y) {
  int n = *((int *)x);
  int m = *((int *)y);
  if (n > m)
    return 1;
  if (n < m)
    return -1;
  return 0;
}

int *intersection(int *nums1, int nums1Size, int *nums2, int nums2Size,
                  int *returnSize) {

  qsort(nums1, sizeof(nums1) / sizeof(int), sizeof(int), comp);
  qsort(nums2, sizeof(nums2) / sizeof(int), sizeof(int), comp);

  int *res = (int *)malloc(sizeof(int) *
                           (nums1Size > nums2Size ? nums2Size : nums1Size));

  int i = 0, j = 0, resi = 0;
  int n = nums1[0] == 0 ? 1 : 0;
  while (i < nums1Size && j < nums2Size) {
    if (nums1[i] == n) {
      i++;
      continue;
    }
    if (nums2[j] == n) {
      j++;
      continue;
    }
    if (nums1[i] == nums2[j]) {
      res[resi] = n = nums1[i];
      i++;
      j++;
      resi++;
    } else if (nums1[i] < nums2[j]) {
      i++;
    } else {
      j++;
    }
  }

  *returnSize = resi;
  return res;
}

int main(int argc, char const *argv[]) {
  int nums1[] = {1};
  int nums2[] = {1};
  int returnSize;
  int *res = intersection(nums1, sizeof(nums1) / sizeof(int), nums2,
                          sizeof(nums2) / sizeof(int), &returnSize);
  printf("[%d, %d], size %d\n", res[0], res[1], returnSize);
  return 0;
}
