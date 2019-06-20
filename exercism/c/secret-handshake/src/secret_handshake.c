#include "secret_handshake.h"
#include <stdlib.h>

const char *actions[4] = {"wink", "double blink", "close your eyes", "jump"};
int forward[4] = {0, 1, 2, 3};
int back[4] = {3, 2, 1, 0};

const char **commands(int n) {
  const char **out = malloc(4 * sizeof(char *));
  int k = 0;
  int *dir = (n & 16) ? back : forward;
  for (int i = 0; i < 4; i++)
    if (n & (1 << dir[i]))
      out[k++] = actions[dir[i]];
  if (k == 0)
    out[0] = NULL;
  return out;
}
