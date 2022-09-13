# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursion
        '''
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] 
        '''
        
        #iteration
        '''
        if not root :
            return []
        stk = [root]
        result  = []
        while stk :
            temp = stk.pop()
            result.insert(0,temp.val)
            if temp.left :
                stk.append(temp.left)
            if temp.right :
                stk.append(temp.right)
        return result
        '''
        
        ans = deque()
        stack = [root]
        while stack: 
            node = stack.pop()
            if not node:
                continue
            ans.appendleft(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return ans