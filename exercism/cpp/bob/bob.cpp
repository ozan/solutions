#include <regex>
#include "bob.h"

// At least one upper case letter, no lower case letters
std::regex yelling("^[^a-z]+[A-Z][^a-z]+$");

// Question mark at the end
std::regex question("\\?\\W*$");

// Nothing but whitespace
std::regex silence("^\\W*$");

std::string bob::hey(const std::string &prompt) {
  if (regex_search(prompt, yelling))
    return "Whoa, chill out!";
  if (regex_search(prompt, question))
    return "Sure.";
  if (regex_search(prompt, silence))
    return "Fine. Be that way!";
  return "Whatever.";
}
