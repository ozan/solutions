#include <string>
#include <vector>

namespace anagram {
class anagram {
  std::string subject;

public:
  anagram(std::string given) : subject(given) {}
  std::vector<std::string> matches(std::vector<std::string> candidates);
};
}
