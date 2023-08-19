import collections
from typing import List, Any


class UnionFindSet:
    def __init__(self, n=0):
        # Initialize the data structures for Union-Find set.
        self.parents = {}  # Mapping of elements to their parents.
        self.ranks = {}    # Mapping of elements to their ranks.
        self.count = 0     # Count of distinct elements in the set.
        for i in range(n):
            self.add(i)     # Initialize each element as its own parent.

    def add(self, p):
        # Add a new element to the set.
        self.parents[p] = p  # Initialize the parent of the element to itself.
        self.ranks[p] = 1    # Initialize the rank of the element to 1.
        self.count += 1      # Increase the count of elements.

    def find(self, u):
        # Find the root parent of the given element 'u'.
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])  # Path compression.
        return self.parents[u]

    def union(self, u, v):
        # Union two groups represented by elements 'u' and 'v'.
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False  # If they are already in the same group, no need to union.

        # Perform union by rank.
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        self.count -= 1  # Decrease the count as two groups are merged.
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> list[set[Any]]:
        # Function to perform DFS to mark critical and pseudo-critical edges.
        def dfs(curr, level, parent):
            levels[curr] = level  # Set the level of the current node.
            for child, i in graph[curr]:
                if child == parent:
                    continue
                elif levels[child] == -1:
                    levels[curr] = min(levels[curr], dfs(child, level + 1, curr))
                else:
                    levels[curr] = min(levels[curr], levels[child])
                if levels[child] >= level + 1 and i not in p_cri:
                    cri.add(i)
            return levels[curr]

        cri, p_cri = set(), set()  # Initialize sets to store critical and pseudo-critical edges.

        dic = collections.defaultdict(list)  # Dictionary to store edges by their weights.
        for i, (u, v, w) in enumerate(edges):
            dic[w].append([u, v, i])  # Add the edge to the dictionary based on its weight.

        union_set = UnionFindSet(n)  # Initialize the Union-Find set.

        for w in sorted(dic):
            seen = collections.defaultdict(set)  # Dictionary to store edges seen for each parent pair.
            for u, v, i in dic[w]:
                pu, pv = union_set.find(u), union_set.find(v)
                if pu == pv:
                    continue
                seen[min(pu, pv), max(pu, pv)].add(i)  # Store the edge connecting the parent pair.

            w_edges, graph = [], collections.defaultdict(list)  # Lists to store weight-w edges and graph.
            for pu, pv in seen:
                if len(seen[pu, pv]) > 1:
                    p_cri |= seen[pu, pv]  # Multiple edges connect the same parent pair, pseudo-critical.
                edge_idx = seen[pu, pv].pop()
                graph[pu].append((pv, edge_idx))
                graph[pv].append((pu, edge_idx))
                w_edges.append((pu, pv, edge_idx))
                union_set.union(pu, pv)  # Union the parent groups.

            levels = [-1] * n  # Initialize levels for DFS.
            for u, v, i in w_edges:
                if levels[u] == -1:
                    dfs(u, 0, -1)  # Run DFS to mark critical edges.
            for u, v, i in w_edges:
                if i not in cri:
                    p_cri.add(i)  # Edges not in 'cri' are pseudo-critical.

        return [cri, p_cri]  # Return the sets of critical and pseudo-critical edges.