class Solution:
    def trap(self, height: List[int]) -> int:
        #stack
        my_stack = []  # store the index
        total_volume = 0
        for i, v in enumerate(height):
            while my_stack and height[my_stack[-1]] <= v:
                h1 = height[my_stack.pop()]
                if my_stack:
                    h2 = min(height[my_stack[-1]], v)
                    total_volume += (h2 - h1) * (i - my_stack[-1] - 1)
            my_stack.append(i)
        return total_volume