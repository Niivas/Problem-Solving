from typing import List

class Solution:
    @staticmethod
    def minTaps(n: int, ranges: List[int]) -> int:
        # Initialize an array to represent the maximum rightmost coverage of each tap location
        sprinkleRanges = [-1] * n

        # Initialize the number of taps used
        taps = 0

        # Iterate through each tap's coverage range and update the sprinkleRanges array
        for idx, val in enumerate(ranges):
            if val == 0:
                continue
            # Calculate the leftmost and rightmost coverage of the current tap
            leftMost = max(0, idx - val)
            rightMost = min(n, idx + val)
            # Update the sprinkleRanges array with the maximum coverage
            sprinkleRanges[leftMost] = max(sprinkleRanges[leftMost], rightMost)

        # Initialize variables for tracking the current position and the farthest reachable point
        cur = 0
        farCanReach = -1

        # Iterate through the sprinkleRanges array to find the minimum number of taps needed
        for idx, rightMost in enumerate(sprinkleRanges):
            # Update the farCanReach with the maximum reachable point
            farCanReach = max(farCanReach, rightMost)

            # If the current index reaches the current position, update the position and increment taps
            if idx == cur:
                # If there's no coverage for the current tap and farCanReach doesn't reach this point, return -1
                if rightMost == -1 and farCanReach <= idx:
                    return -1
                cur = farCanReach
                taps += 1

        # If the farCanReach reaches the last position, return the number of taps used
        if farCanReach == n:
            return taps
        # Otherwise, it's not possible to cover the entire area, so return -1
        return -1
