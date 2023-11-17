
class Solution:
    @staticmethod
    def numDecodings(s: str) -> int:
        n=len(s)
        @lru_cache(None)
        def dfs(i):
            if i>n:
                return 0
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            #count=0
            if int(s[i:i+2])<27:
                return dfs(i+2)+dfs(i+1)
            return dfs(i+1)
        return dfs(0)

