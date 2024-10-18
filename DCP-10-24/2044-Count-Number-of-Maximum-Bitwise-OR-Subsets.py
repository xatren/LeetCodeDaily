class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for num in nums:
            max_or |= num
        
        def backtrack(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            
            count = backtrack(index + 1, current_or | nums[index])
            
            count += backtrack(index + 1, current_or)
            
            return count
        
        return backtrack(0, 0)