
class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, size):
        self.size = size
        self.clear()

    def clear(self):
        self.buffer = [None] * self.size
        self.wp = 0  # write pointer
        self.rp = 0  # read pointer
        self.readable = 0  # semaphore

    def read(self):
        if self.readable == 0:
            raise BufferEmptyException()
        val = self.buffer[self.rp]
        self.buffer[self.rp] = None
        self.rp = (self.rp + 1) % self.size
        self.readable -= 1
        return val

    def write(self, val):
        if self.readable == self.size:
            raise BufferFullException()
        self.buffer[self.wp] = val
        self.wp = (self.wp + 1) % self.size
        self.readable += 1

    def overwrite(self, val):
        if self.readable < self.size:
            return self.write(val)
        self.buffer[self.rp] = val
        self.rp = (self.rp + 1) % self.size
