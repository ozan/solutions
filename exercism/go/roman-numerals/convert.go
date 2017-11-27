package romannumerals

import (
	"bytes"
	"errors"
)

var decimals = [13]int{
	1000, 900, 500, 400, 100, 90,
	50, 40, 10, 9, 5, 4, 1}
var romans = [13]string{
	"M", "CM", "D", "CD", "C", "XC",
	"L", "XL", "X", "IX", "V", "IV", "I"}

// ToRomanNumeral converts given integer to roman numeral form
func ToRomanNumeral(n int) (string, error) {
	if n <= 0 || n > 3000 {
		return "", errors.New("Given value not in range")
	}

	var buf bytes.Buffer
	var i int

	for n > 0 {
		for decimals[i] > n {
			i++
		}
		buf.WriteString(romans[i])
		n -= decimals[i]
	}

	return buf.String(), nil
}
