# 1091

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] or grid[-1][-1]:
            return -1
        
        
        queue = collections.deque([(0, 0, 1)])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        grid[0][0] = 1

        while queue:
            x, y, d = queue.popleft()

            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return d
            
            for x_inc, y_inc in directions:
                new_x = x + x_inc
                new_y = y + y_inc

                if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])) and not grid[new_x][new_y]:
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y, d + 1))
        
        return -1
        