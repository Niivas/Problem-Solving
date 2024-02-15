from typing import List
import collections

class Solution:
    @staticmethod
    def shortestPathAllKeys(grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        
        # Dictionary to store visited cells for each key state
        seen = collections.defaultdict(set)
        
        # Sets to store keys and locks
        key_set, lock_set = set(), set()
        
        # Variable to store the bitmask of all keys
        all_keys = 0
        
        # Variables to store the starting position
        start_r, start_c = -1, -1
        
        # Iterate through the grid to process cells
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                
                if cell in 'abcdef':
                    # Found a key, update key set and bitmask
                    all_keys += (1 << (ord(cell) - ord('a')))
                    key_set.add(cell)
                
                if cell in 'ABCDEF':
                    # Found a lock, update lock set
                    lock_set.add(cell)
                
                if cell == "@":
                    # Found the starting position
                    start_r, start_c = i, j
        
        # Add the starting position to the queue with initial key state and distance
        queue.append((start_r, start_c, 0, 0))
        
        # Mark the starting position as visited with the initial key state
        seen[0].add((start_r, start_c))
        
        # Perform breadth-first search
        while queue:
            cur_r, cur_c, keys, dist = queue.popleft()
            
            # Explore four possible movements: up, down, left, right
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                new_r, new_c = cur_r + dr, cur_c + dc
                
                # Check if the new cell is reachable
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] != '#':
                    cell = grid[new_r][new_c]
                    
                    if cell in key_set and not ((1 << (ord(cell) - ord('a'))) & keys):
                        # Found a new key that hasn't been collected yet
                        
                        # Update key state by setting the corresponding bit
                        new_keys = (keys | (1 << (ord(cell) - ord('a'))))
                        
                        if new_keys == all_keys:
                            # Collected all keys, return the distance + 1
                            return dist + 1
                        
                        # Mark the new cell as visited with the updated key state
                        seen[new_keys].add((new_r, new_c))
                        
                        # Add the new cell to the queue with the updated key state and distance
                        queue.append((new_r, new_c, new_keys, dist + 1))
                      
                    elif cell in lock_set and not (keys & (1 << (ord(cell) - ord('A')))):
                        # Found a locked door without the corresponding key, continue to the next iteration
                        continue
                        
                    elif (new_r, new_c) not in seen[keys]:
                        # Found a reachable cell with the same key state that hasn't been visited before
                        
                        # Mark the new cell as visited with the current key state
                        seen[keys].add((new_r, new_c))
                        
                        # Add the new cell to the queue with the current key state and distance
                        queue.append((new_r, new_c, keys, dist + 1))
            
        # Could not collect all keys, return -1
        return -1
