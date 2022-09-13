class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        N = len(data)
        print(list(bin(x) for x in data))
        
        i=0
        while i<N:
            if (data[i] & (1<<7)) == 0:
                # 1 byte char
                i += 1
                continue
            
            byte = 0
            while (data[i] & (1 << (7- byte))) > 0 and byte<=5:
                byte += 1
                
            if byte == 1 or byte > 4:
                return False
            
            for j in range(1,byte):
                if i+j >= N:
                    return False
                if (data[i+j] & ((1 << 7) | (1 << 6))) != (1 << 7):
                    return False
            i += byte
        return True