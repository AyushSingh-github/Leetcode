@lru_cache(maxsize=None)
try adding the (maxsize=None)
i tried it out with the first solution and it worked
​
from: https://realpython.com/lru-cache-python/
Python's @lru_cache decorator offers a maxsize attribute that defines the maximum number of entries before the cache starts evicting old items. By default, maxsize is set to 128 . If you set maxsize to None , then the cache will grow indefinitely, and no entries will be ever evicted.
​
once the cache hits a size of 128, it will remove previously calculated problems...and thus they have to be calculated again. imagine when n=30, k=30, target=500, you would have to recalculate many subproblems along the way, each of which would have a large recursive depth. so it would pretty much be as bad as not using a cache at all for large values of n,k and target.
​
well, this is my understanding of it. this is personally the first time i've used @lru_cache in a problem, so someone with more experience with it can chime in. it seems pretty useful for solving any dynamic programming problem in python..basically removes the need to manually memoize and/or think of an iterative solution.
​
what you've done in the second solution is manually keeping track of the sub problems, so that's why it works, there is no max size for your memo table(i don't know if python caps array/dict sizes, but clearly the max array/dict size is not reached by any means in this problem)