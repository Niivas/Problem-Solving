class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize defaultdicts to keep track of seen digits in each row, column, and block
        row_map, column_map, block_map = defaultdict(set), defaultdict(set), defaultdict(set)

        # Iterate through each cell of the board
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":  # If the cell has a digit
                    val, id = board[i][j], ((i // 3) * 3) + j // 3 + 1  # Get the digit and its block ID
                    # Check if the digit is already seen in the same row, column, or block
                    if (val in row_map[i] or val in column_map[j] or val in block_map[id]):
                        return False  # If the digit is already seen, the board is invalid
                    else:
                        row_map[i].add(val)  # Add the digit to the row_map
                        column_map[j].add(val)  # Add the digit to the column_map
                        block_map[id].add(val)  # Add the digit to the block_map

        return True  # If all cells are checked and no duplicates were found, the board is valid
