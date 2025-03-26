class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        flat_list = [num for row in grid for num in row]
        
        remainder = flat_list[0] % x
        for num in flat_list:
            if num % x != remainder:
                return -1
        
        flat_list.sort()
        
        median = flat_list[len(flat_list) // 2]
        
        operations = sum(abs(num - median) // x for num in flat_list)
        
        return operations