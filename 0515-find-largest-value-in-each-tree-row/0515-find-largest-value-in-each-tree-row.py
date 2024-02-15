# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def largestValues(root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level_nodes = deque([root])
        res = []

        while level_nodes:
            n = len(level_nodes)
            level_max = -float('inf')
            for _ in range(n):
                node = level_nodes.popleft()
                level_max = max(level_max,node.val)
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
            res.append(level_max)
        return res

