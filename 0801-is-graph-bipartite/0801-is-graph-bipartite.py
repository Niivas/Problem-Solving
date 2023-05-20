class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        num_nodes = len(graph)
        color = [0] * num_nodes

        for node in range(num_nodes):
            if color[node] != 0:
                continue

            queue = deque()
            queue.append(node)
            color[node] = 1

            while queue:
                current_node = queue.popleft()

                for neighbor in graph[current_node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[current_node]
                        queue.append(neighbor)
                    elif color[neighbor] != -color[current_node]:
                        return False

        return True
