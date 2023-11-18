class Solution:
    @staticmethod
    def find132pattern(nums: List[int]) -> bool:
        # n: number of elements in the array
        # smallest_element_seen_so_far: smallest element seen so far
        # stack_of_greater_elements: stack of elements that are greater than smallest_element_seen_so_far

        n = len(nums)
        smallest_element_seen_so_far = float('-inf')
        stack_of_greater_elements = []

        # Iterate over the array from right to left
        for i in range(n - 1, -1, -1):

            # If the current element is less than smallest_element_seen_so_far, return True
            if nums[i] < smallest_element_seen_so_far:
                return True

            # Otherwise, pop elements from the stack until we find an element that is greater than the current element and less than smallest_element_seen_so_far
            while stack_of_greater_elements and nums[i] > stack_of_greater_elements[-1]:
                smallest_element_seen_so_far = stack_of_greater_elements.pop()

            # Push the current element onto the stack
            stack_of_greater_elements.append(nums[i])

        # Return False if no 132 pattern is found
        return False
