class Solution(object):
    def addDigits(self, num):
        if num == 0: return 0
        return num - 9 * ((num - 1) / 9)
