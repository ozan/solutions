#include "grade_school.h"

const std::map<int, std::vector<std::string>> grade_school::school::roster() {
  return _roster;
}

void grade_school::school::add(std::string name, int grade) {
  _roster[grade].push_back(name);
  std::sort(_roster[grade].begin(), _roster[grade].end());
}

std::vector<std::string> grade_school::school::grade(int n) {
  return _roster[n];
}
