# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #dfs recursion
        '''
        if not root:
            return None
    
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        '''
        
        #bfs with queue
        '''
        if not root:
            return
        queue = deque([root])
        #print(queue,"\n")
        
        while queue:
            curr  = queue.popleft()
            curr.left , curr.right = curr.right , curr.left
            if curr.left :
                queue.append(curr.left)
                #print(queue)
            if curr.right :
                queue.append(curr.right)
        return root 
        '''
        
        #simple recursion
        if not root:
            return
        root.left, root.right =  self.invertTree(root.right), self.invertTree(root.left)
        return root
        
        
        
        
        
        
        
        
        
        
        
        
    
    