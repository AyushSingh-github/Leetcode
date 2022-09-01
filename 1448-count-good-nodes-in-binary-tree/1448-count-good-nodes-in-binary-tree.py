# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        paths=[]
        sub_paths=[]
        
        def getpath(root,path):
            if not root:
                return False
            
            path.append(root.val)
            paths.append(path.copy())
            
            if getpath(root.left,path) or getpath(root.right,path):
                return True
            
            path.pop()
            return False
        
        getpath(root,sub_paths)
        print(paths)
        
        count=0
        for path in paths:
            flag=False
            current_node_val = path[-1]
            print(current_node_val,end=" ")
            
            for i in path:
                if i>current_node_val:
                    flag = True
                    break
            if flag!=True:
                count+=1
                
        return count
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, curMax):
            if not node:
                return
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        count = [0]
        #calling dfs
        dfs(root, root.val)
        
        return count[0]
