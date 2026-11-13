class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashset = {}

        # for i, n in enumerate(numbers, start=1):
        #     d = target - n
        #     if d in hashset:
        #         return [hashset[d], i]
        #     hashset[n]=i
        # return [0,0]
        
        l, r = 0, len(numbers)-1
        
        while l < r:
            curSum = numbers[l]+numbers[r]
            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                return [l+1,r+1]
        
        return []
