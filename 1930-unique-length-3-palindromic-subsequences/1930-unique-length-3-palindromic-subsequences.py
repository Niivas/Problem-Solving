import string


class Solution:
    @staticmethod
    def countPalindromicSubsequence(s: str) -> int:
        res = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i != -1:
                res += len(set(s[i+1:j]))
        return res
