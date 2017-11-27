package wordcount

// import "fmt"

// Frequency is a mapping of words to their counts
type Frequency map[string]int

// WordCount returns the frequency of words in the given phrase
func WordCount(phrase string) Frequency {
	freqs := make(Frequency, 0)
	word := make([]byte, 20)
	wi := 0
	var d byte

	// copy each string, up to a delimiter, out of phrase
	for i := 0; i < len(phrase); i++ {
		c := phrase[i]
		if i == len(phrase)-1 {
			d = 0x00
		} else {
			d = phrase[i+1]
		}

		// downcase
		if c >= 'A' && c <= 'Z' {
			c += 32
		}

		// add c to token if a-z0-9 or ' not at start of token
		if alphanum(c) || (c == '\'' && wi != 0 && alphanum(d)) {
			word[wi] = c
			wi++
		}

		// count token if non-alphanumed char or end of string
		if wi != 0 && (!alphanum(c) && !(c == '\'' && alphanum(d)) || d == 0x00) {
			extracted := string(word[:wi])
			freqs[extracted]++
			wi = 0
		}

	}

	return freqs
}

func alphanum(c byte) bool {
	return (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')
}
