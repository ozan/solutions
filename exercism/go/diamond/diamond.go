package diamond

import "errors"

// Gen generates the diamond
func Gen(letter byte) (string, error) {
	if letter < 'A' || letter > 'Z' {
		return "", errors.New("Letter out of range")
	}
	dim := 1 + 2*(letter-'A')
	bs := make([]byte, int(dim)*(int(dim)+1)) // extra +1 needed for \n
	i := 0
	var col byte
	back := false
	for c := byte('A'); c >= 'A'; {
		for col = 0; col < dim; col++ {
			if letter-c == col || letter-c == dim-col-1 {
				bs[i] = c
			} else {
				bs[i] = ' '
			}
			i++
		}
		bs[i] = '\n'
		i++
		if c == letter {
			back = true
		}
		if back {
			c--
		} else {
			c++
		}
	}
	return string(bs), nil
}
