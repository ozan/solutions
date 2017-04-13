
PLACE_VALUES = [
    (0, 1), (0, 2), (0, 4), (0, 8), (0, 16), (0, 32),
    (1, 0), (2, 0), (4, 0), (8, 0)
]


def gen_times(on, idx=9):
    if on == 0:
        return [(0, 0)]
    if idx < 0:
        return []
    dh, dm = PLACE_VALUES[idx]
    on_case = [(h + dh, m + dm) for h, m in gen_times(on - 1, idx - 1)
               if h + dh < 12 and m + dm < 60]
    return gen_times(on, idx - 1) + on_case


class Solution(object):
    def readBinaryWatch(self, num):
        return ['{}:{:02d}'.format(h, m) for h, m in gen_times(num)]


if __name__ == '__main__':
    s = Solution()
    assert set(s.readBinaryWatch(1)) == set([
        '1:00', '2:00', '4:00', '8:00', '0:01',
        '0:02', '0:04', '0:08', '0:16', '0:32'
    ])
    assert len(s.readBinaryWatch(4)) == 181
    print('ok')
