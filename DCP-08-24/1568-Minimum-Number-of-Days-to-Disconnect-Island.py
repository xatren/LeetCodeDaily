class Solution:
    def minDays(self, grid):
        def is_connected(grid):
            def dfs(x, y):
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                    return
                grid[x][y] = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dfs(x + dx, y + dy)
                    
            found_land = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        if found_land:
                            return False
                        dfs(i, j)
                        found_land = True
            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return False
            
            return found_land
        
        if not is_connected([row[:] for row in grid]):
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected([row[:] for row in grid]):
                        return 1
                    grid[i][j] = 1
        
        return 2
