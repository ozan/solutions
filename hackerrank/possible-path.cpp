#include <iostream>
using namespace std;

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

bool can_reach(int a, int b, int x, int y) { return gcd(a, b) == gcd(x, y); }

int main() {
  int n;
  cin >> n;

  for (int i = 0; i < n; i++) {
    int a, b, x, y;
    cin >> a >> b >> x >> y;
    cout << (can_reach(a, b, x, y) ? "YES" : "NO") << endl;
  }
  return 0;
}
