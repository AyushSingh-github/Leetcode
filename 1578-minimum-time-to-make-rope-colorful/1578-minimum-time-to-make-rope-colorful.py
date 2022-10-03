class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
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