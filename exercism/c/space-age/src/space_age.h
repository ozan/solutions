#ifndef SPACE_AGE_H
#define SPACE_AGE_H

typedef enum {
  EARTH,
  MERCURY,
  VENUS,
  MARS,
  JUPITER,
  SATURN,
  URANUS,
  NEPTUNE
} planet_t;

float convert_planet_age(planet_t planet, long age_in_seconds);

#endif
