class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Initialize a memoization table with -1 for each cell
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]

        # Possible directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x: int, y: int, prev_height: int) -> int:
            # Check if the current cell is out of bounds or violates the height constraint
            if x < 0 or x >= rows or y < 0 or y >= cols or prev_height >= grid[x][y]:
                return 0

            # Check if the number of paths for this cell has already been calculated
            if memo[x][y] != -1:
                return memo[x][y]

            # Initialize the number of paths for this cell to 1
            paths = 1

            # Explore the four possible directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                # Recursively count the number of paths from the new cell
                paths += dfs(new_x, new_y, grid[x][y])

            # Store the result in the memoization table for future use
            memo[x][y] = paths

            return paths

        # Accumulate the number of paths starting from each cell
        total_paths = 0
        for i in range(rows):
            for j in range(cols):
                total_paths += dfs(i, j, -1)

        # Return the result modulo (10^9 + 7)
        return total_paths % (10**9 + 7)