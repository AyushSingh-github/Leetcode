class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for i in paths:
            files = i.split()
            path = files[0]
            for index in range(1,len(files)):
                name, content = files[index].split("(")
                content = content[:-1]
                if content in d:
                    d[content].append(path+"/"+name)
                else:
                    d[content] = [path+"/"+name]
        ans = []
        for i in d:
            if len(d[i])>1:
                ans.append(d[i])
        return ans