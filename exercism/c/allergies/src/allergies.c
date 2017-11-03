#include <stdlib.h>

#include "allergies.h"

bool is_allergic_to(allergen_t allergen, int score) {
  return score & (1 << allergen);
}

void get_allergens(int score, allergen_list_t *allergen_list) {
  allergen_list->allergens = malloc(ALLERGEN_COUNT * sizeof(allergen_t));
  for (int i = 0; i < ALLERGEN_COUNT; i++)
    if (is_allergic_to(i, score))
      allergen_list->allergens[allergen_list->count++] = i;
}
