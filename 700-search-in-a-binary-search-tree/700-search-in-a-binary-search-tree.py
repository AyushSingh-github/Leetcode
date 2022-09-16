# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return root
        '''
        
        #bfs queue
        q = deque()
        q.append(root)
        
        while q:            
            node = q.popleft()
            # print(node.val)
            if node.val == val:
                return node
            elif val < node.val and node.left:
                q.append(node.left)
            elif val > node.val and node.right:
                q.append(node.right)
        return None        