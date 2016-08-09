#include <iostream>
using namespace std;

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int a, b, d;
    cin >> a >> b;
    d = gcd(a, b);
    cout << (a / d) * (b / d) << endl;
  }
  return 0;
}
