class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lenS = len(s)  # Length of string s
        lenT = len(t)  # Length of string t
        
        if lenS > lenT:
            return False  # If s is longer than t, it cannot be a subsequence
        
        p1, p2 = 0, 0  # Pointers for string s and t
        
        while p1 < lenS and p2 < lenT:
            if s[p1] == t[p2]:  # If characters match, move pointer p1
                p1 += 1
            p2 += 1  # Move pointer p2 regardless
            
        if p1 == lenS:
            return True  # If p1 reached the end of s, s is a subsequence of t
        
        return False  # Otherwise, s is not a subsequence of t