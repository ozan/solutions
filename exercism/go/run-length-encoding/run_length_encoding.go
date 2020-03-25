package encode

import "strconv"

func RunLengthEncode(in string) (out string) {
	var n = 1
	for i, x := range in {
		if i+1 < len(in) && x == rune(in[i+1]) {
			n += 1
			continue
		}
		if n > 1 {
			out += strconv.Itoa(n)
		}
		out += string(x)
		n = 1
	}
	return
}

func RunLengthDecode(in string) (out string) {
	var n = 0
	for _, c := range in {
		if '0' < c && c < '9' {
			n = n*10 + int(c-'0')
			continue
		}
		if n == 0 {
			n = 1
		}
		for ; n > 0; n-- {
			out += string(c)
		}
	}
	return
}
