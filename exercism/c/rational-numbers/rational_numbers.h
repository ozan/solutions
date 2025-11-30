#ifndef RATIONAL_NUMBERS_H
#define RATIONAL_NUMBERS_H

#include <stdint.h>

typedef struct {
  int16_t numerator, denominator;
} rational_t;

rational_t add(rational_t, rational_t);
rational_t subtract(rational_t, rational_t);
rational_t multiply(rational_t, rational_t);
rational_t divide(rational_t, rational_t);
rational_t absolute(rational_t);
rational_t exp_rational(rational_t, int16_t);
float exp_real(int16_t, rational_t);
rational_t reduce(rational_t);

#endif
