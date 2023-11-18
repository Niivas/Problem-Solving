class Solution:
    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix: # handle empty matrix
            return result
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while top <= bottom and left <= right:
            # Traverse top row
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            # Traverse right column
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            # Traverse bottom row
            if top <= bottom: # check if any rows left to traverse
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            # Traverse left column
            if left <= right: # check if any columns left to traverse
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result