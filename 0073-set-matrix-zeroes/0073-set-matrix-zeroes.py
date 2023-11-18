class Solution:
    @staticmethod
    def setZeroes(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        rowSet,columnSet = set(),set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    columnSet.add(j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i in rowSet or j in columnSet:
                        matrix[i][j] = 0