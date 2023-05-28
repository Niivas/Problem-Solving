class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, j):
            if j<=i+1:
                return 0
            # i+1<j
            res = float('inf')
            for k in range(i+1, j):
                # cut [cuts[i], cuts[j]] at k
                res =min(res, cuts[j]-cuts[i]+dp(i,k) + dp(k,j))
            return res
        cuts.append(0)
        cuts.append(n)
        cuts = sorted(cuts)
        return dp(0, len(cuts)-1)