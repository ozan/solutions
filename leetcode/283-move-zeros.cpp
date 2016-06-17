#include <vector>

using namespace std;

class Solution {
public:
  void moveZeroes(vector<int> &nums) {
    int slot = 0;
    for (int i = 0; i < nums.size(); i++) {
      int num = nums[i];
      if (num != 0 && i != 0) {
        for (int j = slot; j < i; j++) {
          if (nums[j] == 0) {
            nums[j] = num;
            nums[i] = 0;
            slot = j + 1;
            break;
          }
        }
      }
    }
  }
};
