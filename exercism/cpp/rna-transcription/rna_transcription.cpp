#include "rna_transcription.h"
#include <sstream>
#include <unordered_map>

char transcription::to_rna(char base) {
  static const std::unordered_map<char, char> mapping = {
      {'G', 'C'}, {'C', 'G'}, {'T', 'A'}, {'A', 'U'}};
  return mapping.at(base);
}

std::string transcription::to_rna(std::string bases) {
  std::stringstream ss;
  for (auto &ch : bases)
    ss << transcription::to_rna(ch);
  return ss.str();
}
