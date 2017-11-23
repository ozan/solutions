package sieve

// Sieve performs Eratosthenes sieve to find primes up to given limit
func Sieve(limit int) []int {
	sieve := make([]bool, limit+1) // TODO could use bitset instead of bool array
	primes := make([]int, 0)

	for p := 2; p <= limit; p++ {
		if sieve[p] {
			continue
		}
		primes = append(primes, p)
		for q := p; q <= limit; q += p {
			sieve[q] = true
		}
	}
	return primes
}
