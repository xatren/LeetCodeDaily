class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        max_unmatched = 0
        
        for bracket in s:
            if bracket == '[':
                balance += 1
            else:  # bracket == ']'
                balance -= 1
            
            max_unmatched = max(max_unmatched, -balance)
        
        return (max_unmatched + 1) // 2