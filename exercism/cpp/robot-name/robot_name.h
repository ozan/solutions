#include <string>

namespace robot_name {
std::string rand_name();

class robot {
  std::string _name;

public:
  robot() { reset(); }
  const std::string name() const { return _name; }
  void reset() { _name = rand_name(); }
};
}
