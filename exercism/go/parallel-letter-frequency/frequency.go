package letter

// FreqMap is a count per rune
type FreqMap map[rune]int

// Frequency sequentially counts the frequency of each rune in the given string
func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

// ConcurrentFrequency counts frequency of each rune with 1 goroutine per member of ss
func ConcurrentFrequency(ss []string) FreqMap {
	c := make(chan FreqMap, len(ss))
	m := FreqMap{}
	for _, s := range ss {
		go func(s string) {
			c <- Frequency(s)
		}(s)
	}
	for range ss {
		for k, v := range <-c {
			m[k] += v
		}
	}
	return m
}
