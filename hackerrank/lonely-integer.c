#include <stdio.h>

int main() {
  int res = 0, n, k;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &k);
    res ^= k;
  }
  printf("%d", res);
}
