class Solution:
    def convert(self, s: str, numrows: int) -> str:
        if numrows == 1:
            return s

    # Create a list of empty strings to store the zigzag pattern
        zigzag = ['' for _ in range(numrows)]
    # Initialize the current row index to 0
        row = 0
    # Initialize the step direction to 1 (to move down)
        step = 1
    # Iterate over the characters of the input string
        for c in s:
        # Append the current character to the current row
            zigzag[row] += c
        # If the current row is the last row, change the step direction to -1 (to move up)
            if row == numrows-1:
                step = -1
        # If the current row is the first row, change the step direction to 1 (to move down)
            elif row == 0:
                step = 1
        # Move to the next row
            row += step
    # Return the zigzag pattern as a single string
        return ''.join(zigzag)