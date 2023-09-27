class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        N = 0
        for i, c in enumerate(s):
            N = N * int(c) if c.isdigit() else N + 1
            if k <= N: break
        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                N /= int(c)
                k %= N
            else:
                if k == N or k == 0: return c
                N -= 1