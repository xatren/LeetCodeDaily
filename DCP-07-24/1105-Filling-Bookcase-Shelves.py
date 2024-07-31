class Solution:
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  
        
        for i in range(1, n + 1):
            width = 0
            height = 0
            for j in range(i - 1, -1, -1):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)
                
        return dp[n]
