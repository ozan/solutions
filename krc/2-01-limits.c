/*
Write a program to determine the ranges of char, short, int and long variables,
both signed and unsigned, by printing appropriate values from standard headers
and by direct computation. Harder if you compute them: determine the ranges of
the various floating-point types.
*/

#include <float.h>
#include <limits.h>
#include <stdio.h>

int main() {

  printf("%-20s%d\n", "char min", CHAR_MIN);
  printf("%-20s%d\n", "char max", CHAR_MAX);
  printf("%-20s%d\n", "unsigned char max", UCHAR_MAX);
  printf("%-20s%d\n", "short min", SHRT_MIN);
  printf("%-20s%d\n", "short max", SHRT_MAX);
  printf("%-20s%d\n", "unsigned short max", USHRT_MAX);
  printf("%-20s%d\n", "int min", INT_MIN);
  printf("%-20s%d\n", "int max", INT_MAX);
  printf("%-20s%u\n", "unsigned int max", UINT_MAX);
  printf("%-20s%ld\n", "long min", LONG_MIN);
  printf("%-20s%ld\n", "long max", LONG_MAX);
  printf("%-20s%lu\n", "unsigned long max", ULONG_MAX);

  printf("%-20s%.10e\n", "float min", FLT_MIN);
  printf("%-20s%.10e\n", "float max", FLT_MAX);

  return 0;
}
