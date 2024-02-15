class Solution:
    @staticmethod
    def maxArea(H: List[int]) -> int:
        # initialize the maximum area seen so far and the two pointers
        ans, i, j = 0, 0, len(H)-1
        
        # iterate until the two pointers meet
        while (i < j):
            # compute the area between the two pointers
            if H[i] <= H[j]:
                res = H[i] * (j - i)
                i += 1
            else:
                res = H[j] * (j - i)
                j -= 1
            
            # update the maximum area seen so far
            if res > ans:
                ans = res
        
        # return the maximum area seen
        return ans
