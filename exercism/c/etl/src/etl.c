#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "etl.h"

int cmp(const void *a, const void *b) {
  return ((new_map *)a)->key - ((new_map *)b)->key;
}

int convert(legacy_map input[], int input_len, new_map *output[]) {
  int len = 0, n = 0, i;
  char *val, c;

  // first pass, count letters
  for (i = 0; i < input_len; i++)
    len += strlen(input[i].value);

  // allocate output array
  *output = malloc(len * sizeof(new_map));

  // second pass, fill in output
  for (i = 0; i < input_len; i++) {
    val = input[i].value;
    while ((c = *val++)) {
      (*output)[n].key = tolower(c);
      (*output)[n].value = input[i].key;
      n++;
    }
  }

  // output is expected to be sorted
  qsort(*output, n, sizeof(new_map), cmp);

  return len;
}

