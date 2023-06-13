from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Create a dictionary to store the count of rows
        row_counts = defaultdict(int)
        num_rows = len(grid)

        # Count the occurrences of each row in the grid
        for i in range(num_rows):
            row_tuple = tuple(grid[i])
            row_counts[row_tuple] += 1
        
        # Transpose the grid by swapping elements across the diagonal
        for i in range(num_rows):
            for j in range(i, num_rows):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
        
        equal_pairs_count = 0
        # Count the number of equal pairs of rows in the transposed grid
        for i in range(num_rows):
            row_tuple = tuple(grid[i])
            equal_pairs_count += row_counts[row_tuple]
        
        return equal_pairs_count
