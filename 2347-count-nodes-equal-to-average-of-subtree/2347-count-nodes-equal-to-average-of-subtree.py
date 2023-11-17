# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def avgSum(node):
            if not node:
                return 0
            return node.val + avgSum(node.left)+avgSum(node.right)
        def length(node):
            if not node:
                return 0
            return 1 + length(node.left)+ length(node.right)
        ans = 0
        def preOrder(node):
            nonlocal ans
            if not node:
                return
            if avgSum(node)//length(node) == node.val:
                ans +=1
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return ans
