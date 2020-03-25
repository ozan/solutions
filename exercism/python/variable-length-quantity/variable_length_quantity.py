def encode(numbers):
    out = []
    for n in reversed(numbers):
        if n == 0:
            out.append(0)
        msb = 0
        while n > 0:
            out.append(msb ^ (n & 127))
            msb = 128
            n >>= 7
    return out[::-1]


def decode(bytes_):
    out = []
    n = 0
    for i, b in enumerate(bytes_):
        n = (n << 7) + (b & 127)
        if b & 128 == 0:
            out.append(n)
            n = 0
        elif i == len(bytes_) - 1:
            raise ValueError('Incomplete sequence')
    return out
