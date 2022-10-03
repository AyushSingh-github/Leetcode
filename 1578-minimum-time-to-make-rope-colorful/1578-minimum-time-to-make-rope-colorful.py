class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''
        output = 0
        currentColor = ""
        currentSequence = []

        for t, color in enumerate(colors):
            if color != currentColor:
                if currentSequence:
                    output += sum(currentSequence) - max(currentSequence)

                currentColor = color
                currentSequence = []
                currentSequence.append(neededTime[t])
            else:
                currentSequence.append(neededTime[t])

        if currentSequence:
            output += sum(currentSequence) - max(currentSequence)

        return output
        '''
        
        col=[colors[0]]
        # ind=list()
        x=0
        maxi=0
        total=neededTime[0]
        n=len(colors)
        for i in range(1,n):
            total+=neededTime[i]
            if colors[i]!=col[-1]:
                col.append(colors[i])
                maxi+=max(neededTime[x:i])
                x=i
            else:
                continue
        maxi+=max(neededTime[x:len(neededTime)])
        # print(total,maxi)
        return total-maxi   