# Monotonic Stack
**Key**:
​
Using a Monotonic Stack which maintains the element in the form (idx, price) whose price is bigger than current element.
​
Each time we execute the next function , starts from the top of the stack, and all the elements that less or equal than price are removed from the stack. We can find the nearest position on the left of the current element price that is larger than it.
​
* A good intuition for monotonic increase is imagining a bar graph with the bar height being score of the day. Think of these bars as walls. If you keep pouring water to the left of the current day wall until the water reaches bar height. The left wall would be a bar which is larger than or equal to the current bar. Whatever bar inbetween are smaller and becomes insignifcant.