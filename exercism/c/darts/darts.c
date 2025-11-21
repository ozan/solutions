#include "darts.h"

uint8_t score(coordinate_t c) {
  float dist_sq = c.x * c.x + c.y * c.y;
  if (dist_sq <= 1)
    return 10;
  if (dist_sq <= 25)
    return 5;
  if (dist_sq <= 100)
    return 1;
  return 0;
}
