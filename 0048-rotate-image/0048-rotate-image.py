class Solution:
    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def transpose():
            for i in range(n):
                for j in range(i,n):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
            for i in range(n):
                matrix[i] = matrix[i][::-1]
        transpose()
