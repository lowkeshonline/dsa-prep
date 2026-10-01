class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(i + 1, cols):

                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            
        
        for i in range(rows):
            for j in range(cols // 2):

                temp = matrix[i][j]
                matrix[i][j] = matrix[i][cols - 1 - j]
                matrix[i][cols - 1 - j] = temp
        
        return matrix
        