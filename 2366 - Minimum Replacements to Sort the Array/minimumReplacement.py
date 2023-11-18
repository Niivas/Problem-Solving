import math
from typing import List

class Solution:
    @staticmethod
    def minimumReplacement(nums: List[int]) -> int:
        # Get the length of the input list 'nums'
        n = len(nums)

        # Initialize 'cur' to point to the second-to-last element and 'prev' to the last element of the list
        cur, prev = n - 2, nums[-1]

        # Initialize the variable 'ans' to keep track of the number of replacements needed
        ans = 0

        # Iterate through the list in reverse order
        while cur >= 0:
            # If the current element is less than or equal to the previous element
            if nums[cur] <= prev:
                # Update 'prev' to the current element
                prev = nums[cur]
            else:
                # Calculate the minimum number of replacements needed to make the current element less than or equal to 'prev'
                k = math.ceil(nums[cur] / prev)

                # Increase the answer by (k - 1) since we will perform (k - 1) replacements
                ans += k - 1

                # Update 'prev' to the result of dividing the current element by 'k'
                prev = nums[cur] // k

            # Move to the previous element
            cur -= 1

        # Return the total number of replacements needed
        return ans
