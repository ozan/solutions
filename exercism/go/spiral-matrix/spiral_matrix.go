package spiralmatrix

func SpiralMatrix(n int) (matrix [][]int) {
	// initialize
	matrix = make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}
	// fill
	for i, j, di, dj, m := 0, 0, 0, 1, 1; m <= n*n; i, j, m = i+di, j+dj, m+1 {
		matrix[i][j] = m
		ii, jj := i+di, j+dj
		if jj == n || ii == n || jj < 0 || matrix[ii][jj] != 0 {
			di, dj = dj, -di
		}
	}
	return matrix
}
