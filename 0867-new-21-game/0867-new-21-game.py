class Solution:
    @staticmethod
    def new21Game(N: int, K: int, maxPts: int) -> float:
        # Check if winning is guaranteed
        if K == 0 or N >= K + maxPts:
            return 1.0

        # Initialize the probability list
        probabilities = [1.0] + [0.0] * N

        # Initialize the sum of probabilities for the last W cards
        last_maxPts_sum = 1.0

        # Calculate the probabilities for each score from 1 to N
        for i in range(1, N + 1):
            # Probability of achieving score i
            probabilities[i] = last_maxPts_sum / maxPts

            # Update the sum of probabilities for the last W cards
            if i < K:
                last_maxPts_sum += probabilities[i]

            if i - maxPts >= 0:
                last_maxPts_sum -= probabilities[i - maxPts]

        # Return the sum of probabilities starting from index K
        return sum(probabilities[K:])
