A majority element is one that appears more than half of the time in the input elements. However, if there is no majority, the algorithm will not recognize this and will continue to output one of the items.
​
The algorithm is divided into two parts. A first pass identifies an element as a majority, and a second pass confirms that the element identified in the first pass is indeed a majority.
​
The method will not identify the majority element if it does not exist, and will thus return an arbitrary element.