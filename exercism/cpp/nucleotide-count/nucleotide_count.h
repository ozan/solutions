#include <map>
#include <sstream>
#include <string>

namespace dna {
class counter {
  std::map<char, int> counts = {{'A', 0}, {'T', 0}, {'C', 0}, {'G', 0}};

public:
  counter(std::string bases);
  std::map<char, int> nucleotide_counts() const { return counts; };
  int count(char ch) const;
};
}
