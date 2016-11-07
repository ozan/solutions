class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        mx = 0
        while r > l:
            area = (r - l) * min(height[r], height[l])
            if area > mx:
                mx = area
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return mx
        
        