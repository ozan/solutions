package twelve

import (
	"bytes"
)

var gifts = []string{
	"a Partridge in a Pear Tree.",
	"two Turtle Doves, ",
	"three French Hens, ",
	"four Calling Birds, ",
	"five Gold Rings, ",
	"six Geese-a-Laying, ",
	"seven Swans-a-Swimming, ",
	"eight Maids-a-Milking, ",
	"nine Ladies Dancing, ",
	"ten Lords-a-Leaping, ",
	"eleven Pipers Piping, ",
	"twelve Drummers Drumming, ",
}

var ordinals = []string{
	"On the first day of Christmas my true love gave to me, ",
	"On the second day of Christmas my true love gave to me, ",
	"On the third day of Christmas my true love gave to me, ",
	"On the fourth day of Christmas my true love gave to me, ",
	"On the fifth day of Christmas my true love gave to me, ",
	"On the sixth day of Christmas my true love gave to me, ",
	"On the seventh day of Christmas my true love gave to me, ",
	"On the eighth day of Christmas my true love gave to me, ",
	"On the ninth day of Christmas my true love gave to me, ",
	"On the tenth day of Christmas my true love gave to me, ",
	"On the eleventh day of Christmas my true love gave to me, ",
	"On the twelfth day of Christmas my true love gave to me, ",
}

// Verse returns the verse for a given day
func Verse(n int) string {
	var buf bytes.Buffer
	buf.WriteString(ordinals[n-1])
	for i := n - 1; i >= 0; i-- {
		if n > 1 && i == 0 {
			buf.WriteString("and ")
		}
		buf.WriteString(gifts[i])
	}
	return buf.String()
}

// Song returns the full 12 days song
func Song() string {
	var buf bytes.Buffer
	for i := 1; i <= 12; i++ {
		buf.WriteString(Verse(i))
		buf.WriteByte('\n')
	}
	return buf.String()
}
