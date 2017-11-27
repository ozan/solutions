package allergies

var allergens = [8]string{
	"eggs",
	"peanuts",
	"shellfish",
	"strawberries",
	"tomatoes",
	"chocolate",
	"pollen",
	"cats",
}

// Allergies lists all allergies for the score
func Allergies(score uint) (results []string) {
	var val uint = 1
	for _, candidate := range allergens {
		if score&val > 0 {
			results = append(results, candidate)
		}
		val <<= 1
	}
	return results
}

// AllergicTo determines if score matches given allergen
func AllergicTo(score uint, a string) bool {
	for i, candidate := range allergens {
		if candidate == a && (1<<uint(i))&score > 0 {
			return true
		}
	}
	return false
}
