package palindrome

import "errors"

// Product is a product and its factors
type Product struct {
	Product        int
	Factorizations [][2]int
}

const maxint32 = 1<<31 - 1

// Products returns min and max palindromic products, and their factors
func Products(fmin, fmax int) (pmin, pmax Product, err error) {
	if fmin > fmax {
		return pmin, pmax, errors.New("fmin > fmax")
	}
	pmin.Product = maxint32

	for a := fmin; a <= fmax; a++ {
		for b := a; b <= fmax; b++ {
			ab := a * b
			if isPalindrome(ab) {
				switch {
				case pmin.Product == ab:
					pmin.Factorizations = append(pmin.Factorizations, [2]int{a, b})
				case pmin.Product > ab:
					pmin = Product{ab, [][2]int{{a, b}}}
				case pmax.Product == ab:
					pmax.Factorizations = append(pmax.Factorizations, [2]int{a, b})
				case pmax.Product < ab:
					pmax = Product{ab, [][2]int{{a, b}}}
				}
			}
		}
	}
	if pmin.Product == maxint32 {
		return pmin, pmax, errors.New("no palindromes")
	}
	return pmin, pmax, nil
}

func isPalindrome(n int) bool {
	digits := make([]int, 20)
	i := 0
	for n > 0 {
		digits[i] = n % 10
		n /= 10
		i++
	}
	for j := i / 2; j >= 0; j-- {
		if digits[j] != digits[i-j-1] {
			return false
		}
	}
	return true
}
