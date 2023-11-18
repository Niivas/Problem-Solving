# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    @staticmethod
    def diameterOfBinaryTree(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = -1

        def height(root):
            nonlocal ans
            if not root:
                return -1
            left_height = height(root.left)
            right_height = height(root.right)
            ans = max(ans,left_height+right_height+2)
            return max(right_height,left_height)+1
        height(root)
        return ans