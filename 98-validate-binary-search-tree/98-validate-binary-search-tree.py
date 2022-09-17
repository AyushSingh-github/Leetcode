# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        a=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)
            
        inorder(root)
        for i in range(len(a)-1):
            if a[i] >= a[i+1]:
                return False
        return True
         