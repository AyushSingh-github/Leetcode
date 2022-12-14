# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root):
            if root:
                if root.val == p.val or root.val == q.val:
                    return root
                if p.val > root.val and q.val > root.val:
                    return traverse(root.right)
                elif root.val > p.val and root.val > q.val:
                    return traverse(root.left)
                else:
                    return root
        return traverse(root)
'''
class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		if not root or root == p or root == q:
			return root

		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)

		if left and right:
			return root

		return left or right 