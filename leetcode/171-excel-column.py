import string

to_i = dict(zip(string.ascii_uppercase, range(1, 27)))


class Solution:
    def titleToNumber(self, s):
        return sum(26**i * to_i[char] for i, char in enumerate(reversed(s)))
