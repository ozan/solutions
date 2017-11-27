package circular

import "errors"

// Buffer is a circular buffer
type Buffer struct {
	size, rp, wp, readable int
	items                  []byte
}

// NewBuffer constructs a new buffer of given size
func NewBuffer(size int) *Buffer {
	return &Buffer{size, 0, 0, 0, make([]byte, size)}
}

// ReadByte returns the next byte, if available
func (b *Buffer) ReadByte() (byte, error) {
	if b.readable == 0 {
		return 0x00, errors.New("Read beyond available data")
	}
	item := b.items[b.rp]
	b.rp = (b.rp + 1) % b.size
	b.readable--
	return item, nil
}

// WriteByte writes a byte to the next location, if available
func (b *Buffer) WriteByte(c byte) error {
	if b.readable == b.size {
		return errors.New("Write beyond available capacity")
	}
	b.items[b.wp] = c
	b.wp = (b.wp + 1) % b.size
	b.readable++
	return nil
}

// Overwrite writes a byte whether it is safe to do so or not
func (b *Buffer) Overwrite(c byte) {
	if b.readable < b.size {
		b.WriteByte(c)
		return
	}
	b.items[b.rp] = c
	b.rp = (b.rp + 1) % b.size
}

// Reset resets the state of the buffer. Data is retained, only pointers are changed
func (b *Buffer) Reset() {
	b.rp, b.wp, b.readable = 0, 0, 0
}
