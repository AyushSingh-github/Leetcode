With this reasoning, would the space complexity technically be O(min(m,n))?
The hollow diamond would only continue growing until we hit the edge of matrix, which will happen first in the smaller dimension, restricting the side lengths to be O(min(m,n)).
I haven't been able to think of a case where we have O(max(m,n)) or O(m+n) positions in the queue at any point.