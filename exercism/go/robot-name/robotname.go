package robotname

import (
	"fmt"
	"math/rand"
)

// Robot is a value in [0, 676000) since 676,000 = 26*26*10*10*10
type Robot uint32

const numAvailableNames = 676000

var queue = rand.Perm(numAvailableNames)
var queuePos uint

// Name returns the robot name, setting it if needed
func (r *Robot) Name() string {
	if *r == 0 {
		r.Reset()
	}
	return r.String()
}

// Reset forces reset of the robot name
func (r *Robot) Reset() {
	queuePos++
	if queuePos >= numAvailableNames {
		panic("No more available names")
	}
	*r = Robot(queuePos)
}

// String computes the string form of the robot's uint value
// TODO this could be cached to avoid repeat computation, if the same
// robot's name is known to be accessed repeatedly
func (r *Robot) String() string {
	n := uint32(queue[*r])
	return string(fmt.Sprintf("%c%c%d%d%d", 'A'+n/26000, 'A'+(n%26000)/1000, (n%1000)/100, (n%100)/10, n%10))
}
