class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total_sum = (n + m) * mean
        known_sum = sum(rolls)
        missing_sum = total_sum - known_sum
        
        if missing_sum < n or missing_sum > 6*n:
            return []
        
        result = [missing_sum // n] * n
        remainder = missing_sum % n
        
        for i in range(remainder):
            result[i] += 1
        
        return result