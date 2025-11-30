#include "rational_numbers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int16_t gcd(int16_t a, int16_t b) {
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

rational_t reduce(rational_t r) {
  int16_t d = abs(gcd(r.numerator, r.denominator));
  r.numerator = r.numerator / d;
  r.denominator = r.denominator / d;
  if (r.denominator < 0) {
    r.numerator = -r.numerator;
    r.denominator = -r.denominator;
  }
  return r;
}

rational_t add(rational_t a, rational_t b) {
  rational_t out = {a.numerator * b.denominator + b.numerator * a.denominator,
                    a.denominator * b.denominator};
  return reduce(out);
}

rational_t subtract(rational_t a, rational_t b) {
  rational_t out = {a.numerator * b.denominator - b.numerator * a.denominator,
                    a.denominator * b.denominator};
  return reduce(out);
}

rational_t multiply(rational_t a, rational_t b) {
  rational_t out = {a.numerator * b.numerator, a.denominator * b.denominator};
  return reduce(out);
}

rational_t divide(rational_t a, rational_t b) {
  rational_t out = {a.numerator * b.denominator, a.denominator * b.numerator};
  return reduce(out);
}

rational_t absolute(rational_t r) {
  rational_t out = {abs(r.numerator), abs(r.denominator)};
  return reduce(out);
}

rational_t exp_rational(rational_t r, int16_t n) {
  rational_t out;
  if (n > 0) {
    out.numerator = pow(r.numerator, n);
    out.denominator = pow(r.denominator, n);
  } else {
    int16_t m = abs(n);
    out.numerator = pow(r.denominator, m);
    out.denominator = pow(r.numerator, m);
  }
  return reduce(out);
}

float exp_real(int16_t x, rational_t r) {
  return pow(pow(x, r.numerator), 1. / r.denominator);
}
