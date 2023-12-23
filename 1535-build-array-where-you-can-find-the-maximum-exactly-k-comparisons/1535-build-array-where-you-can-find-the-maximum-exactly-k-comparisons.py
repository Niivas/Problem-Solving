class Solution:
    @staticmethod
    def numOfArrays(n: int, m: int, k: int) -> int:
        # dp[a][b][c] = dp[a-1][x][c-1] (1 <= x < b) + dp[a-1][b][c] * b
        dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
        mod = 10 ** 9 + 7

        for j in range(1, m+1):
            dp[1][j][1] = 1

        for a in range(1, n+1):
            for b in range(1, m+1):
                for c in range(1, k+1):
                    s = 0
                    for x in range(1, b):
                        s += dp[a-1][x][c-1] % mod
                    s += b * dp[a-1][b][c] % mod
                    dp[a][b][c] += s % mod

        ans = 0
        for j in range(1, m+1):
            ans = (ans + dp[n][j][k]) % mod
        return ans
