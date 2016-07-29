#include <stdio.h>

int getSum(int a, int b) {
  int total = a ^ b;
  int c = a & b;
  while (c != 0) {
    c <<= 1;
    int temp = total ^ c;
    c = total & c;
    total = temp;
  }
  return total;
}

int main(int argc, char const *argv[]) {
  printf("%d\n", getSum(1, 2));
  printf("%d\n", getSum(4, -1));
  return 0;
}
