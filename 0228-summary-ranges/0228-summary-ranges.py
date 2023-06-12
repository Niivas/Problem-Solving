from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        result = []  # List to store summary ranges
        prev = nums[0]  # Initialize prev with the first element
        start = 0  # Keep track of the starting index of a potential summary range
        n = len(nums)  # Length of the input list

        # Iterate through the input list starting from the second element
        for i in range(1, n):
            if nums[i] - prev == 1:  # Check if the current element is consecutive
                prev = nums[i]  # Update prev and continue to the next iteration
                continue
            else:
                if i - start > 1:  # Check if the potential range has more than one element
                    result.append(str(nums[start]) + "->" + str(nums[i - 1]))  # Add summary range to the result
                else:
                    result.append(str(nums[start]))  # Add single element to the result
                start = i  # Update start to the current index
            prev = nums[i]  # Update prev to the current element

        # Check for a remaining potential range after the last element
        if n - start > 1:
            result.append(str(nums[start]) + "->" + str(nums[-1]))  # Add summary range to the result
        else:
            result.append(str(nums[start]))  # Add single element to the result

        return result  # Return the list of summary ranges
