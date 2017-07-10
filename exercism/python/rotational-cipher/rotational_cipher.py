import string


def rotate(given, n):
    n = n % 26
    low, up = string.ascii_lowercase, string.ascii_uppercase
    mapping = dict(zip(low + up, low[n:] + low[:n] + up[n:] + up[:n]))
    return ''.join(mapping[ch] if ch in mapping else ch for ch in given)
