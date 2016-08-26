#include <stdio.h>

int main() {
  int t, n, a, b;
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    scanf("%d", &a);
    for (int i = 1; i < n; i++) {
      scanf("%d", &b);
      if (i % 2 == 0)
        a ^= b;
    }
    printf("%d\n", n % 2 == 1 ? a : 0);
  }

  return 0;
}
