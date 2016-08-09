#include <vector>

using namespace std;

class Solution {
public:
  int searchInsert(vector<int> &nums, int target) {
    int a = 0, b = nums.size() - 1;
    while (a <= b) {
      int cand = a + (b - a) / 2;
      int actual = nums[cand];
      if (target == actual)
        return cand;
      if (target < actual) {
        b = cand - 1;
      } else {
        a = cand + 1;
      }
    }
    return a;
  }
};

int main() {
  Solution s;
  int a[] = {1, 3, 5, 6};
  vector<int> v(a, a + 4);
  printf("%d (expected 2)\n", s.searchInsert(v, 5));
  printf("%d (expected 1)\n", s.searchInsert(v, 2));
  printf("%d (expected 4)\n", s.searchInsert(v, 7));
  printf("%d (expected 0)\n", s.searchInsert(v, 0));
  return 0;
}
