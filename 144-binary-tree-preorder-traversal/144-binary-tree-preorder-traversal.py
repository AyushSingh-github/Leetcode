# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Recursion
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        #Iteratively
        '''
    if root==None:
        return root
    else:
        myList=[]
        stack = [root]
        while stack:
            current = stack.pop()
            myList.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
       return myList
'''