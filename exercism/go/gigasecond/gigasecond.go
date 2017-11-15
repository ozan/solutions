package gigasecond

import "time"

const gigasecond = 1000000000 * time.Second

// AddGigasecond returns a time 1,000,000,000 seconds later than given time
func AddGigasecond(t time.Time) time.Time {
	return t.Add(gigasecond)
}
