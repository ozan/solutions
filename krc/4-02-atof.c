#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

double my_atof(char *s) {
  double val, power;
  int i, sign, exponent, expsign = 1;

  for (i = 0; isspace(s[i]); i++)
    ; // skip white space
  sign = (s[i] == '-') ? -1 : 1;

  if (s[i] == '+' || s[i] == '-')
    i++;
  for (val = 0.0; isdigit(s[i]); i++)
    val = 10.0 * val + (s[i] - '0');
  if (s[i] == '.')
    i++;
  for (power = 1.0; isdigit(s[i]); i++) {
    val = 10.0 * val + (s[i] - '0');
    power *= 10.0;
  }
  if (s[i] == 'e' || s[i] == 'E')
    i++;
  if (s[i] == '-') {
    expsign = -1;
    i++;
  }
  for (exponent = 0; isdigit(s[i]); i++)
    exponent = 10 * exponent + (s[i] - '0');
  return sign * val / power * pow(10, expsign * exponent);
}

int near_equal(double a, double b) { return fabs(a - b) < 0.0001; }

int main() {
  assert(my_atof("1.234") == 1.234);
  assert(near_equal(my_atof("1.1e2"), 110.0));
  assert(near_equal(my_atof("1.1e-2"), 0.011));
  return 0;
}
