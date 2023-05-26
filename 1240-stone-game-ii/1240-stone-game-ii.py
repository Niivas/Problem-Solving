class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        prefix_sum = [piles[0]]
        for i in range(1,len(piles)):
            prefix_sum.append(prefix_sum[i-1]+piles[i])
    
        @lru_cache(None)
        def dfs(start, M):
            res = 0
            total = prefix_sum[-1]-prefix_sum[start-1] if start>0 else prefix_sum[-1]
            for i in range(1, min(2 * M + 1, len(piles) - start + 1)):
                optima = dfs(start + i, max(M, i))
                res = max(res, total - optima)
            return res

        return dfs(0, 1)