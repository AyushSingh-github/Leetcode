# Monotonic Stack
**Key**:
​
Using a Monotonic Stack which maintains the element in the form (idx, price) whose price is bigger than current element.
​
Each time we execute the next function , starts from the top of the stack, and all the elements that less or equal than price are removed from the stack. We can find the nearest position on the left of the current element price that is larger than it.
​
* A good intuition for monotonic increase is imagining a bar graph with the bar height being score of the day. Think of these bars as walls. If you keep pouring water to the left of the current day wall until the water reaches bar height. The left wall would be a bar which is larger than or equal to the current bar. Whatever bar inbetween are smaller and becomes insignifcant.
​
## 1. ans
​
***Intuition***
Here we need to check for everyday's stock price and if it is less than the previous day or cumulative previous days then we need to give for how many days.
​
***Approach***
The idea that come to my mind after seeing the problem is like first I'll create a stack and I'll try to give value 1 to each stock price. And everytime before pushing the value to the stack we've to check if there is a stock price less than that and if yes then for how many days we've to iterate that res part which I've taken here as consideration.
​
So I'll try to explain my approach with the first example given in the question.
​
Suppose the first 7 days stock prices would be like this :-
[100,80,60,70,60,75,85]
​
* I'll start iterating through this list and I'll assign each stock price with value 1.
* So, for 100 I'll check that yes my stack is empty and no value is less than that so I'll push the pair [100,1] in the stack.
*
For now stack is :- [100,1]
Now, I'll go for 80 and I'll check if there is a value on top of stack less than 80 in stack, and there is no such value so we'll push [80,1] also in the stack.
​
For now stack is :- [80,1]
[100,1]
Now, I'll go for 60 and I'll check if there is a value less than 60 on top of the stack and there is no such value so we'll push [60,1] also in the stack.
​
For now stack is :- [60,1]