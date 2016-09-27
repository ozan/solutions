#include <assert.h>

int strend(char *s, char *t) {
  char *se = s, *te = t;
  while (*se++)
    ;
  while (*te++)
    ;
  while (se > s && te > t)
    if (*--se != *--te)
      return 0;
  return 1;
}

int main() {
  assert(strend("foobar", "foo") == 0);
  assert(strend("foobar", "bar") == 1);
  assert(strend("foobar", "") == 1);
  assert(strend("foobar", "foobar") == 1);
}
