# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def findMode(root: Optional[TreeNode]) -> List[int]:
        # 1. Initialize a dictionary to store the frequency of each node
        freq = {}

        # 2. Define a helper function to traverse the tree in-order
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            freq[node.val] = freq.get(node.val, 0) + 1
            inorder(node.right)
        
        # 3. Traverse the tree in-order
        inorder(root)
        
        # 4. Find the mode(s)
        max_freq = max(freq.values())
        return [k for k, v in freq.items() if v == max_freq]