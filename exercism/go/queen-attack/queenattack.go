package queenattack

import "errors"

// CanQueenAttack determines if queens (in algebraic notation) are prone to attack
func CanQueenAttack(w, b string) (bool, error) {
	if len(w) != 2 || len(b) != 2 || // incorrect move format
		w[0] < 'a' || w[0] > 'h' || b[0] < 'a' || b[0] > 'h' || // off board vertically
		w[1] < '1' || w[1] > '8' || b[1] < '1' || b[1] > '8' || // off board horizontally
		w == b /* same square */ {
		return false, errors.New("Invalid arguments")
	}
	return w[0] == b[0] || w[1] == b[1] || delta(w[0], b[0]) == delta(w[1], b[1]), nil
}

func delta(a, b byte) byte {
	if a < b {
		a, b = b, a
	}
	return a - b
}
