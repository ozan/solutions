#include <assert.h>
#include <vector>

using namespace std;

class Solution {
public:
  int lengthOfLIS(vector<int> &nums) {
    int memo[nums.size()];
    int global_max = 0;

    for (int i = 0; i < nums.size(); i++) {
      int max = 0;
      for (int j = 0; j < i; j++) {
        if (nums[j] < nums[i] && memo[j] > max) {
          max = memo[j];
        }
      }
      memo[i] = max + 1;
      if (max + 1 > global_max)
        global_max = max + 1;
    }

    return global_max;
  }
};

int main() {
  Solution s;
  vector<int> given = {10, 9, 2, 5, 3, 7, 101, 18};
  vector<int> longer = {1, 3, 6, 7, 9, 4, 10, 5, 6};
  assert(s.lengthOfLIS(given) == 4);
  assert(s.lengthOfLIS(longer) == 6);
  return 0;
}
