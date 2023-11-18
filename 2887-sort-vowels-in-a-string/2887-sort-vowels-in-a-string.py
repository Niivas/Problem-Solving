class Solution:
    @staticmethod
    def sortVowels(s: str) -> str:
        s = list(s)
        vowels = set("AEIOU") | set("aeiou")
        toBeSorted = []
        for i in s:
            if i in vowels:
                toBeSorted.append(i)
        toBeSorted.sort()
        n = len(s)
        k = 0
        for i in range(n):
            if s[i] in vowels:
                s[i]= toBeSorted[k]
                k+=1
        return "".join(s)
