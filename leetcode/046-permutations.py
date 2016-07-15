class Solution(object):
    def permute(self, nums):
        if not nums:
            return [[]]
        return [
            [n] + perm
            for i, n in enumerate(nums)
            for perm in self.permute(nums[:i] + nums[(i+1):])
        ]


if __name__ == '__main__':
    assert Solution().permute([1, 2, 3]) == [
      [1, 2, 3],
      [1, 3, 2],
      [2, 1, 3],
      [2, 3, 1],
      [3, 1, 2],
      [3, 2, 1]
    ]
