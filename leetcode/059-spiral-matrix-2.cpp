#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> generateMatrix(int n) {
    auto M = emptyMatrix(n);
    int r = 0, c = 0, dr = 0, dc = 1;
    for (int k = 1; k <= n * n; k++) {
      M[r][c] = k;
      int nr = r + dr;
      int nc = c + dc;
      if (nr == -1 || nc == -1 || nr == n || nc == n || M[nr][nc] > 0) {
        if (dc == 0) {
          dc = -dr;
          dr = 0;
        } else {
          dr = dc;
          dc = 0;
        }
      }
      r += dr;
      c += dc;
    }
    return M;
  }

  vector<vector<int>> emptyMatrix(int n) {
    vector<vector<int>> M;
    for (int i = 0; i < n; i++) {
      vector<int> row;
      for (int j = 0; j < n; j++)
        row.push_back(0);
      M.push_back(row);
    }
    return M;
  }
};

int main() {
  Solution s;
  int n = 5;
  auto M = s.generateMatrix(n);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << M[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
