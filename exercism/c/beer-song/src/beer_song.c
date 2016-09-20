#include "beer_song.h"
#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 1024

void verse(char *out, int n) {
  switch (n) {
  case 0:
    strcpy(out,
           "No more bottles of beer on the wall, no more bottles of beer.\nGo "
           "to the store and buy some more, 99 bottles of beer on the wall.\n");
    break;
  case 1:
    strcpy(out,
           "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and "
           "pass it around, no more bottles of beer on the wall.\n");
    break;
  case 2:
    strcpy(out,
           "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down "
           "and pass it around, 1 bottle of beer on the wall.\n");
    break;
  default:
    snprintf(out, BUFFER_SIZE, "%d bottles of beer on the wall, %d bottles of "
                               "beer.\nTake one down and pass it around, %d "
                               "bottles of beer on the wall.\n",
             n, n, n - 1);
  }
}

void sing(char *out, int start, int end) {
  char buffer[BUFFER_SIZE], *target = out, *bp, ch;

  for (int i = start; i >= end; i--) {
    if (i != start)
      *target++ = '\n';
    verse(buffer, i);
    bp = buffer;
    while ((ch = *bp++) != '\0')
      *target++ = ch;
  }
  *target = '\0';
}
