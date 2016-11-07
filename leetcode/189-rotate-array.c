#include <stdio.h>

void reverse(int *nums, int a, int b) {
  int tmp;
  while (a < b) {
    tmp = nums[b];
    nums[b] = nums[a];
    nums[a] = tmp;
    a++;
    b--;
  }
}

void rotate(int *nums, int numsSize, int k) {
  k = k % numsSize;
  reverse(nums, 0, numsSize - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, numsSize - 1);
}

int main(int argc, char const *argv[]) {
  int a[] = {1, 2, 3, 4, 5, 6, 7};
  rotate(a, 7, 3);

  for (int i = 0; i < 7; i++)
    printf("%d ", a[i]);
  printf("\n");

  return 0;
}
