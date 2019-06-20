#include <stdio.h>

void two_fer(char *response, char *name) {
  sprintf(response, "One for %s, one for me.", name ? name : "you");
}

