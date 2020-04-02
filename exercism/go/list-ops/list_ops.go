package listops

type IntList []int
type binFunc func(x, y int) int
type unaryFunc func(x int) int
type predFunc func(x int) bool

func (xs IntList) Foldl(fn binFunc, y int) int {
	for _, x := range xs {
		y = fn(y, x)
	}
	return y
}

func (xs IntList) Foldr(fn binFunc, y int) int {
	for i := len(xs) - 1; i >= 0; i-- {
		y = fn(xs[i], y)
	}
	return y
}

func (xs IntList) Filter(fn predFunc) IntList {
	out := []int{}
	for _, x := range xs {
		if fn(x) {
			out = append(out, x)
		}
	}
	return out
}

func (xs IntList) Length() (n int) {
	return len(xs)
}

func (xs IntList) Reverse() IntList {
	n := xs.Length()
	for i := 0; i < n/2; i++ {
		xs[i], xs[n-i-1] = xs[n-i-1], xs[i]
	}
	return xs
}

func (xs IntList) Map(fn unaryFunc) IntList {
	out := make([]int, xs.Length())
	for i, x := range xs {
		out[i] = fn(x)
	}
	return out
}

func (xs IntList) Append(ys IntList) IntList {
	xs = append(xs, ys...)
	return xs
}

func (xs IntList) Concat(yss []IntList) IntList {
	for _, ys := range yss {
		xs = append(xs, ys...)
	}
	return xs
}
