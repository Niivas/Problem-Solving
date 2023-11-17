class Solution:
    @staticmethod
    def minDeletions(s: str) -> int:
        # Initialize an array to count the frequency of each lowercase alphabet character
        charArray = [0] * 26

        # Count the frequency of characters in the input string
        for char in s:
            charArray[ord(char) - 97] += 1

        # Sort the character frequencies in descending order
        charArray.sort(reverse=True)

        # Initialize a set to keep track of characters with the same frequency
        charset = {charArray[0]}

        # Initialize the variable to store the minimum number of deletions
        ans = 0

        # Iterate through the character frequencies
        for i in range(1, 26):
            # If the count of the character is 0, no more characters with higher frequencies exist
            if charArray[i] == 0:
                break

            # While the character is already in the set, increment deletions, decrement count
            while charArray[i] in charset:
                ans += 1
                charArray[i] -= 1

                # If the count becomes 0, break out of the loop
                if charArray[i] == 0:
                    break

            # If the count is not 0 after the loop, add it to the set
            if charArray[i] != 0:
                charset.add(charArray[i])

        # Return the minimum number of deletions required
        return ans
