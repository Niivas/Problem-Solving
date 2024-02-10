class Solution:
    @staticmethod
    def integerBreak(n: int) -> int:
        # create a list of length n+1 to store the maximum product for each subproblem
        dp = [0]*(n+1)
        # base cases: dp[1] = dp[2] = 1
        dp[1] = 1
        dp[2] = 1
        # loop from 3 to n, which are the subproblems we need to solve
        for i in range(3,n+1):
            # initialize a variable to store the maximum product for i
            maxProduct = 0
            # loop from 1 to i//2, which are the possible ways to split i into two parts
            for j in range(1,(i//2)+1):
                # calculate the product of breaking i-j and j into smaller parts or using them as they are
                product = max(dp[i-j],i-j)*max(dp[j],j)
                # update maxProduct with the maximum value of this product and the current maxProduct
                maxProduct = max(maxProduct,product)
            # set dp[i] to maxProduct, which is the maximum product for i
            dp[i]=maxProduct

        # return dp[n], which is the final answer
        return dp[n]
