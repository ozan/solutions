#include <string>

using namespace std;

namespace date_independent {
class clock {
  int minutes;
  explicit clock(int mins);

public:
  static clock at(int hours, int mins = 0);
  clock plus(int mins) const;
  clock minus(int mins) const;
  bool operator==(const clock &other) const;
  bool operator!=(const clock &other) const;
  explicit operator string() const;
};
}
