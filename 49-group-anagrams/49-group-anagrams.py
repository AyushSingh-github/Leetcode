'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            #print(''.join(sorted(strs[i])))
            d[i] = ''.join(sorted(strs[i]))
        print(d)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idx_map = {}
        res = []
        sorted_strs=[]
        
        for i in range(len(strs)):
            sorted_strs.append(''.join(sorted(strs[i])))
        #print(sorted_strs)
        
        for index, word in enumerate(sorted_strs):
            if word in idx_map:
                
			    # get the original string values as list into the hashmap of key, value pair of sorted_strs:list of strs values at that same index
                
                idx_map[word].append(strs[index])
            else:
                idx_map[word] = [strs[index]]
        #print(idx_map)
                
        for entry in idx_map.values():
            res.append(entry)
        
        return res