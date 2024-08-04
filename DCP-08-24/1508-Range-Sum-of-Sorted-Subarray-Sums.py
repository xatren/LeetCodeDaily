class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10**9 + 7
        subarray_sums = []
        
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                subarray_sums.append(current_sum)
        
        subarray_sums.sort()
        
        result = sum(subarray_sums[left-1:right]) % MOD
        
        return result