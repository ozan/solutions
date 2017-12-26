package transpose

// Transpose returns a transposed matrix of characters
func Transpose(given []string) []string {
	// first, determine the size of the output as the
	// length of the longest input string
	outLen := 0
	for i := 0; i < len(given); i++ {
		if n := len(given[i]); n > outLen {
			outLen = n
		}
	}

	maxOut := len(given) // maxOut is the length of the longest string in the output
	out := make([]string, outLen)
	s := make([]byte, maxOut) // s will hold output strings as we construct them

	for i := 0; i < outLen; i++ {
		last := 0
		for j := 0; j < maxOut; j++ {
			if g := given[j]; len(g) > i {
				s[j] = g[i]
				last = j
			} else {
				s[j] = ' '
			}
		}
		out[i] = string(s[:last+1])
	}
	return out
}
