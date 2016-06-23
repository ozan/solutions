#include "beer_song.h"
#include <iostream>
#include <sstream>

std::string beer::verse(int n) {
  switch (n) {
  case 0:
    return "No more bottles of beer on the wall, no more bottles of beer.\nGo "
           "to the store and buy some more, 99 bottles of beer on the wall.\n";
  case 1:
    return "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and "
           "pass it around, no more bottles of beer on the wall.\n";
  case 2:
    return "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down "
           "and pass it around, 1 bottle of beer on the wall.\n";
  default:
    std::stringstream ss;
    ss << n << " bottles of beer on the wall, " << n
       << " bottles of beer.\nTake one down and pass it around, " << n - 1
       << " bottles of beer on the wall.\n";
    return ss.str();
  }
}

std::string beer::sing(int start, int end) {
  std::stringstream ss;
  for (int i = start; i >= end; i--) {
    if (i != start)
      ss << '\n';
    ss << verse(i);
  }
  return ss.str();
}
