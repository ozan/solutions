#include "complex_numbers.h"
#include <math.h>

complex_t c_add(complex_t a, complex_t b)
{
  complex_t z = {.real = a.real + b.real, .imag = a.imag + b.imag};
  return z;
}

complex_t c_sub(complex_t a, complex_t b)
{
  complex_t z = {.real = a.real - b.real, .imag = a.imag - b.imag};
  return z;
}

complex_t c_mul(complex_t a, complex_t b)
{
  complex_t z = {.real = a.real * b.real - a.imag * b.imag,
                 .imag = a.imag * b.real + a.real * b.imag};
  return z;
}

complex_t c_div(complex_t a, complex_t b)
{
  double denom = b.real * b.real + b.imag * b.imag;
  complex_t z = {.real = (a.real * b.real + a.imag * b.imag) / denom,
                 .imag = (a.imag * b.real - a.real * b.imag) / denom};
  return z;
}

double c_abs(complex_t x) { return sqrt(x.real * x.real + x.imag * x.imag); }

complex_t c_conjugate(complex_t x)
{
  complex_t z = {.real = x.real, .imag = -x.imag};
  return z;
}

double c_real(complex_t x) { return x.real; }

double c_imag(complex_t x) { return x.imag; }

complex_t c_exp(complex_t x)
{
  double e_x = exp(x.real);
  complex_t z = {.real = e_x * cos(x.imag), .imag = e_x * sin(x.imag)};
  return z;
}
