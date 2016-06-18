#include "phone_number.h"
#include <sstream>

phone_number::phone_number(const std::string &given) {
  std::stringstream ss;
  for (auto ch : given) {
    if (isdigit(ch))
      ss << ch;
  }
  auto candidate = ss.str();
  if (candidate.length() == 11 && candidate[0] == '1') {
    digits = candidate.substr(1);
  } else if (candidate.length() == 10) {
    digits = candidate;
  } else {
    digits = "0000000000";
  }
}

const std::string phone_number::number() const { return digits; }

const std::string phone_number::area_code() const {
  return digits.substr(0, 3);
}

phone_number::operator std::string() const {
  std::stringstream ss;
  ss << '(' << area_code() << ") " << digits.substr(3, 3) << '-'
     << digits.substr(6);
  return ss.str();
}
