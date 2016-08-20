#include <iostream>
using namespace std;

int main() {
  int T, N;
  cin >> T;
  for (; T > 0; T--) {
    cin >> N;
    int counts[N], histo[N], i, v;
    long total = 1;

    // zero out counts and histogram
    for (i = 0; i < N; i++) {
      counts[i] = 0;
      histo[i] = 0;
    }

    // determine counts of each value
    for (i = 0; i < N; i++) {
      cin >> v;
      counts[v]++;
    }

    // construct histogram of counts <= each value
    histo[0] = counts[0];
    for (i = 1; i < N; i++)
      histo[i] = counts[i] + histo[i - 1];

    // calculate total posibilities
    for (i = 0; i < N; i++) {
      v = histo[i] - i;
      if (v <= 0) {
        total = 0;
        break;
      }
      total = (total * v) % 1000000007;
    }

    cout << total << endl;
  }
  return 0;
}
