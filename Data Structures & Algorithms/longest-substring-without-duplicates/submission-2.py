class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0: return 0

        l,r = 0,1
        maxL = 1

        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
            else:
                maxL = max(maxL, r-l+1)
                r += 1

        return maxL

