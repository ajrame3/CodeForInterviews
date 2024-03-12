# 498 Diagnol Traverse

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        row = 0
        col = 0
        height = len(mat) - 1
        width = len(mat[0]) - 1

        res = []
        going_up = True

        while not self.is_bound(row, col, height, width):
            res.append(mat[row][col])

            if going_up:
                if row == 0 or col == width:
                    going_up = False

                    if col == width:
                        row += 1
                    else:
                        col += 1

                else:
                    row -= 1
                    col += 1
            
            else:
                if col == 0 or row == height:
                    going_up = True

                    if row == height:
                        col += 1
                    else:
                        row += 1
                
                else:
                    row += 1
                    col -= 1
        return res

    def is_bound(self, row, col, height, width):
        # this will return true if any of this condition is met
        return row < 0 or col < 0 or row > height or col > width
                

        