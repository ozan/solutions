#include "largest_series_product.h"

/*

Objective: solve in O(length of digits) time, using O(n) space, by keeping
a running product. In order to calculate the next candidate product, divide
by the (i - n)th digit then multiply by the ith digit.

For instance, given the digits 32142 and n=2, we have the state table:

i   digit seen  prod  max
.   .     [1,1] 1     1
0   3     [3,1] 3     1    // don't update max, yet
1   2     [3,2] 6     6    // prod/=1, prod*=2, update max
2   1     [1,2] 2     6    // prod/=seen[i%2] (2), prod *= 1
3   4     [1,4] 4     6
4   2     [2,4] 8     8

Zero is a special case: if one is encountered, reset state as if considering
the remaining substring as a new problem.
*/

long largest_series_product(char *digits, int n) {
  long max = 0, prod = 1, m = 0;
  char seen[n], c, i = 0;

  if (n == 0)
    return 1;

  while ((c = *digits++) != '\0') {
    m++;
    if (c < '0' || c > '9')
      return -1;
    if (c == '0') {
      prod = 1;
      i = 0;
      continue;
    }
    prod *= (c - '0');
    if (i >= n)
      prod /= seen[i % n];
    if (i >= (n - 1))
      max = prod > max ? prod : max;
    seen[i % n] = (c - '0');
    i++;
  }

  return m < n ? -1 : max;
}
