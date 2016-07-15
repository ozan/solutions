
letters_for_digit = dict(zip(
    '0123456789',
    ('', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
))


class Solution(object):
    def letterCombinations(self, digits):
        if digits == '':
            return []
        heads = letters_for_digit[digits[0]]
        tails = self.letterCombinations(digits[1:])
        return list(set(h + t for h in heads for t in tails or ['']))


if __name__ == '__main__':
    actual = set(Solution().letterCombinations('23'))
    expected = {'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'}
    assert actual == expected
