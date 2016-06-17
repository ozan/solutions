#include "food_chain.h"
#include <sstream>

std::string exclamations[] = {
    "",
    "fly.",
    "spider.\nIt wriggled and jiggled and tickled inside her.",
    "bird.\nHow absurd to swallow a bird!",
    "cat.\nImagine that, to swallow a cat!",
    "dog.\nWhat a hog, to swallow a dog!",
    "goat.\nJust opened her throat and swallowed a goat!",
    "cow.\nI don't know how she swallowed a cow!",
    "horse.\nShe's dead, of course!"};

std::string reasons[] = {
    "She swallowed the cow to catch the goat.",
    "She swallowed the goat to catch the dog.",
    "She swallowed the dog to catch the cat.",
    "She swallowed the cat to catch the bird.",
    "She swallowed the bird to catch the spider that wriggled and jiggled and "
    "tickled inside her.",
    "She swallowed the spider to catch the fly.",
    "I don't know why she swallowed the fly. Perhaps she'll die."};

const std::string food_chain::verse(int n) {
  std::stringstream ss;
  ss << "I know an old lady who swallowed a ";
  ss << exclamations[n] << '\n';
  if (n < 8) {
    for (int i = 7 - n; i < 7; i++) {
      ss << reasons[i] << '\n';
    }
  }
  return ss.str();
}

const std::string food_chain::verses(int a, int b) {
  std::stringstream ss;
  for (int i = a; i <= b; i++)
    ss << verse(i) << '\n';
  return ss.str();
}

const std::string food_chain::sing() { return verses(1, 8); }
