

class Solution(object):
    def nthUglyNumber(self, n):
        seen = [1]
        i2, i3, i5 = 0, 0, 0
        while len(seen) < n:
            v2, v3, v5 = 2 * seen[i2], 3 * seen[i3], 5 * seen[i5]
            minv = min(v2, v3, v5)
            if minv == v2:
                i2 += 1
            if minv == v3:
                i3 += 1
            if minv == v5:
                i5 += 1
            seen.append(minv)
        return seen[-1]
