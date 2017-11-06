#include <stdlib.h>
#include <string.h>

#include "pascals_triangle.h"

size_t **create_triangle(int rows) {
  int i, j;
  size_t **t = malloc(sizeof(size_t *) * (rows > 0 ? rows : 1));

  if (rows < 0)
    return (void *)(0);

  if (rows == 0) {
    t[0] = malloc(sizeof(size_t));
    t[0][0] = 0;
    return t;
  }

  for (i = 0; i < rows; i++) {
    t[i] = malloc(sizeof(size_t) * rows);
    for (j = 0; j < rows; j++)
      t[i][j] = i == 0 ? j == 0 : (j == 0 ? 1 : t[i - 1][j - 1] + t[i - 1][j]);
  }
  return t;
}

void free_triangle(size_t **t, int rows) {
  while (rows--)
    free(t[rows]);
  free(t);
}
