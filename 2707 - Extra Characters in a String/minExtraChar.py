from typing import List

class Solution:
    @staticmethod
    def minExtraChar(s: str, dictionary: List[str]) -> int:
        # Initialize the maximum value to represent an upper bound
        max_val = len(s) + 1

        # Initialize a dynamic programming (dp) list to store results for each position in s
        dp = [max_val] * (len(s) + 1)

        # The base case: No extra characters needed to make an empty string
        dp[0] = 0

        # Convert the dictionary into a set for faster lookup
        dictionary_set = set(dictionary)

        # Loop through each position in the string s
        for i in range(1, len(s) + 1):
            # By default, assume one more extra character than the previous position
            dp[i] = dp[i - 1] + 1

            # Iterate through all possible substrings ending at position i
            for j in range(1, i + 1):
                # Check if the current substring is in the dictionary_set
                if s[i - j:i] in dictionary_set:
                    # If it is, update dp[i] to the minimum between its current value and dp[i - l]
                    dp[i] = min(dp[i], dp[i - j])

        # Return the minimum number of extra characters needed to make the entire string valid
        return dp[-1]
