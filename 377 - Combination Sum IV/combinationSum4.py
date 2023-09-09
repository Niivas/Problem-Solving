class Solution:
    def combinationSum4(self, nums, target):
        # Sort the inputs list 'nums' in ascending order.
        nums.sort()

        # Initialize a list 'combs' to store the number of combinations for each target sum.
        # The length of 'combs' is (target + one) to account for the target sum of 0.
        combs = [1] + [0] * target

        # Loop through all possible target sums from one to 'target'.
        for i in range(1, target + 1):
            # Loop through each number in 'nums'.
            for num in nums:
                # If the current number is greater than the target sum, break the loop.
                if num > i:
                    break
                # If the current number is equal to the target sum, increment the count of combinations.
                if num == i:
                    combs[i] += 1
                # If the current number is less than the target sum, add the number of combinations
                # for the remaining sum (i - num) to the count of combinations for the current sum (i).
                if num < i:
                    combs[i] += combs[i - num]

        # Return the number of combinations for the target sum.
        return combs[target]
