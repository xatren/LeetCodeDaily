class Solution(object):
    def largestNumber(self, nums):
        \\\
        :type nums: List[int]
        :rtype: str
        \\\
        #Convert int to str
        nums = [str(num) for num in nums]
        
        # Define function
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        nums.sort(cmp=compare)
        
        result = ''.join(nums).lstrip('0')
        
        # If the result is empty return '0'
        return result if result else '0'