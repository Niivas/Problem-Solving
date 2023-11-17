class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        inDegree = [0] * n
        for u, v in relations:
            u,v = u-1, v-1
            graph[u].append(v)
            inDegree[v] += 1

        queue = deque([])
        dist = [0] * n
        for i in range(n):
            if inDegree[i] == 0:
                queue.append(i)
                dist[i] = time[i]
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                inDegree[child] -= 1
                dist[child] = max(dist[child], dist[node] + time[child])
                if inDegree[child] == 0:
                    queue.append(child)
        return max(dist)
