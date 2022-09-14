# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freq=[0 for x in range(10)]
        self.pointer=0
        
        def dfs(node,freq):
            if not node: 
                return
            freq[node.val]+=1
            if not node.left and not node.right:
                odd=0
                for i in freq:
                    if i%2!=0: 
                        odd+=1
                if odd<=1:
                    self.pointer+=1
            dfs(node.left,freq)
            dfs(node.right,freq)
            freq[node.val]-=1
            
        dfs(root,freq)
        return self.pointer