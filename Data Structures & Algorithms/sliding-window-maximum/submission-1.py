class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0

        res = []
        for l in range(len(nums)-k+1):
            maxIt = nums[l]
            r = l
            while r < l+k and r < len(nums):
                maxIt = max(nums[r], maxIt)
                r+=1
            
            res.append(maxIt)


        return res
