class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        
        def expand(string, start, end):
            temp = ""
            length = len(string)
            while (start>=0 and end<length):
                if start == end:
                    temp += string[start]
                    start -= 1
                    end += 1
                    continue
                if string[start] == string[end]:
                    temp = string[start] + temp + string[end]
                    start -= 1
                    end += 1
                else:
                    break
            return temp
        n = len(s)
        res = ""
        for i in range(n):
            palin = expand(s,i,i)
            if len(palin)> len(res):
                res = palin
        for i in range(n):
            palin = expand(s,i,i+1)
            if len(palin)> len(res):
                res = palin
        return res