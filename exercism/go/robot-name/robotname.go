package robotname

// Robot is 5 bytes
type Robot [5]byte

var seen = map[string]bool{}
var seed = 1

func rand() int {
	seed = (1103515245*seed + 12345) % (2 << 31)
	return seed
}

// Name returns the robot name, setting it if needed
func (r *Robot) Name() string {
	if string(r[:5]) == "\x00\x00\x00\x00\x00" {
		r.Reset()
	}
	return string(r[:5])
}

// Reset forces reset of the robot name
func (r *Robot) Reset() {
	r[0] = byte('A' + rand()%26)
	r[1] = byte('A' + rand()%26)
	r[2] = byte('0' + rand()%10)
	r[3] = byte('0' + rand()%10)
	r[4] = byte('0' + rand()%10)
	s := string(r[:5])
	if seen[s] {
		r.Reset()
		return
	}
	seen[s] = true
}
