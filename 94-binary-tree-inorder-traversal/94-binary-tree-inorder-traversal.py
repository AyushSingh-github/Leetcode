# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #recursive
        '''
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        '''
        
        #iterative
        stack, res = [], []      
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack: return res
            node = stack.pop()
            res.append(node.val)
            root=node.right