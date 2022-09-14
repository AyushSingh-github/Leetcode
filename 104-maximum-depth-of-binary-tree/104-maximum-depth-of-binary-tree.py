# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursion dfs
        '''
        if root is None:
            return 0
        else:
            lefth=self.maxDepth(root.left)
            righth=self.maxDepth(root.right)
        return 1 + max(lefth,righth)
        '''
        
        #bfs
        '''
        if not root: return 0
        q = deque([root])
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1
        return res
        '''
        
        #iterative DFS
        if not root:
            return 0
        stack=[[root, 1]]
        res =1
        while stack:
            node, depth = stack.pop()
            if node:
                res= max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
