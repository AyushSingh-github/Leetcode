# **Stack**
This problem is very similar to "The area of the largest rectangle" problem. Both use monotonic stack to solve. In this problem, we define a monotonic stack to store the index of the next greater element. If curr_v < height[stack.top], we just add it to the stack; else we pop the top element in the stack as the bottom height (h1). If the stack is not empty, which means we have the upper height (h2), we calculate the water area using (h2-h1) * width. Note that here we can only ensure curr_v > h1, curr_v may be smaller/equal/larger than h2. Thus, we have : h2 = min(height[stack.top], curr_v).
​
We keep popping elements at the top of the stack until the stack is empty or curr_v < height[stack.top]. Then we add the index of curr_v into the stack.
​
​
​
​