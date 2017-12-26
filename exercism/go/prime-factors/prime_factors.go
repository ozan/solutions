package prime

// Factors returns the prime factors of `n` in ascending order
func Factors(n int64) []int64 {
	var k int64 = 2
	factors := make([]int64, 0)
	for n > 1 {
		if n%k == 0 {
			factors = append(factors, k)
			n = n / k
		} else {
			k++
		}
	}
	return factors
}
