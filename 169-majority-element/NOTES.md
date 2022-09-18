* A majority element is one that appears more than half of the time in the input elements. However, if there is no majority, the algorithm will not recognize this and will continue to output one of the items.
​
* The algorithm is divided into two parts. A first pass identifies an element as a majority, and a second pass confirms that the element identified in the first pass is indeed a majority.
​
* The method will not identify the majority element if it does not exist, and will thus return an arbitrary element.
​
The algorithm maintains in its local variables a sequence element and a counter, with the counter initially zero. It then processes the elements of the sequence, one at a time. When processing an element x, if the counter is zero, the algorithm stores x as its remembered sequence element and sets the counter to one. Otherwise, it compares x to the stored element and either increments the counter (if they are equal) or decrements the counter (otherwise). At the end of this process, if the sequence has a majority, it will be the element stored by the algorithm. This can be expressed in pseudocode as the following steps:
​
# Boyer Moore's Voting Algo
```
Initialize an element m and a counter i with i = 0:
For each element x of the input sequence:
If i = 0:
then assign m = x and i = 1
else if m = x:
then assign i = i + 1
else:
assign i = i − 1
Return m
```
Even when the input sequence has no majority, the algorithm will report one of the sequence elements as its result. However, it is possible to perform a second pass over the same input sequence in order to count the number of times the reported element occurs and determine whether it is actually a majority. This second pass is needed, as it is not possible for a sublinear-space algorithm to determine whether there exists a majority element in a single pass through the input.[3]
​