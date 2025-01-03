class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        count_0_start = 0
        count_1_start = 0
        
        for i in range(n):
            if i % 2 == 0:  
                if s[i] != '0':
                    count_0_start += 1
                if s[i] != '1':
                    count_1_start += 1
            else:  
                if s[i] != '1':
                    count_0_start += 1
                if s[i] != '0':
                    count_1_start += 1
        
        return min(count_0_start, count_1_start)
