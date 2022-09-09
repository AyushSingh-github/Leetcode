class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
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
        # sort properties in descending order of attack but ascending order of defense
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        max_defense = 0
        weak_count = 0
        
        for _, defense in properties:
            # for any given element:
            # - every attack must be less than or equal to what we have already seen
            # - if the attack is the same, then the defense must be greater than what we have already seen for this attack value
            if defense < max_defense:
                weak_count += 1
            else:
                max_defense = defense
            
        return weak_count
        '''