#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int a0 = 0; a0 < T; a0++) {
    int N;
    cin >> N;
    cout << N * (N - 1) / 2 << endl;
  }
  return 0;
}
