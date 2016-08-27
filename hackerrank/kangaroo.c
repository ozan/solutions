#include <stdio.h>

int main() {
  int x1, v1, x2, v2;
  scanf("%d %d %d %d", &x1, &v1, &x2, &v2);
  printf("%s", x1 == x2 || (v1 != v2 && (x2 - x1) % (v1 - v2) == 0 &&
                            (x2 - x1) / (v1 - v2) > 0)
                   ? "YES"
                   : "NO");
  return 0;
}
