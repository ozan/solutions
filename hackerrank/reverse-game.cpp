#include <iostream>

using namespace std;

int f(int N, int K) { return K < N / 2 ? 2 * K + 1 : 2 * (N - K - 1); }

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, K;
    cin >> N >> K;
    cout << f(N, K) << endl;
  }
  return 0;
}
