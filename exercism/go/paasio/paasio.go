package paasio

import (
	"io"
	"sync"
)

type meter struct {
	n     int64
	nops  int
	mutex sync.Mutex
}

type meteredIOProxy struct {
	writer                 io.Writer
	reader                 io.Reader
	readMeter, writeMeter  meter
	bytesWriten, bytesRead int64
}

func (m *meter) add(n int64) {
	m.mutex.Lock()
	m.n += n
	m.nops++
	m.mutex.Unlock()
}

func (proxy *meteredIOProxy) Write(p []byte) (int, error) {
	n, err := proxy.writer.Write(p)
	proxy.writeMeter.add(int64(n))
	return n, err
}

func (proxy *meteredIOProxy) Read(p []byte) (int, error) {
	n, err := proxy.reader.Read(p)
	proxy.readMeter.add(int64(n))
	return n, err
}

func (proxy *meteredIOProxy) WriteCount() (int64, int) {
	return proxy.writeMeter.n, proxy.writeMeter.nops
}

func (proxy *meteredIOProxy) ReadCount() (int64, int) {
	return proxy.readMeter.n, proxy.readMeter.nops
}

// NewWriteCounter returns an implementation of `WriteCounter`
func NewWriteCounter(w io.Writer) WriteCounter {
	return &meteredIOProxy{writer: w}
}

// NewReadCounter returns an implementation of `ReadCounter`
func NewReadCounter(r io.Reader) ReadCounter {
	return &meteredIOProxy{reader: r}
}

// NewReadWriteCounter returns an implementation of `WriteCounter`
func NewReadWriteCounter(rw io.ReadWriter) ReadWriteCounter {
	return &meteredIOProxy{writer: rw, reader: rw}
}
