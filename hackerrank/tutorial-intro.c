#include <stdio.h>

int main() {
  int target, n;
  scanf("%d %d", &target, &n);
  int nums[n];
  for (int i = 0; i < n; i++)
    scanf("%d", &nums[i]);

  int a = 0, b = n - 1;
  while (a <= b) {
    int mid = (a + b) / 2;
    int probe = nums[mid];
    if (probe == target) {
      printf("%d", mid);
      return 0;
    } else if (probe < target) {
      a = mid + 1;
    } else {
      b = mid - 1;
    }
  }

  // no solution - violation of constraint
  return -1;
}
