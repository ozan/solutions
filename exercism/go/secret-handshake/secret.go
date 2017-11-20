package secret

// Handshake returns a secret handshake
func Handshake(n uint) (res []string) {
	if n&1 == 1 {
		res = append(res, "wink")
	}
	if n&2 == 2 {
		res = append(res, "double blink")
	}
	if n&4 == 4 {
		res = append(res, "close your eyes")
	}
	if n&8 == 8 {
		res = append(res, "jump")
	}
	if n&16 == 16 {
		for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
			res[i], res[j] = res[j], res[i]
		}
	}
	return
}
