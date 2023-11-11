class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            self.graph[u].append((v, cost))

    def addEdge(self, edge: List[int]) -> None:
        u, v, cost = edge
        self.graph[u].append((v, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float("inf")] * len(self.graph)
        dist[node1] = 0
        pq = [(0, node1)]
        while pq:
            d, node = heapq.heappop(pq)
            if node == node2:
                return d
            if d > dist[node]:
                continue
            for neighbor, cost in self.graph[node]:
                if d + cost < dist[neighbor]:
                    dist[neighbor] = d + cost
                    heapq.heappush(pq, (dist[neighbor], neighbor))
        return -1
    


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)