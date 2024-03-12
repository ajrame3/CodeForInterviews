# 827 - Making a largest island. 

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        self.island_id = -1
        self.island_areas = {}
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    island_area = self.dfs(grid, r, c)
                    self.island_areas[self.island_id] = island_area
                    self.island_id -= 1
        
        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if not grid[r][c]:
                    area = 1
                    surrounding = set()
                    for r_inc, c_inc in self.directions:
                        new_r = r + r_inc
                        new_c = c + c_inc

                        if (0 <= new_r < len(grid)) and (0 <= new_c < len(grid[0])) and grid[new_r][new_c] != 0:
                            surrounding.add(grid[new_r][new_c])
                    
                    for island_id in surrounding:
                        area += self.island_areas[island_id]
                    
                    max_area = max(max_area, area)
        
        return max_area if max_area else len(grid) ** 2

    
    def dfs(self, grid, m, n):
        if (0 <= m < len(grid)) and (0 <= n < len(grid[m])) and grid[m][n] == 1:
            grid[m][n] = self.island_id
            area = 1

            for m_inc, n_inc in self.directions:
                area += self.dfs(grid, m + m_inc, n + n_inc)
            
            return area
        else:
            return 0