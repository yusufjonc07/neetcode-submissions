class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        ## bruteForce
        # l = 0, k-1
        # 
        # for l in range(len(nums)-k+1):
        #     maxIt = nums[l]

        #     r = l
        #     while r < l+k and r < len(nums):
        #         maxIt = max(nums[r], maxIt)
        #         r+=1
            
        #     res.append(maxIt)

        # decreasing deque

        l, r = 0, 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
