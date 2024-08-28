class Solution:
    def countSubIslands(self, grid1, grid2):
        def dfs(i, j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True
            if grid1[i][j] == 0:
                return False
            
            grid2[i][j] = 0  
            
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            
            return up and down and left and right
        
        sub_islands = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        sub_islands += 1
                        
        return sub_islands
