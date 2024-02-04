'''
The problem presents a 3x3 matrix grid, where each cell of the grid contains a certain number of stones, 
with a total of 9 stones distributed across the matrix. Here, it's possible to have multiple stones in 
a single cell. The task is to move the stones such that there is exactly one stone in each cell. 
A move consists of transferring a stone from one cell to any adjacent cell (one that shares a side).

To solve this problem, we need to determine the minimum number of moves necessary to achieve the goal
where each cell contains just one stone.

'''

def minimum_moves(grid):

    # Calculates the Manhattan distance between point a and point b.
    def calculate_distance(a: tuple, b: tuple) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    empty_cells = []
    filled_cells = []

    # iterate the grid find empty cells and filled cells
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                empty_cells.append((i, j))
            else:
                for _ in range(grid[i][j] - 1):
                    filled_cells.append((i, j))
    
    # Initialize an array 'dp' to store the minimum distance for each subset of empty cells.
    num_of_empty_cells = len(empty_cells)
    dp = [float('inf')] * [1 << num_of_empty_cells]
    dp[0] = 0

    # Iterate over all subsets of empty cells.
    for mask in range(1, 1 << num_of_empty_cells):
        num_filled_cells = mask.bit_count()
        for j in range(num_of_empty_cells):
            if mask >> j & 1:
            # For each subset, calculate the minimum distance to move the
            # filled cell 'num_filled_cells - 1' to the position of the j-th empty cell.
            # Remove the j-th empty cell (1 << j) from the current subset (mask ^ (1 << j)).
            # min_distance is the minimum of the current value and the new calculated distance.
                dp[mask] = min(dp[mask], dp[mask ^ (1 << j)] + calculate_distance(empty_cells[num_filled_cells - 1], filled_cells[j]))
      
        # Return the last element in dp which represents the minimum distance
        # for all empty cells filled.
        return dp[-1]
