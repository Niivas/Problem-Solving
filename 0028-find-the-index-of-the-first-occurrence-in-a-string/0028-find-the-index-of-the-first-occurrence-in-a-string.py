class Solution:
    def strStr(self,haystack: str, needle: str) -> int:
        # check if needle is empty
        if not needle:
            return 0

        # get the length of haystack and needle
        n = len(haystack)
        m = len(needle)

        # iterate over possible starting indices of needle in haystack
        for i in range(n - m + 1):
            # initialize variable j to 0 for comparing characters
            j = 0
            # iterate over characters of needle and compare with haystack
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            # if all characters of needle are found in haystack, return the index
            if j == m:
                return i

        # needle is not found in haystack
        return -1
