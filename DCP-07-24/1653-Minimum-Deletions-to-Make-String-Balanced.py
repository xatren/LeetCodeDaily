class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        a_count = [0] * (n + 1)  
        
        for i in range(n - 1, -1, -1):
            a_count[i] = a_count[i + 1] + (1 if s[i] == 'a' else 0)
        
        b_count = 0
        min_deletions = float('inf')
        
        for i in range(n):
            min_deletions = min(min_deletions, b_count + a_count[i])
            
            if s[i] == 'b':
                b_count += 1
        
        min_deletions = min(min_deletions, b_count)
        
        return min_deletions
