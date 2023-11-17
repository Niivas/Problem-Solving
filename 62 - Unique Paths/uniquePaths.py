class Solution:
    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        # create a 2D grid of size m x n initialized with zeros
        dp = [[0]*n for _ in range(m)]

        # iterate over each cell in the grid
        for i in range(m):
            for j in range(n):
                # if we are in the first row or the first column, there is only one way to reach this cell
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # otherwise, the number of unique paths that lead to this cell is the sum of the number
                    # of unique paths that lead to the cell above it and the cell to the left of it
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # return the number of unique paths that lead to the bottom-right corner of the grid
        return dp[m-1][n-1]
