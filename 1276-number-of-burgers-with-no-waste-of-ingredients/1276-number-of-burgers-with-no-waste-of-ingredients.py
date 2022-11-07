class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        tomato, cheese = tomatoSlices, cheeseSlices
        if tomato < 2*cheese or (tomato - 2*cheese)%2 != 0:
            return []
        if 4*cheese < tomato or (4*cheese - tomato)%2 != 0:
            return []
        
        return [ (tomato - 2*cheese)//2, (4*cheese - tomato)//2 ]