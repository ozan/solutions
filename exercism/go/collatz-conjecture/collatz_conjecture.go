package collatzconjecture

import "errors"

func CollatzConjecture(n int) (steps int, e error) {
	if n < 1 {
		return -1, errors.New("n must be >= 1")
	}
	for n > 1 {
		if n&1 == 0 {
			n >>= 1
		} else {
			n = 3*n + 1
		}
		steps += 1
	}
	return
}
