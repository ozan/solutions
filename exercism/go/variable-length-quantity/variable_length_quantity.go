package variablelengthquantity

import "errors"

func EncodeVarint(ints []uint32) (out []byte) {
	for i := len(ints) - 1; i >= 0; i-- {
		n := ints[i]
		var high byte = 0x00
		for {
			out = append(out, high^byte(n&0x7f))
			n >>= 7
			high = 0x80
			if n == 0 {
				break
			}
		}
	}
	reverse(out)
	return
}

func DecodeVarint(bytes []byte) (ints []uint32, e error) {
	if bytes[len(bytes)-1]&0x80 != 0 {
		return nil, errors.New("Incomplete sequence")
	}
	var n uint32
	for _, b := range bytes {
		n = (n << 7) ^ uint32(b&0x7f)
		if b&0x80 == 0 {
			ints = append(ints, n)
			n = 0
		}
	}
	return
}

func reverse(a []byte) {
	for i := len(a)/2 - 1; i >= 0; i-- {
		opp := len(a) - 1 - i
		a[i], a[opp] = a[opp], a[i]
	}
}
