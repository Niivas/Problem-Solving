class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words using whitespace as the delimiter
        s = s.split()

        # Reverse the order of words
        s = s[::-1]
        
        # Join the reversed words with whitespace and return the result
        return " ".join(s)
