package wordsearch

import "errors"

var bearings = [][]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}

func Solve(words, puzzle []string) (map[string][2][2]int, error) {
	location := make(map[string][2][2]int)
	for _, w := range words {
		for i, row := range puzzle {
			for j := 0; j < len(row); j++ {
			NextBearing:
				for _, b := range bearings {
					ii, jj := i, j
					for cidx := 0; cidx < len(w); cidx, ii, jj = cidx+1, ii+b[0], jj+b[1] {
						if ii < 0 || jj < 0 || ii >= len(puzzle) || jj >= len(row) || puzzle[ii][jj] != w[cidx] {
							continue NextBearing
						}
					}
					location[w] = [2][2]int{{j, i}, {jj - b[1], ii - b[0]}}
				}
			}
		}
		if _, ok := location[w]; !ok {
			return nil, errors.New("No match")
		}
	}
	return location, nil
}
