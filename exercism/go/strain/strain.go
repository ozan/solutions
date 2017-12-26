package strain

type Ints []int
type Lists [][]int
type Strings []string

// Keep ints passing the predicate
func (xs Ints) Keep(f func(int) bool) Ints {
	if xs == nil {
		return nil
	}
	out := make(Ints, 0)
	for _, x := range xs {
		if f(x) {
			out = append(out, x)
		}
	}
	return out
}

// Discard ints failing the predicate
func (xs Ints) Discard(f func(int) bool) Ints {
	if xs == nil {
		return nil
	}
	out := make(Ints, 0)
	for _, x := range xs {
		if !f(x) {
			out = append(out, x)
		}
	}
	return out
}

// Keep lists of ints passing the predicate
func (xs Lists) Keep(f func([]int) bool) Lists {
	if xs == nil {
		return nil
	}
	out := make(Lists, 0)
	for _, x := range xs {
		if f(x) {
			out = append(out, x)
		}
	}
	return out
}

// Keep strings passing the predicate
func (xs Strings) Keep(f func(string) bool) Strings {
	if xs == nil {
		return nil
	}
	out := make(Strings, 0)
	for _, x := range xs {
		if f(x) {
			out = append(out, x)
		}
	}
	return out
}
