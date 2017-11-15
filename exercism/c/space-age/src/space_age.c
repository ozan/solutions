#include "space_age.h"

static const float YEAR_SECONDS[] = {31557600.0,    7600543.82,   19414149.05,
                                     59354032.69,   374355659.12, 929292362.88,
                                     2651370019.33, 5200418560.03};

float convert_planet_age(planet_t planet, long age_in_seconds) {
  return age_in_seconds / YEAR_SECONDS[planet];
}
