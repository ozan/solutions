package cryptosquare

// Encode returns the square encoding of the given plain text
func Encode(pt string) string {

	cleaned := make([]byte, len(pt))
	nChars, width, nextSquare := 0, 0, 1

	// extract the valid characters, calculating the rectangle width
	// as we go (to avoid a later sqrt)
	for i := 0; i < len(pt); i++ {
		c := pt[i]
		// discard most invalid chars: will deal with rest later
		if c < '0' || (c > '9' && c < 'A') || c == 0x60 {
			continue
		}
		// can safely force lower case
		c |= 0x20
		// and deal with remaining invalid chars
		if c > 'z' {
			continue
		}
		cleaned[nChars] = c
		nChars++
		// when we encounter a square, it means me can widen the rectangle
		if nChars == nextSquare {
			width++
			nextSquare += width + width + 1
		}
	}
	if width*width < nChars {
		width++
	}
	if width == 0 {
		return ""
	}
	height := (nChars-1)/width + 1

	// perform the transpose, interleaving spaces as needed
	encrypted := make([]byte, nChars+width)
	for i, c := 0, 0; c < width; c++ {
		for r := 0; r <= height; r++ {
			if r*width+c >= nChars {
				encrypted[i] = ' '
				i++
				break
			}
			encrypted[i] = cleaned[r*width+c]
			i++
		}
	}
	return string(encrypted[:len(encrypted)-1])
}
