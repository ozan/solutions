#include <stdio.h>

int popcount(unsigned long long int n) {
  int count = 0;
  while (n) {
    n &= (n - 1);
    count++;
  }
  return count;
}

int main() {
  int t;
  scanf("%d\n", &t);
  while (t--) {
    unsigned long long int n;
    scanf("%llu\n", &n);
    printf("%s\n", popcount(n - 1) & 1 ? "Louise" : "Richard");
  }
  return 0;
}
