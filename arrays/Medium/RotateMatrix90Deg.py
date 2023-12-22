class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topleft = matrix[top][l + i]

                #move bottom left to the top left
                matrix[top][l + i] = matrix[bottom - i][l]

                #Move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #Move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #Move top left to top right
                matrix[top + i][r] = topleft
            
            r -= 1
            l += 1
        
            


