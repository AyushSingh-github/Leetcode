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
        seen, losses_count = set(),{}
        
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
'''
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
'''

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

#You can also use max(loss.keys) instead of max(chain(*matches)) but it was much slower for me.

#Algorithm:
#Count losses in matches using a hashmap.

#Iterate through all integers until largest in matches, only add integers in our hashmap and with a value less than or equal to 1 to our result output.

#Return our result! Range of integers is already sorted, therefore no need for a wasteful sorted() function call.

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss, res = {}, [[], []]
        for winner, loser in matches:
            loss[winner] = loss.get(winner, 0)
            loss[loser] = loss.get(loser, 0) + 1
        for player in range(max(chain(*matches)) + 1):
            if player in loss and loss[player] <= 1:
                res[loss[player]].append(player)
        return res

#Complexity Analysis:
#Let n be the size of our input array matches:

#Time Complexity: O(n)
#We iterate through matches and count up losses and then iterate up to the largest integer in matches, "k". k is an integer so this simplifies to O(n).

#Space Complexity: O(n)
#loss and res each take up n space, 2n simplifies to n space

#We do not need to generate k arbitrary space for players not in matches nor hardcode an arbitrary maximum set in the constraints.