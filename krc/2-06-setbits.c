/*
Write a function setbits(x, p, n, y) that returns x with the n bits that begin
at position p set to the rightmost n bits of y, leaving the other bits
unchanged.
*/

#include <stdlib.h>

unsigned long setbits(unsigned long x, unsigned int p, unsigned int n,
                      unsigned long y) {
  unsigned long mask = ~(~0 << n);
  return (x & ~(mask << (p - n + 1))) | (y & mask) << (p - n + 1);
}
