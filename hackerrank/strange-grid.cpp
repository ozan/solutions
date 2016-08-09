#include <iostream>
using namespace std;

int f(int r, int c) { return (r - 1) / 2 * 10 + (r + 1) % 2 + (c - 1) * 2; }

int main() {
  int r, c;
  cin >> r >> c;
  cout << f(r, c) << endl;
  return 0;
}
