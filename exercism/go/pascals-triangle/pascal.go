package pascal

// Triangle returns the first n rows of Pascal's triangle
func Triangle(n int) [][]int {
	rows := make([][]int, n)
	for i := 0; i < n; i++ {
		rows[i] = make([]int, i+1)
		rows[i][0] = 1
		rows[i][i] = 1
		for j := 1; j < i; j++ {
			rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
		}
	}
	return rows
}
