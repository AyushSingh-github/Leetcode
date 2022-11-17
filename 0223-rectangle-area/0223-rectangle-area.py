class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        #area of A and B rect = length * breath
        A = (ay2-ay1) * (ax2-ax1)
        B = (by2-by1) * (bx2-bx1)
        
        #x overlap
        l = max(ax1, bx1)
        r = min(ax2, bx2)
        xoverlap = r - l

        #y overlap
        u = min(ay2, by2)
        d = max(ay1, by1)
        yoverlap = u - d

        overlap = 0
        if xoverlap > 0 and yoverlap > 0:
            overlap = xoverlap * yoverlap

        res = A + B - overlap

        return res