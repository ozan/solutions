

def parse_binary(chrs):
    if set(chrs) > set('10'):
        raise ValueError
    return sum(int(d) << i for i, d in enumerate(chrs[::-1]))
