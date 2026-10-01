class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Brute force: visit each element and if it's zero then mark the entire row and column -1 and later replace with zero on another iteration

        Better : Take row and col arrays. Mark the rows and columns that contains zero in them. later make the rows and columns zero
        """
        
        n = len(matrix)

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        #check if first row has zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
        
        #check if first col has zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True

        #mark first row and first col based on remaining matrix
        for i in range(1, rows):
            for j in range(1, cols):

                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # convert all rows
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
        
        #convert all cols
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        
        # check if first row has zero if yes convert the row to zero
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # check if the col has zero if yes convert the col to zero
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

        return matrix

