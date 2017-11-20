package house

import "bytes"

var parts = []string{
	"the horse and the hound and the horn\nthat belonged to ",
	"the farmer sowing his corn\nthat kept ",
	"the rooster that crowed in the morn\nthat woke ",
	"the priest all shaven and shorn\nthat married ",
	"the man all tattered and torn\nthat kissed ",
	"the maiden all forlorn\nthat milked ",
	"the cow with the crumpled horn\nthat tossed ",
	"the dog\nthat worried ",
	"the cat\nthat killed ",
	"the rat\nthat ate ",
	"the malt\nthat lay in ",
	"the house that Jack built.",
}

// Verse constructs just the nth verse of the song
func Verse(n int) string {
	var b bytes.Buffer
	b.WriteString("This is ")
	for _, v := range parts[len(parts)-n:] {
		b.WriteString(v)
	}
	return b.String()
}

// Song constructs the entire song
func Song() string {
	var b bytes.Buffer
	for n := 1; n <= len(parts); n++ {
		if n > 1 {
			b.WriteString("\n\n")
		}
		b.WriteString(Verse(n))
	}
	return b.String()
}
