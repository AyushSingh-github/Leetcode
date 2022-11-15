# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root:
            return self.countNodes(root.left)+ self.countNodes(root.right) + 1
        return 0
'''

#First we calculate the height of the tree by reaching the leftmost node. Then we calculate the number of node empty leaf nodes using reverse preorder traversal. Why? because we only need to find the number of empty leaves and we know the complete binary tree fills from left, so we count from right.

#How does it take < O(n)? Since we only process till nodes at maxheight - 1 and we dont process the leaf nodes, we also break once we find a non-empty leaf node.



class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        node = root
        height = 0
        
        while node: # find height
            height += 1
            node = node.left
        
        stack = [(root, 1)]
        empties = 0
        
        while stack: # find empty leaf nodes
            node, h = stack.pop()
            
            if h == height - 1:
                if node.right is None: empties += 1
                else: break
                if node.left is None: empties += 1
                else: break
                continue
            
            if node.left: stack.append((node.left, h + 1))
            if node.right: stack.append((node.right, h + 1))
        
        return 2 ** height - 1 - empties 