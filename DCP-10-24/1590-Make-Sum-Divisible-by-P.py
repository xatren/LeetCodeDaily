class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        target = total_sum % p
        
        if target == 0:
            return 0
        
        curr_sum = 0
        seen = {0: -1}
        min_length = n
        
        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            complement = (curr_sum - target) % p
            
            if complement in seen:
                min_length = min(min_length, i - seen[complement])
            
            seen[curr_sum] = i
        
        return min_length if min_length < n else -1