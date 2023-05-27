class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def game(i):
            if i>=n:
                return 0
            
            sum = stoneValue[i]
            value = sum-game(i+1)
            for j in range(i+1,min(i+3,n)):
                sum += stoneValue[j]
                value = max(value,sum-game(j+1))
            return value

        score = game(0)

        if score>0:
            return "Alice"
        elif score<0:
            return "Bob"
        return "Tie"

