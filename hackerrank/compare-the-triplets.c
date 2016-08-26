#include <stdio.h>

int main() {
  int a0, a1, a2;
  scanf("%d %d %d", &a0, &a1, &a2);
  int b0, b1, b2;
  scanf("%d %d %d", &b0, &b1, &b2);
  printf("%d %d", (a0 > b0) + (a1 > b1) + (a2 > b2),
         (a0 < b0) + (a1 < b1) + (a2 < b2));
}
