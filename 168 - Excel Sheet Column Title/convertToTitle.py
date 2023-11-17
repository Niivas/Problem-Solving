class Solution:
    @staticmethod
    def convertToTitle(columnNumber: int) -> str:
        ans = ""  # Initialize an empty string to store the resulting column title

        while columnNumber:
            columnNumber -= 1  # Decrement columnNumber by 1 for 1-based indexing

            # Calculate the character corresponding to the current column number
            # Modulo operation gives position in the alphabet, adding 65 converts to ASCII
            current_char = chr((columnNumber % 26) + 65)

            ans += current_char  # Append the calculated character to the ans string
            columnNumber //= 26  # Integer divide columnNumber by 26 to move left

        return ans[::-1]  # Reverse the ans string before returning the final result
