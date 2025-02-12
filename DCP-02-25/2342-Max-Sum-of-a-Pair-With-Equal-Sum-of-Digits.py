class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(x):
            return sum(int(digit) for digit in str(x))
        
        max_per_digit_sum = {}
        result = -1
        #todo:
        for num in nums:
            current_sum = digit_sum(num)
            if current_sum in max_per_digit_sum:
                current_result = num + max_per_digit_sum[current_sum]
                if current_result > result:
                    result = current_result
                if num > max_per_digit_sum[current_sum]:
                    max_per_digit_sum[current_sum] = num
            else:
                max_per_digit_sum[current_sum] = num
        
        return result