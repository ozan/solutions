#include "word_count.h"
#include <vector>

const std::string str(const std::vector<char> &vec) {
  return std::string(vec.begin(), vec.end());
}

bool is_delimiter(const char &ch) {
  return ch == ' ' || ch == '\n' || ch == ',';
}

const std::map<std::string, int> word_count::words(const std::string &phrase) {
  std::map<std::string, int> counts;

  std::vector<char> token;

  for (int i = 0; i < phrase.length(); i++) {
    auto &ch = phrase[i];
    if (is_delimiter(ch) && !token.empty()) {
      counts[str(token)] += 1;
      token = std::vector<char>();
    } else if (isalnum(ch) || (ch == '\'' && isalnum(phrase[i - 1]) &&
                               isalnum(phrase[i + 1]))) {
      token.push_back(tolower(ch));
    }
  }
  if (!token.empty())
    counts[str(token)] += 1;

  return counts;
}
