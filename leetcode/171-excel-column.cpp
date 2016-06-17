#include <assert.h>
#include <string>

using namespace std;

class Solution {
public:
  int titleToNumber(string s) {
    int total = 0, factor = 1;
    int len = s.length();
    for (int i = 0; i < len; i++) {
      char ch = s[len - i - 1];
      total += (ch - 'A' + 1) * factor;
      factor *= 26;
    }
    return total;
  }
};

int main(int argc, char const *argv[]) {
  assert((new Solution())->titleToNumber("A") == 1);
  assert((new Solution())->titleToNumber("AB") == 28);
  return 0;
}
