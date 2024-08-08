class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        r, c = rStart, cStart
        
        result = [[r, c]]
        
        steps = 1
        
        total_cells = rows * cols
        
        direction_index = 0
        
        visited_cells = 1
        
        while visited_cells < total_cells:
            for _ in range(2):
                for _ in range(steps):
                    r += directions[direction_index][0]
                    c += directions[direction_index][1]
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        visited_cells += 1
                
                direction_index = (direction_index + 1) % 4
            
            steps += 1
        
        return result