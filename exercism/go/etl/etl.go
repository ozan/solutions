package etl

// Transform returns a transformed scrabble score format
func Transform(given map[int][]string) map[string]int {
	out := make(map[string]int)
	for k, v := range given {
		for _, c := range v {
			out[string(c[0]+32)] = k
		}
	}
	return out
}
