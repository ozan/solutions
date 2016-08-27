#include <stdio.h>

#define MAX_N 100

int min(int a, int b) { return a < b ? a : b; }

int main() {
  int n;
  scanf("%d", &n);
  int blocked[n];
  for (int i = 0; i < n; i++)
    scanf("%d", &blocked[i]);
  int a = 0, b = 1, temp;
  for (int i = 2; i < n; i++) {
    if (blocked[i]) {
      a = b;
      b = MAX_N;
    } else {
      temp = b;
      b = 1 + min(a, b);
      a = temp;
    }
  }
  printf("%d", b);
  return 0;
}
