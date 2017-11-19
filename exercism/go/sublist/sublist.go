package sublist

// Relation is a type of string
type Relation string

// Sublist determines if there's a sub or superlist, or equality relationship between given lists
func Sublist(a, b []int) Relation {
	switch {
	case len(a) == len(b) && prefixEqual(a, b):
		return "equal"
	case len(a) > len(b) && isSublist(b, a):
		return "superlist"
	case isSublist(a, b):
		return "sublist"
	default:
		return "unequal"
	}
}

func isSublist(a, b []int) bool {
	if len(b) < len(a) {
		return false
	}
	return prefixEqual(a, b) || isSublist(a, b[1:])
}

func prefixEqual(a, b []int) bool {
	for i, aa := range a {
		if b[i] != aa {
			return false
		}
	}
	return true
}
