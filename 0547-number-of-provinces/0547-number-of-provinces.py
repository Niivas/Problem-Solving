from collections import defaultdict, deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Step 1: Create a dictionary that represents the adjacency list of the graph
        graph = defaultdict(set)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i+1].add(j+1)
                    graph[j+1].add(i+1)

        # Step 2: Initialize variables
        count, visited = 0, set()

        # Step 3-5: Perform BFS for each unvisited vertex
        for key in graph:
            if key in visited:
                continue
            queue = deque()
            queue.append(key)
            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
            count += 1

        # Step 6: Return the final count
        return count
