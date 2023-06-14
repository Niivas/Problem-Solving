# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev,ans = None,math.inf
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.ans

        self.getMinimumDifference(root.left)

        if self.prev != None:
            self.ans = min(self.ans,abs(root.val - self.prev))
        self.prev = root.val
        
        self.getMinimumDifference(root.right)
        return self.ans