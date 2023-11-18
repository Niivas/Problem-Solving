from typing import List


class Solution:
    @staticmethod
    def generate(numRows: int) -> List[List[int]]:
        # special cases for numRows = 1 or 2
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        # initialize dp with first two rows of Pascal's Triangle
        dp = [[1], [1, 1]]

        # iterate from row 2 to numRows-1
        for i in range(2, numRows):
            # create a new row with the first element as 1
            row = [1]
            # iterate over previous row and compute sum of adjacent elements
            for j in range(1, len(dp[-1])):
                row.append(dp[-1][j] + dp[-1][j - 1])
            # append 1 to the end of row and append row to dp
            row.append(1)
            dp.append(row)

        # return dp representing Pascal's Triangle
        return dp
