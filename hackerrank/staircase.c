#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  for (int row = 0; row < n; row++) {
    for (int col = 0; col < n; col++)
      printf("%c", col >= n - row - 1 ? '#' : ' ');
    printf("\n");
  }
  return 0;
}
