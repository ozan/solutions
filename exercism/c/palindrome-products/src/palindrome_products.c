#include <limits.h>
#include <string.h>

#include "palindrome_products.h"

int is_palindrome(int n) {
  int i = 0, j;
  char digits[10];
  memset(digits, 0, 10);
  while (n > 0) {
    digits[i++] = n % 10;
    n /= 10;
  }
  for (j = i << 1; j >= 0; j--)
    if (digits[j] != digits[i - j - 1])
      return 0;
  return 1;
}

product_t get_palindrome_product(int a, int b) {
  int ax, bx, ab;
  product_t product = {INT_MAX, -1};

  for (ax = a; ax <= b; ax++) {
    for (bx = ax; bx <= b; bx++) {
      ab = ax * bx;
      if (is_palindrome(ab)) {
        product.smallest = (product.smallest < ab ? product.smallest : ab);
        product.largest = (product.largest > ab ? product.largest : ab);
      }
    }
  }
  return product;
}
