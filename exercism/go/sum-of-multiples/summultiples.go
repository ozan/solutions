package summultiples

// SumMultiples calculates sum of multiples of given divisors up to given limit
func SumMultiples(limit int, divisors ...int) (sum int) {
	for n := 1; n < limit; n++ {
		for _, d := range divisors {
			if n%d == 0 {
				sum += n
				break
			}
		}
	}
	return
}
