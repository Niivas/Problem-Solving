import collections
from typing import List

class Solution:
    @staticmethod
    def isPossibleToCross(row: int, col: int, cells: List[List[int]], day: int) -> bool:
        # Initialize the grid with all cells set to 0
        grid = [[0] * col for _ in range(row)]
        queue = collections.deque()
        
        # Mark the cells as blocked for the given day
        for r, c in cells[:day]:
            grid[r - 1][c - 1] = 1
            
        # Enqueue the cells in the first row that are not blocked
        for i in range(col):
            if not grid[0][i]:
                queue.append((0, i))
                grid[0][i] = -1

        # Perform a BFS traversal of the grid
        while queue:
            r, c = queue.popleft()
            if r == row - 1:
                return True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    grid[nr][nc] = -1
                    queue.append((nr, nc))
                    
        return False
    
    
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, row * col
        
        # Perform binary search
        while left < right:
            mid = right - (right - left) // 2
            if self.isPossibleToCross(row, col, cells, mid):
                left = mid
            else:
                right = mid - 1
                
        return left
