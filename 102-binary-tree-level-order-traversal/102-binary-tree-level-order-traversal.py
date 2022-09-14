# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs = []
        if root is None:
            return bfs
        queue = deque([])
        queue.append(root)
        while len(queue)!=0:
            level_size = len(queue)
            current_level = []
            
            for i in range(level_size):
                current = queue.popleft()
                current_level.append(current.val)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            bfs.append(current_level)
        return bfs 