class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_length = 1
        inc_length = 1
        dec_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Strictly increasing
                inc_length += 1
                dec_length = 1  # Reset decreasing count
            elif nums[i] < nums[i - 1]:  # Strictly decreasing
                dec_length += 1
                inc_length = 1  # Reset increasing count
            else:
                inc_length = 1
                dec_length = 1
            
            max_length = max(max_length, inc_length, dec_length)
        
        return max_length