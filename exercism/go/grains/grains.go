package grains

import "errors"

// Square returns the number of grains of rice on the nth square
//
// Note: would be better for n to be uint8, but I'm conforming with existing
// test cases.
func Square(n int) (uint64, error) {
	if n < 1 || n > 64 {
		return 0, errors.New("Input n must be in range [1, 64]")
	}
	return 1 << (uint(n) - 1), nil
}

// Total returns the sum of grains on the entire board
func Total() uint64 {
	return 0xffffffffffffffff
}
