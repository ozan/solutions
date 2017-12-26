package igpay

import "strings"

// PigLatin converts the given string according to the pig latin rules
func PigLatin(phrase string) string {
	english := strings.Split(phrase, " ")
	latin := make([]string, len(english))
	for i, word := range english {
		isVowel := false
		n := 1
		for _, r := range rules {
			if head := word[:len(r.stem)]; head == r.stem {
				isVowel = r.isVowel
				n = len(r.stem)
				break
			}
		}
		if isVowel {
			latin[i] = word + "ay"
		} else {
			latin[i] = word[n:] + word[:n] + "ay"
		}
	}
	return strings.Join(latin, " ")
}

var rules = []struct {
	stem    string
	isVowel bool
}{
	{"ch", false}, {"qu", false}, {"squ", false}, {"thr", false}, {"th", false}, {"sch", false},
	{"yt", true}, {"xr", true}, {"a", true}, {"e", true}, {"i", true}, {"o", true}, {"u", true},
}
