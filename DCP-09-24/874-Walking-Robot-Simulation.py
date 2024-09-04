class Solution(object):
    def robotSim(self, commands, obstacles):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        obstacle_set = set(map(tuple, obstacles))
        
        x, y, direction = 0, 0, 0
        max_distance_squared = 0
        
        for command in commands:
            if command == -2:  # Turn left
                direction = (direction - 1) % 4
            elif command == -1:  # Turn right
                direction = (direction + 1) % 4
            else:
                dx, dy = directions[direction]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_distance_squared = max(max_distance_squared, x * x + y * y)
                    else:
                        break
        
        return max_distance_squared
