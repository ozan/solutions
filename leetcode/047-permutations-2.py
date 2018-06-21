class Solution(object):
    def permuteUnique(self, nums):
        results, seen = [], set()
        for i, n in enumerate(nums):
            if n not in seen:
                results.extend([n] + sub for sub in self.permuteUnique(nums[:i] + nums[i+1:]) or [[]])
                seen.add(n)
        return results


if __name__ == '__main__':
    assert Solution().permute([1, 1, 2]) == [
      [1, 1, 2],
      [1, 2, 1],
      [2, 1, 1]
    ]
