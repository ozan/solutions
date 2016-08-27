#include <stdio.h>

int main() {
  int t, n, m, s;
  scanf("%d", &t);
  while (t--) {
    scanf("%d %d %d", &n, &m, &s);
    printf("%d\n", 1 + (m + s - 2) % n);
  }
  return 0;
}
