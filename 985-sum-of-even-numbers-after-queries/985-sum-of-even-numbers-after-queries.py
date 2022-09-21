class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        maxsum = 0
        for n in nums:
            if not n%2:
                maxsum+=n
                
        answer = []
        for [val, i] in queries:
            newsum = nums[i] + val
            
            #the already even num in nums was added so need to delete from maxsum as if it was not simply add new sum to nums[i] if even else no need to change anything
            if nums[i] % 2 == 0:
                maxsum -= nums[i]
            
            #if newsum if even then prev maxsum has to be updated, if not then prev nums[i] if even is already there
            if newsum % 2 == 0:
                maxsum += newsum
            
            nums[i] = newsum
            answer.append(maxsum)
        return answer