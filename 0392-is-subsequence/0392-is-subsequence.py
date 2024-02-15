class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if lenS>lenT:
            return False
        p1,p2 = 0,0
        while(p1<lenS and p2<lenT):
            if s[p1] == t[p2]:
                p1 +=1
            p2 +=1
        if p1 == lenS:
            return True
        return False
