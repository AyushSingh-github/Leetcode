'''
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        
        """
            . after deleting k characters, we need run-length encoded of "s" to be of lowers size
            
            q. is their a greedy way to know which element to start deleting from?
            a. greedy1. does deleting elements with smallest counts help..
                    e1.aaaaaaaaaabaaa, k = 2
                    counts : a11 b1 a3
                    deleting 2 elemts from smalles
                    couunts: a11 b0 a2 -> a11a2 = a13
                    
                    e2: aaaaaaaaaaabbbb
                    counts a11 b4
                    delete 2 smallest count: a11 b2 = length(a11b2) = 5
                    optimal way would be deleting "a" : a9 b4 = length = 4
                    
                    doest seem possible to prematurely know if which element to delete in beginning
                    
            greedy2. deleting all combinations of s and find lowest len. 
                too much re work. will be done which probably can be prevented using DP
            
            
            a. DP seems viable solution. we either take current word or not
            
            dp-type: BOUNDED(use each value once) / Sequence matter(use ci+1 in parameter) 
            DP(ci, k_remains, curr_running_elem, curr_letter_count)
            states:
                ci = current index
                k_remains = remaining elements to be deleted
                curr_running_elem = the last running character
                curr_letter_count = count of the last running character
            state transition:
                either onsider taking current element
                    : if both current and prev are same count++ and ci+1
                    : else ???
                or skip it if we have k_remains>0
                    : ci+1
                
                min(take, notake)
                
                
            exit condition:
                ci == len(s) return final length
        """
        
        @cache
        def dp(ci, curr_running_char, curr_running_char_count, remains):
            
            if ci == len(s):
                return 0
            
            
            delete_char_distance = inf
            if remains > 0:
                delete_char_distance = dp(ci+1, curr_running_char, curr_running_char_count, remains - 1)
            
            curr_letter = s[ci]
            
            keep_ch_cost = inf
            if curr_letter == curr_running_char:
                # same letter as previous
                add = 0
                
                # if curr_running_char_count == 1 , since we donot add a1 but only a2, 
                if curr_running_char_count == 1 or len(str(curr_running_char_count + 1)) > len(str(curr_running_char_count)):
                    add = 1
                
                keep_ch_cost = add + dp(ci+1, curr_letter, curr_running_char_count + 1, remains)
            else:
                # different letter
                keep_ch_cost = 1 + dp(ci+1, curr_letter, 1, remains)
            
            return min(keep_ch_cost, delete_char_distance)
                
            
        res = dp(0, "", 0, k)
        return res
            
'''

'''
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        #traverse the string
        #keep track of the status of delete or not delete current character
        #the status includes current index, number of delete, the previous character, and the runing length of previous character
        #return the minium length of compresed between delete or not delete
		#O(n^2*26*k) = O(n^2*k) time and space
        
        memo = {}
        return self.dfs(s, 0, k, None, 0, memo)
    
    def dfs(self, s, i, k, prev, l, memo):
        if i == len(s):
            return 0
        if (i, k, prev, l) in memo:
            return memo[(i, k, prev, l)]
        
        if k > 0:
            delete = self.dfs(s, i + 1, k - 1, prev, l, memo)
        else:
			#in this case, we cannot delete, set it as INF to choose skip in the end
            delete = float("inf")
        
        if s[i] == prev:
		    #need one more digit for the count
            carry = 1 if l == 1 or len(str(l + 1)) > len(str(l)) else 0
            skip = carry + self.dfs(s, i + 1, k, s[i], l + 1, memo)
        else:
            skip = 1 + self.dfs(s, i + 1, k, s[i], 1, memo)
        
        memo[(i, k, prev, l)] = min(delete, skip)
        
        return memo[(i, k, prev, l)]
            
'''

'''
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, prev, prev_cnt, k):
            # set it to inf as we will take the min later
            if k < 0: return inf
            # we delete all characters, return 0
            if i == len(s): return 0
            # here we can have two choices, we either
            # 1. delete the current char
            # 2. keep the current char
            # we calculate both result and take the min one
            delete = dp(i + 1, prev, prev_cnt, k - 1)
            if s[i] == prev:
                # e.g. a2 -> a3
                keep = dp(i + 1, prev, prev_cnt + 1, k)
                # add an extra 1 for the following cases
                # since the length of RLE will be changed
                # e.g. prev_cnt = 1: a -> a2
                # e.g. prev_cnt = 9: a9 -> a10
                # e.g. prev_cnt = 99: a99 -> a100 
                # otherwise the length of RLE will not be changed
                # e.g. prev_cnt = 3: a3 -> a4
                # e.g. prev_cnt = 8: a8 -> a9
                # alternative you can calculate `RLE(prev_cnt + 1) - RLE(cnt)`
                if prev_cnt in [1, 9, 99]:
                    keep += 1
            else:
                # e.g. a
                keep = dp(i + 1, s[i], 1, k) + 1
            return min(delete, keep)
        
        # dp(i, prev, prev_cnt, k) returns the length of RLE with k characters to be deleted
        # starting from index i 
        # with previous character `prev`
        # with `prev_cnt` times repeated so far
        return dp(0, "", 0, k)
    '''
#4.
from functools import lru_cache
from math import inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        # Get length of s
        n = len(s)

        # Return the minimum length of the run-length encoded version of s
        # k: the number of skip remaining
        # i: pointer to the current character
        # j: pointer to the previously picked character 
        # c: the count of previously picked character
        @lru_cache(None)
        def counts(k, i, j, c):

            # If we skip more than allowed, return infinity
            if k < 0:
                return inf

            # If we reach the end of s, return 0
            if i >= n:
                return 0

            # If the current character is the same as the previously picked character, we pick it and increment the minimum length if the count of previously picked character is at 1, 9, or 99
            if 0 <= j <= n and s[i] == s[j]:

                return int(c == 1 or c == 9 or c == 99) + counts(k, i + 1, i, c + 1)

            # Else, take the minimum between picking the current character or skipping the current character
            return min(1 + counts(k, i + 1, i, 1), counts(k - 1, i + 1, j, c))

        return counts(k, 0, -1, 0)