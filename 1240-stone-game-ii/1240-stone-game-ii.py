from typing import List
from functools import lru_cache

class Solution:
    @staticmethod
    def stoneGameII(piles: List[int]) -> int:
        # Calculate prefix sums
        prefix_sum = [piles[0]]
        for i in range(1, len(piles)):
            prefix_sum.append(prefix_sum[i-1] + piles[i])

        @lru_cache(None)
        def dfs(start: int, M: int) -> int:
            res = 0
            # Calculate the total number of stones remaining
            total = prefix_sum[-1] - prefix_sum[start-1] if start > 0 else prefix_sum[-1]

            # Iterate over the possible number of stones to take in the next move
            for i in range(1, min(2 * M + 1, len(piles) - start + 1)):
                # Recursively call the function with updated parameters
                optima = dfs(start + i, max(M, i))
                # Update the maximum number of stones the first player can obtain
                res = max(res, total - optima)

            return res

        # Start the recursion from the beginning of the array with M as 1
        return dfs(0, 1)
