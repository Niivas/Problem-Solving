class Solution:
    def shortestPathLength(self, graph):
        hm = defaultdict(list)
        n = len(graph)
        
        # Adjacency list of the graph
        for i in range(n):
            hm[i] = graph[i]
        
        # Dist 2D array
        # Row: bitmask -> visited node set bits are 1
        # Column: leading node
        row = 1 << n
        col = n
        dist = [[-1 for _ in range(col)] for _ in range(row)]
        
        # Queue: [{leading node 1, mask}, {leading node 2, mask}, ...]
        q = deque()
        
        for i in range(n):
            lead = i
            mask = self.setbit(0, i)
            q.append((lead, mask))
            dist[mask][lead] = 0
        
        # Applying simultaneous BFS
        while q:
            size = len(q)
            for _ in range(size):
                lead, mask = q.popleft()
                
                if mask == row - 1:  # all nodes visited
                    return dist[mask][lead]
                
                # iterate over neighbors of lead
                for child in hm[lead]:
                    newlead = child
                    newmask = self.setbit(mask, newlead)
                    
                    # avoid cycle: intelligent bfs: checking if this set is already visited
                    # set: lead, mask (visited nodes)
                    if dist[newmask][newlead] != -1:
                        continue
                    
                    dist[newmask][newlead] = dist[mask][lead] + 1
                    q.append((newlead, newmask))
        
        return 1221  # magic - LOL
    
    def setbit(self, mask, i):
        return mask | (1 << i)
