package brackets

// Bracket determines if the given string is validly parenthesized
func Bracket(chars string) (bool, error) {
	var b, c byte
	si := 0
	stack := make([]byte, len(chars)>>1+1)

	for i := 0; i < len(chars); i++ {
		c = chars[i]
		switch c {
		case '(', '{', '[':
			stack[si] = c
			si++
		case ')', '}', ']':
			if si == 0 {
				return false, nil // too many righthand symbols
			}
			b = stack[si-1]
			si--
			if b == '(' && c != ')' || b == '{' && c != '}' || c == '[' && c != ']' {
				return false, nil // mismatch
			}
		}
	}
	return si == 0, nil // very not too many lefthand symbols
}
