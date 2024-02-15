from collections import defaultdict
from typing import List

class Solution:
    @staticmethod
    def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
        # Create a defaultdict to represent the graph where each node maps to a set of connected nodes
        graph = defaultdict(set)

        # Populate the graph with the given road connections
        for i, j in roads:
            graph[i].add(j)
            graph[j].add(i)

        # Initialize variables to keep track of the two nodes with maximum network ranks and the final answer
        max_rank_node1, max_rank_node2 = 0, 1
        max_network_rank = 0

        # Iterate through each node in the graph
        for key in graph:
            # Iterate through each other node in the graph
            for key2 in graph:
                if key != key2:
                    # Calculate the network rank of the two nodes
                    if key2 in graph[key]:
                        network_rank = len(graph[key]) + len(graph[key2]) - 1
                    else:
                        network_rank = len(graph[key]) + len(graph[key2])

                    # Update the maximum network rank if needed
                    max_network_rank = max(network_rank, max_network_rank)

        return max_network_rank
