class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        '''
        stack = []
        properties.sort(key = lambda x: (x[0], -x[1]))
        #print(properties)
        count = 0
        
        for attack, defense in properties:
            while stack and attack > stack[-1][0] and defense > stack[-1][1]:
                count += 1
                #print(stack)
                stack.pop()
                #print(stack)
                
            stack.append((attack, defense))
            #print(stack)
        
        return count
    
        '''
        properties.sort(key=lambda x: (-x[0], x[1]))
        print(properties)
        topmax = 0
        count = 0
        
        for attack, defense in properties:
            if defense < topmax:
                count += 1
            else:
                topmax = defense
                print(topmax)
            
        return count
        