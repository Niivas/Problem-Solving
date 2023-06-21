from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # Find the minimum and maximum values in the nums list
        left, right = min(nums), max(nums)

        # Helper function to calculate the cost for a given base value
        def get_cost(base):
            # Sum up the costs for each number based on the absolute difference from the base value
            return sum(abs(base - num) * c for num, c in zip(nums, cost))

        # Initialize the answer with the cost for the first number
        ans = get_cost(nums[0])

        # Binary search to find the minimum cost
        while left <= right:
            # Calculate the middle value
            mid = (left + right) >> 1

            # Calculate costs for the current middle value and the next value
            cost_1, cost_2 = get_cost(mid), get_cost(mid + 1)

            # Update the answer with the minimum cost
            ans = min(cost_1, cost_2)

            # Adjust the search range based on the comparison of costs
            if cost_1 > cost_2:
                left = mid + 1
            else:
                right = mid - 1

        # Return the minimum cost
        return ans