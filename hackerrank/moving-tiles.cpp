#include <cmath>
#include <iostream>
using namespace std;

double t(int v, int L, double qi) {
  return (sqrt(2.0) * (L - sqrt(qi))) / abs(v);
}

int main() {
  int L, S1, S2, Q;
  cin >> L >> S1 >> S2 >> Q;
  for (int i = 0; i < Q; i++) {
    double qi;
    cin >> qi;
    printf("%.17g\n", t(S2 - S1, L, qi));
  }
  return 0;
}
