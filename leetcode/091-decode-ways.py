def score(s):
    return int(0 < int(s) <= 26)


class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        p, pp, pdig = 1, 1, None
        for digit in reversed(s):
            if not pdig:
                pdig = digit
                p = score(digit)
                continue
            one_and = score(digit) * p
            two_and = score(digit + pdig) * pp
            p, pp = score(digit) and (one_and + two_and) or 0, p
            pdig = digit

        return s and p or 0
