from typing import List

class Solution:
    @staticmethod
    def numOfWays(nums: List[int]) -> int:
        # Calculate the length of the input list
        n = len(nums)
        
        # Create a 2D table to store Pascal's triangle values
        pascal_table = [[0 for _ in range(n)] for _ in range(n)]
        
        # Define the modulo value
        mod = (10 ** 9 + 7)

        # Fill the Pascal's triangle values in the table
        for i in range(n):
            for j in range(i + 1):
                if j == 0 or i == j:
                    pascal_table[i][j] = 1
                else:
                    pascal_table[i][j] = (pascal_table[i - 1][j] + pascal_table[i - 1][j - 1]) % mod

        # Recursive function to compute the number of ways to arrange the numbers
        def count_arrangements(arr: List[int]) -> int:
            # Base case: If the length of the array is <= 2, there's only one way to arrange the numbers
            if len(arr) <= 2:
                return 1

            # Divide the array into left and right subarrays based on the first element
            left_arr = [val for val in arr if val < arr[0]]
            right_arr = [val for val in arr if val > arr[0]]

            # Compute the number of ways by multiplying the following values:
            # - The value from Pascal's triangle for the current subarray
            # - The number of ways for the left and right subarrays (recursively)
            return (
                pascal_table[len(left_arr) + len(right_arr)][len(right_arr)]
                * count_arrangements(left_arr)
                * count_arrangements(right_arr)
            )

        # Return the final result modulo mod
        return (count_arrangements(nums) - 1) % mod