# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #bfs
        if root is None:
            return 0
        else:
            lefth=self.maxDepth(root.left)
            righth=self.maxDepth(root.right)
        return 1 + max(lefth,righth)