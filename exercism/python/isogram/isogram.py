def is_isogram(s):
    bs = 0
    for c in s:
        n = ord(c.lower()) - ord('a')
        if not 0 <= n < 26:
            continue
        if bs & (1 << n):
            return False
        bs |= (1 << n)
    return True
