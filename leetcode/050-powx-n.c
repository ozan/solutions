#include <assert.h>

double myPow(double x, long n) {
  if (n == 0)
    return 1.0;
  if (n < 0)
    return 1.0 / myPow(x, -n);
  double sub = myPow(x, n / 2);
  return sub * sub * (n % 2 ? x : 1);
}

int main(int argc, char const *argv[]) {
  assert(myPow(2.0, 0) == 1.0);
  assert(myPow(2.0, 1) == 2.0);
  assert(myPow(2.0, 2) == 4.0);
  assert(myPow(2.0, 3) == 8.0);
  assert(myPow(34.00515, -3) - 0.000025 < 0.0001);
  assert(myPow(1.0, -2147483648) == 1.0);
  return 0;
}
