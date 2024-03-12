#695 Max area of an island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def find_area(grid, cur_row, cur_col):
            if (0 <= cur_row < len(grid)) and (0 <= cur_col < len(grid[0])) and grid[cur_row][cur_col] == 1:
                grid[cur_row][cur_col] = 0
                area = 1

                for r, c in directions:
                    area += find_area(grid, cur_row + r, cur_col + c)
                
                return area
            else:
                return 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                area = find_area(grid, row, col)
                max_area = max(max_area, area)
        
        return max_area