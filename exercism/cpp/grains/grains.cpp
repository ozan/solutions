#include "grains.h"

uint64_t grains::square(int n) { return static_cast<uint64_t>(1) << (n - 1); }

uint64_t grains::total() { return static_cast<uint64_t>(-1); }
