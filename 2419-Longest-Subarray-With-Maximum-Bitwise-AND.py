class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the maximum element in the array
        max_num = max(nums)
        
        # variables
        current_length = 0
        max_length = 0
        
        for num in nums:
            if num == max_num:
                # If the current number is equal to the maximum,
                # increment the current length
                current_length += 1
                # Update max_length if necessary
                max_length = max(max_length, current_length)
            else:
                # reset the current length
                current_length = 0
        
        return max_length