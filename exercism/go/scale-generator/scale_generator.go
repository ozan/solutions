package scale

import "strings"

func Scale(tonic, interval string) (scale []string) {
	var baseScale []string
	switch tonic {
	case "C", "G", "D", "A", "E", "B", "F#", "a", "e", "b", "f#", "c#", "g#", "d#":
		baseScale = []string{"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"}

	case "F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb":
		baseScale = []string{"C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"}
	}
	// find starting index within baseScale
	var si int
	tonic = strings.Title(tonic)
	for i, x := range baseScale {
		if tonic == x {
			si = i
			break
		}
	}
	// stride through baseScale as a ring
	if interval == "" {
		interval = "mmmmmmmmmmmm"
	}
	for _, x := range interval {
		scale = append(scale, baseScale[si%12])
		si += strings.IndexRune(" mMA", x)
	}
	return
}
