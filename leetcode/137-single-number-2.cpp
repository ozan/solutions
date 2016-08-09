#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int singleNumber(vector<int> &nums) {
    int single = 0;
    for (int i = 0; i < 32; i++) {
      int n_has = 0;
      for (int n : nums) {
        n_has += (n >> i) & 1;
      }
      if (n_has % 3 == 1)
        single += 1 << i;
    }
    return single;
  }
};

int main(int argc, char const *argv[]) {
  Solution s;
  vector<int> v = {-2, -2, 1, 1, -3, 1, -3, -3, -4, -2};
  printf("%d\n", s.singleNumber(v));
  return 0;
}
