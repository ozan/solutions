#include <stdlib.h>
#include <string.h>

#include "series.h"

series_results_t series(char *input_text, unsigned int substring_length) {
  unsigned int input_length = strlen(input_text), i, j;
  series_results_t *r = malloc(sizeof(series_results_t));

  if (substring_length == 0) {
    r->substring_count = 0;
    return *r;
  }

  r->substring_count = input_length - substring_length + 1;
  r->substring = malloc(sizeof(char *) * r->substring_count);

  for (i = 0; i < r->substring_count; i++) {
    r->substring[i] = malloc(substring_length + 1);
    for (j = 0; j < substring_length; j++)
      r->substring[i][j] = input_text[i + j];
    r->substring[i][j] = '\0';
  }
  return *r;
}
