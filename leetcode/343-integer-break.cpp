/*

Recurence:

f(1) = 1
f(n) = max(f(k) * f(n-k) for k in range [1, n // 2])

Strategy: use dynamic programming, store greatest product summing to
all k up to n

f(2) = 1 * 1 = 1
f(3) = 1 * 2 = 2
f(4) =

*/

#include <algorithm>
#include <assert.h>

class Solution {
public:
  int integerBreak(int n) {
    int memo[n + 1];
    memo[1] = 1;
    for (int i = 2; i <= n; i++) {
      int max;
      for (int k = 1; k <= i / 2; k++) {
        int left = std::max(k, memo[k]);
        int right = std::max(i - k, memo[i - k]);
        int prod = left * right;
        if (prod > max)
          max = prod;
      }
      memo[i] = max;
    }
    return memo[n];
  }
};

int main(int argc, char const *argv[]) {
  Solution s;
  assert(s.integerBreak(2) == 1);
  assert(s.integerBreak(3) == 2);
  assert(s.integerBreak(10) == 36);
  return 0;
}
