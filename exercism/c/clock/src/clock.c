#include <stdio.h>

#include "clock.h"

#define MINS_IN_DAY 1440

int modulo(int a, int b) { return a < 0 ? a % b + b : a % b; }

void clock(time_text_t time_text, int hour, int minute) {
  int mins = modulo(60 * hour + minute, MINS_IN_DAY);
  sprintf(time_text, "%02d:%02d", mins / 60, mins % 60);
}

void clock_add(time_text_t time_text, int minute_offset) {
  int hour, minute;
  sscanf(time_text, "%02d:%02d", &hour, &minute);
  clock(time_text, hour, minute + minute_offset);
}
