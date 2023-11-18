class Solution:
    @staticmethod
    def longestSubarray(nums):
        left_ptr = 0  # Pointer for the left end of the current subarray
        delete_index = -1  # Index of the previous zero element encountered
        longest_length = 0  # Length of the longest subarray
        right_ptr = 0  # Pointer for the right end of the current subarray

        while right_ptr < len(nums) and left_ptr < len(nums):
            if nums[left_ptr] == 0:
                # Skip the current zero element
                left_ptr += 1
                right_ptr = left_ptr + 1
                delete_index = -1
                continue

            if nums[right_ptr] == 0:
                if delete_index == -1:
                    # Found the first zero element
                    delete_index = right_ptr
                    right_ptr += 1
                else:
                    # Found a second zero element
                    length = right_ptr - left_ptr - 1
                    longest_length = max(longest_length, length)
                    left_ptr = delete_index + 1
                    delete_index = right_ptr
                    right_ptr += 1
            else:
                # Expand the subarray
                right_ptr += 1

        if left_ptr < len(nums) and nums[left_ptr] != 0:
            # Check if there are remaining non-zero elements at the end
            if delete_index == -1:
                length = right_ptr - left_ptr
            else:
                length = right_ptr - left_ptr - 1
            longest_length = max(longest_length, length)

        return longest_length if longest_length != len(nums) else longest_length - 1
