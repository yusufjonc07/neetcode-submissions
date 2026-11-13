class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s): return ""
        
        sWin, tWin = {}, {}
        for c in t:
            tWin[c] = 1 + tWin.get(c, 0)
        
        have, need = 0, len(tWin)
        res, resLen = (-1, -1), float('inf')

        l = 0
        for r in range(len(s)):
            c = s[r]
            sWin[c] = 1 + sWin.get(c, 0)
            
            if c in tWin and sWin[c] == tWin[c]:
                have += 1

            while have == need:
                print(s[l:r+1])
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                sWin[s[l]] -= 1
                if s[l] in tWin and sWin[s[l]] < tWin[s[l]]:
                    have -= 1
                l += 1


        l,r = res 
        
        return s[l:r+1] if resLen != float('inf') else ""