package prime

// Nth returns the Nth prime
func Nth(n int) (int, bool) {
	if n == 0 {
		return 0, false
	}

	primes := make([]int, n)
	k, p := 0, 2

	for ; k < n; p++ {
		// if any prime divides p, it is not prime
		for i := 0; i < k; i++ {
			if p%primes[i] == 0 {
				goto next
			}
		}
		primes[k] = p
		k++
	next:
	}
	return p - 1, true
}
