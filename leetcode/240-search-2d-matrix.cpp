#include <vector>

using namespace std;

class Solution {
public:
  bool searchMatrix(const vector<vector<int>> &matrix, int target) {
    const int height = matrix.size(), width = matrix.at(0).size();
    int i = 0, j = width - 1;
    while (i < height && j >= 0) {
      int val = matrix[i][j];
      if (val == target)
        return true;
      if (val < target)
        i += 1;
      if (val > target)
        j -= 1;
    }
    return false;
  }
};
