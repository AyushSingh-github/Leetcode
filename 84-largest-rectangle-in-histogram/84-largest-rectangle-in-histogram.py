class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        nser = [len(heights) for _ in range(len(heights))]
        
        stack = [len(heights)-1]
        
        for i in range(len(heights)-2,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nser[i] = stack[-1]
            stack += [i]
        
        
        nsel = [-1 for _ in range(len(heights))]
        
        stack = [0]
        
        for i in range(1,len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nsel[i] = stack[-1]
            stack += [i]
            
        ans = 0
        for i in range(len(heights)):
            width = nser[i]-nsel[i]-1
            ans = max(ans,heights[i]*width)
        return ans