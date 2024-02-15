from typing import List
import heapq


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        This function calculates the largest possible perimeter of a polygon that can be formed from a given list of side lengths.

        Parameters:
        nums (List[int]): A list of integers representing the side lengths.

        Returns:
        int: The largest possible perimeter if a polygon can be formed, otherwise -1.
        """

        # Calculate the total sum of all side lengths
        totalSum = sum(nums)

        # Convert the list into a max heap
        heapq._heapify_max(nums)

        # Loop until there are no more elements in the heap
        while nums:
            # Pop the maximum element from the heap
            maxElement = heapq._heappop_max(nums)

            # Subtract the maximum element from the total sum
            totalSum -= maxElement

            # If the remaining sum of side lengths is greater than the maximum element,
            # a polygon can be formed. Return the sum of the remaining side lengths and the maximum element.
            if totalSum > maxElement:
                return totalSum + maxElement

        # If no polygon can be formed, return -1
        return -1
