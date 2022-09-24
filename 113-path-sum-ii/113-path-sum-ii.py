# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def solve(root,curr_path):
            if not root:
                return 
            curr_path.append(root.val)
            
            if not root.left and not root.right and sum(curr_path) == targetSum:
                res.append(list(curr_path))
                print(curr_path)
                
                
            solve(root.left,curr_path)
            solve(root.right,curr_path)
            curr_path.pop()
            
        solve(root,[])
        return res