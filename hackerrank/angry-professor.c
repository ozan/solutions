#include <stdio.h>

int main() {
  int t, n, k, a;
  scanf("%d", &t);
  while (t--) {
    scanf("%d %d", &n, &k);
    while (n--) {
      scanf("%d", &a);
      if (a <= 0)
        k--;
    }
    printf("%s\n", k > 0 ? "YES" : "NO");
  }
  return 0;
}
