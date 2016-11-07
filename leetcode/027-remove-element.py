class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        try:
            while True:
                nums.remove(val)
        except ValueError:
            return len(nums)