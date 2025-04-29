class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val = max(nums)
        count = 0
        left = 0
        max_count = 0
        
        for right in range(len(nums)):
            if nums[right] == max_val:
                max_count += 1

            while max_count >= k:
                # All subarrays starting at left and ending at or after right are valid
                count += len(nums) - right
                if nums[left] == max_val:
                    max_count -= 1
                left += 1
        
        return count