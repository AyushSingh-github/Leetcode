#We create all possible moves for each coordinate in sparse matrix of img1, then check after applying #those moves one by one if the new coordinates exist in the sparse matrix of the img2. If yes, then we #increase the count. For each move we get the number of overlaps. We return the max overlap for any #particular move.
#TC -> O(N4)


class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        spm1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c]] # only indices having 1
        spm2 = set([(r, c) for r in range(n) for c in range(n) if img2[r][c]]) # only indices having 1, set in order to check later if the coordinates match
        check = [(r, c) for r in range(-n + 1, n) for c in range(-n + 1, n)] # all possible directions the points can take -> bottom right point can even be moved to top left, so indices moves start from -ve
        res = 0
        
        for x, y in check:
            temp = 0
            
            for r, c in spm1:
                if (r + x, c + y) in spm2: temp += 1 # check if the coordinates of 1 match in the set spm2
            
            res = max(temp,res)
            
        return res