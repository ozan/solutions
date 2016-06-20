#include "space_age.h"

const long EARTH_SECONDS = 31557600;

float space_age::space_age::on_earth() const {
  return _seconds / (1.0 * EARTH_SECONDS);
}

float space_age::space_age::on_mercury() const {
  return _seconds / (0.2408467 * EARTH_SECONDS);
}

float space_age::space_age::on_venus() const {
  return _seconds / (0.61519726 * EARTH_SECONDS);
}

float space_age::space_age::on_mars() const {
  return _seconds / (1.8808158 * EARTH_SECONDS);
}

float space_age::space_age::on_jupiter() const {
  return _seconds / (11.862615 * EARTH_SECONDS);
}

float space_age::space_age::on_saturn() const {
  return _seconds / (29.447498 * EARTH_SECONDS);
}

float space_age::space_age::on_uranus() const {
  return _seconds / (84.016846 * EARTH_SECONDS);
}

float space_age::space_age::on_neptune() const {
  return _seconds / (164.79132 * EARTH_SECONDS);
}
