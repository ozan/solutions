#include <stdio.h>
#include <string.h>

#include "meetup.h"

int weekday(int y, int m, int d) {
  return (d += m < 3 ? y-- : y - 2,
          23 * m / 9 + d + 4 + y / 4 - y / 100 + y / 400) %
         7;
}

int days_in_month(int y, int m) {
  if (m == 2)
    return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0) ? 29 : 28;
  return (m == 4 || m == 6 || m == 9 || m == 11) ? 30 : 31;
}

int weekday_for_day(char *day) {
  if (strcmp(day, "Sunday") == 0)
    return 0;
  if (strcmp(day, "Monday") == 0)
    return 1;
  if (strcmp(day, "Tuesday") == 0)
    return 2;
  if (strcmp(day, "Wednesday") == 0)
    return 3;
  if (strcmp(day, "Thursday") == 0)
    return 4;
  if (strcmp(day, "Friday") == 0)
    return 5;
  if (strcmp(day, "Saturday") == 0)
    return 6;
  return -1;
}

int offset_for_descriptor(char *descriptor, int year, int month) {
  if (strcmp(descriptor, "first") == 0)
    return 1;
  if (strcmp(descriptor, "second") == 0)
    return 8;
  if (strcmp(descriptor, "third") == 0)
    return 15;
  if (strcmp(descriptor, "fourth") == 0)
    return 22;
  if (strcmp(descriptor, "fifth") == 0)
    return 29;
  if (strcmp(descriptor, "teenth") == 0)
    return 13;
  if (strcmp(descriptor, "last") == 0)
    return days_in_month(year, month) - 6;
  return -1;
}

int meetup_day_of_month(int year, int month, char *descriptor, char *day) {
  int offset = offset_for_descriptor(descriptor, year, month);
  int first_weekday = weekday(year, month, offset);
  int target_weekday = weekday_for_day(day);

  if (days_in_month(year, month) < offset)
    return 0;
  return offset + (target_weekday - first_weekday + 7) % 7;
}
