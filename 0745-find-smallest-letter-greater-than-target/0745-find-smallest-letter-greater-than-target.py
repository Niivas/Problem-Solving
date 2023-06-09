from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Initialize the lower and upper bounds for binary search
        low, high = 0, len(letters) - 1

        # Initialize the answer with the first letter as the default value
        result = letters[0]

        # Perform binary search
        while low <= high:
            mid = (low + high) // 2

            if letters[mid] > target:
                # If the middle letter is greater than the target, update the answer
                result = letters[mid]

                # Adjust the upper bound to search for a smaller value
                high = mid - 1
            else:
                # If the middle letter is less than or equal to the target, update the lower bound
                low = mid + 1

        # Return the final answer
        return result
