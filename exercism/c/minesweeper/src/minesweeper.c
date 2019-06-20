#include <stdlib.h>
#include <string.h>

const char deltas[8][2] = {{-1, -1}, {0, -1}, {1, -1}, {1, 0},
                           {1, 1},   {0, 1},  {-1, 1}, {-1, 0}};

char **annotate(const char *minefield[], int rows) {
  int cols, i, j, c, d, ii, jj;
  char **annotation;

  if (rows == 0)
    return NULL;

  cols = strlen(minefield[0]);
  annotation = malloc(rows * sizeof(char *));

  for (i = 0; i < rows; i++) {
    annotation[i] = malloc(cols + 1);
    for (j = 0; j < cols; j++) {
      // mines stay mines
      if (minefield[i][j] == '*') {
        annotation[i][j] = '*';
        continue;
      }
      // spaces are filled with counts of adjacent mines
      c = 0;
      for (d = 0; d < 8; d++) {
        ii = i + deltas[d][0];
        jj = j + deltas[d][1];
        // ensure neighbor index is within bounds
        c += ii >= 0 && jj >= 0 && ii < rows && jj < cols &&
             minefield[ii][jj] == '*';
      }
      annotation[i][j] = c == 0 ? ' ' : '0' + c;
    }
    annotation[i][cols] = '\0';
  }
  return annotation;
}

void free_annotation(char **annotation) {
  if (annotation == NULL)
    return;
  int rows = sizeof(annotation) / sizeof(annotation[0]);
  while (--rows >= 0)
    free(annotation[rows]);
  free(annotation);
}

