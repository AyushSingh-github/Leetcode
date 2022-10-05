# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        '''
        if depth < 2:
            node=TreeNode(val)
            node.left=root
            return node
        
        def dfs(node,ht):
            if ht==depth-1:
                cur1=TreeNode(val)
                cur2=TreeNode(val)
                cur1.left=node.left
                cur2.right=node.right
                node.left=cur1
                node.right=cur2
                
            if node.left:
                dfs(node.left,ht+1)
            if node.right:
                dfs(node.right,ht+1)
            
            
        dfs(root,1)
        return root
        '''
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # deal with depth=1 first
        # simply make the root node a left child of the new node
        if depth == 1:
            return TreeNode(val=val, left=root)  
        
        def dfs(node, level):
            if level == depth - 1:  
                
                # check if current depth (i.e. level) is at depth-1
				# if so, check left and right children
				# if left child exists (we'll call it the old left child), create a new node of value val 
                #and make the old left child the left child of the new node.
				# else (i.e. the left child doesn't exist), create a new leaf node of value val and set it
                #as the left child
                
				# same for right child
                if node.left:
                    node.left = TreeNode(val, left=node.left) 
                else:
                    node.left = TreeNode(val)
                
                if node.right:
                    node.right = TreeNode(val, right=node.right)
                else:
                    node.right = TreeNode(val)
                return node
            
            # current depth is not depth-1 --> check left and right children recursively
            else: 
                if node.left: 
                    node.left = dfs(node.left, level+1)
                if node.right:
                    node.right = dfs(node.right, level+1)
                return node
            
        # add row
        # call dfs starting from the root which is at level/current depth=1
        root = dfs(root, 1)  
        return root