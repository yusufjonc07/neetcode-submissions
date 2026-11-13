class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char
    
        return clean_s == "".join([clean_s[i] for i in range(len(clean_s)-1, -1, -1)])