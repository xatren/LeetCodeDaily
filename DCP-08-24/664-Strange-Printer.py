class Solution(object):
    def strangePrinter(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        n = len(s)
        dp = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):  
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] - (1 if s[i] == s[j] else 0))
        
        return dp[0][n-1]