class Solution:
    def repeatedSubstringPattern(self,s: str) -> bool:
        i, j = 1, 0
        n = len(s)

        # Create a list to store the "longest proper prefix which is also a suffix" values.
        dp = [0] * (n + 1)

        # Construct the DP list using the Knuth-Morris-Pratt (KMP) algorithm.
        while i < len(s):
            if s[i] == s[j]:
                i += 1
                j += 1
                dp[i] = j
            elif j == 0:
                i += 1
            else:
                j = dp[j]

        # Check if the input string can be formed by repeating a substring.
        # This is determined by the last value in the DP list and the length of the input string.
        return (dp[n] > 0 and dp[n] % (n - dp[n]) == 0)
