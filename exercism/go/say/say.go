package say

// Say converts the given integer to an english phrase
func Say(n int64) (string, bool) {
	if n < 0 || n >= 1e12 {
		return "", false
	}
	if n == 0 {
		return "zero", true
	}
	return sayPart(n, ""), true
}

func sayPart(n int64, prefix string) string {
	for _, p := range parts {
		high, low := n/p.value, n%p.value
		if high == 0 {
			continue
		}
		if p.value < 100 {
			return prefix + p.name + sayPart(low, "-")
		}
		return sayPart(high, prefix) + " " + p.name + sayPart(low, " ")
	}
	return ""
}

var parts = []struct {
	value int64
	name  string
}{
	{1000000000, "billion"},
	{1000000, "million"},
	{1000, "thousand"},
	{100, "hundred"},
	{90, "ninety"},
	{80, "eighty"},
	{70, "seventy"},
	{60, "sixty"},
	{50, "fifty"},
	{40, "forty"},
	{30, "thirty"},
	{20, "twenty"},
	{19, "nineteen"},
	{18, "eighteen"},
	{17, "seventeen"},
	{16, "sixteen"},
	{15, "fifteen"},
	{14, "fourteen"},
	{13, "thirteen"},
	{12, "twelve"},
	{11, "eleven"},
	{10, "ten"},
	{9, "nine"},
	{8, "eight"},
	{7, "seven"},
	{6, "six"},
	{5, "five"},
	{4, "four"},
	{3, "three"},
	{2, "two"},
	{1, "one"},
}
