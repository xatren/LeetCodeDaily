class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        #max_nums
        max_num = (1 << maximumBit) - 1  
        current_xor = 0
        
        for num in nums:
            current_xor ^= num
        
        #empty result
        result = []
        
        for i in range(len(nums)):
            k = max_num ^ current_xor
            result.append(k)
            current_xor ^= nums[len(nums) - 1 - i]
        
        #return result
        return result
