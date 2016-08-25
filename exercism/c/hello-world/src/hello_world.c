#include "hello_world.h"
#include <stdio.h>

void hello(char *buffer, int size, char *name) {
  char *adressee = *name == '\0' ? "World" : name;
  snprintf(buffer, size, "Hello, %s!", adressee);
}
