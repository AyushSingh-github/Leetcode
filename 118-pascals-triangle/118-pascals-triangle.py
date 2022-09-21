        #TO CALC ROW AND COL NUM value directly, we use (r-1)C(c-1) 
        #TC= O(N2), SC= O(N2), to print full triangle
        
        #TC= O(N), SC= O(1), to get just value on row and column
        
        #TC= O(N), Sc= O(N), to print all row, get previous ans like 4th row
        # 4C0 = 1, 4C1 = 4, 4C2 = 4*3/1*2. 4C3 = (4*3)*2/(1*2)*3  == 4C2 * (2/col num), ie, each rCc has equal numerator/demoninator
        
        #ex = 4C3 = (4*3*2)/(1*2*3), r=4, c=3,   for i = 0 to 3:  product_num *= r-i, product_deno *= i+1 = num/deno
        
#python brute force solution
'''
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,n):
            s=0
            b=[]
            b.append(1)
            for j in range(i-1):
                s = ans[i-1][j] + ans[i-1][j+1]
                b.append(s)
            b.append(1)
            ans.append(b)
        return ans
'''    
#optimized solution
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[[1]*(i+1) for i in range(n)]
        for i in range(n):
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans
