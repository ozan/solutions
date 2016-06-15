#include "anagram.h"
#include <boost/algorithm/string.hpp>

std::string key(const std::string &given) {
  std::string normalized = boost::algorithm::to_lower_copy(given);
  std::sort(normalized.begin(), normalized.end());
  return normalized;
}

std::vector<std::string>
anagram::anagram::matches(std::vector<std::string> candidates) {
  std::string target = key(subject);
  std::vector<std::string> matching;
  for (const auto &candidate : candidates) {
    if (key(candidate) == target &&
        boost::algorithm::to_lower_copy(candidate) !=
            boost::algorithm::to_lower_copy(subject))
      matching.push_back(candidate);
  }
  return matching;
}
