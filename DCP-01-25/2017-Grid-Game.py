class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        
        top_prefix_sum = [0] * (n + 1)
        bottom_prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            top_prefix_sum[i + 1] = top_prefix_sum[i] + grid[0][i]
            bottom_prefix_sum[i + 1] = bottom_prefix_sum[i] + grid[1][i]
        
        min_second_robot_points = float('inf')
        
        for i in range(n):
            points_above = top_prefix_sum[n] - top_prefix_sum[i + 1]
            points_below = bottom_prefix_sum[i]
            
            max_points_second_robot = max(points_above, points_below)
            min_second_robot_points = min(min_second_robot_points, max_points_second_robot)
        
        return min_second_robot_points
