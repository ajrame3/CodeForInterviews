class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square_grid = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col] == '.':
                    continue
                
                if (board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in square_grid[(row // 3, col // 3)]):
                    return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                square_grid[(row // 3, col // 3)].add(board[row][col])
        
        return True