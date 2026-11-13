class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for c in s:
            hashS[c] = 1 + hashS.get(c, 0)
        for d in t:
            hashT[d] = 1 + hashT.get(d, 0)

        for c in hashS:
            if hashS[c] != hashT.get(c, 0):
                return False


        return True
        