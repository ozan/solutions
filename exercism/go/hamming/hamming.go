package hamming

import "errors"

// Distance returns hamming distance between given strings
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return -1, errors.New("Input strings must be of equal length")
	}
	count := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			count++
		}
	}
	return count, nil
}
