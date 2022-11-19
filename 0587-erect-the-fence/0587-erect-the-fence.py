class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Gram Scan Convex Hull
        '''
        def compare_slopes(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2) 
        
        upper, lower  = [], []
        
        for point in sorted(trees):
            while len(lower) >= 2 and compare_slopes(lower[-2], lower[-1], point) < 0: lower.pop()
            while len(upper) >= 2 and compare_slopes(upper[-2], upper[-1], point) > 0: upper.pop()
                
            lower.append(tuple(point))
            upper.append(tuple(point))  
            
        return list(set(lower + upper))
        '''
        
        #Monotone Chain Convex Hull

        trees = sorted(trees, key = lambda e:(e[0],e[1]))
        if len(trees) <= 1:
            return trees
        
        #checking orientation of vectors oa and ob
        def ccw(o,a,b):
            return (a[0]-o[0])*(b[1]-o[1])-(b[0]-o[0])*(a[1]-o[1]) > 0
        lower_chain = []
        
        for p in trees:
            while len(lower_chain) > 1 and ccw(lower_chain[-1], lower_chain[-2], p):
                lower_chain.pop()
            lower_chain.append(p)
        upper_chain = []
        
        for p in reversed(trees):
            while len(upper_chain) > 1 and ccw(upper_chain[-1], upper_chain[-2], p):
                upper_chain.pop()
            upper_chain.append(p)
        return set([(e[0],e[1]) for e in lower_chain[:-1]+upper_chain[:-1]])