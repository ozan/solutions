package phonenumber

import (
	"errors"
	"fmt"
)

// Number cleans the given phone number, if possible
func Number(given string) (string, error) {
	out := make([]byte, len(given))
	outI := 0
	for i := 0; i < len(given); i++ {
		c := given[i]
		switch {
		case c == '(' || c == ')' || c == ' ' || c == '+' || c == '-' || c == '.':
			continue
		case c >= '0' && c <= '9':
			out[outI] = c
			outI++
		default:
			return "", errors.New("Invalid input character")
		}
	}
	if outI == 11 && out[0] == '1' {
		out = out[1:]
	} else if outI != 10 {
		return "", errors.New("Invalid number of digits")
	}
	if out[0] < '2' {
		return "", errors.New("Area code must start with 2-9")
	}
	if out[3] < '2' {
		return "", errors.New("Exchange code must start with 2-9")
	}
	return string(out[:10]), nil
}

// AreaCode retrieves the area code of the cleaned phone number, if valid
func AreaCode(given string) (string, error) {
	clean, err := Number(given)
	if err != nil {
		return clean, err
	}
	return clean[:3], nil
}

// Format returns the standard format of the cleaned number, if valid
func Format(given string) (string, error) {
	clean, err := Number(given)
	if err != nil {
		return clean, err
	}
	return fmt.Sprintf("(%s) %s-%s", clean[:3], clean[3:6], clean[6:10]), nil
}
