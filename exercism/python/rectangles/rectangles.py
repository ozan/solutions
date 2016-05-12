from functools import reduce


def count(drawing=''):
    memo = {'total': 0, 'corners': []}
    return reduce(reduce_line, enumerate(drawing), memo)['total']


def reduce_line(memo, line):
    i, chars = line
    if i % 2 == 0:
        latest_corners = corners(chars)
        memo['total'] += sum(1 for p in memo['corners'] if p in latest_corners)
        memo['corners'] += list(latest_corners)
    else:
        memo['corners'] = corners_still_valid(memo['corners'], chars)
    return memo


def corners_still_valid(corners, chars):
    pipes = set([i for i, ch in enumerate(chars) if ch == '|'])
    return [(a, b) for a, b in corners if a in pipes and b in pipes]


def corners(chars):
    pairs = set()
    connected_corners = []
    for i, ch in enumerate(chars):
        if ch == '+':
            pairs.update([(j, i) for j in connected_corners])
            connected_corners.append(i)
        if ch == ' ':
            connected_corners = []
    return pairs
