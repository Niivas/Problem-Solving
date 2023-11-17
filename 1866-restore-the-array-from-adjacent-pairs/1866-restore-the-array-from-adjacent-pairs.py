class Solution:
    
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
            
        result = []
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                result = [node, neighbors[0]]
                break
        
        while len(result) <= len(pairs):
            last, prev = result[-1], result[-2]
            candidates = graph[last]
            if candidates[0] != prev:
                result.append(candidates[0])
            else:
                result.append(candidates[1])
        
        return result   
