from typing import List

class Solution:
    def putMarbles(self, weights: List[int], target_pairs: int) -> int:
        # Calculate the number of weights
        num_weights = len(weights)

        # Initialize a list to store pair weights
        pair_weights = [0] * (num_weights - 1)

        # Calculate the sum of consecutive pairs of weights
        for i in range(num_weights - 1):
            pair_weights[i] += weights[i] + weights[i + 1]

        # Sort the pair weights in ascending order
        pair_weights.sort()

        # Calculate the sum of weight differences between the largest and smallest pairs
        total_difference = 0
        for i in range(target_pairs - 1):
            total_difference += pair_weights[num_weights - 2 - i] - pair_weights[i]

        # Return the total weight difference
        return total_difference
