package lsproduct

/*
Objective: solve in O(length of digits) time, using O(span) space, by keeping
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

import "errors"

// LargestSeriesProduct returns the largest product of `span` consecutive digits
func LargestSeriesProduct(digits string, span int) (int, error) {
	var max, i int
	prod := 1

	switch {
	case span == 0:
		return 1, nil
	case span < 0:
		return -1, errors.New("Span must be >= 0")
	case span > len(digits):
		return -1, errors.New("Span exceeds given digits")
	}

	seen := make([]byte, span)

	for m := 0; m < len(digits); m++ {
		c := digits[m] - '0'
		switch {
		case c == 0:
			prod = 1
			i = 0
		case c < 0 || c > 9:
			return -1, errors.New("Invalid character")
		default:
			prod *= int(c)
			if i >= span {
				prod /= int(seen[i%span])
			}
			if i >= span-1 && prod > max {
				max = prod
			}
			seen[i%span] = c
			i++
		}
	}
	return max, nil
}
