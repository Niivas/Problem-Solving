class Solution:
    @staticmethod
    def twoSum(numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers, left and right, pointing to the beginning and end of the input list
        left, right = 0, len(numbers) - 1

        # Continue searching until the pointers meet or cross
        while left < right:
            # Compute the current sum of the numbers pointed to by the two pointers
            curSum = numbers[left] + numbers[right]

            # If the current sum is equal to the target, return the indices of the two numbers
            if curSum == target:
                return [left + 1, right + 1]

            # If the current sum is greater than the target, move the right pointer to the left
            elif curSum > target:
                right -= 1

            # If the current sum is less than the target, move the left pointer to the right
            else:
                left += 1
