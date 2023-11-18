class Solution:
        @staticmethod
        def minCostConnectPoints(p: List[List[int]]) -> int:
        
            def manhattan(x, y):
                return abs(x[0]-y[0]) + abs(x[1]-y[1])
            
            ans, n = 0, len(p)
            seen = set()
            vertices = [(0, (0, 0))]
            
            while len(seen) < n:
                # print(vertices, seen)
                w, (u, v) = heapq.heappop(vertices)            
                if v in seen: continue
                ans += w
                seen.add(v)
                for j in range(n):
                    if j not in seen and j!=v:
                        heapq.heappush(vertices, (manhattan(p[j], p[v]), (v, j)))
            return ans
