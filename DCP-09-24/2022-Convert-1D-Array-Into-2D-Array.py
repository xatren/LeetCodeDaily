class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m * n:
            return []
        
        result = []
        for i in range(m):
            row = original[i * n:(i + 1) * n]
            result.append(row)
        
        return result