class Solution:
    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)

        for i in t:
            if i not in c1:
                return i
            if c2[i]>c1[i]:
                return i