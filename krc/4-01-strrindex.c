#include <assert.h>

int strrindex(char *s, char *t) {
  int i, k, ret = -1;

  for (i = 0; s[i] != '\0'; i++) {
    for (k = 0; t[k] != '\0' && s[i + k] == t[k]; k++)
      ;
    if (k > 0 && t[k] == '\0')
      ret = i;
  }
  return ret;
}

int main() {
  assert(strrindex("funkfunk", "unk") == 5);
  return 0;
}
