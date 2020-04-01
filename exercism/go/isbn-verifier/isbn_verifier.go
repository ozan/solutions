package isbn

func IsValidISBN(isbn string) bool {
	var n, sum byte = 10, 0 // slightly faster to avoid conversion from int
	for i := 0; i < len(isbn); i++ {
		c := isbn[i]
		switch {
		case c >= '0' && c <= '9':
			sum += n * (c - '0')
			n--
		case c == '-':
			continue
		case c == 'X' && n == 1:
			sum += 10
			n--
		default:
			return false
		}
		if n == 6 {
			sum %= 11 // byte can overflow otherwise
		}
	}
	return sum%11 == 0 && n == 0
}
