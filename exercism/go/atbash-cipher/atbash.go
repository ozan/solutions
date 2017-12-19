package atbash

import "bytes"

// Atbash encodes text using the atbash cipher
func Atbash(plaintext string) string {
	var b bytes.Buffer
	var c, x byte
	for i, n := 0, 0; i < len(plaintext); i++ {
		c = plaintext[i]
		switch {
		case c >= '0' && c <= '9':
			x = c
		case c >= 'A' && c <= 'Z':
			x = 187 - c // 187 = 'a' + 'Z'
		case c >= 'a' && c <= 'z':
			x = 219 - c // 219 = 'a' + 'z'
		default:
			continue
		}
		if n%5 == 0 && n != 0 {
			b.WriteByte(' ')
		}
		b.WriteByte(x)
		n++
	}
	return b.String()
}
