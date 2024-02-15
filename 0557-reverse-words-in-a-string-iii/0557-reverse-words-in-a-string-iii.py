class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        return " ".join(list(map(lambda x:x[::-1],s.split(" "))))
