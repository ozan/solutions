#include <assert.h>
#include <string>

using namespace std;

class Solution {
public:
  bool isNumber(string s) {
    bool nonempty_encounted = false;
    bool late_space_encountered = false;
    bool dot_encountered = false;
    bool e_encountered = false;
    bool digit_after_e = false;
    bool digit_encountered = false;

    for (int i = 0; i < s.length(); i++) {
      char ch = s[i];

      if (ch == ' ') {
        if (nonempty_encounted)
          late_space_encountered = true;
        continue;
      }

      if (ch != ' ') {
        nonempty_encounted = true;
        if (late_space_encountered)
          return false;
      }

      if (ch == '.') {
        if (dot_encountered || e_encountered)
          return false;
        dot_encountered = true;
        continue;
      }

      if (ch == 'e') {
        if (e_encountered || !digit_encountered)
          return false;
        if (dot_encountered && !digit_encountered)
          return false;
        e_encountered = true;
        continue;
      }

      if (ch == '-') {
        if (digit_encountered && s[i - 1] != 'e')
          return false;
        if (dot_encountered && !digit_encountered)
          return false;
        continue;
      }

      if (ch == '+') {
        if ((dot_encountered || digit_encountered) && s[i - 1] != 'e')
          return false;
        continue;
      }

      if (ch < '0' || ch > '9')
        return false;

      if (e_encountered)
        digit_after_e = true;

      digit_encountered = true;
    }

    if (e_encountered && !digit_after_e)
      return false;

    return digit_encountered;
  }
};

int main() {
  Solution s;
  assert(!s.isNumber(" "));
  assert(!s.isNumber("e9"));
  assert(s.isNumber("0"));
  assert(s.isNumber(" 0 "));
  assert(!s.isNumber("1 1"));
  assert(!s.isNumber("a"));
  assert(s.isNumber(" 0.1 "));
  assert(!s.isNumber("0.0.1"));
  assert(!s.isNumber("abc"));
  assert(!s.isNumber("1 a"));
  assert(s.isNumber("2e10"));
  assert(!s.isNumber("2e"));
  assert(!s.isNumber("."));
  assert(s.isNumber("3."));
  assert(s.isNumber("-1."));
  assert(s.isNumber("3e-4"));
  assert(!s.isNumber("3-e10"));
  assert(!s.isNumber("3e1-0"));
  assert(!s.isNumber(".-4"));
  assert(s.isNumber("+.8"));
  assert(!s.isNumber(".+8"));
  assert(!s.isNumber("6+1"));
  assert(s.isNumber("0050407e+6"));
  assert(s.isNumber("1.38354e+8"));
  /* code */
  return 0;
}
