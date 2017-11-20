package triangle

import "math"

// Kind is a kind of triangle
type Kind uint8

const (
	// NaT is an invalid triangl
	NaT = 0
	// Equ (ilateral) triangles have 1 total unique side lengths
	Equ = 1 // equilateral
	// Iso (sceles) triangles have 2 total unique side lengths
	Iso = 2 // isosceles
	// Sca (lene) triangles have 3 total unique side lengths
	Sca = 3 // scalene
)

// KindFromSides determines the triangle kind given 3 side lengths
func KindFromSides(a, b, c float64) Kind {
	switch {
	case a <= 0 || b <= 0 || c <= 0 || math.IsNaN(a+b+c) || math.IsInf(a+b+c, 0) || a+b < c || a+c < b || b+c < a:
		return NaT
	case a == b && b == c && c == a:
		return Equ
	case a == b || b == c || c == a:
		return Iso
	default:
		return Sca
	}
}
