#include <map>
#include <sstream>
#include <string>
#include <vector>

namespace grade_school {
class school {
  std::map<int, std::vector<std::string>> _roster;

public:
  const std::map<int, std::vector<std::string>> roster();
  void add(std::string name, int grade);
  std::vector<std::string> grade(int n);
};
}
