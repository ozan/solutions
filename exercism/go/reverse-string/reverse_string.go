package reverse

// String reverses the given string
func String(in string) string {
	n := len(in)
	out := make([]byte, n)
	for i := 0; i < n; i++ {
		out[n-i-1] = in[i]
	}
	return string(out)
}
