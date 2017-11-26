package perfect

import (
	"errors"
	"math"
)

// Classification is a designation as abundant, deficient or perfect
type Classification uint8

// ClassificationAbundant indicates that the sum of factors of a number is greater than the number
const (
	ClassificationAbundant Classification = iota
	ClassificationDeficient
	ClassificationPerfect
)

// ErrOnlyPositive indicates that an argument wasn't positive
var ErrOnlyPositive = errors.New("Must be positive")

// Classify determines the Classification of the given number
func Classify(n int64) (Classification, error) {
	var total, i int64
	if n <= 0 {
		return 0, ErrOnlyPositive
	}
	lim := int64(math.Sqrt(float64(n)))
	for i = 1; i <= lim; i++ {
		if n%i == 0 {
			total += i
			if i > 1 && n/i != i {
				total += n / i
			}
		}
	}
	if total == n && n > 1 {
		return ClassificationPerfect, nil
	}
	if total > n {
		return ClassificationAbundant, nil
	}
	return ClassificationDeficient, nil
}
