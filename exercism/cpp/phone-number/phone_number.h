#include <string>

class phone_number {
  std::string digits;

public:
  phone_number(const std::string &given);
  const std::string number() const;
  const std::string area_code() const;
  operator std::string() const;
};
