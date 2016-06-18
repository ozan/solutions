#include "nucleotide_count.h"

dna::counter::counter(std::string bases) {
  for (auto b : bases) {
    counts[b] += 1;
  }
}

int dna::counter::count(char ch) const {
  try {
    return counts.at(ch);
  } catch (std::out_of_range) {
    throw std::invalid_argument("Not a nucleotide");
  }
}
