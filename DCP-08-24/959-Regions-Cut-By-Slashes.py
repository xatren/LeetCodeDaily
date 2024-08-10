class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        expanded_grid = [[0] * (n * 3) for _ in range(n * 3)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded_grid[i * 3][j * 3 + 2] = 1
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1
                    expanded_grid[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    expanded_grid[i * 3][j * 3] = 1
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1
                    expanded_grid[i * 3 + 2][j * 3 + 2] = 1
        
        def dfs(x, y):
            if x < 0 or x >= len(expanded_grid) or y < 0 or y >= len(expanded_grid) or expanded_grid[x][y] != 0:
                return
            expanded_grid[x][y] = 1  # Mark the cell as visited
            # Explore all 4 possible directions
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        
        regions = 0
        for i in range(len(expanded_grid)):
            for j in range(len(expanded_grid)):
                if expanded_grid[i][j] == 0:
                    regions += 1
                    dfs(i, j)
        
        return regions