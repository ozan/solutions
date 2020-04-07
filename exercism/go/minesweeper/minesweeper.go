package minesweeper

import "errors"

type delta struct{ i, j int }

var deltas = []delta{{-1, -1}, {0, -1}, {1, -1}, {-1, 0}, {1, 0}, {-1, 1}, {0, 1}, {1, 1}}
var invalidBoard = errors.New("Invalid board")

func (b *Board) Count() error {
	height, width := len(*b), 0
	for i, row := range *b {
		if i == 0 {
			width = len(row)
		}
		for j, x := range row {
			switch {
			case len(row) != width:
				return invalidBoard
			case i == 0 && j == 0,
				i == 0 && j == width-1,
				i == height-1 && j == 0,
				i == height-1 && j == width-1:
				if x != '+' {
					return invalidBoard
				}
			case i == 0,
				i == height-1:
				if x != '-' {
					return invalidBoard
				}
			case j == 0,
				j == width-1:
				if x != '|' {
					return invalidBoard
				}
			case x == '*':
				continue
			case x == ' ':
				var count byte = '0'
				for _, d := range deltas {
					if (*b)[i+d.i][j+d.j] == '*' {
						count += 1
					}
				}
				if count > '0' {
					row[j] = count
				}
			default:
				return invalidBoard
			}
		}
	}
	return nil
}
