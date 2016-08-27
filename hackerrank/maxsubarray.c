#include <stdio.h>

int max(int a, int b) { return a > b ? a : b; }

int main() {
  int t, n, a;
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    n--;
    scanf("%d", &a);
    int maxcont = a, maxhere = a, maxany = a;
    while (n--) {
      scanf("%d", &a);
      maxhere = max(a, maxhere + a);
      maxcont = max(maxcont, maxhere);
      maxany = max(a, max(a + maxany, maxany));
    }
    printf("%d %d\n", maxcont, maxany);
  }
  return 0;
}
