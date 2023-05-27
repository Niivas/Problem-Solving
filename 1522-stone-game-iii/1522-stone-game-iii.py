from typing import List
from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def game(i: int) -> int:
            # Base case: no more stones to pick
            if i >= n:
                return 0

            # Calculate the sum of the current stone
            total = stoneValue[i]

            # Calculate the optimal value Alice can obtain
            value = total - game(i + 1)

            # Iterate over the different choices Alice can make
            for j in range(i + 1, min(i + 3, n)):
                # Update the sum with the value of the stone
                total += stoneValue[j]

                # Calculate the maximum value Alice can obtain
                value = max(value, total - game(j + 1))

            return value

        # Calculate the score (optimal value for Alice)
        score = game(0)

        # Determine the winner based on the score
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        return "Tie"
