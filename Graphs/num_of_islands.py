#200 Number of islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def set_islands(grid, row, col):
            if (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == "1":
                grid[row][col] = "0"

                for row_inc, col_inc in directions:
                    set_islands(grid, row + row_inc, col + col_inc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    num_islands += 1

                    set_islands(grid, row, col)
        
        return num_islands
        