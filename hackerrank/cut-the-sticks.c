#include <stdio.h>

#define MAX_A 1000

int main() {
  int n, a;
  scanf("%d", &n);
  int counts[MAX_A + 1] = {0};
  for (int i = 0; i < n; i++) {
    scanf("%d", &a);
    counts[a]++;
  }
  int i = 1, cnt;
  while (n) {
    if ((cnt = counts[i])) {
      printf("%d\n", n);
      n -= cnt;
    }
    i++;
  }
}
