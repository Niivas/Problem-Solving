class Solution:
    def candy(self, ratings):
        # Get the number of children
        n = len(ratings)
        
        # Create an array to store the number of candies for each child, initialize all with 1
        candies_array = [1] * n

        # First pass: Check ratings from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                # If the current child has a higher rating than the previous one, give them one more candy
                candies_array[i] = candies_array[i - 1] + 1

        # Second pass: Check ratings from right to left
        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i + 1]:
                # If the current child has a higher rating than the next one, make sure they have more candies if needed
                candies_array[i] = max(candies_array[i + 1] + 1, candies_array[i])

        # Return the total number of candies required, which is the sum of candies for all children
        return sum(candies_array)
