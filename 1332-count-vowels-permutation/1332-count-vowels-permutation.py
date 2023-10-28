class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7  # Define a constant MOD for modulo arithmetic

        # Create a 2D list dp to store the number of valid strings of length i ending with each vowel
        dp = [[0] * 5 for _ in range(n)]

        # Initialize the base case for strings of length 1
        for i in range(5):
            dp[0][i] = 1

        # Calculate the number of valid strings for each length from 2 to n
        for i in range(1, n):
            # For each vowel, calculate the number of valid strings ending with that vowel
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MOD  # 'a' can follow 'e', 'i', or 'u'
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD  # 'e' can follow 'a' or 'i'
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD  # 'i' can follow 'e' or 'o'
            dp[i][3] = dp[i - 1][2]  # 'o' can only follow 'i'
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MOD  # 'u' can follow 'i' or 'o'

        # The final result is the sum of all valid strings of length n, modulo MOD
        return sum(dp[-1]) % MOD
