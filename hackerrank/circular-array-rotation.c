#include <stdio.h>

int main() {
  int n, k, q, qx;
  scanf("%d %d %d", &n, &k, &q);
  int nums[n];
  for (int ni = 0; ni < n; ni++)
    scanf("%d", &nums[ni]);
  while (q--) {
    scanf("%d", &qx);
    printf("%d\n", nums[(n + qx - (k % n)) % n]);
  }
  return 0;
}
