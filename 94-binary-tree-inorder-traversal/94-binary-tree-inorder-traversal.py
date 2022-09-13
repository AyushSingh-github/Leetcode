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
        A = []
        stack = []
        cur_node = root
        while stack or cur_node:
            if not cur_node:
                node = stack.pop()
                A.append(node.val)
                cur_node = node.right
    
            else:
                stack.append(cur_node)
                cur_node = cur_node.left
        
        return A