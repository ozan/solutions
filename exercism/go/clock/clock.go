package clock

import "fmt"

// Clock is a type represeting a time of day (in minutes and hours) but modelled as a single number of minutes
type Clock uint16

const minutesInDay int = 1440

func modulus(a, b int) uint {
	return uint((a%b + b) % b)
}

// New creates a new clock reflecting the given hours and minutes
func New(hour, minute int) Clock {
	return Clock(modulus(hour*60+minute, minutesInDay))
}

func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c/60, c%60)
}

// Add returns a new clock `minutes` ahead of (or behind) received clock
func (c Clock) Add(minutes int) Clock {
	return New(0, int(c)+minutes)
}
