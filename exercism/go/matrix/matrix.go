package matrix

import (
	"errors"
)

// Matrix is represented as row-major order 1d slice of ints
type Matrix struct {
	width  int
	values []int
}

// Rows returns a copy of the rows of the matrix
func (matrix *Matrix) Rows() [][]int {
	height := len(matrix.values) / matrix.width
	rows := make([][]int, height)
	for j := 0; j < height; j++ {
		rows[j] = make([]int, matrix.width)
		for i := 0; i < matrix.width; i++ {
			rows[j][i] = matrix.values[j*matrix.width+i]
		}
	}
	return rows
}

// Cols returns a copy of the columns of the matrix
func (matrix *Matrix) Cols() [][]int {
	height := len(matrix.values) / matrix.width
	cols := make([][]int, matrix.width)
	for i := 0; i < matrix.width; i++ {
		cols[i] = make([]int, height)
		for j := 0; j < height; j++ {
			cols[i][j] = matrix.values[j*matrix.width+i]
		}
	}
	return cols
}

// Set sets a given value to a given row/col
func (matrix *Matrix) Set(r, c, val int) bool {
	i := matrix.width*r + c
	if r < 0 || c < 0 || c >= matrix.width || i >= len(matrix.values) {
		return false
	}
	matrix.values[matrix.width*r+c] = val
	return true
}

// New parses and return a new Matrix from the given string
func New(s string) (*Matrix, error) {
	count := 0
	val := -1
	matrix := &Matrix{}

	pushValue := func() {
		matrix.values = append(matrix.values, val)
		val = -1
		count++
	}

	for i := 0; i <= len(s); i++ {
		switch {
		case i == len(s) || s[i] == '\n':
			// end of line: add to values and check or set width
			pushValue()
			if matrix.width == 0 {
				matrix.width = count
			}
			if matrix.width == 0 || count != matrix.width {
				return nil, errors.New("Inconsistent row widths")
			}
			count = 0
		case s[i] == ' ':
			// end of token: add to values
			if val != -1 {
				pushValue()
			}
		case s[i] >= '0' && s[i] <= '9':
			k := int(s[i] - '0')
			if val == -1 {
				val = k
			} else {
				prior := val
				val = 10*val + k
				if val <= prior {
					return nil, errors.New("Overflowing value")
				}
			}
		default:
			return nil, errors.New("Unexpected character")
		}
	}
	return matrix, nil
}
