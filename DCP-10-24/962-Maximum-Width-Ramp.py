class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        n = len(nums)
        
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        
        for i in range(n - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                max_width = max(max_width, i - stack.pop())
            
            if not stack:
                break
        
        return max_width