package acronym

import (
	"unicode"
)

// Abbreviate returns an acronym extracted from s
func Abbreviate(s string) string {
	prior := ' '
	acronym := make([]rune, 0)
	for _, c := range s {
		if prior == ' ' || prior == '-' {
			acronym = append(acronym, unicode.ToUpper(c))
		}
		prior = c
	}
	return string(acronym)
}
