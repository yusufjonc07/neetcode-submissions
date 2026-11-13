class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = [0] * 26
        tCount = [0] * 26

        
        for a in s:
            sCount[ord(a) - ord('a')] += 1
        
        for b in t:
            tCount[ord(b) - ord('a')] += 1
        
        return sCount == tCount

