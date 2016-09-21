/*
Write a function rightrot(x, n) that returns the value of the integer x rotated
to the right by n bit positions.
*/

#include <limits.h>

unsigned rightrot(unsigned x, unsigned n) {
  unsigned mask = ~(~0 << n);
  return (x & mask) << (WORD_BIT - n) | x >> n;
}
