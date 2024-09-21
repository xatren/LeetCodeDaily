class Solution(object):
    def lexicalOrder(self, n):
        \\\
        :type n: int
        :rtype: List[int]
        \\\
        result = []
        
        def dfs(current):
            if current > n:
                return
            
            result.append(current)
            
            for i in range(10):
                if current * 10 + i > n:
                    return
                dfs(current * 10 + i)
        
        for i in range(1, 10):
            dfs(i)
        
        return result