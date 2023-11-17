from typing import List

class Solution:
    @staticmethod
    def countNegatives(grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Start from the bottom-left element
        row = num_rows - 1
        col = 0

        # Initialize the counter for negative integers
        negative_count = 0

        # Traverse the grid
        while row >= 0 and col < num_cols:
            # If the current element is negative, count the remaining elements in the row
            if grid[row][col] < 0:
                negative_count += num_cols - col
                row -= 1
            else:
                # Move to the next column
                col += 1

        # Return the count of negative integers
        return negative_count