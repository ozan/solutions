package rotationalcipher

func RotationalCipher(in string, n int) (out string) {
	buf := make([]rune, 0, len(in))
	for _, c := range in {
		if c >= 'a' && c <= 'z' {
			c = 'a' + (c-'a'+rune(n))%26
		} else if c >= 'A' && c <= 'Z' {
			c = 'A' + (c-'A'+rune(n))%26
		}
		buf = append(buf, c)
	}
	return string(buf)
}
