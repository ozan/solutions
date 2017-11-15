package isogram

import "unicode"

// IsIsogram determines whether the given string is an isogram
func IsIsogram(letters string) bool {
	var bset, b uint32
	for _, ch := range letters {
		ch = unicode.ToLower(ch)
		if !unicode.IsLower(ch) {
			continue
		}
		b = 1 << (uint)(ch-'a')
		if (bset & b) > 0 {
			return false
		}
		bset |= b
	}
	return true
}
