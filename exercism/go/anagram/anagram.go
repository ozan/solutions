package anagram

import "strings"

// Detect selects anagrams of a given word among candidates
func Detect(subject string, candidates []string) (matches []string) {
	sLower := strings.ToLower(subject)
	sCounts := counts(sLower)
	for _, other := range candidates {
		oLower := strings.ToLower(other)
		if oLower == sLower {
			continue
		}
		if counts(oLower) == sCounts {
			matches = append(matches, other)
		}
	}
	return matches
}

func counts(s string) string {
	freqs := make([]byte, 26)
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c < 'a' || c > 'z' {
			continue
		}
		freqs[c-'a']++
	}
	return string(freqs)
}
