class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Step 1: DFS to label islands and calculate their sizes
        def dfs(x, y, island_id):
            stack = [(x, y)]
            grid[x][y] = island_id
            size = 0
            
            while stack:
                i, j = stack.pop()
                size += 1
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = island_id
                        stack.append((ni, nj))
            
            return size
        
        # Dictionary to store island sizes by their IDs
        island_sizes = {}
        island_id = 2  # Start assigning unique IDs from 2
        
        # First pass: Label islands and compute their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size = dfs(i, j, island_id)
                    island_sizes[island_id] = island_size
                    island_id += 1
        
        # Step 2: Try flipping each 0 and calculate the resulting island size
        max_island_size = max(island_sizes.values()) if island_sizes else 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_islands = set()
                    total_size = 1  # Start with the flipped '0' as part of the island
                    
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            island_id = grid[ni][nj]
                            if island_id not in seen_islands:
                                total_size += island_sizes[island_id]
                                seen_islands.add(island_id)
                    
                    max_island_size = max(max_island_size, total_size)
        
        # Step 3: Return the result
        return max_island_size
