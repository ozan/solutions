/*
Write a function invert(x, p, n) that returns x with the n bits that begin at
position p inverted (i.e., 1 changed into 0 and vice versa), leaving the others
unchanged.
*/

unsigned long invert(unsigned long x, int p, int n) {
  return x ^ ((~(~0 << n)) << (p + 1 - n));
}
