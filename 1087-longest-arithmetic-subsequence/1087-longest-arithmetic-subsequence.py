from typing import List

class Solution:
    @staticmethod
    def longestArithSeqLength(nums: List[int]) -> int:
        n = len(nums)

        # If the length of the list is less than or equal to 2, return the length itself
        if n <= 2:
            return n

        # Initialize the length of the longest arithmetic subsequence found so far
        longest_length = 2

        # Create a dynamic programming table to store the lengths of arithmetic subsequences
        dp = [{} for _ in range(n)]

        # Iterate over each index 'i' in the input list
        for i in range(n):
            # Iterate over each index 'j' from 0 to 'i-1'
            for j in range(i):
                # Calculate the difference between the values at indices 'i' and 'j'
                diff = nums[i] - nums[j]

                # Update the dynamic programming table at index 'i'
                dp[i][diff] = dp[j].get(diff, 1) + 1

                # Update the longest length found so far
                longest_length = max(longest_length, dp[i][diff])

        # Return the length of the longest arithmetic subsequence
        return longest_length
