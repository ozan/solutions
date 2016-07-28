
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        l = [0] * (num + 1)
        l[1] = 1
        d = 2

        while True:
            for i in xrange(d):
                if d + i >= num + 1:
                    return l
                l[d + i] = l[i] + 1
            d = 2


if __name__ == '__main__':
    s = Solution()
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
