class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Define the relative positions of the neighbors
        neighbors = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
        rows, cols = len(board), len(board[0])

        # Function to count the number of live neighbors for a given cell
        def count_live_neighbors(row, col):
            count = 0
            for dr, dc in neighbors:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 1:
                    count += 1
            return count

        # Set to store the positions of cells that need to be inverted
        cells_to_be_inverted = set()

        # Iterate over each cell in the board
        for row in range(rows):
            for col in range(cols):
                live_neighbors = count_live_neighbors(row, col)
                # Apply the rules of the Game of Life
                if board[row][col] == 0 and live_neighbors == 3:
                    cells_to_be_inverted.add((row, col))
                elif board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    cells_to_be_inverted.add((row, col))

        # Invert the state of the cells based on the set of positions
        for row, col in cells_to_be_inverted:
            board[row][col] = (board[row][col] + 1) % 2
