#include "leap.h"

bool leap::is_leap_year(unsigned short int year) {
  return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
}
