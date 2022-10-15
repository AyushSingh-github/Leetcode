# 4.
Instead of considering k as the number of removal, think of k as the number of characters we can skip when counting s.
​
Let counts(k, i, j, c) be the function that return the minimum length of the run-length encoded version of s given
​
k: the number of skip remaining
i: pointer to the current character
j: pointer to the previously picked character
c: the count of previously picked character
​
​
1. If s[i] == s[j], we always pick the current character and it will increase the minimum length
only when c is 1, 9, and 99.
​
Note: we don't consider skipping the current character here because skipping it is the same as if we were to skip the previous character. Thus, the second case will take care of it.
​
```
Ex: b -> a -> a -> a        b -> a -> a -> a
✓   ✓   ✗   ✓        ✓    ✗   ✓   ✓
​
b -> a -> a -> a        b -> a -> a -> a
✓   ✓   ✗    ✗       ✓    ✗    ✗   ✓
```
​
2. If s[i] != s[j], we have to consider the case where we pick the current character and the case where we skip the current character. Then, we just pick the one that give the minimum length.
Complexity:
Time: O(n2**k) because we have two options for every character character up to k character
Space: O(kn**2)