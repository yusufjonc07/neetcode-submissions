class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}

        for i, n in enumerate(numbers, start=1):
            d = target - n
            if d in hashset:
                return [hashset[d], i]
            hashset[n]=i
        return [0,0]