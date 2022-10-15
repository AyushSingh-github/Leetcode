class Solution:
    def partitionLabels(self, s: str) -> List[int]:
#greedy + hashmap
        '''
        #find the last position of letter and update the max value till where the string is possible else update the new string with new position of i and again find max value of last index of the new string with i index value
        
        #store last index of occurance
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        #print(d)
        
        #store successive sum of index of last occurance of letter in the new string 
        ar = []
        maxx = -1
        for i in range(len(s)):
            #if last occurance is > max (previous letter value) update max 
            if maxx < d[s[i]]:
                maxx = d[s[i]]
                #print(maxx,i)
                
            #if present letter is same till the max value, it means it in included in the previus string and update arr with the last occurance of new string formed 
            if i == maxx:
                ar.append(i+1)
        #print("array till new string is sliced",ar)
        
        #successive diff to get length of new string by (last occurance of new str - last occurance of previous str) 
        for i in range(len(ar)-1,0,-1):
            ar[i]=ar[i]-ar[i-1]
        #print("after deletion",ar)
        return ar
'''
#greedy no hashing 
        red,green = 0,0
        out = []
        current_part_size = 0
        
        while (green < len(s) and red < len(s)):
            for i in range(red+1, len(s)):
                if s[i] == s[green]:
                    red = i
                    #print("red",red)
                    
            if green == red:
                red += 1
                out.append(current_part_size + 1)
                current_part_size = 0
                #print("red if",red)
                #print("out",out)
            else:
                current_part_size += 1
                #print("size",current_part_size)
            
            green += 1
            #print("green",green)
        return out    
    