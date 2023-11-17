from collections import defaultdict, deque
from typing import List

class Solution:
    def maxProbability(self, num_nodes: int, edges: List[List[int]], success_probabilities: List[float], start_node: int, end_node: int) -> float:
        # Create an adjacency list representation of the graph
        graph = defaultdict(list)
        num_edges = len(edges)
        for i in range(num_edges):
            src, dest = edges[i]
            prob = success_probabilities[i]
            graph[src].append((dest, prob))
            graph[dest].append((src, prob))

        # Initialize an array to store the maximum probabilities of reaching each node
        max_probabilities = [0.0] * num_nodes
        max_probabilities[start_node] = 1.0

        # Use a queue for breadth-first search
        queue = deque([start_node])

        # Perform breadth-first search to calculate maximum probabilities
        while queue:
            current_node = queue.popleft()

            # Iterate through the neighbors of the current node
            for neighbor, edge_prob in graph[current_node]:
                new_prob = max_probabilities[current_node] * edge_prob

                # If a higher probability path is found to reach the neighbor node, update the maximum probability
                if new_prob > max_probabilities[neighbor]:
                    max_probabilities[neighbor] = new_prob
                    queue.append(neighbor)

        # Return the maximum probability of reaching the end node from the start node
        return max_probabilities[end_node]
