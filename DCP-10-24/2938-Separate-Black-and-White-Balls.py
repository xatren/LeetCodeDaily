class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = 0
        right = n - 1
        steps = 0
        
        while left < right:
            # Find the rightmost black ball
            while right > left and s[right] == '1':
                right -= 1
            
            # Find the leftmost white ball
            while left < right and s[left] == '0':
                left += 1
            
            if left < right:
                # Calculate the distance to swap
                steps += right - left
                left += 1
                right -= 1
        
        return steps