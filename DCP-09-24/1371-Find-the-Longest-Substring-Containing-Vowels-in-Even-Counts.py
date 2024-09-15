class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = 'aeiou'
        state = 0
        seen = {0: -1}
        max_length = 0
        
        for i, char in enumerate(s):
            if char in vowels:
                state ^= 1 << vowels.index(char)
            
            if state in seen:
                max_length = max(max_length, i - seen[state])
            else:
                seen[state] = i
        
        return max_length