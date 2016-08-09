#include <iostream>
using namespace std;

int main() {
  int n_cases;
  cin >> n_cases;
  for (int i = 0; i < n_cases; i++) {
    int total = 1;
    int n_towns, n_paths;
    cin >> n_towns;
    for (int ti = 0; ti < n_towns - 1; ti++) {
      cin >> n_paths;
      total = (total * n_paths) % 1234567;
    }
    cout << total << endl;
  }

  return 0;
}
