class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0]*len(temps)
        s = []

        for i, t in enumerate(temps):
            
            while s and temps[s[-1]] < t:
                lastIndex = s.pop()
                res[lastIndex] = i - lastIndex

            s.append(i)
        return res

            

