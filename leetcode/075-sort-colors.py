class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        rw = 0  # pointer separating red and white
        wb = len(nums) - 1  # pointer separating white and blue
        i = 0
        while i <= wb:
            n = nums[i]
            if n == 0:
                nums[i], nums[rw] = nums[rw], nums[i]
                rw += 1
            if n == 2:
                nums[i], nums[wb] = nums[wb], nums[i]
                wb -= 1
            else:
                i += 1
    
