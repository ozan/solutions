package twofer

import "fmt"

// ShareWith returns a phrase indicating with whom a thing is shared
func ShareWith(s string) string {
	if s == "" {
		s = "you"
	}
	return fmt.Sprintf("One for %s, one for me.", s)
}
