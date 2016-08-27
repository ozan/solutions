#include <stdio.h>

int main() {
  int h, m, s;
  char a_or_p;
  scanf("%02d:%02d:%02d%cM", &h, &m, &s, &a_or_p);
  printf("%02d:%02d:%02d", (h % 12) + 12 * (a_or_p == 'P'), m, s);
  return 0;
}
