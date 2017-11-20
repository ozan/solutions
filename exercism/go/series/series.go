package series

// All returns all substrings of length n of s
func All(n int, s string) []string {
	subs := make([]string, len(s)-n+1)
	for i := 0; i < len(s)-n+1; i++ {
		subs[i] = s[i : i+n]
	}
	return subs
}

// UnsafeFirst returns first substring of length n of s
func UnsafeFirst(n int, s string) string {
	return s[:n]
}

// First returns first substring, if possible
func First(n int, s string) (first string, ok bool) {
	if len(s) < n {
		return
	}
	return s[:n], true
}
