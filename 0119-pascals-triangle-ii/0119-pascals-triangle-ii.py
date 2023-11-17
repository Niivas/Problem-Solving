class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+1       
        # initialize dp with first two rows of Pascal's Triangle
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prev = [1,1]
        
        # iterate from row 2 to numRows-1
        for i in range(2,numRows):
            # create a new row with the first element as 1
            cur = [1]
            # iterate over previous row and compute sum of adjacent elements
            for j in range(1,len(prev)):
                cur.append(prev[j]+prev[j-1])
            # append 1 to the end of row and append row to dp
            cur.append(1)
            prev = cur.copy()
            
        # return dp representing Pascal's Triangle
        return cur
