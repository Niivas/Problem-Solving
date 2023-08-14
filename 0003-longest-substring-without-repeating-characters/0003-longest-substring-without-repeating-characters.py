class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        left, right, n, maxLength, map_ = 0, 0, len(s), 0, {}
        # Initialize variables for left and right pointers, length of input string, max length of substring, and a hash map
        while right < n:
            # Loop through each character in the string
            if s[right] in map_:
                # If the current character is already in the hash map, we have found a repeated character
                if map_[s[right]] >= left:
                    # If the index of the repeated character is greater than or equal to the left pointer,
                    # it means that this repeated character is in the current substring, and we need to update the left pointer
                    maxLength = max(maxLength, right - left + 1)
                    # Update the max length of substring found so far
                    left = map_[s[right]] + 1
                    # Update the left pointer to the index of the repeated character plus one
            map_[s[right]] = right
            # Add the current character to the hash map with its index as the value
            right += 1
            # Move the right pointer to the next character
        return max(maxLength, right - left + 1) - 1
        # Return the max length of substring found so far, minus one (since we're dealing with indices here)
