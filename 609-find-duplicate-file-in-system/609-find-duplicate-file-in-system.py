class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for i in paths:
            files = i.split()
            #print(len(files))
        
            path = files[0]
            #print(path)    #for root and dir
            #print(files)
            
            for index in range(1,len(files)):
                #print(files[index].split("("))
                
                name, content = files[index].split("(")
                #print(name," ",content)
                
                content = content[:-1]
                #print(content)
                
                if content in d:
                    d[content].append(path+"/"+name)
                else:
                    d[content] = [path+"/"+name]
                #print(d)
        ans = []
        for i in d:
            if len(d[i])>1:
                ans.append(d[i])
        return ans