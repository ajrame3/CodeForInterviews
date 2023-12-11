# Walk the matrix in clockwise direction

def WalkAMatrix(matrix):
    result = []
    row_count = len(matrix)
    col_count = len(matrix[0])

    start_row = 0
    end_row = row_count - 1
    start_col = 0
    end_col = col_count - 1

    while(end_row >= start_row and end_column >= start_column):
        # Walk across the top starting row for each column from beginning to end
        # This is left-right across the top
        for column in range(start_column, end_column + 1):
            # Add the item to result in order
            result.append(matrix[start_row][column])

        # Increment our start row since we visited each value
        start_row += 1

         # Walk top-bottom for the end column
        for row in range(start_row, end_row + 1):
            result.append(matrix[row][end_column])

        end_column -= 1

         # Since we increment start_row, we need to make sure we are still in bounds
        if end_row >= start_row:
            #  Walk left-right on the bottom row
            for column in range(end_column, start_column - 1, -1):
                result.append(matrix[end_row][column])

        end_row -= 1

         # Since we increment start_row, we need to make sure we are still in bounds
        if end_column >= start_column:
            # walk bottom-top for the start column
            for row in range(end_row, start_row - 1, -1):
                result.append(matrix[row][start_column])


        start_column += 1

    return result