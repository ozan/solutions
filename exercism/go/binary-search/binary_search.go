package binarysearch

func SearchInts(ints []int, x int) (i int) {
	for a, b := 0, len(ints); a < b; {
		mid := a + (b-a)>>1 // (a + b) / 2 can overflow
		probe := ints[mid]
		if x == probe {
			return mid
		}
		if x < probe {
			b = mid
		} else {
			a = mid + 1
		}
	}
	return -1
}
