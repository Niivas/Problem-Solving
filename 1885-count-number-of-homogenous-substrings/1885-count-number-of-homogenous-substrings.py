class Solution:
    @staticmethod
    def countHomogenous(s: str) -> int:
        n = len(s)
        i,j = 0,0
        ans = 0
        while j<n:
            if s[i]==s[j]:
                j +=1
            else:
                ans += (j-i)*(j-i+1)//2
                i = j
        ans += (j-i)*(j-i+1)//2
        return ans%(10**9 + 7)
