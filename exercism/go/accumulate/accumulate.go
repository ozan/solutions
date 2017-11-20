package accumulate

// Accumulate maps over the given data
func Accumulate(given []string, f func(string) string) []string {
	out := make([]string, len(given))
	for i, x := range given {
		out[i] = f(x)
	}
	return out
}
