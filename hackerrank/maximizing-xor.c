#include <stdio.h>

int main() {
  int res = 0, l, r;
  scanf("%d %d", &l, &r);
  for (int i = l; i <= r; i++) {
    for (int j = i + 1; j <= r; j++) {
      int x = i ^ j;
      res = x > res ? x : res;
    }
  }
  printf("%d", res);
  return 0;
}
