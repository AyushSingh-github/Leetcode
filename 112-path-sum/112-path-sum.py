# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #dfs recursion
        '''
        if not root: return
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum-root.val)
        '''
        
        #iteration
        if root:
            stack = [[root,targetSum - root.val]]
        else:
            return []
        
        while stack:
            currnode, currsum = stack.pop() 
            if (not currnode.left and not currnode.right and currsum == 0):
                return True
            
            if currnode.left:
                stack.append([currnode.left , currsum - currnode.left.val])
                
            if currnode.right:
                stack.append([currnode.right, currsum - currnode.right.val])
                
        return False