#include "triangle.h"

int valid(triangle_t t) {
  return t.a > 0 && t.b > 0 && t.c > 0 && t.a < t.b + t.c && t.b < t.a + t.c &&
         t.c < t.a + t.b;
}

int is_equilateral(triangle_t t) {
  return valid(t) ? t.a == t.b && t.b == t.c : 0;
}

int is_isosceles(triangle_t t) {
  int ab = t.a == t.b, bc = t.b == t.c, ca = t.c == t.a;
  return valid(t) ? ab + bc + ca > 0 : 0;
}

int is_scalene(triangle_t t) {
  return valid(t) ? t.a != t.b && t.b != t.c && t.c != t.a : 0;
}
