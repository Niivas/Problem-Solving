# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Store the sorted values of the nodes
        sorted_values = []
        
        # Perform in-order traversal to populate the sorted_values list
        def inorder(node):
            nonlocal sorted_values
            if not node:
                return
            inorder(node.left)  # Traverse left subtree
            sorted_values.append(node.val)  # Append current node value
            inorder(node.right)  # Traverse right subtree
        
        # Call inorder function to populate the sorted_values list
        inorder(root)
        
        # Initialize the minimum difference to positive infinity
        min_diff = math.inf
        
        # Iterate over the sorted array and calculate minimum difference
        for i in range(1, len(sorted_values)):
            diff = sorted_values[i] - sorted_values[i - 1]
            min_diff = min(min_diff, diff)
        
        # Return the minimum difference
        return min_diff