class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prior = None
        i = 0
        while True:
            try:
                if nums[i] == prior:
                    del nums[i]
                else:
                    prior = nums[i]
                    i += 1
            except IndexError:
                return len(nums)