#include <string>
#include <vector>

namespace crypto_square {
class cipher {
  std::string text;
  const std::vector<std::string> chunk(int width, std::string chars) const;

public:
  cipher(std::string given);
  const std::string normalize_plain_text() const;
  unsigned int size() const;
  const std::vector<std::string> plain_text_segments() const;
  const std::string cipher_text() const;
  const std::string normalized_cipher_text() const;
};
}
