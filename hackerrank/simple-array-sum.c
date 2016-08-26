#include <stdio.h>

int main() {
  int n, k;
  int total = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &k);
    total += k;
  }
  return 0;
}
