class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        l = len(edges)
        for i in range(l):
            graph[edges[i][0]].append((edges[i][1],succProb[i]))
            graph[edges[i][1]].append((edges[i][0],succProb[i]))
        
        distance = [0.0]*n
        distance[start] = 1.0
        queue = deque([start])

        while queue:
            cur_node = queue.popleft()

            for neighbor,prob in graph[cur_node]:
                new_prob =  distance[cur_node]*prob

                if new_prob>distance[neighbor]:
                        distance[neighbor] = new_prob
                        queue.append(neighbor)
        return distance[end]   