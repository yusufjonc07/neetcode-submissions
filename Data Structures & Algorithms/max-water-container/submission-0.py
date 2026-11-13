class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0, len(heights)-1
        max_amount = 0
        while l < r:
            w = r - l
            
            max_amount = max(max_amount, w*min(heights[r],heights[l]))
            
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return max_amount

