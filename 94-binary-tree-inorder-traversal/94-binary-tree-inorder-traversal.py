# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        
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
        
        
        #iteration   
        stack, res = [], []      
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack: return res
            node = stack.pop()
            res.append(node.val)
            root=node.right
'''

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        while curr:
            # If left null, print curr and move right
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
			# before going left, make right most node on left subtree connected to current node, then go left
            else:
                prev = curr.left
                while prev.right and prev.right!=curr:
                    prev = prev.right
                # make thread
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                # if thread is already pointed to current node, means You have visited the node, cut the thread, print the root and  move to the right
                else:
                    prev.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res