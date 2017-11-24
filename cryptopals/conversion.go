package cryptopals

const hexSyms = "0123456789abcdef"
const base64Syms = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
const inv = 255 // sentinel byte for invalidity
var hexValues = [128]byte{
	inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
	inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, inv, inv, inv, inv, inv, inv,
	inv, 10, 11, 12, 13, 14, 15, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
	inv, 10, 11, 12, 13, 14, 15, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
}
var base64Values = [128]byte{
	inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv,
	inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, inv, 63, inv, inv, inv, 62, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, inv, inv, inv, 0, inv, inv,
	inv, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, inv, inv, inv, inv, inv,
	inv, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, inv, inv, inv, inv, inv,
}

// EncodeHex returns a hex string encoding of the given byte slice
func EncodeHex(bs []byte) string {
	out := make([]byte, len(bs)*2)
	for i := 0; i < len(bs); i++ {
		out[i<<1] = hexSyms[bs[i]>>4]
		out[i<<1^1] = hexSyms[bs[i]&0x0f]
	}
	return string(out)
}

// DecodeHex returns a slice of byte decodings of the hex chars in the given string
func DecodeHex(s string) []byte {
	out := make([]byte, len(s)/2)
	for i := 0; i < len(s); i += 2 {
		a, b := hexValues[s[i]], hexValues[s[i+1]]
		if a == inv || b == inv {
			panic("invalid hex symbol")
		}
		out[i/2] = a<<4 ^ b
	}
	return out
}

// EncodeBase64 returns a base64 string encoding of the given byte slice
func EncodeBase64(bs []byte) string {
	out := make([]byte, len(bs)*4/3)
	// TODO is this the expected behavior with null bytes?
	for i := 0; i < len(bs)%3; i++ {
		bs = append(bs, 0)
	}
	for i, j := 0, 0; i < len(bs); i += 3 {
		out[j] = base64Syms[bs[i]>>2]
		out[j+1] = base64Syms[(bs[i]&0x03)<<4^(bs[i+1]>>4)]
		out[j+2] = base64Syms[(bs[i+1]&0x0f)<<2^(bs[i+2]>>6)]
		out[j+3] = base64Syms[bs[i+2]&0x3f]
		j += 4
	}
	return string(out)
}

// DecodeBase64 return a byte slice representing the decoded form of the given b64 encoded string
func DecodeBase64(s string) []byte {
	out := make([]byte, len(s)*3/4)
	for i, j := 0, 0; i < len(s); i += 4 {
		// 4 b64 chars -> 3 bytes
		a, b, c, d := base64Values[s[i]], base64Values[s[i+1]], base64Values[s[i+2]], base64Values[s[i+3]]
		if a == inv || b == inv || c == inv || d == inv {
			panic("invalid base64 symbol")
		}
		out[j] = (a << 2) ^ (b >> 4)
		out[j+1] = (b&0x0f)<<4 ^ (c >> 2)
		out[j+2] = (c&0x03)<<6 ^ d
		j += 3
	}
	return out
}
