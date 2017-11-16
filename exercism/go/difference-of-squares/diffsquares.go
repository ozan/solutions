package diffsquares

// SquareOfSums returns the square of the sum of the first n integers
func SquareOfSums(n int) int {
	sum := n * (n + 1) >> 1
	return sum * sum
}

// SumOfSquares returns the sum of the first n squares
func SumOfSquares(n int) int {
	return n * (n + 1) * (2*n + 1) / 6
}

// Difference return the difference between the square of sums and sum of squares
func Difference(n int) int {
	return SquareOfSums(n) - SumOfSquares(n)
}
