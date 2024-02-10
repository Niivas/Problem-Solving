# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    # Initialize prev and ans as class variables
    prev = None
    ans = math.inf

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Base case: empty tree, return the current minimum difference (ans)
        if not root:
            return self.ans

        # Traverse the left subtree recursively
        self.getMinimumDifference(root.left)

        # Check if prev is not None (not the first node)
        if self.prev is not None:
            # Calculate the absolute difference between current node value and previous node value
            diff = abs(root.val - self.prev)
            # Update the minimum difference (ans) if the current difference is smaller
            self.ans = min(self.ans, diff)

        # Update prev to the current node value
        self.prev = root.val

        # Traverse the right subtree recursively
        self.getMinimumDifference(root.right)

        # Return the minimum difference (ans)
        return self.ans
