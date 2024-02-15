class Solution:
    def isCyclic(self, adj_list, src, visited, recursion_stack):
        visited[src] = True
        recursion_stack[src] = True
        for neighbor in adj_list[src]:
            if not visited[neighbor] and self.isCyclic(adj_list, neighbor, visited, recursion_stack):
                return True
            if recursion_stack[neighbor]:
                return True
        recursion_stack[src] = False
        return False

    def eventualSafeNodes(self, graph):
        num_nodes = len(graph)
        adj_list = [[] for _ in range(num_nodes)]

        # Construct the adjacency list
        for node in range(num_nodes):
            for neighbor in graph[node]:
                adj_list[node].append(neighbor)

        visited = [False] * num_nodes
        recursion_stack = [False] * num_nodes

        # Perform DFS on all nodes to detect cycles
        for node in range(num_nodes):
            if not visited[node]:
                self.isCyclic(adj_list, node, visited, recursion_stack)

        eventual_safe_nodes = []
        for node, item in enumerate(recursion_stack):
            if not item:
                eventual_safe_nodes.append(node)
        return eventual_safe_nodes
