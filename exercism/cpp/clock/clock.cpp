#include "clock.h"
#include <stdio.h>
#include <string>

namespace date_independent {

clock::clock(int mins) { minutes = (mins % (24 * 60) + (24 * 60)) % (24 * 60); }

clock clock::at(int hours, int mins) { return clock(hours * 60 + mins); }

clock clock::plus(int mins) const { return clock(minutes + mins); }

clock clock::minus(int mins) const { return plus(-mins); }

bool clock::operator==(const clock &other) const {
  return minutes == other.minutes;
};
bool clock::operator!=(const clock &other) const { return !(*this == other); }

clock::operator string() const {
  char buffer[5];
  sprintf(buffer, "%02d:%02d", minutes / 60, minutes % 60);
  return buffer;
}
}
