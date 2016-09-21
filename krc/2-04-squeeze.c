/*
Write an alternate version of squeeze(s1, s2) that deletes each character is s1
that matches any character in the string s2.
*/

#include <stdio.h>

void squeeze(char *s1, char *s2) {
  int i, j, flag;
  char ch, *sp;

  for (i = j = 0; s1[i] != '\0'; i++) {
    flag = 0;
    sp = s2;
    while ((ch = *sp++))
      flag = flag || s1[i] == ch;

    if (!flag)
      s1[j++] = s1[i];
  }
  s1[j] = '\0';
}

int main() {
  char s1[] = "abcdefg";
  squeeze(s1, "acf");
  printf("%s\n", s1);
  return 0;
}
