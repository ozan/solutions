
class CircularBuffer {
  constructor (size) {
    this.clear(size)
  }
  clear (size) {
    size = size || this.buffer.length
    this.buffer = Array(size)
    this.writePointer = 0
    this.readPointer = 0
    this.semaphore = 0
  }
  read () {
    if (!this.semaphore) throw new BufferEmptyException
    const val = this.buffer[this.readPointer]
    this.readPointer = this.next(this.readPointer)
    this.semaphore -= 1
    return val
  }
  write (val) {
    if (!val) return
    if (this.semaphore >= this.buffer.length) throw new BufferFullException()
    this.buffer[this.writePointer] = val
    this.writePointer = this.next(this.writePointer)
    this.semaphore += 1
  }
  forceWrite (val) {
    try {
      this.write(val)
    } catch (BufferFullException) {
      this.buffer[this.writePointer] = val
      this.writePointer = this.next(this.writePointer)
      this.readPointer = this.next(this.readPointer)
    }
  }
  next (pointer) {
    return (pointer + 1) % this.buffer.length
  }
}


class BufferEmptyException extends Error {}
class BufferFullException extends Error {}


module.exports = {
  circularBuffer: (n) => new CircularBuffer(n),
  bufferEmptyException: () => new BufferEmptyException(),
  bufferFullException: () => new BufferFullException()
}
