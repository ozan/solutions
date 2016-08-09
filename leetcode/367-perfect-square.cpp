#include <iostream>

class Solution {
public:
  bool isPerfectSquare(int num) {
    if (num == 0)
      return true;
    long a = 1, b = num;
    while (b >= a) {
      printf("%ld, %ld\n", a, b);
      long cand = a + (b - a) / 2;
      long sq = cand * cand;
      if (num == sq)
        return true;
      if (num < sq) {
        b = cand - 1;
      } else {
        a = cand + 1;
      }
    }
    return false;
  }
};

int main() {
  Solution s;
  printf("%d: %d\n", 2147483647, s.isPerfectSquare(2147483647));
  // for (int i = 0; i < 20; i++) {
  //   printf("%d: %d\n", i, s.isPerfectSquare(i));
  // }
  return 0;
}
