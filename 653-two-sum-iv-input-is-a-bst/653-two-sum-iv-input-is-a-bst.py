# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = set()
        def solve(root):
            if not root:
                return 
            if k - root.val in nodes:
                return True
            nodes.add(root.val)
            return solve(root.left) or solve(root.right)
        return solve(root)

    
class Solution(object):
	def findTarget(self, root, k):

		visited = set()
		stack = [root]

		while stack:
			node = stack.pop()

			if node:
				if node.val in visited: return True 
				stack.append(node.right)
				stack.append(node.left)

				visited.add(k - node.val)
'''
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        a=[]
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)
        inorder(root)
        
        #two pointer
        start=0
        end=len(a)-1
        while start != end:
            summ = a[start] + a[end]
            if summ == k:
                return True
            if summ > k:
                end -= 1
            else:
                start += 1
        return False