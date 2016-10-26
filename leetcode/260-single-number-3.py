class Solution(object):
    def singleNumber(self, nums):
        x, a, b, d = 0, 0, 0, 1
        for n in nums:
            x ^= n
        while not x & d:
            d <<= 1
        for n in nums:
            if n & d:
                a ^= n
            else:
                b ^= n
        return a, b


if __name__ == '__main__':
    f = Solution().singleNumber
    assert sorted(f([1, 2, 1, 3, 2, 5])) == [3, 5]
