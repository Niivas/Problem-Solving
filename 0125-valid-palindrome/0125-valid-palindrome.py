class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        # Convert the string to lowercase
        s = s.lower()

        # Initialize an empty string to store alphanumeric characters
        res = ""

        # Iterate through each character in the string
        for i in s:
            # Check if the character is alphabetic or alphanumeric
            if i.isalpha() or i.isalnum():
                # If it is, add it to the result string
                res += i
        
        # Check if the result string is equal to its reverse
        return res == res[::-1]
