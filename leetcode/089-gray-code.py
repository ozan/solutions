class Solution(object):
    def grayCode(self, n):
        code = [0]
        code_set = {0}
        while True:
            previous = code[-1]
            for i in range(n):
                candidate = previous ^ (1 << i)
                if candidate not in code_set:
                    code.append(candidate)
                    code_set.add(candidate)
                    break
            else:
                return code


if __name__ == '__main__':
    assert Solution().grayCode(2) == [0, 1, 3, 2]
