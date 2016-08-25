#include "raindrops.h"
#include <stdio.h>

char *convert(char *buffer, int size, int n) {
  int div3 = n % 3 == 0;
  int div5 = n % 5 == 0;
  int div7 = n % 7 == 0;

  if (div3 || div5 || div7) {
    snprintf(buffer, size, "%s%s%s", div3 ? "Pling" : "", div5 ? "Plang" : "",
             div7 ? "Plong" : "");
  } else {
    snprintf(buffer, size, "%d", n);
  }
  return buffer;
}
