#ifndef PALINDROME_PRODUCTS_H
#define PALINDROME_PRODUCTS_H

typedef struct {
  int smallest;
  int largest;
} product_t;

product_t get_palindrome_product(int a, int b);

#endif
