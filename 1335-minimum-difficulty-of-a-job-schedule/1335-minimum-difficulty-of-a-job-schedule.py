class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(999)
        def solve(i,j):
            if j == 1 and i < len(jobDifficulty):
                return max(jobDifficulty[i:])
            else:
                ans = 99999
                maxx = 0
                for k in range(i, len(jobDifficulty)):
                    maxx = max(maxx, jobDifficulty[k])
                    ans = min(ans, maxx + solve(k+1, j-1))
                    # print(ans,i,j,maxx)
                return ans
            
        ans = solve(0,d) 
        if ans != 99999:
            return ans
        return -1