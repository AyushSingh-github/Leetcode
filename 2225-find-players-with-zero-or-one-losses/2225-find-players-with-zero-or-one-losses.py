#Set,    TC-> O(N.logN),    SC-> O(N)
'''
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_losses = set()
        
        for winner, loser in matches:
            # Add winner
            if (winner not in one_loss) and (winner not in more_losses):
                zero_loss.add(winner)
            
            # Add or move loser.
            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            elif loser in more_losses:
                continue
            else:
                one_loss.add(loser)          
            
        return [sorted(list(zero_loss)), sorted(list(one_loss))]

'''

#hashMap + Set,   TC-> O(N.logN), SC-> (N)
'''
class Solution: 
    def findWinners(self, matches : List[List[int]]) ->List[List[int]]: 
        seen = set(), losses_count = {}
        
        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            losses_count[loser] = losses_count.get(loser, 0) + 1
        
        #Add players with 0 or 1 loss to the corresponding list.
        zero_lose, one_lose = [], []
        for player in seen:
            count = losses_count.get(player, 0)
            if count == 0:
                zero_lose.append(player)
            elif count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]
''' 

#HashMap, TC-> O(), SC-> O()

class Solution: 
    def findWinners(self, matches: List[List[int]]) ->List[List[int]]: 
        losses_count = {}
        
        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] = losses_count.get(loser, 0) + 1
        
        zero_lose, one_lose = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_lose.append(player)
            if count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]


#Counting with array-> Counting sort
#TC-> O(N+K), SC-> O(k)  { N iterations + K types }

'''
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = [-1] * 100001

        for winner, loser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[loser] == -1:
                losses_count[loser] = 1
            else:
                losses_count[loser] += 1
            
        answer = [[], []]
        for i in range(100001):
            if losses_count[i] == 0:
                answer[0].append(i)
            elif losses_count[i] == 1:
                answer[1].append(i)
                
        return answer
'''