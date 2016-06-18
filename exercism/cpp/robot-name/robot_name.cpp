#include "robot_name.h"
#include <sstream>

auto alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
auto numeric = "0123456789";

char rand_alpha() { return alpha[rand() % 26]; }

char rand_numeric() { return numeric[rand() % 10]; }

std::string robot_name::rand_name() {
  std::stringstream ss;
  ss << rand_alpha() << rand_alpha() << rand_numeric() << rand_numeric()
     << rand_numeric();
  return ss.str();
}
