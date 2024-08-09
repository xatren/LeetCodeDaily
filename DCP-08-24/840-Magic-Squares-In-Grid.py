class Solution:
    def numMagicSquaresInside(self, grid):
        def is_magic(r, c):
            s = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if num < 1 or num > 9:
                        return False
                    s.add(num)
            if len(s) != 9:
                return False
            
            if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15 or
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15 or
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15 or
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return False
            
            return True
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r+1][c+1] == 5 and is_magic(r, c):
                    count += 1
        return count
