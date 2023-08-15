from typing import List

class Solution:
    def findMaxAverage(nums: List[int], k: int) -> float:
        # Initialize the current sum as the sum of the first (k-1) elements
        curSum = sum(nums[:k-1])

        # Initialize pointers for the left and right boundaries of the subarray
        left, right = 0, k - 1

        # Initialize the maximum sum with negative infinity
        maxSum = -float('inf')

        # Iterate through the array while the right boundary is within bounds
        while right < len(nums):
            # Add the current element to the current sum
            curSum += nums[right]

            # Update the maximum sum if the current sum is greater
            if curSum > maxSum:
                maxSum = curSum

            # Subtract the leftmost element from the current sum
            curSum -= nums[left]

            # Move the left and right boundaries one step to the right
            left += 1
            right += 1

        # Return the maximum average by dividing the maximum sum by k
        return maxSum / k
