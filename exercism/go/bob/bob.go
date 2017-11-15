package bob

import (
	"unicode"
)

// Hey returns Bob's response to a remark
func Hey(remark string) string {
	var hasDigit, hasUpper, hasLower, isQuestion bool

	for _, ch := range remark {
		switch {
		case unicode.IsDigit(ch):
			hasDigit = true
		case unicode.IsLower(ch):
			hasLower = true
			isQuestion = false
		case unicode.IsUpper(ch):
			hasUpper = true
			isQuestion = false
		case ch == '?':
			isQuestion = true
		}
	}

	switch {
	case hasUpper && !hasLower:
		return "Whoa, chill out!"
	case isQuestion:
		return "Sure."
	case !hasUpper && !hasLower && !hasDigit:
		return "Fine. Be that way!"
	default:
		return "Whatever."
	}
}
