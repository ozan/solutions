#include "resistor_color.h"

uint16_t color_code(resistor_band_t color) { return color; }

const resistor_band_t color_arr[] = {BLACK, BROWN, RED,    ORANGE, YELLOW,
                                     GREEN, BLUE,  VIOLET, GREY,   WHITE};

const resistor_band_t *colors(void) { return color_arr; }
