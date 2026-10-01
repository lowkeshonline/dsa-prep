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

        row_marker = [False] * rows
        col_marker = [False] * cols

        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] == 0:
                    row_marker[i] = True
                    col_marker[j] = True
        
        for i in range(rows):
            for j in range(cols):

                if row_marker[i] or col_marker[j]:
                    matrix[i][j] = 0
        
        return matrix

