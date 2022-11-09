# Monotonic Stack
**Key**:
​
Using a Monotonic Stack which maintains the element in the form (idx, price) whose price is bigger than current element.
​
Each time we execute the next function , starts from the top of the stack, and all the elements that less or equal than price are removed from the stack. We can find the nearest position on the left of the current element price that is larger than it.