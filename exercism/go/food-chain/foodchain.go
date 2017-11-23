// class FoodChain {
//   verse (n) {
//     const [animal, excl] = animals[n]
//     const theReasons = n === 8 ? '' : takeRight(n, reasons).join('\n') + '\n'
//     return `I know an old lady who swallowed a ${animal}.${excl}\n${theReasons}`
//   }
//   verses (n, m) {
//     return range(n, m + 1).map(this.verse).join('\n') + '\n'
//   }
// }

package foodchain

import "bytes"

var animals = []string{
	"fly.\n",
	"spider.\nIt wriggled and jiggled and tickled inside her.\n",
	"bird.\nHow absurd to swallow a bird!\n",
	"cat.\nImagine that, to swallow a cat!\n",
	"dog.\nWhat a hog, to swallow a dog!\n",
	"goat.\nJust opened her throat and swallowed a goat!\n",
	"cow.\nI don't know how she swallowed a cow!\n",
	"horse.\nShe's dead, of course!",
}

var reasons = []string{
	"She swallowed the cow to catch the goat.\n",
	"She swallowed the goat to catch the dog.\n",
	"She swallowed the dog to catch the cat.\n",
	"She swallowed the cat to catch the bird.\n",
	"She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.\n",
	"She swallowed the spider to catch the fly.\n",
	"I don't know why she swallowed the fly. Perhaps she'll die.",
}

// Verse constructs the nth verse of the song
func Verse(n int) string {
	var b bytes.Buffer
	b.WriteString("I know an old lady who swallowed a ")
	b.WriteString(animals[n-1])
	for i := len(reasons) - n; i >= 0 && i < len(reasons); i++ {
		b.WriteString(reasons[i])
	}
	return b.String()
}

// Verses returns all verses in a range
func Verses(n, m int) string {
	var b bytes.Buffer
	for ; n <= m; n++ {
		b.WriteString(Verse(n))
		if n < m {
			b.WriteString("\n\n")
		}
	}
	return b.String()
}

// Song creates the entire song
func Song() string {
	return Verses(1, 8)
}
