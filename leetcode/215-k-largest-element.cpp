#include <queue>
#include <vector>

class Solution {
public:
  int findKthLargest(const std::vector<int> &nums, int k) {
    std::priority_queue<int> pq(nums.begin(), nums.end());
    for (int i = 0; i < k - 1; i++)
      pq.pop();
    return pq.top();
  }
};
