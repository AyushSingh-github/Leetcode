# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
#iteration        
        temp = root
        while root:
            if root.val < val:
                if not root.right:
                    #if not then insert the treenode with val to right of the root
                    root.right = TreeNode(val)
                    return temp
                # or shift root to root.right
                root = root.right
        
            else:
                if not root.left:
                    #if not then insert th treenode with val to the left of the root
                    root.left = TreeNode(val)
                    return temp
                # or shift the root to root.left
                root = root.left