package darts

func Score(x, y float64) int {
	rsq := x*x + y*y // avoid sqrt
	switch {
	case rsq <= 1.0*1.0:
		return 10
	case rsq <= 5.0*5.0:
		return 5
	case rsq <= 10.0*10.0:
		return 1
	}
	return 0
}
