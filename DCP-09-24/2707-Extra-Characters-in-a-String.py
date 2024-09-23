class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        word_set = set(dictionary)  # Use a set for faster lookup
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: no extra characters when string is empty
        
        for i in range(1, n + 1):
            # Assume the current character at s[i-1] is extra initially
            dp[i] = dp[i - 1] + 1
            
            # Check all possible substrings that end at index i-1
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]
