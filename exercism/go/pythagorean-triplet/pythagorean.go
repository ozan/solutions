package pythagorean

import "math"

// Triplet is an ordered pythagorean triplet
type Triplet [3]int

// Range returns a slice of all triplets in the given range
func Range(min, max int) (out []Triplet) {
	for a := min; a <= max; a++ {
		for b := a + 1; b <= max; b++ {
			c := math.Sqrt(float64(a*a + b*b))
			if math.Floor(c) == c && int(c) <= max {
				out = append(out, Triplet{a, b, int(c)})
			}
		}
	}
	return
}

// Sum returns all Pythagorean triplets which sum to a given number
func Sum(p int) (out []Triplet) {
	for _, t := range Range(1, p/2) {
		if t[0]+t[1]+t[2] == p {
			out = append(out, t)
		}
	}
	return
}
