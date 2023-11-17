from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0  # Stores the largest altitude reached
        current_altitude = 0  # Stores the current cumulative gain

        # Iterate over each gain in the list
        for i in range(len(gain)):
            current_altitude += gain[i]  # Add the current gain to the cumulative sum
            max_altitude = max(max_altitude, current_altitude)  # Update the maximum altitude reached

        return max_altitude  # Return the largest altitude reached
