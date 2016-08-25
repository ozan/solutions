#include "anagram.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void count_chars(int *counts, char *word) {
  char ch; // TODO handle non-ascii
  while ((ch = *word++) != '\0')
    counts[tolower(ch)]++;
}

struct Vector anagrams_for(char *target, struct Vector vin) {
  char(*matches)[MAX_STR_LEN] =
      (char(*)[MAX_STR_LEN])malloc(vin.size * MAX_STR_LEN);
  int num_matches = 0;

  // Count frequency of target characters
  int target_counts[128] = {0};
  count_chars(target_counts, target);

  for (int i = 0; i < vin.size; i++) {
    // If case insensitive same as target, ignore
    if (0 == strcasecmp(target, vin.vec[i]))
      continue;

    // Count frequency of candidate characters
    int candidate_counts[128] = {0};
    count_chars(candidate_counts, vin.vec[i]);

    // Anagram if frequencies are identical
    if (0 == memcmp(target_counts, candidate_counts, sizeof(target_counts)))
      strcpy(matches[num_matches++], vin.vec[i]);
  }

  struct Vector vout = {matches, num_matches};
  return vout;
}
