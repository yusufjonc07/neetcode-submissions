class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        caravan = []

        for p, s in sorted(pairs, reverse=True):
            caravan.append((target-p)/s)
            if len(caravan) > 1 and caravan[-1] <= caravan[-2]:
                caravan.pop()

        
        return len(caravan)
