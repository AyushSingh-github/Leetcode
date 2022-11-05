#Neetcode . Brute force =  No. of words(W)  TC-> [W*(mn*4^mn)]
'''
class TrieNode:
    def __init__(self):
        # key->chars, value->child trie nodes
        #list of children as dict
        self.children = {}
        #if end of word node or not
        self.isWord= False
    
    #searching simultaneously for every dfs 
    def addWord(self,word):
        #adding to trie word to word letters using cur ptr
        cur = self
        for c in word:
            #f not exit then insert at char c else move cur to next cur children
            if c not in cur.children:
                
                #create node at Trie for char c
                cur.children[c] = TrieNode()
                
            # move cur to that present pos at the end   
            cur = cur.children[c]
            
        #this is the end of word and marked as True
        cur.isWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        #add words in Trie using addWord func for every w in words list
        for w in words:
            root.addWord(w)
        
        #dfs
        rows,cols =  len(board), len(board[0])
        
        #to prevent visit of duplicates and not to repeat chars twice
        res, visit = set(), set()
        
        #node-> (cur node in trie), word-> what word we go till now 
        def dfs(r,c,node,word):
            #if node is end of word so add word to res
            #base case
                #out of bounds
            if (r<0 or c<0 or  
                r==rows or c==cols or 
                
                #pos is already visited
                (r,c) in visit or 
                
                #char at r,c is not in Trie
                #(cur chldren nodes so its not a word) 
                board[r][c] not in node.children):
                return
            
            #if in Trie first mark visited for no repeatition
            visit.add((r,c))
            
            #update node to cur pos(next letter)
            node = node.children[board[r][c]]
            
            #update word we reached till now
            word += board[r][c]
            
            #if end of word
            if node.isWord:
                res.add(word) #str word found and not the node as final result
                node.isWord = True
            
            #backtrack in all directions
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            
            #unvisit for backtrack as if backtrack we can use this pos again
            visit.remove((r,c))
        
        #start from 1st board letter
        for r in range(rows):
            for c in range(cols):
                #start from top of Trie and empty word formed till now
                dfs(r,c,root,"")
        
        return list(res)
'''            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m, n = len(board), len(board[0])
        res, trie, has = list(), dict(), set()
        
        for r in range(m):
            for c in range(n - 1):
                has.add(board[r][c] + board[r][c + 1])
        for r in range(m - 1):
            for c in range(n):
                has.add(board[r][c] + board[r + 1][c])
        
        for word in words:
            for i in range(len(word) - 1):
                a, b = word[i], word[i + 1]
                if a + b not in has and b + a not in has:
                    break
            else:
                cur = trie
                for c in word:
                    if c not in cur: cur[c] = {}
                    cur = cur[c]
                cur['*'] = word
        
        def dfs(r, c, node):
            node = node[board[r][c]]
            if '*' in node:
                res.append(node['*'])
                del node['*']
            rc = board[r][c]
            board[r][c] = '*'
            for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
                dr, dc = r + i, c + j
                if dr < 0 or dr >= m or dc < 0 or dc >= n \
                or board[dr][dc] not in node:
                    continue
                dfs(dr, dc, node)
                if len(node[board[dr][dc]]) == 0:
                    del node[board[dr][dc]]
            board[r][c] = rc
        
        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)
        
        return res
        
        
        
        