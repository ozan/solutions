#include <stdio.h>

int min(int a, int b) { return a < b ? a : b; }

int max(int a, int b) { return a > b ? a : b; }

int main() {
  int n, k, a, total = 0;
  scanf("%d %d", &n, &k);
  int mods[k];
  for (int i = 0; i < k; i++)
    mods[i] = 0;
  while (n--) {
    scanf("%d", &a);
    mods[a % k]++;
  }
  // can only have 1 value congruent to 0 mod k
  total += min(1, mods[0]);
  // if even, can only have 1 value congruent to k/2 mod k
  if (k % 2 == 0)
    total += min(1, mods[k / 2]);
  // for all others, pick max of those k and n-k mod k
  for (int d = 1; d < (k + 1) / 2; d++) { // for all others,
    total += max(mods[d], mods[k - d]);
  }
  printf("%d", total);
  return 0;
}
