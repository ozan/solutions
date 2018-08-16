#include <stdlib.h>
#include "diamond.h"

char **make_diamond(char letter) {
  int n = letter - 'A', nn = 2 * n, i, j;
  char c;
  char **diamond = malloc((nn + 1) * sizeof(char *));

  // Allocate all of the strings
  for (i = 0; i <= nn; i++) {
    diamond[i] = malloc(nn + 2);
    diamond[i][nn + 1] = '\0';
  }

  // Iterate over the top left quarter of the diamond, and set as many as
  // 4 identical values, by horizontal and vertical symmetry
  for (i = 0; i <= n; i++) {
    for (j = 0; j <= n; j++) {
      c = i + j == n ? 'A' + i : ' ';
      diamond[i][j] = c;
      diamond[i][nn - j] = c;
      diamond[nn - i][j] = c;
      diamond[nn - i][nn - j] = c;
    }
  }
  return diamond;
}
