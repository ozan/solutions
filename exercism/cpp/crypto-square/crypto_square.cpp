#include "crypto_square.h"
#include <math.h>
#include <sstream>

namespace crypto_square {

cipher::cipher(std::string given) {
  std::stringstream ss;
  for (char ch : given) {
    if (isdigit(ch))
      ss << ch;
    else if (isalpha(ch))
      ss << static_cast<char>(tolower(ch));
  }
  text = ss.str();
}

const std::string cipher::normalize_plain_text() const { return text; }

unsigned int cipher::size() const {
  return static_cast<unsigned int>(ceil(sqrt(text.length())));
}

const std::vector<std::string> cipher::chunk(int width,
                                             std::string chars) const {
  std::vector<std::string> segments;
  for (int i = 0; i < chars.length(); i += width) {
    segments.push_back(chars.substr(i, width));
  }
  return segments;
}

const std::vector<std::string> cipher::plain_text_segments() const {
  return chunk(size(), text);
}

const std::string cipher::cipher_text() const {
  auto segments = plain_text_segments();
  auto width = size();
  std::stringstream ss;

  for (int i = 0; i < width; i++) {
    for (int j = 0; j < segments.size(); j++) {
      char ch = segments[j][i];
      if (ch)
        ss << ch;
    }
  }
  return ss.str();
}

const std::string cipher::normalized_cipher_text() const {
  auto segments = chunk(size(), cipher_text());
  std::stringstream ss;
  for (int i = 0; i < segments.size(); i++) {
    if (i != 0)
      ss << ' ';
    ss << segments[i];
  }
  return ss.str();
}
}
