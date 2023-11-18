class Solution:
    @staticmethod
    def minSubArrayLen(target: int, nums: List[int]) -> int:
        # Initialize variables for left index, right index, and current sum
        left, right, curSum = 0, 0, 0
        # Initialize variable for minimum subarray length, set to positive infinity
        minLen = math.inf
        # Continue the loop as long as the left index is less than or equal to the right index
        while left <= right:
            # If the current sum is greater than or equal to the target, update the minimum length, remove the left element from the subarray, and increment the left index
            if curSum >= target:
                minLen = min(minLen, right - left)
                curSum -= nums[left]
                left += 1
            # If the current sum is less than the target, add the next element to the subarray and increment the right index
            else:
                # If the right index is greater than or equal to the length of nums, break out of the loop
                if right >= len(nums):
                    break
                else:
                    curSum += nums[right]
                    right += 1
        # Return the minimum subarray length, or 0 if it remains positive infinity
        return minLen if minLen != math.inf else 0
