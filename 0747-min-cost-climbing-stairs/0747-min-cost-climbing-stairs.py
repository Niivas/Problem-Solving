class Solution:
    @staticmethod
    def minCostClimbingStairs(cost: List[int]) -> int:
        # Initialize variables to represent the cost of reaching the first and second stairs.
        a, b = cost[0], cost[1]
        # Get the total number of stairs.
        n = len(cost)
        # Iterate through all stairs, starting from the third stair.
        for i in range(2, n):
            # Update the cost of reaching the current stair.
            # The cost of reaching the current stair is equal to the cost of the current stair
            # plus the minimum of the cost of reaching the previous stair and the cost of reaching the stair before the previous stair.
            a, b = b, cost[i] + min(a, b)
        # The minimum cost of reaching the top of the stairs is the minimum of the cost of reaching the last two stairs.
        return min(a, b)
