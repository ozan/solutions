#include <stdio.h>

void reverse(char *s, char *t) {
  char tmp;
  while (t > s) {
    tmp = *s;
    *s++ = *t;
    *t-- = tmp;
  }
}

void reverseWords(char *s) {
  char *t = s;
  while (*++t)
    ;
  reverse(s, t - 1);
  while (*s) {
    t = s;
    while (*s != ' ' && *s != '\0')
      s++;
    reverse(t, s - 1);
    s++;
  }
}

int main(int argc, char const *argv[]) {
  char words[] = "the sky is blue";
  reverseWords(words);
  puts(words);
  return 0;
}
