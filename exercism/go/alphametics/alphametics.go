package alphametics

import "errors"

func Solve(puzzle string) (map[string]int, error) {
	letters := make([]byte, 0, 10) // the unique letters
	mappings := [128]byte{}        // the value assigned to each letter
	parts := [][]byte{}            // slice containing summands and total

	// parse the puzzle
	part := []byte{}
	for i := 0; i <= len(puzzle); i++ {
		var c byte = 0x00
		if i < len(puzzle) {
			c = puzzle[i]
		}
		switch c {
		case 0x00, ' ': // finalize part
			parts = append(parts, part)
			part = []byte{}
		case '=':
			i += 2
		case '+':
			i += 1
		default:
			if mappings[c] == 0 { // temporarily use `mappings` to check what's been seen
				letters = append(letters, c)
				mappings[c] = 1
			}
			part = append(part, c)
		}
	}

	// perform backtracking search over all possible value assignments
	values := make([]byte, 0, len(letters))
	var search func() bool
	search = func() bool {
		// base case: if all letters have been assigned a value,
		// check if this is a solution
		if len(values) == len(letters) {
			target := 0
			for i, s := range parts {
				v := 0
				for j := 0; j < len(s); j++ {
					v = v*10 + int(mappings[s[j]])
				}
				if i == len(parts)-1 {
					target += v
				} else {
					target -= v
				}
			}
			return target == 0
		}

		// general case: just assign the next value to the next letter
	AssignNext:
		for i := byte(0); i < 10; i++ {
			// skip if already assigned
			for _, v := range values {
				if i == v {
					continue AssignNext
				}
			}
			// skip if leading 0
			if i == 0 {
				for _, p := range parts {
					if letters[len(values)] == p[0] {
						continue AssignNext
					}
				}
			}
			// try assigning
			mappings[letters[len(values)]] = i
			values = append(values, i)
			if found := search(); found {
				return true
			}
			values = values[:len(values)-1]
		}
		return false
	}

	if found := search(); !found {
		return nil, errors.New("No solution")
	}
	// reformat into expected output
	out := make(map[string]int, len(values))
	for i, l := range letters {
		out[string(l)] = int(values[i])
	}
	return out, nil
}
